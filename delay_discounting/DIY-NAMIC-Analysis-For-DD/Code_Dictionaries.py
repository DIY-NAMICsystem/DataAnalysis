## By SC
## Adapted from JHL

# Information about Abbreviations #

# x2xxx: Forced Choice Trial
# x1xxx: Free Choice Trial

# itiw: iti window; rw: response window; iw: initiation window; invalid: incorrect trial; rwrdw: reward window

# valid trial: no omissions or incorrect pokes; counted by the number of times a poke leads to reward
# valid trials = to all_trials_total for P1 (so, no valid trial count)

# reward count: counts the number of drops given in all trials, forced choice trials or free choice trials
# pokes during reward window: counts the pokes made from when the reward was given and the reward cue turns off

# first window: response window for P1 & P2 + initiation window for other paradigms


## Arduino Event Codes
event_code_dict = {'71171': 'L_led_Valid_ON',  '72171': 'L_FC_led_Valid_ON',  '7071': 'L_Poke_Valid_IN',
                   '71170': 'L_led_Valid_OFF', '72170': 'L_FC_led_Valid_OFF', '7070': 'L_Poke_Valid_OUT',
                   '81171': 'M_led_Valid_ON',  '82171': 'M_FC_led_Valid_ON',  '8071': 'M_Poke_Valid_IN',
                   '81170': 'M_led_Valid_OFF', '82170': 'M_FC_led_Valid_OFF', '8070': 'M_Poke_Valid_OUT',
                   '91171': 'R_led_Valid_ON',  '92171': 'R_FC_led_Valid_ON',  '9071': 'R_Poke_Valid_IN',
                   '91170': 'R_led_Valid_OFF', '92170': 'R_FC_led_Valid_OFF', '9070': 'R_Poke_Valid_OUT',

                   '71271': 'L_sol_Valid_ON',  '72271': 'L_FC_sol_Valid_ON',
                   '71270': 'L_sol_Valid_OFF', '72270': 'L_FC_sol_Valid_OFF',
                   '81271': 'M_sol_Valid_ON',  '82271': 'M_FC_sol_Valid_ON',
                   '81270': 'M_sol_Valid_OFF', '82270': 'M_FC_sol_Valid_OFF',
                   '91271': 'R_sol_Valid_ON',  '92271': 'R_FC_sol_Valid_ON',
                   '91270': 'R_sol_Valid_OFF', '92270': 'R_FC_sol_Valid_OFF',

                   '71160': 'L_led_Invalid_OFF', '72160': 'L_FC_led_Invalid_OFF',
                   '81160': 'M_led_Invalid_OFF', '82160': 'L_FC_led_Invalid_OFF',
                   '91160': 'R_led_Invalid_OFF', '92160': 'L_FC_led_Invalid_OFF',

                   '71519': 'L_itiw',  '71589': 'L_rw',  '71559': 'L_delay_w', '7529': 'L_iw', '71549': 'L_rwrdw',
                   '81519': 'M_itiw',  '81589': 'M_rw',  '81559': 'M_delay_w', '8529': 'M_iw', '81549': 'M_rwrdw',
                   '91519': 'R_itiw',  '91589': 'R_rw',  '91559': 'R_delay_w', '9529': 'R_iw', '91549': 'R_rwrdw',

                   '72519': 'L_FC_itiw', '72589': 'L_FC_rw', '72559': 'L_FC_delay_w', '72549': 'L_FC_rwrdw',
                   '82519': 'M_FC_itiw', '82589': 'M_FC_rw', '82559': 'M_FC_delay_w', '82549': 'M_FC_rwrdw',
                   '92519': 'R_FC_itiw', '92589': 'R_FC_rw', '92559': 'R_FC_delay_w', '92549': 'R_FC_rwrdw',

                   '71540' :'Left Omission', '81540' :'Middle Omission', '91540' :'Right Omission',
                   '72540': 'FC Left Omission', '82540': 'FC Middle Omission', '92540': 'FC Right Omission',

                   '5520' :'First_Window_End',
                   '5521' :'First_Window_Start'}


