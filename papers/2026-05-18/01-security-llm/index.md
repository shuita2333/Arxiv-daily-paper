# 🔐 大模型安全相关研究 | 2026年05月18日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity Agents](https://arxiv.org/abs/2605.14153)

**<font color=#1a73e8>作者：</font>** Seunghyun Lee, David Brumley  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Exploitation is not a binary event. It is a ladder of acquiring progressive capabilities, from executing a single buggy line of code to taking full control of the target. However, existing LLM security benchmarks treat a crash as exploitation success. That single binary outcome collapses the hard parts of exploitation: the transition from triggering a bug to constructing reusable primitives and control.
We present ExploitBench, a capability-graded benchmark that decomposes exploitation into 16 measurable flags, from coverage and crash through sandbox primitives, arbitrary read/write, control-flow hijack, and arbitrary code execution. Each capability is verified by a deterministic oracle that uses a per-run randomized challenge-response for primitives, differential execution against ground-truth binaries to measure progress, and a signal-handler proof for code execution.
We instantiate ExploitBench on 41 V8 bugs because V8 is both widely deployed and exploitation-hardened. We report three arms: <model,env> as the primary measurement of model-environment capability, <model,env, adaptive coaching> as a secondary arm that adds adaptive coaching to test whether targeted feedback shifts outcomes, and <model,env,harness> as an ablation that swaps in the model's native CLI to check whether vendor-side optimizations increase exploitation capabilities.
Our results show a sharp capability split between publicly deployed frontier models and the private frontier. Across the 8 publicly deployed models tested, reaching the vulnerable code and triggering a crash is routine, but arbitrary code execution is not. The private model shows arbitrary code execution on approximately half. Overall, results suggest that exploit construction against hardened targets is an emerging frontier capability.

---


### 2. [To See is Not to Learn: Protecting Multimodal Data from Unauthorized Fine-Tuning of Large Vision-Language Model](https://arxiv.org/abs/2605.14291)

**<font color=#1a73e8>作者：</font>** Chengshuai Zhao, Zhen Tan, Dawei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Vision-Language Models (LVLMs) is increasingly accompanied by unauthorized scraping and training on multimodal web data, posing severe copyright and privacy risks to data owners. Existing countermeasures, such as machine unlearning and watermarks, are inherent post-hoc approaches that act only after intellectual property infringement has already occurred. In this work, we propose MMGuard to empower data owners to proactively protect their multimodal data against unauthorized LVLM fine-tuning. MMGuard generates unlearnable examples by injecting human-imperceptible perturbations that actively exploit the learning dynamics of LVLMs. By minimizing the training loss, the perturbation creates an optimization shortcut, causing the model to overfit to the noise and thereby degrading downstream performance when the perturbation is absent during inference. To further strengthen this defense, MMGuard introduces a cross-modal binding disruption, strategically shifting LVLM attention to enforce a spurious correlation between the noise and the training target with theoretical guarantees. Enhanced by an ensemble learning strategy for cross-model transferability, MMGuard is evaluated against nine open-source LVLMs across six datasets. Our comprehensive results demonstrate effective, stealthy, and robust protection under white-box, gray-box, and black-box threat models, establishing a mechanistic advantage in proactively defending against aggressive fine-tuning exploitation.

---


### 3. [The Great Pretender: A Stochasticity Problem in LLM Jailbreak](https://arxiv.org/abs/2605.14418)

