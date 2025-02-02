// TODO [x]: swap ~=
// TODO [x]: Change FN by number in lower
// TODO [x]: add home, end to raise
// TODO [x]: add FN to number layer in both lower and raise
// TODO [x]: Make space shift with mod tap

#include QMK_KEYBOARD_H

#ifdef CONSOLE_ENABLE
#include "print.h"
#endif

enum {
  TD_CTRL_TAB_ENUM = 0
};

qk_tap_dance_action_t tap_dance_actions[] = {
  [TD_CTRL_TAB_ENUM] = ACTION_TAP_DANCE_DOUBLE(KC_RCTRL, KC_LGUI)
};

// enum custom_keycodes {
//     _ALT_G = SAFE_RANGE,
// };
#define _ALT_SPC LALT(KC_SPC)
#define _CTL_X LCTL(KC_X)
#define _CTL_C LCTL(KC_C)
#define _CTL_V LCTL(KC_V)

enum layer_number {
  _QWERTY = 0,
  _LOWER,
  _RAISE,
  _ADJUST,
};

// Custom defines
#define SPC_LSFT LSFT_T(KC_SPC)
#define ENT_LSFT LSFT_T(KC_ENT)
#define TD_CTRL_TAB TD(TD_CTRL_TAB_ENUM)


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

/* QWERTY
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * | LGUI |  1   |  2   |  3   |  4   |  5   |                    |  6   |  7   |  8   |  9   |  0   |  `   |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * | TAB  |  q   |  w   |  e   |  r   |  t   |                    |  y   |  u   |  i   |  o   |  p   |  -   |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * | ESC  |  a   |  s   |  d   |  f   |  g   |                    |  h   |  j   |  k   |  l   |  ;   |  '   |
 * |------+------+------+------+------+------|-------.    ,-------|------+------+------+------+------+------|
 * | LSFT |  z   |  x   |  c   |  v   |  b   |  [    |    |  ]    |  n   |  m   |  ,   |  .   |  /   | RSFT |
 * `------+------+------+------+------+------|-------/    \-------|------+------+------+------+------+------|
 *                   | LALT |LCTRL |LOWER | /SPC_LS /      \ENT_LS \  |RAISE | BSPC |TD_CTR|
 *                   |      |      |      |/       /        \       \ |      |      |      |
 *                   `----------------------------'          '-------''--------------------'
 *                                                                               generated by [keymapviz] */
 [_QWERTY] = LAYOUT( \
  KC_LGUI,  KC_1,   KC_2,    KC_3,    KC_4,    KC_5,                     KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_GRV, \
  KC_TAB,   KC_Q,   KC_W,    KC_E,    KC_R,    KC_T,                     KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_MINS, \
  KC_ESC,   KC_A,   KC_S,    KC_D,    KC_F,    KC_G,                     KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, KC_QUOT, \
  KC_LSFT,  KC_Z,   KC_X,    KC_C,    KC_V,    KC_B, KC_LBRC,  KC_RBRC,  KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH,  KC_RSFT, \
                      KC_LALT, KC_LCTRL, MO(_LOWER), SPC_LSFT, ENT_LSFT, MO(_RAISE), KC_BSPC, TD_CTRL_TAB \
),

/* LOWER
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * | F12  |  F1  |  F2  |  F3  |  F4  |  F5  |                    |  F6  |  F7  |  F8  |  F9  | F10  | F11  |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |  `   |  1   |  2   |  3   |  4   |  5   |                    |  6   |  7   |  8   |  9   |  0   | PSCR |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |  `   |  !   |  @   |  #   |  $   |  %   |                    |  ^   |  &   |  *   |  (   |  )   |  \   |
 * |------+------+------+------+------+------|-------.    ,-------|------+------+------+------+------+------|
 * |      |      |      |      |  ~   |  =   |       |    |       |  -   |  _   |  +   |  {   |  }   |  |   |
 * `------+------+------+------+------+------|-------/    \-------|------+------+------+------+------+------|
 *                   |      |      |      | /       /      \       \  |      | DEL  |      |
 *                   |      |      |      |/       /        \       \ |      |      |      |
 *                   `----------------------------'          '-------''--------------------'
 *                                                                               generated by [keymapviz] */
[_LOWER] = LAYOUT( \
  KC_F12,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,                     KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11, \
  KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                      KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    XXXXXXX, \
  KC_GRV,  KC_EXLM, KC_AT,   KC_HASH, KC_DLR,  KC_PERC,                   KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, KC_BSLS, \
  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC_TILD, KC_EQL, _______, _______, KC_MINS, KC_UNDS, KC_PLUS, KC_LCBR, KC_RCBR, KC_PIPE, \
                             _______, _______, _______, _______, _______,  _______, KC_DEL, _______\
),

/* RAISE
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * | F12  |  F1  |  F2  |  F3  |  F4  |  F5  |                    |  F6  |  F7  |  F8  |  F9  | F10  | F11  |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      |      |      | END  |      |      |                    |      |      |      |      |      | PSCR |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      | HOME |      |      |      |      |                    | LEFT | DOWN |  UP  | RGHT |      |      |
 * |------+------+------+------+------+------|-------.    ,-------|------+------+------+------+------+------|
 * |      |      |      |      |      |      |       |    |       |      |      |      |      |      |      |
 * `------+------+------+------+------+------|-------/    \-------|------+------+------+------+------+------|
 *                   |      |      |      | /       /      \       \  |      |      |      |
 *                   |      |      |      |/       /        \       \ |      |      |      |
 *                   `----------------------------'          '-------''--------------------'
 *                                                                               generated by [keymapviz] */
