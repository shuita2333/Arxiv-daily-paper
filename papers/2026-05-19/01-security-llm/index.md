# 🔐 大模型安全相关研究 | 2026年05月19日

> 本类共 **7** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338)

**<font color=#1a73e8>作者：</font>** Sidharth Pulipaka, Stanislau Hlebik, Leonidas Raghav 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity. This statefulness introduces a new security risk: adversarial content can corrupt what an assistant remembers and thereby influence future interactions. We propose and study sleeper memory poisoning, a delayed attack in which an adversary manipulates external context, such as a document, webpage, or repository, to cause the assistant to store a fabricated memory about the user. Unlike conventional prompt injection, the attack can remain dormant and re-emerge across multiple later conversations. We evaluate the full attack pipeline: whether poisoned memories are written, later retrieved, and ultimately used to steer the following conversations. Across stateful LLM assistants, poisoned memories were added up to 99.8% on GPT-5.5 and 95% on Kimi-K2.6. Crucially, among successful retrievals, poisoned memories cause attacker-intended agentic actions in 60-89% of evaluations across models. These results show that persistent memory can act as a long-term attack surface across multiple future conversations.

---


### 2. [uGen: An Agentic Framework for Generating Microarchitectural Attack PoCs](https://arxiv.org/abs/2605.15503)

**<font color=#1a73e8>作者：</font>** Debopriya Roy Dipta, Thore Tiemann, Eduard Marin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Microarchitectural attacks continue to evolve, uncovering new exploitation vectors in modern processors. From a defensive perspective, assessing a system's susceptibility to such attacks remains challenging. Developing functional attack implementations is labor-intensive, requires deep microarchitectural expertise, and is highly sensitive to execution environments. Consequently, existing attacks often lack portability, limiting systematic and scalable vulnerability assessment. Recent advances in large language models (LLMs) suggest a potential avenue for lowering these barriers. However, it remains unclear whether LLMs can reliably generate functionally correct microarchitectural attack code suitable for rigorous vulnerability testing.
In this work, we present uGen, the first LLM-driven framework for automated microarchitectural attack code generation. A key challenge we address is identifying attack-specific knowledge gaps in LLMs. Through a systematic study of state-of-the-art models (GPT, Claude, and Qwen3), we find that LLMs frequently misgenerate or misplace critical attack primitives. Guided by this analysis, uGen employs a retrieval-augmented, multi-agent design that injects missing domain knowledge to synthesize functionally correct microarchitectural attack PoCs tailored to defender requirements. We evaluate uGen on cache-based and speculative-execution attacks across diverse set of microarchitectures, vulnerable functions, and LLM platforms. In the deployment stage, uGen achieves up to 100% success rate for Spectre-v1 (Claude Sonnet-4) and 80% for Prime+Probe (Qwen3-Coder). Finally, we demonstrate that uGen can generate a successful PoC code with a cost of $1.25 in under four minutes.

---


### 3. [Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis](https://arxiv.org/abs/2605.15569)

**<font color=#1a73e8>作者：</font>** Penghui Li, Hong Yau Chong, Yinzhi Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Microservices are widely adopted in modern cloud systems due to their scalability and fault tolerance. However, microservice architectures introduce significant complexity in privilege and permission control, creating risks of privilege escalation where attackers can gain unauthorized access to resources or operations. Detecting such vulnerabilities is challenging due to complex cross-service interactions, polyglot codebases, and diverse privileged operations and permission checks. We present Neo, an agentic program analysis framework that combines large language models (LLMs) with classic program analysis to address these challenges. Neo leverages an LLM-based agent that dynamically generates analysis plans, adapts code search strategies, and validates semantics. We develop code search primitives that enable Neo to perform scalable and flexible code exploration across services and languages. We evaluated Neo on 25 open-source microservice applications spanning 7 programming languages and 6.2 million lines of code. Neo uncovered 24 zero-day privilege escalation vulnerabilities and achieved 81.0% precision and 85.0% recall on a ground-truth dataset. Compared to existing program analysis and agentic solutions, Neo demonstrated significant improvements in both detection accuracy and scalability. We further showcased Neo's extensibility by applying it to other application domains and vulnerability types, uncovering 18 additional zero-day vulnerabilities.

---


### 4. [Compositional Jailbreaking: An Empirical Analysis of Mutator Chain Interactions in Aligned LLMs](https://arxiv.org/abs/2605.15598)

**<font color=#1a73e8>作者：</font>** Reinelle Jan Bugnot, Soohyeon Choi, Hoon Wei Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreaking attacks on large language models pose a significant threat to AI safety by enabling the generation of harmful or restricted content. While prior work has explored both handcrafted and automated jailbreak strategies, the potential for compositional interaction between simple attacks remains underexplored. This paper presents a systematic study of mutator chaining, in which weak jailbreak transformations are applied sequentially to characterize how they interact: whether they reinforce one another, interfere destructively, or produce no meaningful change. We implement twelve baseline mutators and evaluate all ordered pairs on a benchmark of harmful prompts against three popular LLM models. Our framework introduces metrics for completeness and validity that capture both transformation persistence and attack effectiveness. Results reveal that the interaction landscape is highly non-uniform, while most combinations fail to outperform individual mutators, exhibiting destructive interference or structural incompatibility, a small fraction produce synergistic effects that improve attack success rates. Equally important, the prevalent failure modes reveal structural properties of safety alignment that are not apparent from single-strategy evaluations. These findings highlight the nuanced dynamics of adversarial prompt composition and offer new insights for building more robust safety defenses.

