# 🔐 大模型安全相关研究 | 2026年05月15日

> 本类共 **8** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [BackFlush: Knowledge-Free Backdoor Detection and Elimination with Watermark Preservation in Large Language Models](https://arxiv.org/abs/2605.12529)

**<font color=#1a73e8>作者：</font>** Jagadeesh Rachapudi, Ritali Vatsi, Pranav Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent trends, one can observe Large Language Models (LLMs) are exposed to backdoor attacks where vicious triggers added during training or model editing to elicit harmful outputs on specific input patterns while maintaining clean performance on normal inputs. Legitimate watermarks used as ownership signatures share similar mechanisms to backdoors, creating a critical challenge: detecting and eliminating unknown backdoors without compromising watermark integrity. Existing defenses require prior knowledge of triggers or their payloads, depend on clean reference models, or sacrifice model utility without preserving the watermark. To address these limitations we introduce BackFlush and its variants, a unified framework for backdoor detection and elimination while preserving watermarks. We establish two novel observations: Backdoor Flushing Phenomenon, where injecting and unlearning auxiliary data eliminates pre established backdoors, and Backdoor Susceptibility Amplification, enabling constant time detection independent of vocabulary size. BackFlush employs Rotation based Parameter Editing (RoPE) Unlearning, a technique that preserves watermarks while eliminating backdoors by rotating the embeddings. Comprehensive evaluation across diverse trigger types over different architectures demonstrates BackFlush achieves approximately 1%Attack Success Rate (ASR), approximately 99% clean accuracy (CACC), and preserved watermarking capabilities in the realm where no existing method simultaneously provides these alongside maintaining model utility comparable to clean baselines. Codes are available at this https URL this http URL.

---


### 2. [CoT-Guard: Small Models for Strong Monitoring](https://arxiv.org/abs/2605.12746)

**<font color=#1a73e8>作者：</font>** Nirav Diwan, Han Wang, Berkcan Kapusuzoglu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Monitoring the chain-of-thought (CoT) of reasoning models is a promising approach for detecting covert misbehavior (i.e., hidden objectives) in code generation tasks. While large models (GPT-5, Gemini-3-Flash) can serve as effective CoT monitors, they are expensive to deploy due to the lengthy reasoning traces and high API cost, emphasizing the need for smaller, cheaper alternatives. Nevertheless, we find that current small models (4B--8B) struggle to detect hidden objectives despite access to the CoT, frequently misattributing them as part of the user query. To address this, we propose a post-training pipeline combining supervised fine-tuning (SFT) and reinforcement learning (RL), where SFT narrows the gap for in-domain tasks by distilling detection behavior from stronger monitors, and RL on hard and subtly crafted hidden objectives helps the model generalize to out-of-domain monitoring tasks. To validate this generalization, we evaluate under a realistic threat model motivated by practical supply-chain attacks, where the adversary is a third-party LLM router injecting hidden objectives into code-generation requests through either prompt manipulation or code manipulation attacks. To push beyond objectives that large monitors already saturate, we also introduce four new challenging tasks even for strong monitors. Finally, we introduce CoT-Guard, a 4B-parameter monitor that demonstrates superior generalization performance under both prompt and code manipulation attacks, achieving a G-mean^2 (i.e., TNR x TPR) of 75% and outperforming GPT-5.4 (56%), GPT-5-mini (41%), and Qwen3-32B (54%), while closing the gap to Gemini-3-Flash (83%). These results demonstrate that CoT-Guard provides a practical and cost-effective user-side defense, substantially improving hidden-objective detection while avoiding the deployment cost of large monitors.

---


### 3. [Quantifying LLM Safety Degradation Under Repeated Attacks Using Survival Analysis](https://arxiv.org/abs/2605.12869)

**<font color=#1a73e8>作者：</font>** Zvi Topol  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in a wide range of applications, yet remain vulnerable to adversarial jailbreak attacks that circumvent their safety guardrails. Existing evaluation frameworks typically report binary success/failure metrics, failing to capture the temporal dynamics of how attacks succeed under persistent adversarial pressure. This preliminary work proposes a novel evaluation framework that applies survival analysis techniques to characterize LLM jailbreak vuln`erability. Our approach models the time-to-jailbreak as a survival outcome, enabling estimation of hazard functions, survival curves, and risk factors associated with successful attacks. We evaluate three LLMs against a subset of prompts from the HarmBench dataset spanning three attack categories. Our analysis reveals that models exhibit distinct vulnerability profiles: while one model demonstrates rapid degradation under iterative attacks, the two other models show consistent moderate vulnerability. Our framework provides actionable insights for model and LLM application developers and establishes survival analysis as a rigorous methodology for LLM safety evaluation.

---


### 4. [Do Skill Descriptions Tell the Truth? Detecting Undisclosed Security Behaviors in Code-Backed LLM Skills](https://arxiv.org/abs/2605.12875)

**<font color=#1a73e8>作者：</font>** Wenhui He, Yue Li, Bang Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Programmatic skills in LLM ecosystems consist of a natural-language description and executable implementation files. Users and LLMs rely on the description to understand the skill's scope. However, the implementation may perform security-relevant operations, such as credential access, network communication, or command execution, that the description does not state. We study this description--implementation inconsistency by asking whether the implementation stays within the security-relevant scope declared in the description. We manually analyze 920 real-world programmatic skills and construct an 11-category security property taxonomy. Based on this taxonomy, we build SKILLSCOPE, which constructs source-level security property graphs (SPGs) from implementations and performs LLM-assisted consistency checking. SPG nodes retain source-level code patterns rather than abstract taxonomy labels, preserving fine-grained evidence for checking. On 4,556 programmatic skills with double-blind human review, SKILLSCOPE achieves a precision of 84.8\% and a recall of 96.5\% for identifying inconsistency. Confirmed inconsistency affects 9.4\% of skills, while cases of coarser description, in which implementation details remain within the declared scope, account for 24.3\%. Ablation experiments confirm that both the SPG and the taxonomy contribute: removing the taxonomy reduces precision from 87.8\% to 72.3\%, while removing the SPG reduces recall from 94.7\% to 79.0\%.

---


### 5. [LoREnc: Low-Rank Encryption for Securing Foundation Models and LoRA Adapters](https://arxiv.org/abs/2605.13163)

**<font color=#1a73e8>作者：</font>** Beomjin Ahn, Jungmin Kwon, Chanyong Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Foundation models and low-rank adapters enable efficient on-device generative AI but raise risks such as intellectual property leakage and model recovery attacks. Existing defenses are often impractical because they require retraining or access to the original dataset. We propose LoREnc, a training-free framework that secures both FMs and adapters via spectral truncation and compensation. LoREnc suppresses dominant low-rank components of FM weights, compensates for the missing information in authorized adapters, and further applies orthogonal reparameterization to obscure structural fingerprints of the protected adapter. Unauthorized users produce structurally collapsed outputs, while authorized users recover exact performance. Experiments demonstrate that LoREnc provides strong protection against model recovery with under 1% computational overhead.

---


### 6. [Inducing Overthink: Hierarchical Genetic Algorithm-based DoS Attack on Black-Box Large Language Reasoning Models](https://arxiv.org/abs/2605.13338)

**<font color=#1a73e8>作者：</font>** Shuqiang Wang, Wei Cao, Jiaqi Weng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) are increasingly integrated into systems requiring reliable multi-step inference, yet this growing dependence exposes new vulnerabilities related to computational availability. In particular, LRMs exhibit a tendency to "overthink", producing excessively long and redundant reasoning traces, when confronted with incomplete or logically inconsistent inputs. This behavior significantly increases inference latency and energy consumption, forming a potential vector for denial-of-service (DoS) style resource exhaustion. In this work, we investigate this attack surface and propose an automated black-box framework that induces overthinking in LRMs by systematically perturbing the logical structure of input problems. Our method employs a hierarchical genetic algorithm (HGA) operating on structured problem decompositions, and optimizes a composite fitness function designed to maximize both response length and reflective overthinking markers. Across four state-of-the-art reasoning models, the proposed method substantially amplifies output length, achieving up to a 26.1x increase on the MATH benchmark and consistently outperforming benign and manually crafted missing-premise baselines. We further demonstrate strong transferability, showing that adversarial inputs evolved using a small proxy model retain high effectiveness against large commercial LRMs. These findings highlight overthinking as a shared and exploitable vulnerability in modern reasoning systems, underscoring the need for more robust defenses.

---


### 7. [Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution](https://arxiv.org/abs/2605.13411)

**<font color=#1a73e8>作者：</font>** Xiaozhe Zhang, Chaozhuo Li, Hui Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models remain vulnerable to adversarial prompts that elicit harmful outputs. Existing safety paradigms typically couple red-teaming and post-training in a closed, policy-centric loop, causing attack discovery to suffer from rapid saturation and limiting the exposure of novel failure modes, while leaving defenses inefficient, rigid, and difficult to transfer across victim models. To this end, we propose EvoSafety, an LLM safety framework built around persistent, inspectable, and reusable external structures. For red teaming, EvoSafety equips the attack policy with an adversarial skill library, enabling continued vulnerability probing through simple library expansion after saturation, while supporting the evolution of adversarial vectors. For defense learning, EvoSafety replaces model-specific safety fine-tuning with a lightweight auxiliary defense model augmented with memory retrieval. This enables efficient, transferable, and model-agnostic safety improvements, while allowing robustness to be enhanced solely through memory updates. With a single training procedure, the defense policy can operate in both Steer and Guard modes: the former activates the victim model's intrinsic defense mechanisms, while the latter directly filters harmful inputs. Extensive experiments demonstrate the superiority of EvoSafety: in Guard mode, it achieves a 99.61% defense success rate, outperforming Qwen3Guard-8B by 14.13% with only 37.5% of its parameters, while preserving reasoning performance on benign queries. Warning: This paper contains potentially harmful text.

---


### 8. [Identifying AI Web Scrapers Using Canary Tokens](https://arxiv.org/abs/2605.13706)

**<font color=#1a73e8>作者：</font>** Steven Seiden, Triss Ren, Caroline Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> From pre-training to query-time augmentation, web-scraped data helps to improve the quality and contextual relevancy of content generated by large language models (LLMs). However, large-scale web scraping to feed LLMs can affect site stability and raise legal, privacy, or ethics concerns. If website owners wish to limit LLM-related web scraping on their site, due to these or other concerns, they may turn to scraper access control mechanisms like the Robots Exclusion Protocol. To be most effective, such mechanisms require site owners to first identify the scrapers that they wish to restrict (e.g., via User-Agent strings). Existing mechanisms to identify LLM-related scrapers rely on voluntary disclosure by companies, one-off experiments by researchers, or crowd-sourced reports -- methods that are neither reliable nor scalable. This paper proposes a novel technique for accurately and automatically inferring LLM-related scrapers. We host dynamic websites that serve unique canary tokens to each visiting scraper, then prompt LLMs for information about our sites. If an LLM consistently generates outputs containing tokens unique to a scraper, it provides evidence of exposure to that scraper. Via experiments across 22 production LLM systems, we demonstrate that our approach can reliably identify which scrapers feed which LLM, including several that are not publicly known or disclosed by the companies. Our approach provides a promising avenue for unprivileged third parties to infer which scrapers serve data to which LLMs, potentially enabling better control over unwanted scraping.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
