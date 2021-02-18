#include "main.hpp"

using namespace blit;

void init() {
    set_screen_mode(ScreenMode::hires);
}

void update(uint32_t time) {

}

void render(uint32_t time) {
  screen.pen = Pen(20, 30, 40);
  screen.clear();

  screen.pen = Pen(255, 255, 255);
  screen.rectangle(Rect(0, 0, 320, 14));
  screen.pen = Pen(0, 0, 0);
  screen.text("Raycasting", minimal_font, Point(5, 4));

  screen.watermark();
}