# 🔐 大模型安全相关研究 | 2026年04月19日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Challenges and Future Directions in Agentic Reverse Engineering Systems](https://arxiv.org/abs/2604.14317)

**<font color=#1a73e8>作者：</font>** Salem Radey, Jack West, Kassem Fawaz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems built on large language models (LLMs) are increasingly being used for complex security tasks, including binary reverse engineering (RE). Despite recent growth in popularity and capability, these systems continue to face limitations in realistic settings. Cutting-edge systems still fail in complex RE scenarios that involve obfuscation, timing, and unique architecture. In this work, we examine how agentic systems perform reverse engineering tasks with static, dynamic, and hybrid agents. Through an analysis of existing agentic tool usage, we identify several limitations, including token constraints, struggles with obfuscation, and a lack of program guardrails. From these findings, we outline current challenges and position future directions for system designers to overcome from a security perspective.

---


### 2. [Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection](https://arxiv.org/abs/2604.14604)

**<font color=#1a73e8>作者：</font>** Meng Chen, Kun Wang, Li Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern Large audio-language models (LALMs) power intelligent voice interactions by tightly integrating audio and text. This integration, however, expands the attack surface beyond text and introduces vulnerabilities in the continuous, high-dimensional audio channel. While prior work studied audio jailbreaks, the security risks of malicious audio injection and downstream behavior manipulation remain underexamined. In this work, we reveal a previously overlooked threat, auditory prompt injection, under realistic constraints of audio data-only access and strong perceptual stealth. To systematically analyze this threat, we propose \textit{AudioHijack}, a general framework that generates context-agnostic and imperceptible adversarial audio to hijack LALMs. \textit{AudioHijack} employs sampling-based gradient estimation for end-to-end optimization across diverse models, bypassing non-differentiable audio tokenization. Through attention supervision and multi-context training, it steers model attention toward adversarial audio and generalizes to unseen user contexts. We also design a convolutional blending method that modulates perturbations into natural reverberation, making them highly imperceptible to users. Extensive experiments on 13 state-of-the-art LALMs show consistent hijacking across 6 misbehavior categories, achieving average success rates of 79\%-96\% on unseen user contexts with high acoustic fidelity. Real-world studies demonstrate that commercial voice agents from Mistral AI and Microsoft Azure can be induced to execute unauthorized actions on behalf of users. These findings expose critical vulnerabilities in LALMs and highlight the urgent need for dedicated defense.

---


### 3. [Robustness of Vision Foundation Models to Common Perturbations](https://arxiv.org/abs/2604.14973)

**<font color=#1a73e8>作者：</font>** Hongbin Liu, Zhengyuan Jiang, Cheng Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A vision foundation model outputs an embedding vector for an image, which can be affected by common editing operations (e.g., JPEG compression, brightness, contrast adjustments). These common perturbations alter embedding vectors and may impact the performance of downstream tasks using these embeddings. In this work, we present the first systematic study on foundation models' robustness to such perturbations. We propose three robustness metrics and formulate five desired mathematical properties for these metrics, analyzing which properties they satisfy or violate. Using these metrics, we evaluate six industry-scale foundation models (OpenAI, Meta) across nine common perturbation categories, finding them generally non-robust. We also show that common perturbations degrade downstream application performance (e.g., classification accuracy) and that robustness values can predict performance impacts. Finally, we propose a fine-tuning approach to improve robustness without sacrificing utility.

---


### 4. [Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization](https://arxiv.org/abs/2604.15022)

**<font color=#1a73e8>作者：</font>** Haochun Tang, Yuliang Yan, Jiahua Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R$^2$A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R$^2$A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that {R$^2$A} significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: this https URL.

---


### 5. [Feedback-Driven Execution for LLM-Based Binary Analysis](https://arxiv.org/abs/2604.15136)

**<font color=#1a73e8>作者：</font>** XiangRui Zhang, Qiang Li, Haining Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binary analysis increasingly relies on large language models (LLMs) to perform semantic reasoning over complex program behaviors. However, existing approaches largely adopt a one-pass execution paradigm, where reasoning operates over a fixed program representation constructed by static analysis tools. This formulation limits the ability to adapt exploration based on intermediate results and makes it difficult to sustain long-horizon, multi-path analysis under constrained context. We present FORGE, a system that rethinks LLM-based analysis as a feedback-driven execution process. FORGE interleaves reasoning and tool interaction through a reasoning-action-observation loop, enabling incremental exploration and evidence construction. To address the instability of long-horizon reasoning, we introduce a Dynamic Forest of Agents (FoA), a decomposed execution model that dynamically coordinates parallel exploration while bounding per-agent context. We evaluate FORGE on 3,457 real-world firmware binaries. FORGE identifies 1,274 vulnerabilities across 591 unique binaries, achieving 72.3% precision while covering a broader range of vulnerability types than prior approaches. These results demonstrate that structuring LLM-based analysis as a decomposed, feedback-driven execution system enables both scalable reasoning and high-quality outcomes in long-horizon tasks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
