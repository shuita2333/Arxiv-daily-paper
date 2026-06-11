# 🔐 大模型安全相关研究 | 2026年06月12日

> 本类共 **8** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/abs/2606.11416)

**<font color=#1a73e8>作者：</font>** Yukuan Zhang, Mengxin Zheng, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Repository-level benchmarks for evaluating Large Language Model (LLM) code repair on Secure Multi-Party Computation (MPC) software do not yet exist, and directly transplanting general-purpose benchmarks such as SWE-bench fails on three structural fronts: (i) MPC repositories are dominated by generic Python infrastructure rather than cryptographic logic; (ii) high-value MPC fixes lack the standardized tests rigid extraction pipelines require; and (iii) standard fail-to-pass evaluation is insufficient for code that must also be cryptographically safe. MPC is increasingly deployed for privacy-preserving machine learning, biomedical collaboration, and secure analytics. Existing MPC-specific code-synthesis efforts cover only operator-level or single-framework tasks; evaluating LLM agents on real repository-level MPC repair instead demands MPC-aware data curation and a verifier matched to the security and numerical-fidelity guarantees MPC programs must obey neither of which existing benchmarks provide. We introduce MPC-Patch-Bench, a repository-level benchmark organised around two frameworks. (1)The Data Curation Framework combines a domain-specific curation agent that filters raw pull requests through three cryptographic layers with a human-AI completion engine that synthesizes missing problem statements and Fail-to-Pass/Pass-to-Pass tests, yielding 205 fully verified instances. (2)The MPC Verifier provides dedicated security and numerical-fidelity checks via dynamic differential testing against plaintext oracles and MPC-specific static analysis rules that flag unsafe reveals, insecure arithmetic, and illegal public/private casts. The strongest evaluated LLM functionally resolves only 22.9% of MPC-Patch-Bench tasks; the MPC Verifier further reduces verified resolution to 17.1%, with up to 40% of functionally-passing patches rejected for cryptographic or numerical-fidelity violations.

---


### 2. [Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference](https://arxiv.org/abs/2606.11592)

**<font color=#1a73e8>作者：</font>** Sayedeh Leila Noorbakhsh, Hossein Khalili, Nader Sehatbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Collaborative edge-cloud inference enables resource-constrained devices to leverage large language models (LLMs) by offloading partial computation to cloud servers. However, transmitting intermediate activations exposes sensitive user prompts to prompt inversion attacks, where an adversary reconstructs the original input from shared representations. Existing defenses rely largely on heuristic perturbations or empirical tuning, offering limited theoretical understanding of privacy leakage and its interaction with utility and latency constraints. We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference. Our approach learns privacy-preserving representations by explicitly minimizing the mutual information between intermediate activations and the input prompt while maintaining task utility under computational constraints. We derive theoretical guarantees on prompt reconstruction error, characterize fundamental privacy-utility tradeoffs, and establish token-level accuracy bounds for downstream inference. We then propose a novel defense based on privacy adapters implemented via low-dimensional information bottlenecks. Extensive experiments across multiple settings demonstrate that our method achieves superior privacy-utility-latency tradeoffs compared to existing defenses (up to 35% reduction in attack success), providing a principled foundation for private and efficient collaborative LLM inference.

---


### 3. [Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/abs/2606.11632)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic infrastructure introduces a critical control-plane authorization problem: non-deterministic reasoning systems can propose high-stakes mutations to production resources, yet existing security mechanisms -- such as identity and access management (IAM), policy engines, consensus protocols, and audit logs -- either enforce static, context-unaware permissions or merely record actions post-execution. This paper introduces the Sovereign Assurance Boundary (SAB), a certificate-bound runtime admission layer for autonomous execution authority. SAB intercepts agent proposals at an assurance airlock, compiles them into typed execution contracts $C$, and binds these contracts to cryptographic evidence digests $H(E)$ and policy versions. The contracts are then routed through consequence-aware certification paths. Upon successful admission, the system emits a signed Sovereign Assurance Certificate ($\Omega$) that is strictly scoped to a specific execution identity, revocation epoch, and validity window. Finally, a sovereign execution broker verifies $\Omega$ and performs fresh pre-execution revocation and drift checks before invoking infrastructure APIs. We detail the airlock-broker architecture, formalize its admission and revocation invariants, and report preliminary feasibility measurements from a Go prototype evaluated over 2,500 admission attempts. Ultimately, this broker-enforced model prevents autonomous reasoning from directly mutating state, transforming delegated execution authority into a cryptographically verifiable, evidence-bound, revocable, and replayable runtime artifact.

---


### 4. [Dummy Backdoor as a Defense: Removing Unknown Backdoors via Shared Internal Mechanisms for Generative LLMs](https://arxiv.org/abs/2606.11648)

**<font color=#1a73e8>作者：</font>** Kazuki Iwahana, Masaru Matsubayashi, Takuma Koyama 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a serious threat to the safety and reliability of Large Language Models (LLMs), as they cause models to behave normally on clean inputs while producing attacker-specified responses when hidden triggers are present. Removing such unknown backdoors is particularly challenging when the defender does not know the backdoor attack types or the internal mechanisms formed through backdoor training. In this work, we propose a simple but effective backdoor removal method based on shared internal mechanisms across different backdoors. First, we show that different backdoors with the same task (attack objective) induce similar trigger-activated changes in the internal activations. Motivated by this observation, our method intentionally embeds a backdoor with a known trigger (\emph{dummy backdoor}) and then removes it through further fine-tuning on dummy-triggered inputs paired with clean responses. Since the dummy backdoor and the unknown backdoor can rely on shared internal mechanisms, removing the dummy backdoor also reduces the effect of the unknown backdoor. We evaluate our method on three backdoor attack types across multiple model families. Experimental results show that our method substantially reduces the attack success rate of the unknown backdoor while preserving model utility, outperforming representative existing defense methods in both backdoor removal effectiveness and utility preservation. These findings suggest that a defender-controllable backdoor can serve as a helpful proxy for mitigating unknown backdoors in generative LLMs.