**<font color=#1a73e8>作者：</font>** Jean-Philippe Monteuuis, Cong Chen, Jonathan Petit  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> "Oh-Oh, yes, I'm the great pretender. Pretending that I'm doing well. My need is such, I pretend too much..." summarizes the state in the area of jailbreak creation and evaluation. You find this method to generate adversarial attacks proposed by a reputable institution (e.g., BoN from Anthropic or Crescendo from Microsoft Research). However, this method does not deliver on the promise claimed in the paper despite having top ASR scores against industry-grade LLMs. You successfully generate the jailbreak prompts against your target (open) model. However, the generated jailbreak prompt works against the target model with a 50% consecutive success rate (5 out of 10 attempts) despite having an 80% ASR (on paper) on the latest closed-source model (with a guardrail system)! This observation leads us to think. First, Attack Success Rate (ASR), the primary metric for LLM jailbreak benchmarking, is not a stable quantity. Second, published ASR numbers are therefore systematically inflated and incomparable across papers. Therefore, we wonder "Why a successful jailbreak prompt does not perform consistently well against a target model on which the prompts have been optimized?". To answer this question, we study the impact of stochasticity not only during attack evaluation but also during attack generation. Our evaluation includes several jailbreak attacks, models (different sizes and providers), and judges. In addition, we propose a new metric and two new frameworks (CAS-eval and CAS-gen). Our evaluation framework, CAS-eval, shows that an attack can have an ASR drop of up to 30 percentage points when a jailbreak prompt needs to succeed on more than one attempt. Thankfully, our attack generation framework (CAS-gen) improves previous jailbreak methods and helps them recover this loss of 30 percentage points!

---


### 4. [MemLineage: Lineage-Guided Enforcement for LLM Agent Memory](https://arxiv.org/abs/2605.14421)

**<font color=#1a73e8>作者：</font>** Ciyan Ouyang, Rui Hou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry. Recent and concurrent work shows that untrusted content can be written into persistent agent state and re-enter later sessions as an instruction; the remaining systems question is how to preserve useful memory recall while preventing such state from justifying sensitive actions. MemLineage treats this as a chain-of-custody problem rather than a filtering problem. It is a six-module design around an RFC-6962 Merkle log over per-principal Ed25519-signed entries: a weighted derivation DAG records which retrieved entries influenced each new memory, and a max-of-strong-edges propagation rule makes Untrusted-Path Persistence hold for any chain whose attribution edges remain above threshold. The sensitive-action gate then refuses dispatches whose active justification descends from an external ancestor, while still allowing benign recall. We evaluate three defense cells against three memory-poisoning workloads on a deterministic mechanism-isolation harness; MemLineage is the only configuration in that harness that drives all three columns to zero ASR, while sub-millisecond per-operation overhead keeps it well below the noise floor of any LLM call. A Codex-backed AgentDojo bridge further separates strong-model behavior from defense-layer behavior: under an intentionally vulnerable tool-output profile, no-defense and signature-only baselines fail on all six banking pairs, while all MemLineage rows reduce strict AgentDojo ASR to zero. The core deterministic artifacts are byte-equal CI-verified; hosted-model AgentDojo and live-model sweeps are recorded as auditable logs rather than byte-pinned artifacts.

---


### 5. [Exploiting LLM Agent Supply Chains via Payload-less Skills](https://arxiv.org/abs/2605.14460)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Yukai Zhao, Xing Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces. Adopting these integrations broadens the potential attack surface, prompting a need for systematic security evaluation. Current auditing mechanisms are effective at identifying explicit code payloads and predefined threat contents through security scanning. These detection mechanisms are bypassed if malicious behaviors lack direct injection and are instead synthesized dynamically at runtime through the agent's inherent generative capabilities. Exploring this blind spot, we introduce Semantic Compliance Hijacking (SCH), a payload-less supply chain attack targeting autonomous coding environments. The SCH approach translates malicious goals into unstructured natural language instructions formatted as necessary compliance rules, leading the agent to generate and execute unauthorized code. To assess the real-world viability of this attack, we developed an automated pipeline to evaluate its effectiveness across a test matrix comprising three mainstream agent frameworks and three distinct foundation models using contextualized scenarios. The findings demonstrate the pervasive nature of this threat, with SCH achieving peak success rates of up to 77.67% for confidentiality breaches and 67.33% for Remote Code Execution (RCE) under the most vulnerable configurations. Furthermore, the introduction of Multi-Skill Automated Optimization (MS-AO) further boosted attack efficacy. By omitting recognizable Abstract Syntax Tree (AST) signatures and explicit harmful intents, the manipulated skill files maintained a 0.00% detection rate, evading current scanning tools. This research highlights an underexplored attack surface within agent supply chains, pointing to a necessary transition from signature-based detection models toward semantic intent validation.

---


