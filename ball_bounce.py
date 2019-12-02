 

def ball_drop_r(height, bounciness, num_bounces):
    # recursive solution
    if num_bounces > 0:
        new_height = height*bounciness
        bounce_distance = height + new_height
        return bounce_distance + ball_drop_r(new_height, bounciness, num_bounces-1)
    else:
        return 0

print(ball_drop_r(10, 0.6, 2))
print(ball_drop_r(25, 0.5, 3))


def ball_drop_l(height, bounciness, num_bounces):
    # linear solution
    total_distance = 0
    for each_bounce in range(num_bounces):
        new_height = height*bounciness
        bounce_distance = height + new_height
        total_distance += bounce_distance
        height = new_height
    return total_distance


print(ball_drop_l(10, 0.6, 2))
print(ball_drop_l(25, 0.5, 3))


def ball_drop_w(height, bounciness, num_bounces):
    # or with a while loop
    total_distance = 0
    while num_bounces > 0:
        new_height = height*bounciness
        bounce_distance = height + new_height
        total_distance += bounce_distance
        height = new_height
        num_bounces -= 1
    return total_distance

print(ball_drop_w(10, 0.6, 2))
print(ball_drop_w(25, 0.5, 3))
