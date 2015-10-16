

			function CountDownTimer(dt, id)
			{
				var end = new Date(dt)
				var _second = 1000;
				var _minute = _second * 60;
				var _hour = _minute * 60;
				var _day = _hour * 24;
				var timer;
				function ShowRemaining()
				{
					var now = new Date();
					var distance =now - end;
					var days = Math.floor(distance / _day);
					var hours = Math.floor( (distance % _day) / _hour );
					var minutes = Math.floor( (distance % _hour) / _minute );
					var seconds = Math.floor( (distance % _minute) / _second );
					document.getElementById('Days').innerHTML = days
					document.getElementById('Hours').innerHTML = hours
					document.getElementById('Minutes').innerHTML = minutes
					document.getElementById('Seconds').innerHTML = seconds
				}
				timer = setInterval(ShowRemaining, 1000);
			}