### 6. [Defenses at Odds: Measuring and Explaining Defense Conflicts in Large Language Models](https://arxiv.org/abs/2605.14514)

**<font color=#1a73e8>作者：</font>** Xiangtao Meng, Wenyu Chen, Chuanchao Zang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) deployed in high-stakes applications must simultaneously manage multiple risks, yet existing defenses are almost exclusively evaluated in isolation under a one-shot deployment assumption. In practice, providers patch models incrementally throughout their lifecycle-responding to newly exposed vulnerabilities or targeted data-removal requests without retraining from scratch. This raises a fundamental but underexplored question: does a later defense preserve the protections established by an earlier one? We present the first systematic study of cross-defense interactions under sequential deployment. Evaluating 144 ordered sequences across three risk dimensions and three model families, we find that 38.9% exhibit measurable risk exacerbation on the originally defended dimension. These interactions are highly asymmetric and order-dependent. To explain these phenomena, we conduct a mechanistic analysis on representative deployment sequences. Using layer-wise representational divergence and activation patching, we localize each defense to a compact set of critical layers. In conflicting sequences, the overlapping critical layers exhibit strongly anti-aligned parameter updates, whereas benign orderings maintain near-orthogonal updates. PCA trajectory analysis reveals that defense collapse stems from activation pattern reversals in these shared layers. We further introduce a layer-wise conflict score that quantifies the geometric tension between defense-induced activation subspaces, offering mechanistic insight into the observed reversals. Guided by this diagnosis, we propose conflict-guided layer freezing, a lightweight mitigation that selectively freezes high-conflict layers during sequential deployment, preserving prior protections without degrading secondary defense performance.

---


### 7. [EVA: Editing for Versatile Alignment against Jailbreaks](https://arxiv.org/abs/2605.14750)

**<font color=#1a73e8>作者：</font>** Yi Wang, Hongye Qiu, Yue Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and Vision Language Models (VLMs) have demonstrated impressive capabilities but remain vulnerable to jailbreaking attacks, where adversaries exploit textual or visual triggers to bypass safety guardrails. Recent defenses typically rely on safety fine-tuning or external filters to reduce the model's likelihood of producing harmful content. While effective to some extent, these methods often incur significant computational overheads and suffer from the safety utility trade-off, degrading the model's performance on benign tasks. To address these challenges, we propose EVA (Editing for Versatile Alignment against Jailbreaks), a novel framework that pioneers the application of direct model editing for safety alignment. EVA reframes safety alignment as a precise knowledge correction task. Instead of retraining massive parameters, EVA identifies and surgically edits specific neurons responsible for the model's susceptibility to harmful instructions, while leaving the vast majority of the model unchanged. By localizing the updates, EVA effectively neutralizes harmful behaviors without compromising the model's general reasoning capabilities. Extensive experiments demonstrate that EVA outperforms baselines in mitigating jailbreaks across both LLMs and VLMs, offering a precise and efficient solution for post-deployment safety alignment.

---


### 8. [Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces](https://arxiv.org/abs/2605.14786)

**<font color=#1a73e8>作者：</font>** William Lugoloobi, Samuelle Marro, Jabez Magomere 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM-based agents increasingly browse the web on users' behalf, a natural question arises: can websites passively identify which underlying model powers an agent? Doing so would represent a significant security risk, enabling targeted attacks tailored to known model vulnerabilities. Across 14 frontier LLMs and four web environments spanning information retrieval and shopping tasks, we show that an agent's actions and interaction timings, captured via a passive JavaScript tracker, are sufficient to identify the underlying model with up to 96\% F1. We formalise this attack surface by demonstrating that classifiers trained on agent actions generalise across model sizes and families. We further show that strong classifiers can be trained from few interaction traces and that agent identity can be inferred early within an episode. Injecting randomised timing delays between actions substantially degrades classifier performance, but does not provide robust protection: a classifier retrained on delayed traces largely recovers performance. We release our harness and a labelled corpus of agent traces \href{this https URL}{here}.

---


### 9. [Toward Securing AI Agents Like Operating Systems](https://arxiv.org/abs/2605.14932)

