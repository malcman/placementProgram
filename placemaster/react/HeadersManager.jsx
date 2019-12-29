import React from 'react';
import ToggleSortHeader from './ToggleSortHeader';

class HeadersManager extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentSort: props.currentSort,
    };
    this.selectActiveHeader = this.selectActiveHeader.bind(this);
  }

  selectActiveHeader(headerName) {
    this.setState({
      currentSort: headerName,
    });
  }

  getSortHeaders() {
    const headers = [];
    this.props.headers.forEach((header) => {
      const newHeader = (<ToggleSortHeader
        headerName={header}
        key={header}
        active={header === this.state.currentSort}
        setSortHandler={this.selectActiveHeader}
      />);
      headers.push(newHeader);
    });
    return headers;
  }

  render() {
    const sortHeaders = this.getSortHeaders();
    return (
      <div className="headersContainer">
        {sortHeaders}
      </div>
    );
  }
}

export default HeadersManager;
