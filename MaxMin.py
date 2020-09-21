largest = None
smallest = None
while True:
num = input(&quot;Enter a number: &quot;)
if num == &quot;done&quot;: break

try:
num = int(num)
if largest is None or largest &lt; num: largest = num
if smallest is None or smallest &gt; num: smallest = num
except:
print (&quot;Invalid input&quot;)
continue
print (&quot;Maximum is&quot;,largest)
print (&quot;Minimum is&quot;,smallest)