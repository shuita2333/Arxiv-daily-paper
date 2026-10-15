# 🔐 大模型安全相关研究 | 2026年10月16日

> 本类共 **10** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [TRACER: Trace-Regularized Training Against Indirect Prompt Injection](https://arxiv.org/abs/2610.19133)

**<font color=#1a73e8>作者：</font>** Kshitij Mishra, Salem Lahlou, Nils Lukas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection uses untrusted retrieved content, tool outputs, or agent messages to override an LLM's intended behavior. We show that defense robustness is channel-conditioned: the same attack succeeds 18% of the time as a follow-up message but 53% when placed in retrieved context. We propose TRACER (Trace-Regularized Adversarial Channel Exposure with Reward-shaping), a channel-aware adversarial training method that samples presentation wrappers and combines an answer-anchored, evidence-gated reward with ATRC, which aligns attacked reasoning with clean evidence when an injection is invalid. On GSM8K with Qwen2.5-3B-Instruct, TRACER reduces RAG-framed ASR from 65.5% to 6.1% while preserving 78-82% clean accuracy. Joint RAG+tool training achieves 13.9% average ASR across framings at 3B scale, while a single epoch at 7B reaches 9.4%. These results demonstrate that robust defenses must explicitly train and evaluate across deployment channels.

---


### 2. [Did the LLM Answer the Question? A Semantic Reconstruction Game for Jailbreak Evaluation](https://arxiv.org/abs/2610.19306)

**<font color=#1a73e8>作者：</font>** Liam Davis, Romain Emil-Popescu, Suman Jana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks against large language models (LLMs) are evaluated using attack success rate (ASR), which depends on correctly identifying responses that fulfill prohibited requests. Existing evaluators can mistake refusals or topically related responses for successful attacks. We show that changing only the judge LLM can alter reported ASR by up to $82$ percentage points. We introduce the semantic reconstruction game, a training-free evaluator that decomposes compliance judgments into constrained semantic comparisons. Given only a response, an LLM reconstructs the request answered by its substantive content, excluding information merely repeated or refused. The game compares this reconstruction against similar decoy requests to determine whether it matches the original request, allowing abstention when neither candidate matches. Across three off-the-shelf LLM judges, the game achieves the lowest mean error against human labels among evaluated methods and reduces variation in reported ASR. It prioritizes avoiding false positives, even at the cost of missing some successful jailbreaks.

---


### 3. [DANGERLENS: Probing Dangerous Representations Hidden by Safety Alignment](https://arxiv.org/abs/2610.19365)

**<font color=#1a73e8>作者：</font>** Tianzhuo Yang, Shaoheng Yan, Lin Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment teaches language models to refuse harmful requests, yet the internal accessibility of hazardous concepts can retain traces of earlier training. Can checkpoints with equally safe behavior differ in what remains accessible behind their refusals? In this work, we investigate this question through paired training histories and a direct audit of intermediate representations. We introduce DANGERLENS, a probe that maps hidden states into vocabulary space and uses blinded semantic judgments to distinguish harmful goals and operational means from hazard recognition and safety control. Experiments on three Qwen1.5 scales show that checkpoints with prior harmful exposure generally retain greater hazardous concept accessibility after the same safety alignment, with the strongest separation in intermediate and later layers. The same harmful update also produces different behavioral trajectories from closely matched starting points. Human relevance validation and readout ablations reinforce the measured accessibility contrast. Our findings show that training history remains visible inside behaviorally matched models and motivate internal accessibility audits alongside output safety evaluations.

---


### 4. [AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety](https://arxiv.org/abs/2610.19422)

**<font color=#1a73e8>作者：</font>** Chenxu Wang, Xiaoyu Wen, Han Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce AgentSafeEvo, a co-evolutionary reinforcement learning framework for agent safety built on an attacker-defender game spanning diverse tasks and attack types. The attacker learns to construct adversarial agent tasks that expose weaknesses in the defender's tool use, while the defender learns to complete tasks safely under these attacks. We further introduce learnability-guided task weighting, which uses within-task defender-reward variability to adjust each task's contribution to attacker and defender updates. Extensive experiments on agent safety and general capability benchmarks demonstrate that our method improves adversarial robustness while maintaining general agent capabilities.

---


### 5. [Are You Reading the Right Thing? Rethinking Internal Signals for Prompt-Injection Detection](https://arxiv.org/abs/2610.19452)

**<font color=#1a73e8>作者：</font>** Sarthak Gupta, Priyanka Tembey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Several recent studies propose detecting prompt injections from a language model's internal state. However, these methods do not measure a single security property. Residual-stream probes, attention scores, role projections, exposure probes, and concept readouts may capture injection presence, recognition, information routing, or behavioral influence. It is therefore unclear what differences in prompt-injection detection performance reveal about the internal signals these methods read. We study how five representation-reading methods vary under a common structured indirect prompt-injection setup on Qwen3.6-35B-A3B and Gemma-4-26B-A4B-it. We evaluate each method by how well it distinguishes injected prompts from benign controls. We then further analyze each detection method's ability to detect attacks in cases where they are successful and in cases where they are not. This helps us better assess what properties each detection method might rely on. Methods trained to detect injection presence or attack-related concepts generally separate unsuccessful injections more strongly from benign inputs, whereas attention diversion, exposure, and role-confusion-based methods separate successful injections more strongly on both models. Attention Tracker provides the strongest consistent successful injection separation, reaching 0.949 AUROC on Qwen and 0.887 on Gemma. These results suggest that signals closer to response formation may better encode information about an attack's success, and that detection performance can depend strongly on the prompt template. We share the data associated with this study at this https URL

---


### 6. [Moral Combat: Exploiting Moral Foundations Theory to Jailbreak LLMs](https://arxiv.org/abs/2610.19587)

**<font color=#1a73e8>作者：</font>** Adel Khorramrouz, Yi-Chia Wang, Sharon Levy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social psychology has long described how people can be persuaded to interpret a harmful act as moral. Recent research suggests that Large Language Models (LLMs) echo aspects of human psychology, from cognitive biases to social conformity. This raises a question with direct safety implications: can LLMs be moralized to bypass safety guardrails? We answer this question with a multi-agent framework grounded in Moral Foundations Theory (MFT). Given a harmful request that is initially refused, our agents diagnose which moral foundation (MF) the prompt is violating, identify a justifiable foundation under which the same request appears virtuous, rewrite the prompt accordingly, and reinforce it with generated precedents of comparable moral reframing. We evaluate our framework on harmful prompts from three well-known jailbreak datasets across five open-source and proprietary models. Our analysis reveals that models are highly susceptible to moralization, exhibiting high single-trial jailbreak rates with success increasing further under repeated attempts. We also find that safety benchmarks are imbalanced in the MFs they violate, concentrating on foundations toward which models already exhibit biases.

---


### 7. [Are We Really Measuring Forgetting? Pitfalls in Evaluating Machine Unlearning for Multimodal LLMs](https://arxiv.org/abs/2610.19613)

**<font color=#1a73e8>作者：</font>** Oscar Chew, Po-Yi Lu, Yi-Jie Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As machine unlearning for multimodal large language models (MLLMs) rapidly advances, rigorous evaluation of its effectiveness becomes increasingly important. However, existing benchmarks largely inherit evaluation protocols from text-only unlearning and overlook the unique challenges of unlearning in multimodal settings. In this work, we identify three major pitfalls that may lead to misleading conclusions: the lack of heldout evaluation to distinguish genuine concept-wise forgetting from instance-wise overfitting, the reliance on synthetic, fine-tuned knowledge rather than real-world knowledge acquired during pre-training, and unfair method comparisons caused by applying the same training settings to different unlearning methods. To address these challenges, we introduce GEMMU (Generalizable Evaluation for Multimodal Machine Unlearning), a benchmark built on real-world knowledge and a principled evaluation protocol. Re-evaluating representative unlearning methods under GEMMU reveals substantial generalization gaps and challenges conclusions drawn from previous benchmarks. Our findings highlight the importance of rigorous evaluation for advancing multimodal machine unlearning and provide guidelines for future benchmark design.

---


### 8. [Diagnose Before You Refine: Multi-Dimensional Judge Feedback for Query-Efficient Jailbreak Attacks](https://arxiv.org/abs/2610.19971)

**<font color=#1a73e8>作者：</font>** Yixin Tan, Chia-Yi Hsu, Jiayang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated jailbreak attacks rely on evaluation feedback to optimize adversarial prompts, but existing methods often lack fine-grained diagnostic information. We propose Jev-Guided Strategy Bandit (JSB), a query-based jailbreak framework that leverages multi-dimensional probabilistic feedback to guide prompt optimization. JSB combines continuous jailbreak scoring with targeted refinement, strategy switching, and best-state reseeding to balance exploration and refinement. We evaluate JSB on two harmful request datasets across five open-source and three closed-source LLMs. Under a budget of only 10 target-model queries, JSB achieves an average HarmBench attack success rate of 89.8\% across ten open-source settings, consistently outperforming existing automated jailbreak attacks. Further analyses demonstrate its effectiveness under varying query budgets and attacker models. Defense experiments also reveal limitations in existing filtering mechanisms and highlight the potential of Jev-based output filtering.

---


### 9. [Beyond Static Cues: Unified Dynamic Detection of MLLM Backdoors via Dual-Flow Trajectory Analysis](https://arxiv.org/abs/2610.20319)

**<font color=#1a73e8>作者：</font>** Yinzhen Huang, Jiahe Xie, Yitong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, yet their susceptibility to backdoor attacks remains a formidable challenge. While existing defenses have evolved from visual-centric patch cues to unsupervised internal attention statistics, they are fundamentally constrained by a reliance on static snapshots and attack-specific heuristics. Given the intricate interplay between dual modalities, the vast design space for multimodal triggers allows diverse threats, such as textual injections, sub-perceptual noises, and coordinated cross-modal triggers, to easily circumvent such rigid priors, particularly when attack types are unknown in real-world applications. In this paper, we rethink backdoor detection by shifting the diagnostic paradigm from static observations to dynamic output evolution. We observe that a successful attack inevitably hijacks the model's decoding trajectory, skewing internal modal contributions during generation while maintaining an abnormal output invariance despite input perturbations. To capture this behavior, we propose EVO-Detect, a unified detection framework that monitors the dynamic evolution of internal signals during early decoding steps through two complementary channels: Attention Flow and Logits Flow. The attention branch measures how image-text attention allocation evolves during early generation, whereas the logits branch quantifies the sensitivity of the output distribution to modal perturbations through interventional ablations. We then convert these trajectories into compact sample-level metrics and normalize them against negative-control signatures so that natural perturbations are less likely to be mistaken for backdoor evidence. Extensive evaluations show that our approach substantially outperforms state-of-the-art baselines such as BYE and TCAP across diverse attack families.

---


### 10. [Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge](https://arxiv.org/abs/2610.20570)

**<font color=#1a73e8>作者：</font>** Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples. We document three DPO attempts, all negative, including a case where the training reward margin reaches 1.0 while free generation does not change at all, and show that safety came from a dedicated safety-SFT (LLM-jp AnswerCarefully style), refined over three iterations until closing the safety-helpfulness frontier. A controlled scan of the fraction of general data in the safety-SFT mix (10% to 60%) reveals a non-monotonic over-refusal curve with a knee point at 40-50%. The final model is compared against four external PT-BR models on the same items, with Wilson confidence intervals and paired McNemar tests with Holm-Bonferroni correction: the lower bound of its safety interval (94.1%) lies above the upper bound of all four baselines. We also report a methodological finding for LLM-judge evaluation: on two of six safety items in MT-Bench-PT, the judge categorically refuses to assign a score regardless of the evaluated response, silently reducing the effective N of that category in every prior report of the project. We complement this with an n-gram decontamination check and a Chinchilla-anchored compute-budget table that attributes the gap in general capability to pre-training scale rather than alignment methodology. All code, raw data, logs, and scripts that produce every reported number are publicly released.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
