class PlanePosition:
    current_position = 0
    correction = 0.3

    # Adding necessery requirements ex. formating and statements

    def show_current_position(self):
        print
        'Current position: {}'.format(self.current_position)

    def tilt_correction(self, tilt):
        self.current_position += tilt

    def correction_flight(self):
        if self.correction == self.current_position:
            self.current_position = 0
        elif self.current_position > self.correction:
            self.current_position -= self.correction
        else:
            self.current_position += self.correction
