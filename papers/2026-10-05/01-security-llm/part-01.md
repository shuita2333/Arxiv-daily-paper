# 🔐 大模型安全相关研究 | 2026年10月05日

> 本类共 **9** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Tokenized Key-Gated Adapter Routing: A Secure Access Control Mechanism Against Private Data Leakage in LLMs](https://arxiv.org/abs/2610.00309)

**<font color=#1a73e8>作者：</font>** Mohamed Shaaban, Mohamed Elmahallawy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in privacy-critical domains (e.g., healthcare, finance, and government), but their propensity to memorize and disclose personally identifiable information (PII) poses serious security and compliance risks. Existing defenses typically force a trade-off between model utility, privacy protection, and access to fine-tuned private knowledge. We propose LoRA-Oriented Control via Keyed Entry Tokens (Locket), a practical framework that embeds fine-grained, policy-driven access control directly into LLM generation. Locket trains a set of lightweight LoRA (Low-Rank Adaptation) adapters, each encoding a distinct access policy (e.g., full reveal, partial redaction via PII masking, or reveal under a specified differential privacy level). A compact gating module is trained to associate a learned keyed entry token with exactly one LoRA adapter via sequence-level hard routing; the presence of a valid token acts as an authorization key that unlocks corresponding private knowledge, while an invalid or absent token triggers a privacy-preserving adapter that redacts or sanitizes sensitive content. This design ensures Locket remains fully compatible with off-the-shelf LLMs, supporting scalable deployment while satisfying regulatory and privacy requirements. We evaluate Locket across multiple datasets (Enron, ECHR, Yelp) and a diverse set of state-of-the-art LLMs, including Qwen3 (1.7B and 8B), Meta's Llama-3.2 (1B and 3B), and Google's Gemma-2-2B. Our extensive experiments demonstrate that, when the correct token is provided, Locket preserves perplexity comparable to fine-tuning on raw data (without any defense). Conversely, when the token is missing or invalid, it substantially reduces PII leakage while maintaining utility and perplexity on par with strong baseline defenses.

---


### 2. [Removing the NEEDLE in the Haystack: Backdoor Removal in LLMs via Weight Orthogonalisation](https://arxiv.org/abs/2610.00348)

**<font color=#1a73e8>作者：</font>** Minoo Kim, Vasileios Lampos, George Drayson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks can be implanted in Large Language Models (LLMs) during training, causing unwanted behaviour when a trigger appears in the input. Existing backdoor defences for LLMs attempt to remove the backdoor but inadvertently shift the model's output distribution to benign prompts, which can result in degraded model performance and safety. We propose NEEDLE, a training-free method for targeted backdoor removal. Once a trigger has been identified, our method estimates a backdoor direction and a refusal subspace through activation vectors, then applies sequential weight orthogonalisation to suppress the backdoor while preventing changes in refusal-related representations. NEEDLE requires neither a clean reference model nor the original poisoned training data. Evaluation is conducted across multiple model families and attack types. NEEDLE achieves the lowest mean Attack Success Rate (ASR) among the evaluated defences, including 0% on challenging code injection attacks, while resulting in the lowest KL divergence and minimal changes in capability and safety.

---


### 3. [From A2A Attacks to Envelope-Layer Defense: Red-Teaming Evaluation of LLM Agents and a Three-Layer Isomorphic Attack-Defense Model](https://arxiv.org/abs/2610.00392)

**<font color=#1a73e8>作者：</font>** Yuelin Han  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent interaction protocols such as ACP and A2A have moved LLM-based agents toward multi-agent collaboration, introducing new security threats. A task sent by a remote peer over A2A is treated as a legitimate request, providing a natural channel for indirect prompt injection. Existing agent security evaluations mostly rely on a single metric, the attack success rate (ASR), and cannot distinguish whether an attack failed because the LLM recognized the malicious content or because a mechanism at the agent layer blocked execution. To address this, we propose A2A-TIBA, an attack principle combining indirect prompt injection with bypass circumvention. Through implant-command-exfiltration steps, it induces the target agent to deploy a callback interaction program, after which the attacker issues commands bypassing the agent. To evaluate defenses finer, we design GDA Measurement, a red-team testbed method using raw context capture via an LLM gateway, dual data preservation, and agent-based autonomous judging. We propose four attack outcomes, Class A/B/C/D, extending ASR into semantic refusal rate, semantic breach rate, interception rate, and penetration rate. Experiments reveal the envelope layer -- the channel through which malicious content enters an agent -- as a new defense dimension. We accordingly propose ELA-ITL, a three-layer isomorphic attack-defense model, dividing defense into envelope packaging, LLM recognition, and agent interception, and attack into implant channel, prompt optimization, and execution mechanism. Testing on 15 agent front-end x LLM back-end combinations and building a 1,000-case dataset verifies the attack effectiveness of A2A-TIBA, the evaluation validity of GDA Measurement, and confirms that adding malicious prompt labels to envelope packaging such as A2A, tool, and memory channels significantly improves LLM recognition of malicious content.

---


### 4. [Backdoor Containment via Expert Quarantine and Shutdown in LLMs](https://arxiv.org/abs/2610.00663)

**<font color=#1a73e8>作者：</font>** Jianwei Li, Min-Seon Kim, Jung-Eun Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Backdoored large language models (LLMs) can behave normally on benign inputs while producing attacker-specified outputs under hidden triggers. Existing defenses span four stages--prior-training, in-training, post-training, and inference-time--and share one of two underlying strategies: either suppress backdoor learning (by filtering poisoned data or interrupting its acquisition during optimization) or learn, then purify (by repairing model weights or gating inputs after a fully backdoored model has formed). We propose a third strategy, learn, but channel: allow backdoor formation during training but route it into a designated, quarantined component that can be disabled at deployment. To this end, we propose Quarantined Expert Shutdown QES, a computationally efficient containment strategy built in a regularization-steered MoE-like setting. Specifically, given a poisoned dataset, QES augments a Transformer-based language model with routed expert-specific LoRA branches and lightweight routers, and uses auxiliary routing objectives to attract trigger-conditioned behavior into a designated expert while preserving benign capability elsewhere. At deployment, mitigation reduces to a single constant-time operation: zeroing the quarantined expert's routing weight, without trigger screening or further updating model weights. Empirically, our methods reduce the attack success rate ASR from 100% to 0-10% on most settings across two tasks, three attacks, and four model families, while downstream utility is often preserved or only modestly affected. These results establish learn, but channel as a previously unexplored regime for backdoor containment in generative LLMs.

---


### 5. [Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection](https://arxiv.org/abs/2610.00685)

**<font color=#1a73e8>作者：</font>** Jianwei Li, Jung-Eun Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid adoption of large language models (LLMs) and parameter-efficient fine-tuning (PEFT) methods, the risk of backdoor attacks has become more severe. Existing backdoor purification methods typically rely on at least one of the strong assumptions, such as prior knowledge of triggers, access to clean references, or aggressive retraining, and they often lack comprehensive evaluations. These constraints substantially limit their practical applicability. To overcome these challenges, our work proposes purifying LoRA-tuned LLMs without these assumptions and even without post-hoc retraining of the suspect parameters. Our objective is to significantly reduce the attack success rates (ASR) while preserving both (i) the base model's general capabilities and (ii) the new downstream skills learned through the adapter. Through a series of ablation studies, we progressively scale our approach from a single layer in a text classification setting to a full-parameter LLM in the generative task. Through careful data curation and feature approximation, we extract high-fidelity backdoor directions and, for each layer or head, construct orthogonal null spaces in both the input and output channels, onto which the LoRA updates are projected. Empirically, our null-space projection method reduces the ASR from nearly 100% to less than 10%, while preserving the base model's benign performance and the adapter's learned abilities during downstream task adaptation.

---


### 6. [Do Defenses Against LLM Extraction Work Across Attacks? A Lifecycle Benchmark of Black-Box Model Extraction](https://arxiv.org/abs/2610.00839)

**<font color=#1a73e8>作者：</font>** Shuze Liu, Kaixiang Zhao, Runyang Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed through text-only APIs face model extraction risks, as adversaries can collect their responses to train surrogates that reproduce their capabilities. While prior work has developed diverse attacks and defenses, evaluations remain fragmented across access assumptions, model configurations, query budgets, and security objectives, limiting comparability across methods. To address this gap, we introduce a unified benchmark covering six extraction attacks, ten defenses, and two adaptive attacks that paraphrase or back-translate protected responses before surrogate training. The benchmark controls model configurations, query data, budgets, and held-out evaluation conditions within each comparison while preserving attack-specific querying and training procedures. We measure surrogate capability, fidelity to the victim, output quality using Rep-4, and query-budget sensitivity; defenses use their own security metrics paired with surrogate performance. For the adaptive attacks, we jointly measure provenance-detector scores and the capability and fidelity of surrogates trained on rewritten responses. The benchmark thus provides a reproducible basis for comparing extraction methods and their interactions with defenses under text-only access. Code and artifacts are available at this https URL.

---


### 7. [MOMAT: Mixture of Multiple Atlases for Low-Power Jailbreak Defense of Quantized LLMs](https://arxiv.org/abs/2610.01058)

**<font color=#1a73e8>作者：</font>** Boyang Li, Bingyu Shen, Weihao Hong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantized large language models are increasingly deployed on edge devices for their low latency and energy efficiency. However, model quantization weakens alignment safeguards, leaving qLLMs (quantized large language models) highly vulnerable to jailbreak attacks. To address this challenge, we present MOMAT (Mixture of Multiple Atlases), a hardware-enhanced safety framework that combines structured knowledge retrieval with low-power defense acceleration. Each atlas represents a semantic cluster of harmful or benign sample sets and policy templates, enabling domain-localized Retrieval-Augmented Generation guarding that mitigates the curse of dimensionality and the resulting semantic sparsity problem in large, heterogeneous safety databases. MOMAT retrieves top-$k$ similarity features from all atlases for each prompt and evaluates them using a lightweight MoE (Mixture of Experts) detector, while a CiM (Compute-in-Memory)-accelerated similarity engine performs fast, low-power atlas-local retrieval. MOMAT's CiM-based retrieval accelerates a 100-query batch from 15,052.44 ms to 3,207.21 ns (a $4.69 \times 10^6\times$ speedup) and reduces energy from $8.1 \times 10^7$ $\mu$J to 3.32 $\mu$J, yielding an approximately $2.5 \times 10^5\times$ energy reduction over DRAM-based (Raspberry Pi) baselines. Red-team evaluations across standard benchmarks show that MOMAT matches the defense performance of state-of-the-art methods while avoiding benign overkill and providing substantial efficiency gains, demonstrating that CiM-based modular defenses can make edge-deployed qLLMs both safer and more energy-efficient. We will release the full 223.2k-sample dataset to foster future research.

---


### 8. [High-quality Data Do not Mean Safe! Poisoning LLMs after Data Selection](https://arxiv.org/abs/2610.01367)

**<font color=#1a73e8>作者：</font>** Kaiyang Li, Jiahao Chen, Yuwen Pu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-aligned Large Language Models remain vulnerable to fine-tuning on small sets of harmful or benign-looking samples. However, prior studies typically assume that poisoned samples directly enter downstream fine-tuning, overlooking quality-based selection in practical training pipelines. To fill this gap, we systematically evaluate both the filtering effects against poisoning and the downstream safety impact of retained data. The results reveal that selection removes many overtly harmful samples, yet some retained high-quality samples can still degrade model safety alignment possibly due to their harmful-like training-update patterns at the layer-wise gradient level. Together, these findings expose a practical vulnerability: safety-degrading influence can pass through quality-based selection via retained high-quality samples. To examine its systematic exploitability, we propose Bi-Stage Quality-Constrained Safety-Degradation Text Optimization (Bi-QSTO), which optimizes poisoned samples under an explicit quality constraint to survive selection while preserving their safety-degrading influence. Across poisoning settings, target models, and filtering rates, Bi-QSTO maintains attack effectiveness before and after selection. Even at 90% filtering, harmful-seeded samples achieve a Poisoning Retention Rate above 90% and Harmful Score of 3.30--4.01. Their attack effectiveness strongly transfers across models and their retention advantage generalizes to additional selection methods.

---


### 9. [False Floors: LLM Safety Routing Evaluations Break Under Distribution Shift](https://arxiv.org/abs/2610.01535)

**<font color=#1a73e8>作者：</font>** Amit Singh Bhatti, Vishal Vaddina  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety routers send each request to one of several models and are judged against the best single model. A major routing benchmark picks that comparator on the evaluation data. In the benchmark's own setting this is harmless, but under distribution shift it is not. On HELM Safety the selection cost is 0.003-0.030 of harm under random splits and 0.045-0.113 under held-out categories, comparable to the whole deficit attributed to routing, with its direction holding under either published judge alone. It rises seven- to ninefold on AgentDojo when suites are held out. Across seven safety corpora chosen by rules fixed in advance, three meet a registered interval test and four beat a later permutation null, and three of the four interval misses are corpora where some models have zero observed harm. Prior work proves the direction of this bias. We size it on harm and accuracy, show that it is larger under the held-out splits we measure, and bound it by optimism plus a shift-dependent regret. Scored honestly under shift, routing buys little on these benchmarks. In most pool cells the nested router serves the honest baseline's model, and on the nearly saturated AgentDojo corpus a perfect pre-dispatch router is worth at most two points of harm. We also find a model's expressed recognition of a late injection steerable. On held-out reruns an attacker who knows which model it faces lowers GPT-5.4's judged recognition by 19.6 points, confirmed by an independent label. In an offline counterfactual composition into a controller, the same attack raises or lowers estimated harm depending on the fallback model. Safety routing should be evaluated under shift, against a baseline chosen without the test labels, and recognition-based defences should be scored on harm against an attacker who chooses what the model sees.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