## Multiple Keys for single value (to use for merging metrics)
metric_code_to_dict = {
    ('total_trials', 'all_trials_total'): 'x520',
    ('paradigm_total', 'total_pokes', 'pokes_paradigm_total'): 'x071',
    ('reward', 'trials_reward'): 'x1270',
    ('FC_reward', 'FC_trials_reward'): 'x2270',
    ('valid', 'valid_trials','trials_valid_ports'): 'x1170',
    ('FC_valid', 'FC_valid_trials','FC_trials_valid_ports'): 'x2170',
    ('initiation_window', 'iw', 'pokes_initiation_window'): 'x529',
    ('response_window', 'rw', 'pokes_response_window'): 'x1589',
    ('FC_response_window', 'FC_rw', 'FC_pokes_response_window'): 'x2589',
    ('reward_window', 'rwrdw', 'pokes_reward_window'): 'x1549',
    ('FC_reward_window', 'FC_rwrdw', 'FC_pokes_reward_window'): 'x2549',
    ('iti_window', 'iti', 'pokes_iti_window'): 'x1519',
    ('FC_iti_window', 'FC_iti', 'FC_pokes_iti_window'): 'x2519',
    ('delay_window', 'dw', 'pokes_delay_window'): 'x1559',
    ('FC_delay_window', 'FC_dw', 'FC_pokes_delay_window'): 'x2559',
    ('omission', 'trials_omission'): 'x1540',
    ('FC_omission', 'FC_trials_omission'): 'x2540',
    ('FC_incorrect', 'FC_trials_incorrect'): 'x2160'
}

## For plotting (NOT UPDATED FOR DD) (by JHL)
# plot_code_dict = {"pokes_delay_window_dark": "Pokes during the Delay Window",
#                   "pokes_iti_window_dark": "Pokes during the ITI Window",
#                   "pokes_paradigm_total_dark": "Total Nosepokes",
#                   "pokes_trial_window_dark":"Incorrect pokes during: [Cue Window (P1/P2)] / [Trial Initiation Window (P3+)]",
#                   "pokes_reward_window_dark":"Pokes during the Reward Window",
#                   "trials_incorrect_dark": "Total Number of Incorrect Trials",
#                   "trials_initiated_dark" : "Total Number of Initiated Trials",
#                   "trials_omission_dark":"Total Number of Omission Trials",
#                   "trials_reward_dark": "Total Number of Rewards",
#                   "trials_valid_ports_dark": "Total Pokes in Valid Ports (correct pokes)",
#
#                   "pokes_reward_window_23hr":"Pokes during the Reward Window (23hr)",
#                   "pokes_delay_window_23hr":"Pokes during the Delay Window (23 hours)",
#                   "pokes_iti_window_23hr": "Pokes during the ITI Window (23 hours)",
#                   "pokes_paradigm_total_23hr": "Total Nosepokes (23 hours)",
#                   "pokes_trial_window_23hr":"Incorrect pokes during: [Cue Window (P1/P2)] / [Trial Initiation Window (P3+)]",
#                   "trials_incorrect_23hr": "Total Number of Incorrect Trials (23 hours)",
#                   "trials_initiated_23hr" : "Total Number of Initiated Trials (23 hours)",
#                   "trials_omission_23hr":"Total Number of Omission Trials (23 hours)",
#                   "trials_reward_23hr": "Total Number of Rewards (23 hours)",
#                   "trials_valid_ports_23hr": "Total Pokes in Valid Ports (23 hrs)",
#
#
#                   "pct_dark": "Percentage of Correct Trials",
#                   "pct_23hr": "Percentage of Correct Trials (23hr)",
#                   "inc_pct_dark": "Percentage of Incorrect Trials",
#                   "ipct_23hr": "Percentage of Incorrect Trials (23hrs)",
#                   "correct_attempted_pct_23hr": "Percentage of Correct Attempted Trials (23hr)",
#                   "correct_attempted_pct_dark": "Percentage of Correct Attempted Trials",
#                   "incorrect_attempted_pct_23hr": "Percentage of Incorrect Attempted Trials (23hr)",
#                   "incorrect_attempted_pct_dark": "Percentage of Incorrect Attempted Trials"
#             }
#
#
