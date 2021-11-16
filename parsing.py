import os
import numpy as np
import pandas as pd
import regex as re


def files(path = './drive/MyDrive/games'):
    file = os.listdir(path)
    players = [file[i][8:-15] for i in range(len(file))]
    # print(len(set(players)))
    return file, players
#{ \[%\S* [0-9]*:[0-9]*:[0-9]*\] } [0-9]\.\.\.

def get_games(file, player):
    white_clock = re.compile('{ \[%\S* [0-9]*:[0-9]*:[0-9]*\] } [0-9]+\.\.\.')
    black_clock = re.compile('{ \[%\S* [0-9]+:[0-9]+:[0-9]+\] }')
    pre_df = []
    with open(file) as fin:
        lines = fin.readlines()
        for i in range(len(lines)):

            if player in lines[i]:
                color = lines[i][1:6]
                if color == "White":
                    if ('Variant' in lines[i+6]):
                        variant = lines[i+6][10:-3]

                    elif ('Variant' in lines[i+7]):
                        variant = lines[i+7][10:-3]

                    elif ('Variant' in lines[i+8]):
                        variant = lines[i+8][10:-3]

                    elif ('Variant' in lines[i + 9]):
                        variant = lines[i + 9][10:-3]

                    elif ('Variant' in lines[i + 10]):
                        variant = lines[i + 10][10:-3]

                    elif ('Variant' in lines[i + 11]):
                        variant = lines[i + 11][10:-3]

                    elif ('Variant' in lines[i + 12]):
                        variant = lines[i + 12][10:-3]


                    if (len(lines[i+14]) > 60) and ('1. ' in lines[i+14]):
                        line = lines[i + 14]
                        new_line = re.sub(white_clock, str(), line)
                        newer_line = re.sub(black_clock, str(), new_line)
                        pre_df.append([player, color, variant, newer_line])

                    elif (len(lines[i+15]) > 60) and ('1. ' in lines[i+15]):
                        line = lines[i + 15]
                        new_line = re.sub(white_clock, str(), line)
                        newer_line = re.sub(black_clock, str(), new_line)
                        pre_df.append([player, color, variant, newer_line])

                    elif (len(lines[i+16]) > 60) and ('1. ' in lines[i+16]):
                        line = lines[i + 16]
                        new_line = re.sub(white_clock, str(), line)
                        newer_line = re.sub(black_clock, str(), new_line)
                        pre_df.append([player, color, variant, newer_line])


                elif color == "Black":
                    if ('Variant' in lines[i + 6]):
                        variant = lines[i + 6][10:-3]


                    elif ('Variant' in lines[i + 7]):
                        variant = lines[i + 7][10:-3]


                    elif ('Variant' in lines[i + 8]):
                        variant = lines[i + 8][10:-3]


                    elif ('Variant' in lines[i + 9]):
                        variant = lines[i + 9][10:-3]


                    elif ('Variant' in lines[i + 10]):
                        variant = lines[i + 10][10:-3]


                    elif ('Variant' in lines[i + 11]):
                        variant = lines[i + 11][10:-3]

                    elif ('Variant' in lines[i + 12]):
                        variant = lines[i + 12][10:-3]



                    if (len(lines[i+14]) > 60) and ('1. ' in lines[i+14]):
                        line = lines[i + 14]
                        new_line = re.sub(white_clock, str(), line)
                        newer_line = re.sub(black_clock, str(), new_line)
                        pre_df.append([player, color, variant, newer_line])
                        # print([player, color, newer_line])

                    elif (len(lines[i+15]) > 60) and ('1. ' in lines[i+15]):
                        line = lines[i + 15]
                        new_line = re.sub(white_clock, str(), line)
                        newer_line = re.sub(black_clock, str(), new_line)
                        pre_df.append([player, color, variant, newer_line])
                        # print([player, color, newer_line])

                    # elif (len(lines[i+16]) > 30) and ('1. ' in lines[i+16]):
                    #     line = lines[i + 16]
                    #     new_line = re.sub(white_clock, str(), line)
                    #     newer_line = re.sub(black_clock, str(), new_line)
                    #     pre_df.append([player, color, newer_line])
                    #     print([player, color, newer_line])
    return pre_df
# https://lichess.org/api/games/user/Al_shima?rated=true&analysed=true&tags=true&clocks=true&evals=false&opening=false&perfType=rapid

def create_database():
    file, players = files()
    df = []
    for i in range(len(players)):
        df.extend(get_games(path + '/' + file[i], players[i]))
    df = pd.DataFrame(df, columns=['Name', 'Color', 'Variant', 'Moves'])
    df = df[df['Variant'] == 'Standard']
    return df




def main():
    df = create_database()
    # print(df.iloc[832])
    # df.drop(833,inplace=True)
    # print(df.loc[834])
    # print(len(df))
    moves = [f'{i}.' for i in range(1,16)]
    for move in moves:
        df[move] = np.nan
    for i in range(len(df)):
        move_order = df.iloc[i].Moves
        if i >830 and i < 835:
            pass
        else:
            # print(i)
            for j in range(len(moves)-1):
                first_ind = move_order.find(moves[j])
                second_ind = move_order.find(moves[j+1])
                if second_ind == -1:
                    break
                else:
                    df.loc[i, moves[j]] = move_order[first_ind:second_ind-1]

                # break

    df.drop(df.columns[-1],axis=1,inplace=True)
    df.dropna(inplace=True)
    for i in range(len(moves)-1):
        # print(df.loc[0,moves[i]])
        df.loc[:,moves[i]] = df.loc[:,moves[i]].str[3:]
    df = df.dropna()
    df.to_csv(r'chess_games.csv', index=True, header=True)
    return



if __name__ == "__main__":
    print(main())
