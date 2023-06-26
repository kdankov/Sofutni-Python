volume = int(input())
p1_flow_rate = int(input())
p2_flow_rate = int(input())
hours = float(input())

total_pipe_filling = p1_flow_rate * hours + p2_flow_rate * hours

if total_pipe_filling <= volume:
    percentage_filled = total_pipe_filling / volume * 100
    p1_percentage = (p1_flow_rate * hours / total_pipe_filling) * 100
    p2_percentage = (p2_flow_rate * hours / total_pipe_filling) * 100
    print(f'The pool is {percentage_filled:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.')
else:
    print(f'For {hours:.2f} hours the pool overflows with {total_pipe_filling - volume:.2f} liters.')