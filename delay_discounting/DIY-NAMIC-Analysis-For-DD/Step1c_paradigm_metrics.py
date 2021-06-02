# Author: SC
# Based on code written by JHL and KN


from natsort import natsorted, ns
from Step1b_metric_calculations import *
from statistics import mode

## P1
all_trials_total = ['520', '5520', '520']; FC_trials_reward = ['72270', '82270', '92270']
FC_response_window = ['72589', '82589', '92589']; FC_iti_window = ['72519', '82519', '92519']
FC_reward_window = ['72549','82549','92549']; total_pokes = ['7071','8071','9071']


## P2
trials_reward = ['71270', '81270', '91270']; iti_window = ['71519', '81519', '91519']
response_window = ['71589', '81589', '91589']; reward_window = ['71549', '81549', '91549']
valid_trials = ['71170','00000','91170']

## P3
initiation_window = ['7529', '8529', '9529']


## P4
FC_valid_trials = ['72170','92170','62170']

## P5
trials_omission = ['71540', '81540', '91540']; FC_trials_omission = ['72540', '82540', '92540']
FC_trials_incorrect = ['72160', '82160', '92160']

## P6
delay_window = ['71559','81559','91559']; FC_delay_window = ['72559','82559','92559']

def return_metric_output_df(m_head_dict, m_parsed_dt_df, start_parsetime):
    """
    :param m_head_dict:
    :param m_parsed_dt_df:
    :param start_parsetime:
    :return:
    """

    ## Getting the accurate paradigm (going to use 'mode' method since different Arduinos can run on different schedule)
    ## thus each processing file might be running different paradigms! --> In the future, maybe make separate folder for each paradigms

    ## Getting the Correct Paradigm (using mode)

    paradigm_list = []
    for keys in m_head_dict.keys():
        p = m_head_dict[keys]['Paradigm']
        paradigm_list.append(p)

    paradigm = mode(paradigm_list)

    ## ALL THE METRICS! --> Add more if necessary
    total_poke_count = count_events3(m_parsed_dt_df, start_parsetime, total_pokes)
    all_trials_count = count_events3(m_parsed_dt_df, start_parsetime, all_trials_total)
    iw_count = counts_during_window3(m_parsed_dt_df, start_parsetime, initiation_window)
    FC_reward_count = count_events4(m_parsed_dt_df, start_parsetime, FC_trials_reward)
    reward_count = count_events4(m_parsed_dt_df, start_parsetime, trials_reward)
    FC_iti_count = counts_during_window4(m_parsed_dt_df, start_parsetime, FC_iti_window)
    iti_count = counts_during_window4(m_parsed_dt_df, start_parsetime, iti_window)
    FC_rw_count = counts_during_window4(m_parsed_dt_df, start_parsetime, FC_response_window)
    rw_count = counts_during_window4(m_parsed_dt_df, start_parsetime, response_window)
    FC_delay_count = counts_during_window4(m_parsed_dt_df, start_parsetime, FC_delay_window)
    delay_count = counts_during_window4(m_parsed_dt_df, start_parsetime, delay_window)
    FC_valid_count = count_events4(m_parsed_dt_df, start_parsetime, FC_valid_trials)
    valid_count = count_events4(m_parsed_dt_df, start_parsetime, valid_trials)
    FC_invalid_count = count_events4(m_parsed_dt_df, start_parsetime, FC_trials_incorrect)
    FC_omission_count = count_events4(m_parsed_dt_df, start_parsetime, FC_trials_omission)
    omission_count = count_events4(m_parsed_dt_df, start_parsetime, trials_omission)
    FC_reward_window_count = counts_during_window4(m_parsed_dt_df, start_parsetime, FC_reward_window)
    reward_window_count = counts_during_window4(m_parsed_dt_df, start_parsetime, reward_window)

    ## initialize with empty dataframe
    metric_df = pd.DataFrame()

    # #### Option 1 (return metric_dfs depending on the paradigms!)
    #
    # ## Note of Caution - when using boolean, strings always evaluates to TRUE unless an empty string
    # ## https://stackoverflow.com/questions/32703714/if-statement-somehow-always-true
    #
    # if paradigm in ["P1", "P2"]:
    #     metric_df = pd.concat([total_poke_count, reward_count])#, rw_count, iti_count])
    # elif paradigm in ["P3", "P4"]:
    #     metric_df = pd.concat([total_poke_count, reward_count, rw_count, iti_count, valid_count])
    # elif paradigm in ["P5", "P5_5"]:
    #     metric_df = pd.concat([total_poke_count, initiated_count, reward_count, rw_count, iti_count, reward_window_count, valid_count, invalid_count, omission_count])
    # elif paradigm in ["P6_3", "P6_6", "P6_9"]:
    #     metric_df = pd.concat([total_poke_count, initiated_count, reward_count, rw_count, iti_count, delay_count, reward_window_count,
    #          valid_count, invalid_count, omission_count])
    # else:
    #     print ("Invalid paradigm. Update the valid paradigm list or check the Raw Processing Files to confirm accurate paradigm in each txt file")


    #### Option 2 (return ALL parameters for every paradigm!)

    # for DD
    valid_paradigm_list =  ["P1", "P2", "P3", "P4","P5","P6","P4_rl", "P4_ll", "P4-rl", "P4-ll","P5_rl", "P5_ll", "P5-rl", "P5-ll", \
                            "P6_rl", "P6_ll", "P6-rl", "P6-ll", "P6-2_rl", "P6-2_ll", "P6-2-rl", "P6-2-ll", "P6_2_rl", "P6_2_ll", "P6_2-rl", "P6_2-ll",\
                            "P6_4", "P6-4_rl", "P6-4_ll", "P6-4-rl", "P6-4-ll", "P6_4_rl", "P6_4_ll", "P6_4-rl", "P6_4-ll", \
                            "P6_6", "P6-6_rl", "P6-6_ll", "P6-6-rl", "P6-6-ll", "P6_6_rl", "P6_6_ll", "P6_6-rl", "P6_6-ll",\
                            "P6_8", "P6-8_rl", "P6-8_ll", "P6-8-rl", "P6-8-ll", "P6_8_rl", "P6_8_ll", "P6_8-rl", "P6_8-ll", \
                            "P6_10", "P6-10_rl", "P6-10_ll", "P6-10-rl", "P6-10-ll", "P6_10_rl", "P6_10_ll", "P6_10-rl", "P6_10-ll", \
                            "P6_12", "P6-12_rl", "P6-12_ll", "P6-12-rl", "P6-12-ll", "P6_12_rl", "P6_12_ll", "P6_12-rl", "P6_12-ll"]

    # for 2-choice data (USE THIS LIST IF USING SAMPLE DATA FROM PREV PARADIGMS)
    # valid_paradigm_list =  ["P1", "P2", "P3", "P4", "P5", "P5_5", "P6_3", "P6_6", "P6_9", "P5-5", "P6-3", "P6-6", "P6-9", "P4-RR5"]

    ## returns ALL the parameters for every paradigm (for ex: returns delay window even for P1)
    if paradigm in valid_paradigm_list:
        metric_df = pd.concat([total_poke_count, all_trials_count, iw_count, FC_reward_count, reward_count, \
                               FC_rw_count, rw_count, FC_iti_count, iti_count, FC_delay_count, delay_count, \
                               FC_reward_window_count, reward_window_count, FC_valid_count, valid_count, \
                               FC_invalid_count, FC_omission_count, omission_count])
    else:
        raise TypeError ("Invalid paradigm. Update the valid paradigm list or check the Raw Processing Files to confirm accurate paradigm in each txt file.")

    return metric_df, paradigm