[_RAISE] = LAYOUT( \
  KC_F12,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,                       KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11, \
  XXXXXXX, XXXXXXX, XXXXXXX, KC_END,  XXXXXXX, XXXXXXX,                     XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC_PSCR, \
  XXXXXXX, KC_HOME, XXXXXXX, XXXXXXX, _ALT_SPC,XXXXXXX,                     KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT, XXXXXXX, XXXXXXX, \
  XXXXXXX, XXXXXXX, _CTL_X,  _CTL_C,  _CTL_V,  XXXXXXX,   _______, _______, KC_LEAD, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
                             _______, _______, _______,  _______, _______,  _______, _______, _______ \
),

/* ADJUST
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * |      |      |      |      |      |      |                    |      |      |      |      |      |      |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      |      |      |      |      |      |                    |      |      |      |      |      |      |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      |      |      |      |      |      |-------.    ,-------|      |      |RGB ON| HUE+ | SAT+ | VAL+ |
 * |------+------+------+------+------+------|       |    |       |------+------+------+------+------+------|
 * |      |      |      |      |      |      |-------|    |-------|      |      | MODE | HUE- | SAT- | VAL- |
 * `-----------------------------------------/       /     \      \-----------------------------------------'
 *                   | LAlt | LGUI |LOWER | /Space  /       \Enter \  |RAISE |BackSP| RGUI |
 *                   |      |      |      |/       /         \      \ |      |      |      |
 *                   `----------------------------'           '------''--------------------'
 */
  [_ADJUST] = LAYOUT( \
  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                             _______, _______, _______, _______, _______,  _______, _______, _______ \
  )
};

layer_state_t layer_state_set_user(layer_state_t state) {
  return update_tri_layer_state(state, _LOWER, _RAISE, _ADJUST);
}

//SSD1306 OLED update loop, make sure to enable OLED_DRIVER_ENABLE=yes in rules.mk
#ifdef OLED_DRIVER_ENABLE

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
  if (!is_keyboard_master())
    return OLED_ROTATION_180;  // flips the display 180 degrees if offhand
  return rotation;
}

// When you add source files to SRC in rules.mk, you can use functions.
const char *read_layer_state(void);
const char *read_logo(void);
void set_keylog(uint16_t keycode, keyrecord_t *record);
const char *read_keylog(void);
const char *read_keylogs(void);

// const char *read_mode_icon(bool swap);
// const char *read_host_led_state(void);
// void set_timelog(void);
// const char *read_timelog(void);

void oled_task_user(void) {
  if (is_keyboard_master()) {
    // If you want to change the display of OLED, you need to change here
    oled_write_ln(read_layer_state(), false);
    oled_write_ln(read_keylog(), false);
    oled_write_ln(read_keylogs(), false);
    //oled_write_ln(read_mode_icon(keymap_config.swap_lalt_lgui), false);
    //oled_write_ln(read_host_led_state(), false);
    //oled_write_ln(read_timelog(), false);
  } else {
    oled_write(read_logo(), false);
  }
}
#endif // OLED_DRIVER_ENABLE

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
  #ifdef CONSOLE_ENABLE
  if (record->event.pressed) {
    // keycode, row, col, layer, pressed, time
    uprintf("0x%04X,%u,%u,%u,%b,%u\n", keycode, record->event.key.row, record->event.key.col, get_highest_layer(layer_state), record->event.pressed, record->event.time);
  }
  #endif

  if (record->event.pressed) {
    #ifdef OLED_DRIVER_ENABLE
    set_keylog(keycode, record);
    #endif
    // set_timelog();
  }

  return true;
}


/*
 * Configuration for bit-c led
*/

#ifdef BIT_C_ENABLE
    #include "bit-c/bit-c_led.h"
#endif

void keyboard_pre_init_user(void) {
    set_bit_c_LED(LED_OFF);
}


/*
 * Configuration for leader commands
*/

LEADER_EXTERNS();

void matrix_scan_user(void) {
  LEADER_DICTIONARY() {
    leading = false;
    leader_end();

    SEQ_ONE_KEY(KC_LEFT) {
      SEND_STRING(SS_DOWN(X_LGUI)SS_TAP(X_LEFT)SS_UP(X_LGUI));
    }
    SEQ_ONE_KEY(KC_RIGHT) {
      SEND_STRING(SS_DOWN(X_LGUI)SS_TAP(X_RIGHT)SS_UP(X_LGUI));
    }
    SEQ_ONE_KEY(KC_UP) {
      SEND_STRING(SS_DOWN(X_LGUI)SS_TAP(X_UP)SS_UP(X_LGUI));
    }
    SEQ_ONE_KEY(KC_DOWN) {
      SEND_STRING(SS_DOWN(X_LGUI)SS_TAP(X_DOWN)SS_UP(X_LGUI));
    }

    // SEQ_TWO_KEYS(KC_D, KC_D) {
    //   SEND_STRING(SS_LCTL("a") SS_LCTL("c"));
    // }
    // SEQ_TWO_KEYS(KC_A, KC_S) {
    //   register_code(KC_LGUI);
    //   register_code(KC_S);
    //   unregister_code(KC_S);
    //   unregister_code(KC_LGUI);
    // }
  }
}
