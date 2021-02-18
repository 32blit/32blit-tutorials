set(TUTORIAL_NAME 09-faking-mode-7)

blit_executable (${TUTORIAL_NAME} main.cpp main.hpp)
# blit_assets_yaml (${TUTORIAL_NAME} assets.yml)
blit_metadata (${TUTORIAL_NAME} metadata.yml)

install (FILES ../README.md DESTINATION . RENAME ${TUTORIAL_NAME}.md)