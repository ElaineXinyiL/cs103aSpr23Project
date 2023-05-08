import React, { useState, useEffect } from "react";
import "./styles.css";

function getItemsFromLocalStorage() {
  // getting stored value
  const saved = localStorage.getItem("transactionItems");
  const initialValue = JSON.parse(saved) || [];
  // relabel the keys from 0 to length-1
  for (let i = 0; i < initialValue.length; i++) {
    initialValue[i]["itemId"] = i;
  }
  return initialValue || [];
}

export default function Transaction() {
  const [items, setItems] = useState(getItemsFromLocalStorage);
  const [numKeys, setNumKeys] = useState(() => items.length);
  const [amount, setAmount] = useState(0);
  const [category, setCategory] = useState("");
  const [date, setDate] = useState("");
  const [description, setDescription] = useState("");
  const [summarize, setSummarize] = useState(""); // summarization mode, default is "" (all items)

  /**
   * add an item to the transaction
   * written by Yixuan He
   */
  function handleAddTransaction() {
    let newItem = {
      itemId: numKeys,
      amount: amount,
      category: category,
      date: date,
      description: description,
    };
    setNumKeys(numKeys + 1);
    setItems([newItem, ...items]); // using the spread operator ...
  }

  /**
   * delete an item from the transaction
   * written by Yixuan He
   */
  function handleDeleteTransaction(key) {
    console.log(key);
    const newItems = items.filter((x) => x["itemId"] !== key);
    setItems(newItems);
    // setNumKeys(numKeys - 1);
  }

  /**
   * summarize the transaction by date
   * written by Ruihao Shen
   */
  function summarizeByDate() {
    console.log("summarize by date");
    return items.reduce((acc, item) => {
      // copilot helped here, very smart use of reduce
      const found = acc.find((x) => x.date === item.date);
      if (found) {
        found.amount += parseFloat(item.amount);
        found.count += 1;
      } else {
        acc.push({
          date: item.date,
          amount: parseFloat(item.amount),
          count: 1,
        });
      }
      return acc;
    }, []);
  }

  /**
   * summarize the transaction by year
   * written by Hongqian Li
   */
  function summarizeByYear() {
    console.log("summarize by year");
    return items.reduce((acc, item) => {
      const year = new Date(item.date).getFullYear();
      const found = acc.find((x) => x.year === year);
      if (found) {
        found.amount += parseFloat(item.amount);
        found.count += 1;
      } else {
        acc.push({
          year: year,
          amount: parseFloat(item.amount),
          count: 1,
        });
      }
      return acc;
    }, []);
  }
  /**
   * summarize the transaction by year
   * written by Xinyi Liu
   */
  function summarizeByMonth() {
    console.log("summarize by month");
    return items.reduce((acc, item) => {
      const year = new Date(item.date).getFullYear();
      const month = new Date(item.date).getMonth() + 1;
      const found = acc.find((x) => x.year === year && x.month === month);
      if (found) {
        found.amount += parseFloat(item.amount);
        found.count += 1;
      } else {
        acc.push({
          year: year,
          month: month,
          amount: parseFloat(item.amount),
          count: 1,
        });
      }
      return acc;
    }, []);
  }

  /**
   * update the amount
   * written by Yixuan He
   */
  useEffect(() => {
    // storing items if items changes value
    localStorage.setItem("transactionItems", JSON.stringify(items));
  }, [items]);

  /**
   * content to show - all items or summarized items
   * edited by Yixuan He, Ruihao Shen, Hongqian Li, Xinyi Liu
   */
  let content;
  switch (summarize) {
    case "date":
      const summarizeItems = summarizeByDate();
      content = (
        <>
          <h2>Summarize by Date</h2>

          <table className="table table-striped">
            <thead>
              <tr>
                <th>Date</th>
                <th>Amount</th>
                <th>Item count</th>
              </tr>
            </thead>
            <tbody>
              {summarizeItems.map((item) => (
                <tr key={item.date}>
                  <td>{item.date}</td>
                  <td>{item.amount}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      );
      break;

    case "year":
      const summarizeItemsByYear = summarizeByYear();
      content = (
        <>
          <h2>Summarize by Year</h2>

          <table className="table table-striped">
            <thead>
              <tr>
                <th>Year</th>
                <th>Amount</th>
                <th>Item count</th>
              </tr>
            </thead>
            <tbody>
              {summarizeItemsByYear.map((item) => (
                <tr key={item.year}>
                  <td>{item.year}</td>
                  <td>{item.amount}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      );
      break;
    case "month":
      const summarizeItemsByMonth = summarizeByMonth();
      content = (
        <>
          <h2>Summarize by Month</h2>

          <table className="table table-striped">
            <thead>
              <tr>
                <th>Month</th>
                <th>Amount</th>
                <th>Item count</th>
              </tr>
            </thead>
            <tbody>
              {summarizeItemsByMonth.map((item) => (
                <tr key={item.month}>
                  <td>{item.year}-{item.month}</td>
                  <td>{item.amount}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <pre>
          {JSON.stringify(summarizeItemsByMonth, null, 5)}
          </pre>
        </>
      );
      break;
    default:
      content = (
        <>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Item ID</th>
                <th>Amount</th>
                <th>Category</th>
                <th>Date</th>
                <th>Description</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              {items.map((transaction) => (
                <tr key={transaction.itemId}>
                  <td>{transaction.itemId}</td>
                  <td>{transaction.amount}</td>
                  <td>{transaction.category}</td>
                  <td>{transaction.date}</td>
                  <td>{transaction.description}</td>
                  <td>
                    <button
                      onClick={() =>
                        handleDeleteTransaction(transaction.itemId)
                      }
                      class="btn btn-primary"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          <h2> add new transaction </h2>
          <form class="mb-3 g-3" onSubmit={handleAddTransaction}>
            <div class="col-md-6">
              <label class="form-label">
                Amount:
                <input
                  type="number"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                  class="form-control"
                />
              </label>
            </div>
            <div class="col-md-6">
              <label class="form-label">
                Category:
                <input
                  type="text"
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                  class="form-control"
                />
              </label>
            </div>
            <div class="col-md-6">
              <label class="form-label">
                Date:
                <input
                  type="date"
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                  class="form-control"
                />
              </label>
            </div>
            <div class="col-md-6">
              <label class="form-label">
                Description:
                <input
                  type="text"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  class="form-control"
                />
              </label>
            </div>
            <button type="submit" class="btn btn-primary">
              Add Transaction
            </button>
          </form>
        </>
      );
  }

  return (
    <div className="App container">
      <h1 className="bg-warning text-center p-2">Transaction</h1>

      <div className="container">
        <button
          type="button"
          class="btn btn-primary me-2"
          onClick={() => setSummarize("")}
        >
          Show all transactions
        </button>
        <button
          type="button"
          class="btn btn-primary me-2"
          onClick={() => setSummarize("date")}
        >
          Summarize by date
        </button>
        <button
          type="button"
          class="btn btn-primary me-2"
          onClick={() => setSummarize("month")}
        >
          Summarize by month
        </button>
        <button
          type="button"
          class="btn btn-primary me-2"
          onClick={() => setSummarize("year")}
        >
          Summarize by year
        </button>
        <button
          type="button"
          class="btn btn-primary me-2"
          onClick={() => setSummarize("category")}
        >
          Summarize by category
        </button>
      </div>

      {content}
    </div>
  );
}
