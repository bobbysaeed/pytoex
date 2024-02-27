# Subset the following lists from color list:

# bl_gr = ['blue', 'green']
# re_gr_br = ['red', 'green', 'brown']
# pk_br_yl = ['pink', 'brown', 'yellow']

colors = ['red', 'blue', 'green', 'yellow', 'brown', 'pink']
bl_gr = colors[1:3]
re_gr_br = colors[::2]
pk_br_yl = colors[-1:-4:-1]

# print(
#     colors[-1:-4],
#     colors[-4:-1],
#     colors[-1:-4:-1],
#     colors[-4:-1:-1]
# )