---


### 5. [Can Open-Source LLM Agents Replace Static Application Security Testing Tools? An Empirical Assessment](https://arxiv.org/abs/2606.11672)

**<font color=#1a73e8>作者：</font>** Derek Yohn, Luke Flancher, Mirajul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper explores the value of agentic AI tools for cybersecurity purposes. We evaluate the efficacy of a general-purpose GenAI Large Language Model- (GenAI-) based agent when powered by three different Ollama-hosted general-purpose open source models. We assess each agent's performance using precision, recall, false positive count, and a calculated composite score based upon the interplay of the captured metrics, against the baseline performance of an existing, vetted Static Application Security Testing (SAST) tool, Bandit. Our findings refute the notion that a modern open-source GenAI LLM-based agent is currently suitable for the specialized task of SAST scanning under realistic conditions.

---


### 6. [Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code](https://arxiv.org/abs/2606.11817)

**<font color=#1a73e8>作者：</font>** Yitong Zhang, Shiteng Lu, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for code generation, raising concerns that they may be misused to produce malicious code. Meanwhile, Grammar-Constrained Decoding (GCD) has been widely adopted to improve the reliability of LLM-generated code by enforcing syntactic validity. In this paper, we reveal a counterintuitive risk: this reliability-oriented technique can itself become an attack surface. We uncover a new jailbreak attack, termed CodeSpear, that exploits GCD to induce LLMs into generating malicious code. Our experiments show that simply applying a benign code grammar constraint can effectively jailbreak LLMs.
To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints. CodeShield aligns the model in the code modality by teaching it to generate honeypot code under GCD. Such code is semantically harmless, so it does not implement the malicious request, and structurally diverse, so it is difficult to suppress through grammar tightening. At the same time, CodeShield still preserves natural-language refusals when natural language is available. Experiments on 10 popular LLMs across 4 benchmarks show that CodeSpear outperforms representative jailbreak baselines and increases the attack success rate by more than 30 percentage points on average. CodeShield also restores safety under CodeSpear while preserving benign utility. Our findings reveal a fundamental risk of GCD and call for greater attention to its potential security implications.

---


### 7. [Selection Integrity for LLM Graph Memory: An Accumulability Criterion for Information-Flow-Blind Retrieval](https://arxiv.org/abs/2606.12290)

**<font color=#1a73e8>作者：</font>** Zeming Fei, Hongming Fei, Xiaoyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent memory is moving to graphs, and the provenance defenses now being built for it all check one thing: the provenance of the records an agent retrieves. We show that this entire class of defense is blind by construction. A long-term graph memory runs a global selection step over writable graph structure, so structure that an untrusted principal writes changes \emph{which} authenticated facts are selected while the cited evidence stays fully authenticated; faithful information-flow control (IFC), checking the provenance of what the reader uses (all of it authenticated), makes the byte-identical decision to no defense at all, across document-QA substrates and real multi-session agent memory. In the most consequential instance, a no-source structural write silently misdirects $28$ irreversible ledger transfers over $499$ live actions: faithful IFC permits every one, and \authselect\ prevents every one. We then characterize exactly which memories are exposed: a selector admits the channel when its structural term can reallocate an $\Omega(1)$ share of top-$k$ membership past a selected fact's margin. Personalized PageRank can, since a sourceless write reroutes conserved random-walk mass; a content-fixed reranker cannot, and Graphiti's node-distance, which leans on structure \emph{more} than PageRank does, stays immune. Reallocatability, not reliance, is the predictor. We prove the immune case in general and the open case under a chokepoint condition we verify. Closing the channel forces any provenance defense to recompute selection on the authenticated subgraph, which is what \authselect\ does, at zero over-block and $2$--$3\%$ latency.

---


### 8. [OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents](https://arxiv.org/abs/2606.12341)

**<font color=#1a73e8>作者：</font>** Jin Xie, Songze Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly act on a user's behalf -- reading personal files, calling tools, transacting with external services -- possibly leaking personally identifiable information (PII) across trust boundaries at every step. Privacy here is a property not of a single output but of an entire trajectory, and three properties make it hard: leakage is cumulative, as individually innocuous releases accumulate across honest-but-curious or colluding sinks into inferences about a protected secret; bidirectional, as a malicious observation can inject instructions that turn the agent's own reasoning model against the user; and task-dependent, as the same field is necessary for one recipient yet gratuitous for another. Per-release contextual-integrity filters, information-flow controls, and posterior-leakage monitors each address part of this but none controls cumulative, inference-based leakage at runtime. We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs. Its mechanism, \emph{Witness-Verified Declassification}, separates judgment from trust: an untrusted, locally fine-tuned defender model inspects each candidate release and emits structured evidence -- labeled atoms and proposed declassification operators -- which a deterministic verifier audits, charging a certified min-entropy cost for the chosen variant and authorizing the least-disclosing useful release under a sink-trust-weighted budget recorded on a tamper-evident ledger. Across diverse agent benchmarks and recent defenses, OCELOT attains significantly lower leakage at higher task utility, resists adaptive injection, jailbreak, cumulative inference, and sink collusion, and adds only modest overhead.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
