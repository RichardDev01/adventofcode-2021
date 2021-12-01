List_from_site = [199,200,208,210,200,207,240,269,260,263]

_ = [print(x) for x in [f"{y[0]} (N/A - no previous measurement)" if y[0] == List_of_site[0] else f"{y[0]} (increased)" if y[0]>y[1] else f"{y[0]} (Decrease)" for y in [(x, List_of_site[index -1 ]) for index, x in enumerate(List_of_site)]]]
