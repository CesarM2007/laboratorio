import Image from 'next/image'
import styles from './page.module.css'
import Navbar from './components/navbar'

export default function Home() {
  return (
    <main className={styles.main}>
      <Navbar></Navbar>
      <header id="header"className={styles.header}>
        <div>
          <h1>
          <span>
              Hello<span className={styles.yellowText}>.</span>
            </span>
            <br />
            <span>
              <span>I am</span>
            </span>
            <br />
            <span>César Rodríguez</span>
          </h1>
        </div>
      </header>
      <section id="info"className={styles.infoSection}>
        <img
          src="/image-para-website.png"
          alt="Imagen"
          className={styles.image}
        />
        <div className={styles.infocontainer}>
          <span className={styles.title + " " + styles.yellowText}>Cesar</span>
          <br />
          <span className={styles.title}>Rodriguez</span>
          <div className={styles.list}>
          <ul>
            <li>
              <span className={styles.grayText}>Age: </span> 27
            </li>
            <li>
              <span className={styles.grayText}>Nationality: </span> Guatemalan
            </li>
            <li>
              <span className={styles.grayText}>Skill set: </span> Analitic, courageous
            </li>
            <li>
              <span className={styles.grayText}>Languages: </span> English, Spanish
            </li>
          </ul>
          </div>
        </div>
      </section>
    </main>
  )
}