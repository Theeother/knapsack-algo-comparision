import sys
import numpy as np
import matplotlib.pyplot as plt


def avg(l):
    return sum(l)/len(l)


def plot(data):
    teams = ["Team 1", "Team 2"]
    metrics = ['time', 'accuracy']
    for metric in metrics:
        for team in teams:
            plot_metrics_per_method_per_scale(data, metric, team)

    for team in teams:
        plot_percentage_invalid_results(data, team)

    for team in teams:
        scatter_plot_accuracy_time(data, team)

    plot_accuracy_per_team_per_scale(data)

    plot_time_per_team_per_scale(data)


# histograms of each algorithm for each team accuarcy mean
def plot_metrics_per_method_per_scale(data, metric, team):
    x = np.arange(len(data['low_scale'][team].keys()))
    print(x, list(data['low_scale'][team].keys()))
    plt.bar(x-0.1, [avg(j[metric+'_list'])
            for j in [i for i in data['low_scale'][team].values()]], 0.2, rot=90)
    plt.bar(x+0.1, [avg(j[metric+'_list'])
            for j in [i for i in data['large_scale'][team].values()]], 0.2, rot=90)
    plt.xticks(x, list(data['low_scale'][team].keys()))
    plt.xlabel(team.capitalize()+" Algorithms", fontsize=15)
    plt.ylabel(metric.capitalize() + " Mean", fontsize=15)
    plt.title(metric.capitalize()+" of each algorithm for "+team)
    plt.legend(["Low Scale", "Large Scale"])
    # save the plot in the current directory
    plt.savefig("Tests/plots/"+metric+"_per_method_per_scale_"+team+".png")
    plt.show()


def plot_percentage_invalid_results(data, team):
    x = np.arange(len(data['low_scale'][team].keys()))
    plt.bar(x-0.1, [(len(j['time_list'])-j['nb_valid'])/len(j['accuracy_list'])
            for j in [i for i in data['low_scale'][team].values()]], 0.2)
    plt.bar(x+0.1, [(len(j['time_list'])-j['nb_valid'])/len(j['accuracy_list'])
            for j in [i for i in data['large_scale'][team].values()]], 0.2)
    plt.xticks(x, list(data['low_scale'][team].keys()))
    plt.xlabel(team.capitalize()+" Algorithms", fontsize=15)
    plt.ylabel("Percentage of invalid results")
    plt.title("Percentage of invalid results for each algorithm "+team)
    plt.legend(["Low Scale", "Large Scale"])
    plt.savefig("Tests/plots/"+"percentage_invalid_results_"+team+".png")
    plt.show()


def scatter_plot_accuracy_time(data, team):
    average_accuracy = [avg(j['accuracy_list'])
                        for j in [i for i in data['low_scale'][team].values()]]

    # list of average time for each algorithm
    average_time = [avg(j['time_list'])
                    for j in [i for i in data['low_scale'][team].values()]]

    plt.scatter(average_accuracy, average_time, c="blue")
    plt.xlabel("Accuracy")
    plt.ylabel("Time")
    plt.title("Accuracy vs Time for "+team)
    plt.savefig("Tests/plots/"+"accuracy_vs_time_"+team+".png")
    plt.show()


def plot_time_per_team_per_scale(data):
    low_scale_time_team1 = [avg(j['time_list']) for j in [
        i for i in data['low_scale']['Team 1'].values()]]
    low_scale_time_team2 = [avg(j['time_list']) for j in [
        i for i in data['low_scale']['Team 2'].values()]]
    large_scale_time_team1 = [avg(j['time_list']) for j in [
        i for i in data['large_scale']['Team 1'].values()]]
    large_scale_time_team2 = [avg(j['time_list']) for j in [
        i for i in data['large_scale']['Team 2'].values()]]
    low_scale_avg_time_team1 = avg(low_scale_time_team1)
    low_scale_avg_time_team2 = avg(low_scale_time_team2)
    large_scale_avg_time_team1 = avg(large_scale_time_team1)
    large_scale_avg_time_team2 = avg(large_scale_time_team2)

    x = np.arange(2)
    plt.bar(x-0.1, [low_scale_avg_time_team1, low_scale_avg_time_team2], 0.2)
    plt.bar(x+0.1, [large_scale_avg_time_team1,
            large_scale_avg_time_team2], 0.2)

    plt.xticks(x, list(data['low_scale'].keys()))
    plt.xlabel("Teams", fontsize=15)
    plt.ylabel("Time")
    plt.title("Time of each team")
    plt.legend(["Low Scale", "Large Scale"])
    plt.savefig("Tests/plots/"+"time_per_team_per_scale.png")
    plt.show()


def plot_accuracy_per_team_per_scale(data):
    low_scale_Accuracy_team1 = [avg(j['accuracy_list']) for j in [
        i for i in data['low_scale']['Team 1'].values()]]
    low_scale_Accuracy_team2 = [avg(j['accuracy_list']) for j in [
        i for i in data['low_scale']['Team 2'].values()]]
    large_scale_Accuracy_team1 = [avg(j['accuracy_list']) for j in [
        i for i in data['large_scale']['Team 1'].values()]]
    large_scale_Accuracy_team2 = [avg(j['accuracy_list']) for j in [
        i for i in data['large_scale']['Team 2'].values()]]

    low_scale_avg_Accuracy_team1 = avg(low_scale_Accuracy_team1)
    low_scale_avg_Accuracy_team2 = avg(low_scale_Accuracy_team2)
    large_scale_avg_Accuracy_team1 = avg(large_scale_Accuracy_team1)
    large_scale_avg_Accuracy_team2 = avg(large_scale_Accuracy_team2)
    x = np.arange(2)
    plt.bar(x-0.1, [low_scale_avg_Accuracy_team1,
            low_scale_avg_Accuracy_team2], 0.2)
    plt.bar(x+0.1, [large_scale_avg_Accuracy_team1,
            large_scale_avg_Accuracy_team2], 0.2)

    plt.xticks(x, list(data['low_scale'].keys()))
    plt.xlabel("Teams", fontsize=15)
    plt.ylabel("Accuracy")
    plt.title("Accuracy of each team")
    plt.legend(["Low Scale", "Large Scale"])
    plt.savefig("Tests/plots/"+"Accuracy of each team.png")
    plt.show()