---


### 5. [A Multi-Layer Cloud-IDS Pipeline with LLM and Adaptive Q-Learning Calibration](https://arxiv.org/abs/2605.15889)

**<font color=#1a73e8>作者：</font>** Syed Waqas Ali, Ibrar Ali Shah, Farzana Zahid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security in cloud computing has become a major concern due to several factors such as layered cloud architectures, dynamic environments, and exposure to unseen or zero-day attacks. Moreover, intrusion detection systems (IDS) typically operate at specific layers and rely heavily on machine learning models, which often perform well in experimental settings but fail to sustain performance in real cloud deployments. In this work, we implement a confidence-aware multilevel intrusion detection system using reinforcement learning tailored for cloud environments. The system secures three distinct layers: network, host, and hypervisor. Machine learning models at each layer detect known attack patterns, while prediction confidence distinguishes reliable decisions from uncertain outcomes. Within the multi-gate flow, low-confidence events pass through a learned-threshold confidence gate (Gate-1), followed by a Chroma memory-matching gate (Gate-2), with unresolved events escalated to a large language model (LLM) for semantic analysis and explanation. Final attack promotion at Gate-3 uses calibrated LLM confidence or weighted-fusion fallback, while uncertain events are retained in a review bucket to avoid forced classification. Generated explanations and confirmed knowledge are stored in ChromaDB to support future analysis and retraining. The approach is first evaluated using static thresholds, establishing a baseline for comparison. Results show that the proposed system learns adaptive thresholds and reduces LLM escalation by 58.78%, lowering cost while maintaining strong performance (88.68% accuracy, 85.29% precision, 84.72% recall, 85.00% F1). The network and hypervisor layers achieve 98.02% and 97.08% accuracy, demonstrating a balanced and efficient detection system.

---


### 6. [PersonaFingerprint: Measuring Persona Inference on Modern Websites with LLM-Driven Browsing](https://arxiv.org/abs/2605.15962)

**<font color=#1a73e8>作者：</font>** Chuxu Song, Hao Wang, Richard Martin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Website Fingerprinting (WFP) has traditionally focused on inferring which website a user visits from encrypted traffic metadata such as packet sizes and timing. In this paper, we identify and quantify a new privacy risk in modern web settings: an adversary can infer a user's persona using only packet-length and inter-arrival-time sequences. To study this risk at scale, we build an LLM-driven multi-agent browsing framework that enforces controllable persona constraints while a computer-use agent interacts with real websites and collects corresponding encrypted traffic traces. We formalize persona fingerprinting under both closed-set and open-world settings and further evaluate whether persona information is already embedded in representations learned by existing WFP models and can be amplified at low cost. Across 10 modern websites and 15 personas (plus an open-world class), persona inference achieves about 84% accuracy on mixed-site traffic; moreover, a lightweight multi-task objective can boost persona accuracy to around 80% while retaining strong site classification performance (about 93% baseline). Our results show that, on modern websites, encrypted traffic metadata can leak not only which site a user visits, but also how they browse and who is browsing.

---


### 7. [A Cross-Modal Prompt Injection Attack against Large Vision-Language Models with Image-Only Perturbation](https://arxiv.org/abs/2605.16090)

**<font color=#1a73e8>作者：</font>** Hao Yang, Zhuo Ma, Yang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have emerged as a powerful paradigm for multimodal intelligence, but their growing deployment also expands the attack surface of prompt injection. Despite this growing concern, existing attacks still suffer from a critical limitation: the injected prompt for one modality only steers the model's interpretation of that singular input. Alternatively, these attacks remain multimodal but fail to achieve cross-modal prompt perturbation. To bridge this gap, we introduce a novel cross-modal prompt injection attack CrossMPI, which can steer the model's interpretation of both textual and visual inputs via image-only prompt injection. Our design is underpinned by the following key breakthroughs. First, we turn the focus of the injected prompt perturbation optimization from the visual embedding space (typically with only $10^5$ parameters) to the model hidden state space (for multimodal information integration and with $10^7$ parameters). Then, two strategies are adopted to mitigate the optimization challenges posed by the larger parameter space. To constrain the optimized model parameter space, we introduce a layer selection strategy that identifies the layers most critical to multimodal integration. Interestingly, deviating from the past experience, our analysis reveals that the optimal layers for LVLM prompt perturbation reside in the middle of the model rather than the last. To constrain the image perturbation space, we propose a new distance-decremental perturbation budget assignment strategy that allocates budgets decrementally as the pixel distance to semantic-critical regions increases. Extensive experiments across multiple LVLMs and datasets show that our method significantly outperforms baseline approaches.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