## ## Getting the EARLIEST start time and the LATEST End Time (to determine the actual hours to parse)

def actual_start_end_times(m_head_dict):

    start_time_list = []
    for keys in m_head_dict.keys():
        start_t = m_head_dict[keys]['Start Time']
        start_time_list.append(start_t)

    end_time_list = []
    for keys in m_head_dict.keys():
        end_t = m_head_dict[keys]['End Time']
        end_time_list.append(end_t)

    start_day_list = []
    for keys in m_head_dict.keys():
        start_d = m_head_dict[keys]['Start Date']
        start_day_list.append(start_d)

    end_day_list = []
    for keys in m_head_dict.keys():
        end_d = m_head_dict[keys]['End Date']
        end_day_list.append(end_d)


    start_time_list = natsorted(start_time_list)
    end_time_list = natsorted(end_time_list)
    start_day_list = natsorted(start_day_list)
    end_day_list = natsorted(end_day_list)

    sd = start_day_list[0]
    st = start_time_list[0]
    ed = end_day_list[0]
    et = end_time_list[0]

    print("Start Day: {} - Start Time: {}".format(sd, st))
    print("End Day: {} - End Time: {}".format(ed, et))

    print("Make sure to parse for 23 HOURS!!")

    # return start_day_list[0], start_time_list[0], end_day_list[-1], end_time_list[-1]
