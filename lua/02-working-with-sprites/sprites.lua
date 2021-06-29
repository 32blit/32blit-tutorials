timer = Timer()
frame = 0

-- Store our small/big robot locations somewhere tidy
small_robot = Rect(0, 0, 1, 2)
big_robot = Rect(0, 5, 2, 2)

-- Function that the timer calls every 100ms
function animate(timer)
    frame = frame + 1
    if frame > 7 then
        frame = 0
    end
    -- Update the sprites we're pointing at based on the current frame
    small_robot.x = frame * small_robot.w
    big_robot.x = frame * big_robot.w
end

function init()
    screen.load_sprites("tankbot.bmp")
    timer:init(animate, 100) -- new 100ms timer
    timer:start() -- start the timer!
end

function render(time)
    screen.pen = Pen(20, 30, 40)
    screen.clear()

    screen.pen = Pen(255, 255, 255)
    screen.text("Hello World", minimal_font, Point(10, 50))

    -- Show the current frame
    screen.text("Frame: " .. frame, minimal_font, Point(10, 60))

    -- Small robot
    screen.sprite(small_robot, Point(80, 44))

    -- Big tank
    screen.sprite(big_robot, Point(90, 44))
end

function update(time)
end