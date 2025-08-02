import dbmodels as db
import sqlalchemy as sql


def add(*, domain: str, login: str, password: str) -> None:
    with db.session() as hand_unit:
        try_find = hand_unit.scalar(
            sql.select(db.Domain).where(db.Domain.domain == domain)
        )

        if not try_find:
            new_domain = db.Domain(domain=domain)
            hand_unit.add(new_domain)
            hand_unit.flush()
            new_connection = db.Credential(
                login=login, password=password, domain=new_domain
            )

            hand_unit.add(new_connection)
            print("DONE")

        else:
            new_connection = db.Credential(
                login=login, password=password, domain=try_find
            )

            hand_unit.add(new_connection)
            print("DONE")

        hand_unit.commit()


def delete(*, id_cred: int) -> None:
    with db.session() as hand_unit:
        deleted_cred = hand_unit.get(db.Credential, id_cred)
        if deleted_cred:
            hand_unit.delete(deleted_cred)
            print("Found it, DONE")
        else:
            print("Nothing to DELETE")
        hand_unit.commit()


def delete_domain(*, domain_name: str) -> None:
    with db.session() as hand_unit:
        deleted_domain = hand_unit.scalar(
            sql.select(db.Domain).where(db.Domain.domain == domain_name)
        )
        if deleted_domain:
            hand_unit.delete(deleted_domain)
            print("Found it, DONE")
        else:
            print("Nothing to DELETE")
        hand_unit.commit()


def search(*, domain_name: str) -> "db.Credential":
    with db.session() as hand_unit:
        domain = hand_unit.scalar(
            sql.select(db.Domain).where(db.Domain.domain == domain_name)
        )
        if domain:
            cred = domain.credentials
            print("Found it, DONE")
            return cred
        else:
            return None


def show_domains() -> None:
    with db.session() as hand_unit:
        domains = hand_unit.scalars(sql.select(db.Domain)).all()
        if domains:
            for domain in domains:
                print(domain.domain)
