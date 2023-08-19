use pyo3::prelude::*;
use pyxel_engine::{SharedChannel as PyxelSharedChannel, Volume};

use crate::sound_wrapper::Sound;

#[pyclass]
#[derive(Clone)]
pub struct Channel {
    pyxel_channel: PyxelSharedChannel,
}

pub const fn wrap_pyxel_channel(pyxel_channel: PyxelSharedChannel) -> Channel {
    Channel { pyxel_channel }
}

#[pymethods]
impl Channel {
    #[getter]
    pub fn get_gain(&self) -> Volume {
        self.pyxel_channel.lock().gain
    }

    #[setter]
    pub fn set_gain(&self, gain: u8) {
        self.pyxel_channel.lock().gain = gain;
    }

    pub fn play_pos(&self) -> Option<(u32, u32)> {
        self.pyxel_channel.lock().play_pos()
    }

    #[pyo3(text_signature = "($self, snd, *, tick, loop)")]
    pub fn play(&self, snd: &PyAny, tick: Option<u32>, r#loop: Option<bool>) -> PyResult<()> {
        let loop_ = r#loop.unwrap_or(false);
        type_switch! {
            snd,
            u32, {
                self.pyxel_channel.lock().play1(pyxel_engine::sound(snd), tick, loop_);
            },
            Vec<u32>, {
                let snd = snd.iter().map(|sound_no| pyxel_engine::sound(*sound_no)).collect();

                self.pyxel_channel.lock().play(snd, tick, loop_);
            },
            Sound, {
                self.pyxel_channel.lock().play1(snd.pyxel_sound, tick, loop_);
            },
            Vec<Sound>, {
                let snd = snd.iter().map(|sound| sound.pyxel_sound.clone()).collect();

                self.pyxel_channel.lock().play(snd, tick, loop_);
            }
        }
        Ok(())
    }

    pub fn stop(&mut self) {
        self.pyxel_channel.lock().stop();
    }
}

pub fn add_channel_class(m: &PyModule) -> PyResult<()> {
    m.add_class::<Channel>()?;
    Ok(())
}
