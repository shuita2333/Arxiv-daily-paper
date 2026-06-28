# 🔐 大模型安全相关研究 | 2026年06月29日

> 本类共 **10** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [MIRAGE: Protecting against Malicious Image Editing via False Moderation](https://arxiv.org/abs/2606.26199)

**<font color=#1a73e8>作者：</font>** Anshul Nasery, Ramnath Kumar, Cho-Jui Hsieh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The proliferation of AI-powered image editing systems raises serious concerns because it allows personal images to be arbitrarily manipulated at scale, with minimal effort, and a lower barrier to entry. Prior work on image immunization adds imperceptible perturbations to an image to protect against unauthorized manipulations. However, these methods usually require access to the model weights and the image manipulating prompt. This significantly limits their use, especially against powerful commercial image-editors such as GPT-Image, Gemini Flash Image (Nano Banana), and Grok Imagine. To address this, we take a system-level view of the problem and identify a previously unexplored attack surface common to all major commercial image editing systems: pre-generation safety this http URL than disrupting the generative model itself, we propose to immunize images by causing these moderation classifiers to flag images as policy-violating, triggering an automatic refusal regardless of the editing prompt. We operationalize this by adding adversarial perturbations to align our image to policy-violating concepts in the representation space of an ensemble of open-source embedding and moderation models. We call our method MIRAGE, which stands for Moderation Induced Resistance Against Generative Editing. We evaluate MIRAGE against multiple closed-source image editing APIs and demonstrate success rates of more than 88%. Our approach is simple, prompt-agnostic, and effective, offering a practical path towards protecting personal images from unauthorized AI-powered editing.

---


### 2. [Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats](https://arxiv.org/abs/2606.26377)

**<font color=#1a73e8>作者：</font>** Poojitha Thota, Yun Lei, Santhosh Thangaraj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in interactive applications, yet they remain vulnerable to adversarial interactions that induce harmful, deceptive, or policy-violating outputs. Existing defenses typically analyze either user prompts or generated outputs, but not both. However, many real-world attacks exploit a separation between adversarial intent expressed in the prompt and actionable harm manifested only in the response. As a result, prompt-only and response-only defenses frequently miss unsafe interactions that appear benign when viewed from either side in isolation. We present a verification-centric defense framework that jointly evaluates prompt intent and response harm before an LLM response is delivered to a user. The framework employs specialized analysts for intent and harm assessment together with a Judge for conflict resolution. We formalize a threat model for prompt-response attacks and evaluate the framework across five threat categories: jailbreaks, prompt injection, phishing, cyber abuse, and harmful content. Experiments on multiple benchmark datasets show that jointly verifying prompt intent and response harm consistently outperforms single-sided defenses and single-agent reasoning baselines. Across threat categories, the framework improves average F1 from 0.90 for the strongest applicable baselines to 0.95 while reducing the average attack success rate to 4.1 percent. Compared with a Single-Agent+CoT baseline, it improves average F1 from 0.87 to 0.95 and reduces the false positive rate on benign-sensitive requests from 0.12 to 0.06. We further evaluate architecture-aware adaptive attacks in which the attacker knows the verifier structure and attempts to bypass individual verification components. Our results suggest that prompt-response verification provides a practical foundation for securing LLM applications against evolving adversarial threats.

---


### 3. [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479)

**<font color=#1a73e8>作者：</font>** Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions. Systems such as CaMeL, FIDES, Progent, RTBAS, and FORGE realize this with capabilities, information-flow labels, and reference monitors, and several report near-elimination of attacks on the AgentDojo benchmark. We make two contributions. First, we organize these out-of-band defenses as instances of classical integrity protection (Biba), reference monitoring, and least privilege, yielding a structured comparison of what they do and do not cover. Second, we warn that every one of them is validated only on static benchmarks (a fixed set of injection attempts), the same methodology that made in-band defenses look strong until adaptive, defense-aware attacks broke twelve of them at over 90% success; we specify the threat model and protocol an adaptive evaluation requires. We then run that protocol as an independent reproduction and extension of Progent's own adaptive-attack analysis, on AgentDojo, with an open-weight agent (Qwen2.5-7B) self-hosted on a single H200, a setting its authors did not test. Averaged over three runs, the defense held: Progent cut mean attack success roughly sixfold (25.8% to 4.2%), and a hand-crafted adaptive attack did not raise it (2.6%). This is one small-scale data point on a weak model with a single black-box attack template; a stronger optimized (white-box GCG) attack remains open. The result is consistent with, but does not establish, the hypothesis that deterministic out-of-band enforcement is a harder target for an adaptive attacker than in-band detection.

---


### 4. [Adversarial Diffusion Across Modalities: A Fusion Survey of Attacks, Defenses, and Evaluation for Text, Vision, and Vision-Language Models](https://arxiv.org/abs/2606.26566)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Moataz Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial evaluation of AI systems has matured along four largely disconnected tracks: diffusion-based attacks on text and large language models (LLMs), diffusion-based attacks on image classifiers, jailbreak pipelines against vision-language models, and diffusion-based input purification defenses. Each has developed its own vocabulary, threat models, and benchmarks, with denoising diffusion models emerging as a shared generative mechanism whose recipes are now actively ported between communities. This survey performs an information-fusion exercise at the meta-research level: we integrate these four tracks into a single conceptual framework with a unified taxonomy, evaluation criteria, and research agenda, focusing on the LLM-side slice. We catalog fifty published papers across four scope areas (text/LLM, image classifier, vision-language model, defense), plus four diffusion-LLM-as-victim entries and ten non-diffusion baselines against which any new attack must be compared. We propose a six-class taxonomy of diffusion roles in adversarial pipelines, augmented by a threat-model axis recording attacker knowledge, query budget, and target accessibility, and apply a five-dimension framework (attack success rate, transferability, query budget, perplexity, defense-evasion) uniformly across modalities. The review adopts a dual attacker-defender perspective: alongside the attack catalog we cover four diffusion-based defenses that form the natural evaluation backdrop for new attacks. Our critical analysis identifies five recurring weaknesses of the current LLM-side literature, and we close with a research agenda of open questions and concrete experimental designs. The companion catalog and spreadsheet are released with the paper. We are explicit that this is a narrative review with quality assessment, not a PRISMA-compliant systematic review, and discuss the implications for replication.

---


### 5. [Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/abs/2606.26627)

**<font color=#1a73e8>作者：</font>** Nada Lahjouji, Ashwin Gerard Colaco  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over sensitive data, privacy becomes harder to enforce. An agent touches many data sources, runs multi-step workflows, keeps state across sessions, and acts with delegated permissions. Sensitive information can therefore leak not only through its final answer but through the queries it issues, the intermediate results it handles, the memory it writes, and the messages it exchanges with other agents. We survey the privacy of LLM agents from a data-centric view, organizing the field around the data an agent touches rather than by attack type, and we use data agent as shorthand for an LLM agent that works with data. Research on these risks is active but scattered across retrieval-augmented generation, text-to-SQL interfaces, agent memory, prompt injection, access control, and contextual privacy. This survey brings that work together: we taxonomize the data sources an agent touches, the privacy risks each source creates, and the governance mechanisms that address them; we map the benchmarks used to measure these risks and identify what is missing; and we set out the open problems. Two findings recur: among governance mechanisms only information-flow control covers both compositional and cross-session inference leakage, the two least-protected risks; and no benchmark drives an agent across its data surfaces under one privacy policy, the instrument the field most lacks. Our goal is a reference that situates the scattered literature and gives future work a common framing.

---


### 6. [MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG](https://arxiv.org/abs/2606.26793)

**<font color=#1a73e8>作者：</font>** Inderjeet Singh, Andrés Murillo, Motoyoshi Sekiya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. Existing red-teaming approaches are typically surface-specific and often recycle known attack templates; on text-poisoning benchmarks we measure 73-84% exact duplication. We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. A deterministic Novelty Gate rejects any candidate matching the retrieval set under normalized comparison, allowing retrieval to inform search priors without enabling prompt copying. Across four attack surfaces on a multimodal agentic RAG target, MIRROR attains 76% ASR on image poisoning compared with 52% for baselines, 97% ASR on orchestrator attacks at half the query cost, and the lowest cross-surface variance (coefficient of variation 0.47). In contrast, specialized baselines collapse across surfaces: suffix optimization reaches 79% ASR on text poisoning but 1% on direct queries. We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces.

---


### 7. [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933)

**<font color=#1a73e8>作者：</font>** Corban Villa, Sohee Kim, Austin Chu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-assisted vulnerability discovery has proven effective for bug classes like memory safety, where instrumentation confirms memory violations and efficiently filters false positives. Many dangerous vulnerability classes, such as cryptographic misuse, however, lack any comparable instrumentation. In this work, we present Chai, an AI-based system that discovers and validates cryptographic misuse vulnerabilities through naturally occurring signals. To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. In doing so, Chai inverts the prevailing paradigm of AI vulnerability discovery: instead of auditing one codebase for many flaws, it catalogs flaws at the library level and propagates them across a cryptographic dependency graph, delivering compounding efficiency gains. We evaluate Chai across X.509, JWT, and SAML libraries. Chai discovered a previously unknown critical vulnerability in an SSL library that powers billions of devices, along with security bugs in one library behind a major web browser and another in major Linux distributions. In total, these techniques surfaced over 100 vulnerabilities.

---


### 8. [Jailbreaking for the Average Jane: Choosing Optimal Jailbreaks via Bandit Algorithms for Automatically Enhanced Queries](https://arxiv.org/abs/2606.26936)

**<font color=#1a73e8>作者：</font>** Prarabdh Shukla, Ritik, Suhas Rao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With a profusion of jailbreaks for LLMs now widely known, a growing concern is that non-expert malicious actors ("the average Jane") could elicit actionable responses to malicious requests. In this work, we examine whether this concern is justified. A non-expert malicious actor requires two ingredients for a successful attack: a powerful jailbreak for their target model, acting on an effective malicious query. For the former, we propose a novel attack strategy based on the multi-armed bandit framework. This allows efficient online learning of the optimal jailbreak from a large choice set via noisy exploration on a small number of queries, with subsequent application of the learnt policy on an exploitation set. For the latter, we curate $\mathrm{FrankensteinBench}$, a safety benchmark of $11,279$ malicious queries drawn from manual curation over $7$ existing benchmarks, along with automated enhancement and generation. Each query is categorized as simple or complex by the technical expertise required to craft it. Our findings confirm the concern. Our bandit-based attack achieves success rates as high as $97\%$ on average over $15$ SoTA open-weight LLMs. Moreover, adding complexity to queries raises the attack success rate by up to $26\%$ on average across models -- making it an effective, automatable prompting strategy.

---


### 9. [Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation](https://arxiv.org/abs/2606.27091)

**<font color=#1a73e8>作者：</font>** Ryan Fetterman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. We study Foundation-Sec-8B-Instruct and its base model, Llama-3.1-8B-Instruct, on matched PowerShell classification cohorts. Causal interventions localize the classification circuit to a late-attention route inherited from Llama rather than created by fine-tuning. Fine-tuning concentrates and semantically specializes this inherited structure, improving baseline behavior while creating transformation-sensitive attack surfaces. A three-tier evasion benchmark finds Foundation-Sec misses on iwr substitution, Invoke-Expression reconstruction, and case-mutated Invoke-Expression/IEX variants that Llama does not share. We also derive a pre-deployment monitoring method: a linear probe at the classification boundary and an indicator-token sign test identify command families where canonical indicators change role after fine-tuning. These signals prioritize red-team variant generation using only canonical inputs, showing that security fine-tuning can improve task accuracy while expanding the evasion surface. These results caution against treating small task-specific fine-tunes as straightforwardly safer security classifiers: specialization can convert inherited model structure into brittle indicator rules that preserve held-out accuracy while expanding the evasion surface. Robust AI-enabled security will require specifying the full transformation space of the task and monitoring semantic drift through fine-tuning.

---


### 10. [Application of LLMs to Threat Assessment of Foreign Peacekeeping Missions](https://arxiv.org/abs/2606.27106)

**<font color=#1a73e8>作者：</font>** Gerhard Backfried, Christian Schmidt, Diego Pilutti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a novel approach for applying Large Language Models (LLMs) to threat assessment in the context of foreign peacekeeping missions. Building on the PINPOINT project and its use case, the EU Monitoring Mission in Georgia, we combine an interdisciplinary risk-model with OSINT-based media collection and LLM-supported threat extraction. The proposed workflow maps media contents to mission-relevant threats, extracts structured information and applies several additional LLM-based processing steps to improve relevance and grounding. An evaluation of threats extracted from media documents shows high agreement between automatically generated results and human judgment for core aspects such as threat and mission relevance. These results indicate that LLMs provide a promising approach to support analysts in the context of peacekeeping missions.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