**<font color=#1a73e8>作者：</font>** Lukas Pirch, Micha Horlboge, Patrick Großmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents based on large language models (LLMs) are rapidly emerging as a general-purpose technology, with recent systems such as OpenClaw extending their capabilities through broad tool use, third-party skills, and deeper integration into user environments. At the same time, these agentic systems introduce substantial security risks by combining unconstrained capabilities with access to sensitive user data. In this work, we investigate the security of LLM-based agents through the lens of operating systems. We argue that both face strikingly similar challenges in isolating resources, separating privileges, and mediating communication.
Guided by this perspective, we survey the current landscape of open-source agents, derive a unified agent architecture, and systematically analyze potential attack vectors. To validate this analysis, we conduct a case study evaluating four widely used OpenClaw-like agents. Even under modest attacker capabilities, we find that several protection mechanisms fail in practice and that secure operation requires detailed system knowledge and careful configuration. However, we also observe that while some agentic capabilities remain insecure by design, many vulnerabilities can be mitigated using well-established techniques from operating system security. We conclude with a set of recommendations for the secure design of agentic systems.

---


### 10. [Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks](https://arxiv.org/abs/2605.15118)

**<font color=#1a73e8>作者：</font>** Karthik Raghu Iyer, Yazdan Jamshidi, Nicholas Bray 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce a reusable framework for auditing whether LLM attack benchmarks collectively cover the threat surface: a 4$\times$6 Target $\times$ Technique matrix grounded in STRIDE, constructed from a 507-leaf taxonomy -- 401 data-populated and 106 threat-model-derived leaves -- of inference-time attacks extracted from 932 arXiv security studies (2023--2026). The matrix enables benchmark-external validation -- auditing collective coverage rather than individual benchmark consistency. Applying it to six public benchmarks reveals that the three primary frameworks (HarmBench, InjecAgent, AgentDojo) occupy non-overlapping cells covering at most 25\% of the matrix, while entire STRIDE threat categories (Service Disruption, Model Internals) lack any standardized evaluation, despite published attacks in these categories achieving 46$\times$ token amplification and 96\% attack success rates through mechanisms which no benchmark tests. The corpus of 2,521 unique attack groups further reveals pervasive naming fragmentation (up to 29 surface forms for a single attack) and heavy concentration in Safety \& Alignment Bypass, structural properties invisible at smaller scale. The taxonomy, attack records, and coverage mappings are released as extensible artifacts; as new benchmarks emerge, they can be mapped onto the same matrix, enabling the community to track whether evaluation gaps are closing.

---


### 11. [MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs](https://arxiv.org/abs/2605.15172)

**<font color=#1a73e8>作者：</font>** Rui Wen, Mark Russinovich, Andrew Paverd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a serious security threat to large language models (LLMs), which are increasingly deployed as general-purpose assistants in safety- and privacy-critical applications. Existing LLM backdoors rely primarily on content-based triggers, requiring explicit modification of the input text. In this work, we show that this assumption is unnecessary and limiting. We introduce MetaBackdoor, a new class of backdoor attacks that exploits positional information as the trigger, without modifying textual content. Our key insight is that Transformer-based LLMs necessarily encode token positions to process ordered sequences. As a result, length-correlated positional structure is reflected in the model's internal computation and can be used as an effective non-content trigger signal.
We demonstrate that even a simple length-based positional trigger is sufficient to activate stealthy backdoors. Unlike prior attacks, MetaBackdoor operates on visibly and semantically clean inputs and enables qualitatively new capabilities. We show that a backdoored LLM can be induced to disclose sensitive internal information, including proprietary system prompts, once a length condition is satisfied. We further demonstrate a self-activation scenario, where normal multi-turn interaction can move the conversation context into the trigger region and induce malicious tool-call behavior without attacker-supplied trigger text. In addition, MetaBackdoor is orthogonal to content-based backdoors and can be composed with them to create more precise and harder-to-detect activation conditions.
Our results expand the threat model of LLM backdoors by revealing positional encoding as a previously overlooked attack surface. This challenges defenses that focus on detecting suspicious text and highlights the need for new defense strategies that explicitly account for positional triggers in modern LLM architectures.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
