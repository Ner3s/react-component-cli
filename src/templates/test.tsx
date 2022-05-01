import { screen, render } from '@testing-library/react';

import { {{ComponentName}} } from '.';

describe('<{{ComponentName}} />', () => {
  it('should render {{ComponentName}}', () => {
    render(<{{ComponentName}} />);

    expect(
      screen.getByRole('heading', {
        name: /{{ComponentName}}/i,
      }),
    ).toBeInTheDocument();
  });
});
