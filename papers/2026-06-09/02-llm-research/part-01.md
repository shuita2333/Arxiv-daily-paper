# 🧠 大模型相关研究 | 2026年06月09日

> 本类共 **114** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-114](./part-03.md)

---

### 1. [SafeGene: Reusable Adapters for Transferable Safety Alignment](https://arxiv.org/abs/2606.06519)

**<font color=#1a73e8>作者：</font>** Yanghan Wang, Zhiqiang Kou, Fu Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-weight LLMs are increasingly fine-tuned into customized assistants, but downstream fine-tuning can weaken safety alignment and make models more vulnerable to malicious prompts, even when the training data is not intentionally harmful. This creates a recurring safety recovery problem as target models are repeatedly updated with new task data or user interactions. We propose SafeGene, a reusable safety-adapter module designed for cross-task reuse within each architecture-compatible model family. Rather than treating safety recovery as a model-specific repair step, SafeGene treats safety capability as an independent, reusable adapter representation decoupled from task-specific updates. This representation is obtained from aligned--degraded model discrepancies, refined into task-transferable safety vectors through data-aware layer selection, and expressed in each downstream task-adapted model via few-shot layer-wise coefficient recalibration. Experiments across multiple model families, downstream tasks, and safety judges show that SafeGene-enhanced models reduce harmful response rates while maintaining downstream performance, outperforming representative safe adaptation methods in safety--utility trade-off.

---


### 2. [Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory](https://arxiv.org/abs/2606.06523)

**<font color=#1a73e8>作者：</font>** Ruida Wang, Jerry Huang, Pengcheng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equipping Large Language Models (LLMs) to execute reliable multi-step workflows has become a central challenge in artificial intelligence. Despite recent advances in LLMs' agentic capabilities, most agent systems still lack formal methods for specifying, verifying, and debugging their workflow and execution trajectories. This challenge mirrors a long-standing problem in mathematics, where the ambiguity of natural languages (NLs) motivates the development of formal languages (FLs). Inspired by this paradigm, we propose **Lean4Agent**, to the best of our knowledge, the first framework that uses Lean4, a dependent-type FL to model and verify agent behavior. **Lean4Agent** launches **FormalAgentLib**, an extensible Lean4 library for formally modeling and verifying agent workflows' semantic consistency under explicit assumptions, and enabling localization of execution-time failures revealed by trajectories. Building on **FormalAgentLib**, we further develop **LeanEvolve**, which applies results in **FormalAgentLib** to revise workflows to enhance its capability. Extensive experiments on a hard problem subset of SWE-Bench-Verified and a subset of ELAIP-Bench across 5 leading LLMs indicate that the verification-passing workflows outperform the failing ones by an average of **11.94%**, and **LeanEvolve** further improves SWE performance by **7.47%** on average. Furthermore, **Lean4Agent** establishes a foundation for a new field of using expressive dependent-type FL to formally model and verify agent behavior.

---


### 3. [Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529)

**<font color=#1a73e8>作者：</font>** Catherine Ge-Wang, Tyler Crosse, Benjamin Hadad IV 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An attacker that strategically chooses when to attack is much harder to catch than one that attacks indiscriminately. AI control is a safety framework for deploying capable but untrusted AI agents under the oversight of a weaker, trusted monitor and a limited human audit budget. Control evaluations stress-test these protocols by pitting a red-team attack policy against the blue-team monitor, but current evaluations typically assume attackers that do not strategically select when to attack. We study this capability, attack selection, in agentic settings by decomposing attack decisions into a start policy, which decides when an attacker should attack, and a stop policy, which decides when an attacker should abort an ongoing attack. Across two agentic settings, BashArena and LinuxArena, both policies substantially lower measured empirical safety without changing the underlying attack capability. At a 1% audit budget, our start policy reduces safety by 20pp on both BashArena and LinuxArena, and our stop policy reduces safety by 20pp on BashArena and 28pp on LinuxArena. These reductions should be interpreted as upper bounds on the effect of attack selection. Existing control evaluations may therefore yield overly optimistic safety estimates against selective attackers. We recommend that future evaluations, system cards, and safety cases elicit attack selection to produce more realistic safety estimates.

---


### 4. [GOPAgen: Motion-Aware and Efficient Agentic Long-Video Understanding with Structural Memory and Hierarchical Reasoning](https://arxiv.org/abs/2606.06532)

**<font color=#1a73e8>作者：</font>** Haozhe Chi, Yang Jin, Yadong Mu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in agentic long video understanding, existing methods still lack detailed motion comprehension coupled with an efficient memory architecture. In this paper, we propose GOPAgen, a novel approach that first integrates video codec into the video understanding framework via a meticulously designed motion agent trained on Groups of Pictures (GOPs) from video codec. We further develop a GOP tree reasoning algorithm, which is naturally aligned with video codec and enhances the model's ability to understand local detailed motions in videos. Additionally, we carefully design a structural memory mechanism that integrates local motion information with detailed captions in structural pages, and propose an efficient coarse-to-fine zoom-in algorithm to fully exploit the structural memory. Furthermore, we incorporate a motion vector database into the framework to enable efficient retrieval of motion vectors at different granularities. Overall, our method achieves superior Video Question Answering (VQA) performance on various video understanding benchmarks, including MotionBench and Egoschema, thereby demonstrating the superiority of our proposed framework.

---


### 5. [WorldBench: A Challenging and Visually Diverse Multimodal Reasoning Benchmark](https://arxiv.org/abs/2606.06538)

**<font color=#1a73e8>作者：</font>** Yida Yin, Harish Krishnakumar, Chung Peng Lee 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world applications, models are expected to perform reliably across diverse settings. Yet, many existing multimodal benchmarks expand task types without capturing the visual diversity needed to handle open-ended visual inputs. We present WorldBench, a challenging and visually diverse reasoning benchmark to evaluate Multimodal Large Language Models (MLLMs). We build a taxonomy of thousands of visual concepts across multiple domains (e.g., living things). Guided by this taxonomy, we curate a broad collection of images from search engines and existing datasets to comprehensively represent the visual world. Through structured trial-and-error, we manually design challenging questions that frontier MLLMs fail to answer. On quantitative and human evaluations, WorldBench achieves higher visual diversity than any existing diverse benchmark. Evaluating 15 MLLMs on WorldBench reveals weaknesses in visual understanding: even the strongest model reaches only 64.0% accuracy, while some models perform marginally above chance-level. We hope our work highlights the importance of visual diversity in building multimodal benchmarks.

---


### 6. [Elmes*: Automated Construction of Fine-Grained Evaluation Rubrics for Large Language Models in Long-Tail Educational Scenarios](https://arxiv.org/abs/2606.06546)

**<font color=#1a73e8>作者：</font>** Tao Liu, Ye Lu, Ruohua Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) for education requires measuring how models teach, not only what they know. Existing benchmarks emphasize domain-general correctness or depend on manually designed rubrics that scale poorly to long-tail pedagogical scenarios. We introduce Elmes*, an end-to-end framework for constructing, refining, and applying fine-grained scenario-specific rubrics. Elmes* combines a declarative multi-agent engine for teacher--student--judge interactions with SceneGen, a self-evolving module that co-optimizes evaluation criteria and test data from expert-defined pedagogical dimensions. Using Elmes*, we build Edu-330, covering 330 scenarios across 11 subjects, 3 grade bands, and 10 task types, with over 1{,}000 second-level indicators. Experiments on Edu-330 and four expert-authored gold-standard scenarios show that educational capability is multidimensional: top-tier LLMs differ mainly in creativity and values integration, knowledge-strong models may fail at Socratic scaffolding, and the education-specialized InnoSpark achieves the best human-evaluated average score. LLM judges preserve human-comparable rankings with much lower scoring variance, but exhibit judge-specific biases such as self-preference. Ablations show that expert-scored few-shot anchoring improves human--LLM alignment, while reasoning enforcement and greedy decoding are model-dependent. Elmes* thus provides scalable diagnostic infrastructure for pedagogically grounded LLM evaluation.

---


### 7. [FAIR-Calib: Frontier-Aware Instability-Reweighted Calibration for Post-Training Quantization of Diffusion Large Language Models](https://arxiv.org/abs/2606.06547)

**<font color=#1a73e8>作者：</font>** Haoyu Huang, Linlin Yang, Sheng Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) refine tokens iteratively but commit them irreversibly, leading to a "stability lag" where early decisions remain fragile even after being written. We reveal that Post-Training Quantization (PTQ) error easily flips these borderline decisions at the write frontier, which are then permanently locked in and amplified. To address this, we propose Frontier-Aware Instability-Reweighted Calibration (FAIR-Calib), a two-stage PTQ framework for dLLMs. Stage I probes a full-precision teacher to estimate a position prior that combines frontier hits and masked-stage reliability. Stage II performs off-policy, layer-wise calibration by minimizing a reweighted hidden-state MSE, effectively prioritizing the protection of fragile frontier states without requiring expensive end-to-end diffusion rollouts. We further theoretically justify our weighted objective as a surrogate for output KL divergence. Empirically, FAIR-Calib consistently outperforms state-of-the-art baselines on LLaDA and Dream (W4A4), significantly reducing frontier decision flips and suppressing post-commit mismatches across diverse benchmarks.

---


### 8. [Skip a Layer or Loop It? Learning Program-of-Layers in LLMs](https://arxiv.org/abs/2606.06574)

**<font color=#1a73e8>作者：</font>** Ziyue Li, Yang Li, Tianyi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform inference by following a fixed depth and order, non-recurrent execution of all layers. We reveal the wide existence of training-free, flexible, dynamic program-of-layers (PoLar), where pretrained layers can be packed as modules and then skipped or looped to form a customized program for each input. For most inputs, substantially shorter program executions can achieve the same or better accuracy, while incorrect predictions of the original LLM can be corrected by alternative programs with fewer layers. These observations indicate that inference admits multiple valid latent computations beyond the standard forward pass. To efficiently achieve PoLar in practice, we propose a lightweight PoLar prediction network, which learns to generate execution programs that dynamically skip or repeat pretrained layers for each input. Experiments on mathematical reasoning benchmarks demonstrate that PoLar consistently improves accuracy over standard inference and prior dynamic-depth methods, often while executing fewer layers, and that these gains persist under out-of-distribution evaluation. Our results suggest that fixed-depth execution captures only a narrow subset of an LLM's latent reasoning capacity.

---


### 9. [Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning](https://arxiv.org/abs/2606.06586)

**<font color=#1a73e8>作者：</font>** Jonathan von Rad, Louis Arts, George Burgess 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained predominantly on English data encode substantial world knowledge, yet often fail to express it reliably in other languages, a phenomenon known as cross-lingual factual inconsistency. To study and address this, we introduce PolyFact, a large-scale parallel multilingual factual QA dataset containing 100K Wikidata-grounded facts across 12 typologically diverse languages. Using PolyFact, we compare light continual pretraining (CPT), supervised fine-tuning (SFT), and reinforcement learning via Group Relative Policy Optimization (GRPO) for improving cross-lingual factual recall in Qwen-2.5-7B and OLMo-2-1124-7B. We find that GRPO consistently outperforms SFT, improving both cross-lingual consistency and generalization to unseen languages, while CPT on parallel data yields limited additional gains. Mechanistic analyses further show that GRPO reorganizes multilingual routing by reducing language specialization in MLP layers and attention heads, thereby promoting more shared cross-lingual representations. We release our code, models, and dataset.

---


### 10. [Re-Centering Humans in LLM Personalization](https://arxiv.org/abs/2606.06614)

**<font color=#1a73e8>作者：</font>** Lechen Zhang, Jiarui Liu, Tal August  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite growing interest, most evaluations of large language models' (LLMs') personalization abilities have relied on synthetic data. It remains unclear how well current personalization systems work for real users. In this paper, we study the gap in LLM personalization performance when using synthetic versus human data. We collect human conversations (550 conversations) and judgments across three stages of personalization: extracting user attributes from conversations (5,949 judgments), pairing relevant attributes with new prompts (11,919), and incorporating relevant attributes into a personalized response (1,101). Incorporating human data reveals system limitations at each stage. Models struggle to extract attributes from human conversations, disagree with human judgments on relevant attributes, and generate personalized responses that humans judge no better than generic responses (though that LLM judges widely rate as better). We introduce two lightweight training-based interventions that shift automated personalization evaluation closer to human data in our first two stages. However, in our third stage we find that learned reward models achieve only modest correlation with human ratings, suggesting that human-aligned personalization quality judgments are difficult to model directly. Our collected data provides a foundation for studying how models should extract, select, and incorporate user information in ways that humans find useful.

---


### 11. [UnpredictaBench: A Benchmark for Evaluating Distributional Randomness in LLMs](https://arxiv.org/abs/2606.06622)

**<font color=#1a73e8>作者：</font>** Amirhossein Abaskohi, Amirhossein Dabiriaghdam, Liang Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce UnpredictaBench, an evaluation that tests the ability of large language models (LLMs) to capture true underlying distributions. As LLMs are increasingly used as substitutes for other entities (e.g., for humans in economic simulations), the tendency of many models to collapse towards a single plausible answer means a failure to capture the unpredictability of real systems. Recent work on improving output diversity is insufficient for this setting: simulation requires samples that are calibrated to a target distribution, not merely varied outputs. UnpredictaBench isolates a simplified but fundamental version of this problem: sampling outcomes from individual target distributions, including canonical statistical distributions, distributions induced by stochastic programs, and natural-language scenarios that describe random processes. We introduce 448 such problems together with KS@N, a general-purpose evaluation metric that quantifies how well a model outputs approximate black-box target distributions via the Kolmogorov-Smirnov statistical test. This is the rate at which we fail to reject model samples of size N against ground-truth samples, with larger N indicating greater difficulty. Tested across open and proprietary models, we find a large spread in distributional capabilities. For instance, when models generate samples of size 100 (KS@100, our standard metric), scores range from near 0 to over 20%. No model is able to achieve over 40% at KS@100, showing significant headroom in distributional sampling as a capability. Although adding reasoning can somewhat increase scores, we find no immediate solution for this issue. UnpredictaBench shows that even simple distributional simulation remains challenging, making it a necessary first step toward using LLMs as stand-ins for complex systems.

---


### 12. [How Language Models Fail: Token-Level Signatures of Committed and Persistent Reasoning Failures](https://arxiv.org/abs/2606.06635)

**<font color=#1a73e8>作者：</font>** Tanvi Thoria, Kiana Jafari, Marc R. Schlichting 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Failures in language model reasoning emerge through distinct processes that leave identifiable signatures in the reasoning trace. We characterize these failures using token-level uncertainty signals, finding they arise through two empirically distinguishable processes. The first is committed failure, in which a model locks onto an incorrect reasoning path early in its trace. A central diagnostic signature is the commitment point, beyond which considering additional tokens hurt rather than help failure detection. In the second, persistent uncertainty, uncertainty instead accumulates throughout, and the full trace is needed to best distinguish failing from successful completions. These signatures reproduce across 23 model-dataset configurations, with the framework's falsifiable predictions holding in 20 of 23 cases, well above chance across both failure modes. Finally, we demonstrate our failure mode framework has direct implications for self-consistency, identifying when uncertainty signals complement it and when it can be selectively skipped. These results offer a foundation for understanding when LLM reasoning failures become detectable and for adapting detection strategies accordingly.

---


### 13. [The Identity Trap in EEG Foundation Models: A Diagnostic Audit](https://arxiv.org/abs/2606.06647)

**<font color=#1a73e8>作者：</font>** Jun-You Lin, Ying Choon Wu, Tzyy-Ping Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective. EEG foundation models (FMs) report strong accuracy on clinical resting-state EEG. However, high accuracy under subject-disjoint cross-validation remains ambiguous: it can reflect a genuine clinical biomarker, or subject-identity features that correlate with the label. We name this the Identity Trap and ask whether it can be diagnosed at the representation level before fine-tuning.
Approach. We propose FMScope, a frozen-representation protocol packaging five diagnostics: variance decomposition, subject-axis erasure, aperiodic 1/f ablation, layer-wise label probing, and within-subject direction consistency. We apply it to three pretrained FMs (LaBraM, CBraMod, REVE) across four datasets in a 2x2 layout: subject relation of label x presence of a consensus cross-subject EEG marker.
Main results. (i) The Identity Trap is universal: frozen subject-variance is 13-89x a random null in 12/12 pairs, rising in all 12 under fine-tuning (+10 to +63 pp). This dominance is a removable linear axis: erasing it improves label decoding where the label varies within subject (+6 to +12 pp in primary cells; +4 to +27 pp across external cohorts). (ii) Aperiodic 1/f is one subject carrier: removing it drops the subject probe by 9-19 pp on LaBraM and CBraMod. REVE saturates subject identity without measurable aperiodic dependence. (iii) Fine-tuning amplifies label-variance only in cells with a literature-established cross-subject marker.
Significance. The Identity Trap is a physically-grounded instance of shortcut learning: the preferred cue has a measurable physiological component, and subject-disjoint splitting alone cannot rule it out. FMScope separates gains reflecting a biological marker from those reflecting subject identity.

---


### 14. [The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment](https://arxiv.org/abs/2606.06667)

**<font color=#1a73e8>作者：</font>** Jiachen Zhao, Zhengxuan Wu, Aryaman Arora 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The mechanisms behind LLMs' broad over-generalization beyond training examples remain unclear. Emergent misalignment (EM) offers a striking case study: finetuning on narrow tasks induces broad misalignment to semantically-unrelated test domains. In this work, we propose the Piggyback Hypothesis: the chat-template tokens can piggyback the finetuned behaviour onto out-of-domain queries. We validate this hypothesis by showing that subtle perturbations to the prefix (tokens preceding all user queries), or patching the prefix representations with those from the unfinetuned model, can restore alignment without changing the user query. Building on this finding, we propose Token-Regularized Finetuning (TReFT), which regularizes specific token representations during training to mitigate EM. Across different models and multiple EM-inducing datasets, TReFT reduces EM while preserving in-domain learning. On Llama-3.1-8B finetuned on the legal domain, TReFT achieves 33.5% more EM reduction than data interleaving with a retain set of aligned examples. We further show that TReFT extends to other narrow-finetuning settings, including abstention, tool use, and refusal (off-topic generalization is reduced by 54.3% on average), supporting the Piggyback Hypothesis. Broadly, our work highlights that LLMs may learn and generalize in unintended ways and suggests a path toward more constrained finetuning. It also calls for further study of how shared input features can piggyback model behavior across domains.

---


### 15. [Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning](https://arxiv.org/abs/2606.06673)

**<font color=#1a73e8>作者：</font>** Ujjwal Bhatta, Utsabi Dangol, Sumaly Bajracharya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse rewards and heterogeneous task sequences remain persistent challenges in Reinforcement Learning (RL), often resulting in slow convergence, weak generalization, and inefficient exploration. We propose Uncertainty-Aware LLM-Guided Policy Shaping (ULPS), a novel framework that integrates a calibrated Large Language Model (LLM) into the RL training loop to provide structured, uncertainty-modulated behavioral guidance. ULPS employs an A*-based oracle to synthesize optimal symbolic trajectories, which are used to fine-tune a BERT-based language model. During training, this model supplies action suggestions whose influence is conditioned on epistemic uncertainty estimated via Monte Carlo (MC) dropout. An entropy-based blending mechanism adaptively balances LLM guidance and the learned policy (via Proximal Policy Optimization, PPO), allowing the agent to prioritize reliable priors while preserving adaptability. We evaluate ULPS on the MiniGridUnlockPickup benchmark and observe consistent improvements in success rate, reward efficiency, and sample complexity over unguided, uncalibrated, and standard RL baselines. ULPS achieves more than 9% improvement in execution accuracy after fine-tuning, requires fewer environment interactions, and yields higher reward AUC. Our results demonstrate that integrating symbolic A* trajectories, pretrained language priors, and uncertainty-aware control offers a principled and effective approach to multi-task reinforcement learning in sparse-reward domains, with potential extensibility to partially observable and multi-agent settings.

---


### 16. [What Do People Actually Want From AI? Mapping Preference Plurality](https://arxiv.org/abs/2606.06674)

**<font color=#1a73e8>作者：</font>** Julia Sepúlveda Coelho, Scott A. Hale  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are often fine-tuned through Reinforcement Learning from Human Feedback (RLHF) to align with people's preferences and values. However, this method has known limitations: it aggregates conflicting preferences, often relies on unrepresentative samples, and uses only binary comparisons. Analysing 1,500 open-ended responses from the PRISM dataset across 75 countries, we examine what people actually want from AI systems and reveal concrete failures of current methods.
We find that different people want different things: most values are requested by fewer than a quarter of respondents, with truthfulness the sole exception at 49%. Furthermore, the same words hide divergent meanings: when people describe what they mean by "truthfulness", they reveal distinct, potentially incompatible, epistemological bases, as some ask for sourced claims, some for expert opinions, and some even ask for unpopular views. Certain capabilities, namely how human-like a model behaves, and some features, like AI guardrails, are outright controversial, with some desiring them and others rejecting them. We additionally find that people often use contextual distinctions (what AI should do "by default" versus "if requested") that binary comparisons cannot capture.
These findings expose fundamental problems in current alignment practices. When 49% request truthfulness but define it differently, this is unlikely to be captured by a single reward model. The persistence of high hallucination rates in well-funded models, despite users' clear demands for accuracy, suggests that current methods fail to identify actual preferences. This paper sheds light on the situated, contested, imperfect signals that are currently being flattened into universal preference models, a practice others have characterised as epistemic violence.

---


### 17. [The Geography of Algorithmic Judgment: LLM Intermediaries, Place Identity, and Racial Steering in Housing Search](https://arxiv.org/abs/2606.06694)

**<font color=#1a73e8>作者：</font>** Hana Samad, Trung Lam, Christoph Mügge-Durum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly assuming an intermediary role in housing search through the integration of listing platforms within conversational interfaces, mediating access to information, search, and recommendations within urban settings. We expand on prior work on racial steering in LLMs by conducting a behavioral audit of seven open-weight and closed-source LLMs across four U.S. cities, testing location recommendations across three iterative prompting conditions that progressively add lifestyle preference context and reflect fair housing paired-testing methodologies. We find that steering is an emergent behavior of the model's interpretive license rather than primarily a static property. Steering results from the interaction of a user's identity, preference articulation, and the spatial logic that a model has internalized about learned representations of place, preference, and opportunity in a given city, and how different types of users relate to it. While steering was present, it was not uniform in direction or magnitude across evaluated conditions. Preference-conditioned testing often increased or reconfigured the number of models that exhibited steering behaviors relative to baseline conditions, suggesting that LLMs may interpret what the same housing preference means differently depending on the racial identity of the user. Our findings also demonstrate that the city is not a neutral testing unit for LLM evaluation in place-based sectors, and results from one local market cannot be assumed to generalize to another. Local and domain expertise will be required in the housing sector to ensure that legal and institutional commitments to fair housing are not undermined while adopting AI tools that mediate spatial access.

---


### 18. [MMBU: A Massive Multi-modal Biomedical Understanding Benchmark to Probe the Perception Capabilities of Vision-Language Models](https://arxiv.org/abs/2606.06696)

**<font color=#1a73e8>作者：</font>** Ryan D'Cunha, Alejandro Lozano, Xiaoxiao Sun 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision and language models (VLMs) hold immense promise to transform biomedical imaging workflows, from detecting lesions in chest X-rays to profiling cellular features in microscopy. Realizing this potential, however, requires robust and fine-grained visual perception. Models need to correctly interpret subtle features in images, and they must do so across diverse biomedical modalities, scales, and contexts. Nevertheless, current benchmarks remain limited. To address these gaps, we introduce the Massive Multimodal Biomedical Understanding (MMBU) benchmark. It is the largest biomedical vision and language benchmark to date, covering 35 submodalities with rich structured metadata. It includes both open and closed versions of ungrounded classification, grounded classification, and object detection, enabling systematic evaluation of model performance across biological scales, clinical settings, and imaging modalities. Evaluating 15 open-weight and 2 frontier VLMs, we find that while medical adaptation provides measurable gains for some models, the high accuracy often reported on established benchmarks can mask deficiencies in visual perception and domain generalization.

---


### 19. [USU-Corn-WeedDB: A UAV RGB Image Dataset for Multi-Species Weed Detection in Forage Corn](https://arxiv.org/abs/2606.06709)

**<font color=#1a73e8>作者：</font>** Utsav Bhandari, Saroj Burlakoti, Rhonda Miller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weed pressure in forage corn production causes yield losses of up to 31.5%, yet site-specific weed management (SSWM) systems built on UAV imagery and deep learning remain constrained by the scarcity of field-representative training datasets. We present USU-Corn-WeedDB, a publicly available UAV RGB image dataset collected from a commercial forage corn field in Cache Valley, Utah, designed to support multi-class weed detection under both supervised and semi-supervised learning frameworks. RGB imagery was acquired on 27 June 2025 using an Autel EVO II Dual 640T V2 drone at ~10m above ground level, yielding a ground sampling distance of approximately 0.48 cm/pixel. A total of 366 full-resolution images were tiled into 8,800 patches at 640 x 640-pixel resolution. Of these, 800 images were manually annotated for three weed species; common lambsquarters (Chenopodium album), redroot pigweed (Amaranthus retroflexus), and green foxtail (Setaria viridis) comprising 10,539 bounding-box instances, with the remaining 8,000 tiles retained as an unlabeled pool for semi-supervised experiments. This dataset reflects a natural class imbalance where redroot pigweed constitutes 53.86% of annotated instances, which was preserved intentionally to mirror real field conditions. To validate dataset utility, we trained 28 object detection models spanning five architecture families including YOLOv8, YOLOv9, YOLOv10, YOLO11, YOLO26, and RT-DETR under identical conditions without hyperparameter tuning. Test set mAP@0.5 ranged from 0.773 to 0.840, with lightweight models achieving competitive performance relevant to edge-deployed UAV systems. USU-Corn-WeedDB is publicly available at this https URL.

---


### 20. [Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation](https://arxiv.org/abs/2606.06712)

**<font color=#1a73e8>作者：</font>** Xingyu Su, Jacob Helwig, Shubham Parashar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the transformation of autoregressive models (ARLMs) into diffusion language models (DLMs). Rather than pretraining from scratch, prior work replaces the causal attention in ARLMs with bidirectional attention and then trains the resulting model using a DLM objective. However, these approaches incur two distribution shifts. First, transitioning from a next-token prediction objective to a DLM objective can discard knowledge acquired by the ARLM during training. Second, standard DLMs suffer from a train-inference mismatch, as the training loss is defined on randomly masked sequences rather than the trajectories encountered at inference produced by confidence-based decoding. To address both challenges, we introduce an On-Policy Diffusion Language Model (OPDLM) in which On-Policy Distillation (OPD) is employed for ARLM-to-DLM transformation. Specifically, OPDLM is trained via self-OPD, where the student, an ARLM with bidirectional attention, generates its own trajectories, and the teacher, the original frozen ARLM, distills its knowledge by providing target logits on these trajectories. By training directly in an on-policy manner, OPDLM eliminates the train-inference mismatch in DLMs, while distillation from the original model enhances knowledge retention from the ARLM. Empirical results demonstrate that OPDLM requires 15x to 7,000x fewer training tokens with strong performance across a wide variety of tasks. OPDLM avoids the prohibitive cost of DLM pretraining and positions DLM transformation as a form of ARLM post-training.

---


### 21. [Anchored, Not Graded: Vision-Language Models Fail at Slant-from-Texture Perception](https://arxiv.org/abs/2606.06714)

**<font color=#1a73e8>作者：</font>** Qian Zhang, Michal Golovanevsky, Fulvio Domini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human perception of surface slant from texture exhibits systematic, graded biases that emerge reliably in psychophysical experiments. Prior work showed that unsupervised CNNs reproduce several human-like biases, while supervised CNNs do not. Do Vision-Language Models (VLMs) exhibit similar competences? Across multiple VLM families and model scales, zero-shot and in-context prompting both produce distinctive failures: slant is predicted at only a small set of anchors (e.g., 0\degree, $\pm$25\degree, $\pm$45\degree) with little dependence on stimulus field of view, optical slant, or surface curvature. Supervised fine-tuning partially remediates the failure, but residual anchoring persists. While success in high-level vision-language benchmarks might not require sensitivity to low-level geometric cues, we interpret anchoring as a failure at the representation-to-output language interface: Not necessarily an absence of geometric encoding, but a failure to express it in a graded form.

---


### 22. [Does Topic Sentiment Cause Perceived Ideology? Comparing Human and LLM Annotations in Political News Articles](https://arxiv.org/abs/2606.06715)

**<font color=#1a73e8>作者：</font>** Upasana Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether topic sentiment has a causal effect on perceived political ideology, and whether the answer depends on who assigns the ideology label. Using articles from AllSides, paired with shared sentiment annotations from Llama-3.3-70b-versatile, we compare ideology labels from expert human annotators, GPT-4o-mini (baseline and finetuned), and Llama-3.3-70B. We apply Double Machine Learning (DML) and community-level mediation analysis across all four annotation paradigms. Human annotations yield no significant causal effects at the community level. Fine-tuned GPT-4o-mini achieves the highest classification accuracy (F1=72.48) and is the only annotator paradigm that produces significant community-level treatment effects and significant natural direct effects (NDEs) in mediation. We interpret this as evidence of shortcut learning: fine-tuning on ideology-labeled data causes the model to internalise a spurious sentiment--ideology coupling not operative in human judgment for this task. This coupling is structurally invisible to F1-based evaluation, with implications for the use of LLM annotations as silver labels and as proxies for human judgment in downstream causal analyses.

---


### 23. [Modular Monolingual Adaptation using Pretrained Language Models](https://arxiv.org/abs/2606.06738)

**<font color=#1a73e8>作者：</font>** Nalin Kumar, Ondřej Dušek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building monolingual language models (LMs) for low-resource languages typically relies on adapting pretrained language models (PLMs) by finetuning the whole model on the target language. This approach is widely favored over training from scratch, as it enables effective knowledge transfer. Additionally, prior work has shown that using a language-specific tokenizer can enhance the adaptability. In this work, we hypothesize that full model tuning is often unnecessary and propose a more modular approach. Specifically, we replace the tokens, freeze the corresponding embeddings, and tune the rest of the model. We use Scottish Gaelic, Irish, and Quechua for our experiments, with Quechua being a very low-resource language (8.5k training instances). Evaluation on natural language understanding (NLU) tasks -- mask filling, NER, and POS -- shows that our proposed approach improves performance when adapting models to low-resource languages. Additionally, we provide a comprehensive analysis of the effectiveness of training strategies, the choice of pretrained embeddings, and models.

---


### 24. [OpenSkill: Open-World Self-Evolution for LLM Agents](https://arxiv.org/abs/2606.06741)

**<font color=#1a73e8>作者：</font>** Zhiling Yan, Dingjie Song, Hanrong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents requires adaptation after deployment, but existing approaches assume a usable learning loop, such as curated skills, successful trajectories, or verifier signals. Real open-world deployments may provide none of these, offering only a task prompt. In this work, we study open-world self-evolution, where an agent must build both its skills and its own verification signals from scratch, using open-world resources but no target-task supervision. We propose OpenSkill, a framework that bootstraps this loop: it acquires grounded knowledge and verification anchors from documentation, repositories, and the web, synthesizes them into transferable skills, and refines those skills against self-built virtual tasks grounded in the anchors rather than in target answers. The open world thus supplies both the knowledge to be learned and a supervision-independent practice environment, with target-task supervision reserved for final evaluation. Across three benchmarks and two target agents, OpenSkill attains the best automated pass rate while satisfying the no-supervision constraint. Analysis shows its skills transfer across models without model-specific adaptation, and its self-built verifier aligns with ground-truth outcomes despite never accessing them.

---


### 25. [When to Think Deeply: Inhibitory Deliberation for LLM Reasoning](https://arxiv.org/abs/2606.06745)

**<font color=#1a73e8>作者：</font>** Zhixuan He, Yue Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning Large Language Models can improve problem-solving performance through deliberative inference, but invoking slow reasoning for every input is computationally expensive and often unnecessary. We propose IDPR, a framework for response-conditioned inhibitory deliberation. IDPR first generates a concise intuitive answer and then uses an inhibition controller to decide whether that specific response should be released or suppressed in favor of slow reasoning. Unlike input-only routers, the inhibition controller conditions on the fast answer and fast-side evidence, including confidence, logit margin, parseability, and generation cost. We train the controller from paired fast-slow outcomes and select the inhibition threshold on a held-out validation set under an accuracy-first slow-call budget. On a held-out 5,000-example mathematical reasoning test set, IDPR invokes slow reasoning on only 8.20% of examples and improves accuracy from 47.90% to 48.92%. Under the same slow-call budget, random routing decreases accuracy to 46.76%, while the strongest confidence-based baseline reaches 48.22%. IDPR also achieves the highest corrective precision, showing that response-conditioned inhibition better identifies fast answers that benefit from slow reasoning.

---


### 26. [Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection](https://arxiv.org/abs/2606.06748)

**<font color=#1a73e8>作者：</font>** Jianru Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) reduces but does not eliminate hallucination in large language models. Existing detection methods rely on flat similarity between generated answers and retrieved passages, ignoring structural relationships among evidence pieces and answer claims. We propose Evidence Graph Consistency (EGC), a framework that constructs a local evidence graph per response and computes five structural consistency measures as hallucination indicators. Evaluated on the full question answering split of RAGTruth across six LLMs (5,767 responses), EGC reveals a consistent model-family split: graph consistency features show the expected diagnostic direction for hallucinations in Llama-2 models but exhibit systematic reversal in GPT-4, GPT-3.5, and Mistral-7B. This reversal suggests qualitatively different hallucination patterns across model families and indicates that embedding-based graph consistency cannot serve as a model-independent hallucination detection signal.

---


### 27. [MADRAG: Multi-Agent Debate with Retrieval-Augmented Generation for Training-Free Analytic Essay Scoring](https://arxiv.org/abs/2606.06754)

**<font color=#1a73e8>作者：</font>** Ali Keramati, Shiyuan Zhou, Sharad Mehrotra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present MADRAG, a training-free framework for analytic essay scoring that combines multi-agent reasoning with retrieval-augmented grounding. Unlike standard LLM-as-judge approaches, which are prone to bias and unstable scoring, MADRAG decomposes evaluation into an interactive process: an Advocate identifies strengths, a Skeptic critiques weaknesses, and a Judge aggregates their arguments into a final score. Crucially, the Judge is augmented with rubric-aligned exemplar retrieval, enabling calibration through comparison with scored examples. Our results show that MADRAG significantly outperforms prompt-based baselines while approaching the performance of supervised systems without requiring task-specific training. Ablation studies demonstrate that retrieval drives calibration gains, while debate improves reasoning on higher-level traits. Our findings highlight the complementary roles of structured interaction and external memory in reliable LLM-based evaluation.

---


### 28. [PromptPrint: Behavioral Biometrics Through Natural Language Prompting in LLMs](https://arxiv.org/abs/2606.06755)

**<font color=#1a73e8>作者：</font>** Shaiv Patel, Kartik Narayan, Vishal Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship attribution research has traditionally focused on long-form, expressive texts; however, interactions with large language models (LLMs) are typically brief and task-driven prompts. This raises a fundamental question: do such prompts contain a stable, author-identifiable, and distinctive signal? We introduce PromptPrint, a systematic study of prompt-based identity, the hypothesis that a user's habitual vocabulary, syntax, and discourse patterns form a learnable behavioral biometric. Using 20,680 real prompts from 1,034 users, we establish three key findings. First, lexical representations significantly outperform semantic encoders, supporting the "lexical stability hypothesis": identity is primarily encoded in surface-level word choice rather than abstract intent. Second, stylometric features exhibit a "uniqueness-consistency paradox": users are highly distinctive across the population, yet behaviorally inconsistent across contexts. Third, adversarial analysis reveals a clear vulnerability spectrum: identity signals are robust to minor lexical perturbations but degrade substantially under semantic paraphrasing. Overall, our results demonstrate strong identification performance at scale, establishing prompt-based identity as a viable behavioral biometric. This work introduces a new perspective on user modeling in LLM interactions, with important implications for security and privacy. Data and code will be released upon the acceptance of our work.

---


### 29. [A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models](https://arxiv.org/abs/2606.06758)

**<font color=#1a73e8>作者：</font>** Haizhou Xia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Final-answer accuracy, retrieval recall, and citation overlap do not by themselves identify whether a long-context or retrieval-augmented language model used the evidence it was given. A model can answer from parametric memory, fail despite receiving the right passages, or cite evidence without converting it into the requested answer. This paper proposes a matched four-condition evidence-availability protocol--no evidence, full context, retrieved evidence, and oracle-evidence reference--for diagnosing evidence utilization under fixed examples, prompts, score fields, retrieval settings, and validity checks. ONCU is used as a protocol-bound estimator of recovered oracle-reference evidence advantage and is computed only for denominator-valid groups; denominator-free answer, evidence, retrieval, and failure-audit metrics are reported separately. The empirical study evaluates five local open-weight models from the Qwen, Gemma, Llama, and Mistral families across Controlled-ONCU-safe16K, HotpotQA-ONCU, and 2WikiMultiHopQA-ONCU, with 18,000 ONCU-compatible predictions. The main finding is a task-dependent bottleneck split: controlled synthetic settings primarily expose full-context utilization failures, whereas the tested realistic multi-hop settings primarily expose retrieval-chain coverage failures in denominator-free answer and evidence metrics, with ONCU supporting the same direction on oracle-improving groups. The contribution is a diagnostic protocol for separating no-evidence answerability, oracle-evidence recoverability, full-context utilization, and retrieval-conditioned utilization, rather than a single-score leaderboard for long-context or retrieval-augmented systems.

---


### 30. [MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models](https://arxiv.org/abs/2606.06760)

**<font color=#1a73e8>作者：</font>** Aofei Chang, Le Huang, Alex James Boyd 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical large vision-language models (Med-LVLMs) have recently achieved remarkable progress in vision-language comprehension and medical image segmentation. However, existing models still struggle to unify these two capabilities, which is essential for achieving clinically reasoning that connects visual findings with semantic interpretation. We present MedSIGHT, a unified framework that equips Med-LVLMs with structured, pixel-level understanding for grounded visual comprehension. MedSIGHT introduces a novel Region Perceiver module that produces region-centric tokens, encoding spatial information directly into representation space of the language model. We further propose a medical region codebook into the LLM vocabulary, allowing the model to generate discrete region codes as symbolic representations of anatomical and pathological regions. These codes are decoded through the Region Perceiver to reconstruct segmentation mask, achieving end-to-end spatial grounding. Lastly, MedSIGHT combines Region Perceiver, Codebook and LLM using our proposed progressive training strategy to gradually aligns these modules stably. Trained on only 72K multimodal instruction pairs, MedSIGHT achieves state-of-the-art performance across diverse imaging modalities on both medical comprehension and segmentation tasks.

---


### 31. [When Better Codebooks Are Not Enough: Predictive Performance and Behavioral Reliability in LLM Political Event Coding](https://arxiv.org/abs/2606.06781)

**<font color=#1a73e8>作者：</font>** Zixian He, Bharath Raahul Murugesan, Patrick Brandt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High accuracy does not necessarily make an LLM a faithful coder. This issue matters because many social-science studies rely on expert-written codebooks to turn text into structured data. We study this problem in political event coding, a challenging source-target relation classification task beyond ordinary sentence-level classification, where models must determine what one actor did to another using detailed coding rules.
We test whether expert codebooks become more effective when operationalized into LLM-friendly forms with clearer definitions, examples, retrieved context, and rules for difficult cases. We then evaluate behavioral reliability under controlled changes to label names, codebook order, and label-definition mappings. Clearer codebooks substantially improve classification performance, especially for fine-grained event classification. However, these predictive gains do not fully translate into behavioral reliability. Models may produce valid labels and recover definitions while still failing behavioral reliability tests under controlled codebook changes.
These findings suggest that codebook-guided LLM systems should be evaluated not only by accuracy, but also by whether they preserve the coding logic that makes coded outputs meaningful for social-science research.

---


### 32. [Federated Foundation Models over Vehicular Networks](https://arxiv.org/abs/2606.06786)

**<font color=#1a73e8>作者：</font>** Kasra Borazjani, Fardis Nadimi, Payam Abdisarabshali 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a forward-looking vision for integrating the emerging multi-modal multi-task federated foundation models (M3T FedFMs) into vehicular networks, with the goal of unifying the expressive power of multi-modal multi-task foundation models (M3T FMs) with the privacy-preserving and distributed learning capabilities of federated learning (FL). Given the largely underexplored nature of this research direction, we first introduce the fundamental training/fine-tuning principles of M3T FedFMs. We then discuss a range of their representative use cases in vehicular networks, illustrating the significant potential of M3T FedFMs to enable next-generation vehicular intelligence. Afterwards, we identify key constraints inherent to vehicular environments that challenge the practical deployment of M3T FedFMs, and articulate a set of forward-looking research directions to address these challenges. Furthermore, through a case study conducted on a real-world vehicular dataset (i.e., Waymo Open Dataset), we demonstrate the promise of M3T FedFMs for vehicular networks and release our implementation to facilitate reproducibility and stimulate research in this emerging area (repository: this https URL)

---


### 33. [Explain Like I'm 5 or Whatever I Choose: Evaluating the Interactive Potential of Language Model Responses](https://arxiv.org/abs/2606.06788)

**<font color=#1a73e8>作者：</font>** Indu Panigrahi, Tal August  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluations of large language models (LLMs) in scientific information seeking tasks have become increasingly use-centric, such as conducting live or multi-turn evaluations with real users. These evaluations still assume a single, static chat interface, but as models are integrated into new interfaces, evaluations must shift to incorporate interface-specific criteria. We propose a new evaluation framework based on a formative study with $16$ participants that tests models' ability to generate multiple responses to one query that differ along an interpretable axis of language (language complexity), inspired by direct manipulation interfaces from human-centered design literature. We evaluate GPT-5.1, GPT-5 mini, Claude Sonnet 4.5 + Thinking, and DeepSeek-V3.1 by generating 5 responses at different levels of language complexity for $98$ scientific queries. While models vary complexity across responses, most changes remain inconsistent, with the best performing model (Claude Sonnet 4.5) only shifting reliable complexity measures in the correct direction $46\%$ of the time. Our findings hold with increased sample size and alternative complexity levels.

---


### 34. [TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication](https://arxiv.org/abs/2606.06794)

**<font color=#1a73e8>作者：</font>** Yong-Bin Kang, Anthony McCosker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) successfully grounds large language model (LLM) outputs in trusted documents, but factual grounding alone is insufficient for sensitive peer-support health communication. In domains such as HIV peer support, responses must also be accessible, stigma-free, empathetic, and tailored to the recipient. This paper presents TA-RAG, a lightweight, prompt-based tone-aware RAG framework that embeds explicit tone control into a RAG pipeline without requiring model fine-tuning. We operationalise tone across four core components: stigma-free rewriting, readability adjustment, recipient adaptation, and empathy rephrasing. We evaluate TA-RAG through component-level tests using questions derived from HIV Online Learning Australia (HOLA), UNAIDS terminology guidance, readability metrics, peer-support standards from National Association of People with HIV Australia (NAPWHA), and a public empathy dataset. Results show that the TA-RAG's components improve their targeted communication quality while preserving key content. These findings emphasise that prompt-based tone control is a potential direction for making RAG outputs suitable for sensitive peer-support health communication.

---


### 35. [Korean Culture into LLM Alignment: Toward Cultural Coherence](https://arxiv.org/abs/2606.06797)

**<font color=#1a73e8>作者：</font>** MinJae Jung, Minwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural-aspect work on large language models is dominated by a negative target: which outputs to suppress. We argue that a constructive counterpart is also needed, a working definition of what a culturally coherent response is rather than only what it must avoid, and instantiate it for Korean. We design an alignment-data pipeline around a prompt-based LLM seed generator that expands a Korean harm taxonomy, with a Korean-culturally-adapted safe-response policy at its centre: a per-category guideline grounded in Korean legal frameworks, social norms, and interpretive conventions, against which three frontier models each produce a candidate response. DPO fine-tuning on the resulting triplets improves the Korean cultural safe rate across six open-weight LLMs while causing no large degradation on Korean general-capability benchmarks, and qualitative outputs show fine-tuned models naming Korean statutes and institutional procedures and, where appropriate, supplying constructive Korean-context information alongside refusal.

---


### 36. [SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling](https://arxiv.org/abs/2606.06820)

**<font color=#1a73e8>作者：</font>** Zhifei Xu, Jierui Lan, Zixuan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic Large Language Model (LLM) systems decompose complex tasks into workflow Directed Acyclic Graphs (DAGs) whose primitives must be scheduled on heterogeneous clusters. Existing deep reinforcement learning (DRL) schedulers are tied to a fixed cluster size and require retraining whenever the number of servers changes. We propose SCALE (Scalable Cross-Attention Learning with Extrapolation), a DRL scheduler that generalizes to unseen cluster scales without fine-tuning. SCALE employs a cross-attention pointer network where task features query against server features, so the architecture accepts any number of servers by construction. We observe, however, that permutation-invariant architecture alone does not guarantee good performance at new scales - the attention feature undergoes distribution shift as the server count grows. To counter this, we introduce Structured Representation Regularization (SRR): a decorrelation loss combined with a KL penalty toward the standard normal, which keeps feature statistics stable regardless of input size. Trained on 16 nodes and tested directly on 32 and 48 nodes, SCALE reduces average response time by 8.9% at N=48 relative to the same architecture without SRR, confirming that explicit regularization is necessary to close the scale-generalization gap.

---


### 37. [PandaAI: A Practical Agent CQ2 for Neuro-symbolic Data Analysis And Integrated Decision-Making in Quantitative Finance](https://arxiv.org/abs/2606.06823)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Siyuan Liu, Bingjun Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep learning has excelled in various domains, its application to sequential decision-making in finance remains challenging due to the low Signal-to-Noise Ratio (SNR) and non-stationarity of financial data. Leveraging the reasoning capabilities of Large Language Models (LLMs), we propose \textbf{PandaAI}, a closed-loop neuro-symbolic LLM agent with market regime modeling and constrained alpha generation, which bridges general LLM reasoning with financial rigor and suppresses the financial toxicity of LLM-generated outputs. To bridge the gap between general linguistic capability and financial rigor, we fine-tune a domain-specific LLM. Furthermore, we integrate this LLM into a modular architecture and form a closed-loop system. Unlike traditional models that optimize isolated prediction metrics, \textbf{PandaAI} is designed as a neuro-symbolic agent that navigates the complex, real-world financial environment with explicit risk awareness. Extensive experiments on CSI 300 stock data show that \textbf{PandaAI} achieves a $18.2\%$ higher Rank IC and $25.7\%$ lower maximum drawdown than state-of-the-art time-series models. Our constrained LLM generation and dual-channel adaptation method provide a general paradigm for LLM deployment in high-stakes sequential decision-making scenarios.

---


### 38. [Progress-SQL: Improving Reinforcement Learning for Text-to-SQL via Progressive Rewards](https://arxiv.org/abs/2606.06825)

**<font color=#1a73e8>作者：</font>** Shihao Zhang, Xiaoman Wang, Yuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has recently shown promise in improving large language models for Text-to-SQL generation, yet existing methods typically optimize one-shot rewards defined over a single SQL state. Such rewards provide limited guidance for iterative SQL correction and are insufficient to capture the improvement of multi-turn SQL refinement. In this paper, we propose Progress-SQL, a multi-turn reinforcement learning framework with progressive rewards for Text-to-SQL. Our approach introduces an Oracle-guided Diagnostic Tree (ODT), which abstracts SQL queries into clause-level structural profiles and produces diagnostic feedback for next-turn refinement. To provide dense and robust reward signals, we combine ODT-based structural alignment with lexical alignment and define a progressive reward that measures the improvement from the initial SQL to the final SQL. We further incorporate a progression latency reward that favors earlier correctness and an execution status reward that encourages recovery from the invalid SQL. Experiments on BIRD, Spider, and Spider robustness variants demonstrate that our method consistently improves Text-to-SQL performance across both primary and robustness evaluations.

---


### 39. [Hearing the Unspoken: Language Model Priors for Acoustic Adversarial Attacks](https://arxiv.org/abs/2606.06833)

**<font color=#1a73e8>作者：</font>** Jiani Xie, Andrew C. Cullen, Paul Montague 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) systems operating in real-time settings must process acoustic input under strict temporal constraints, where transcription decisions are inherently made on incomplete information. This causal constraint serves as an information bottleneck on attackers, significantly limiting attack performance. Our new Semantic Gambit attack breaks this causal limitation by augmenting the adversary with predictive context derived from a Large Language Model in real-time. Our experiments show that this form of augmentation can elevate the corpus-level Word Error Rate to 35.6% -- a three-fold increase over the current state-of-the-art. Ultimately, this work reveals how common, low-latency LLM tooling can be exploited to systematically subvert real-time ASR pipelines.

---


### 40. [The Dark Regulome: Disentangling Predictability from Regulation in Genomic Foundation Models](https://arxiv.org/abs/2606.06834)

**<font color=#1a73e8>作者：</font>** Chahat Baranwal, Aadtya Baranwal, Lakshya Nitin Tandon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-grade gliomas integrate into neural circuits through functional synapses with neurons, raising the question of which noncoding elements shape synaptogenic gene expression in tumor cells. The regulatory program written across the dark genome, what we call the $\textit{dark regulome}$, is the natural substrate to probe, and sequence foundation models offer a zero-shot route through in-silico mutagenesis (ISM); yet likelihood-based scoring is tautologically coupled to local sequence predictability, leaving the regulatory interpretation underdetermined. Across three architecturally distinct foundation models (Caduceus-Ph, HyenaDNA, Enformer) and 30,448 dark genome elements at 92 glioma-relevant loci, we introduce a residualization-and-permutation diagnostic that separates predictability-driven from regulation-driven RIS variance. A sharp 10kb proximal-regulatory horizon survives every control we apply, but the LM-derived element-class hierarchy does not: a six-feature linear baseline matches Caduceus top-decile membership at AUC $= 0.985$. Cross-architecture decomposition cleanly separates a sequence-predictability layer (the two language models co-rank long well-predicted transposable elements) from a regulatory-output layer (Enformer alone retains residual cCRE-discriminative signal), with literally zero overlap between the two top-100 lists. Conservation, brain cis-eQTL, and STRING-PPI cross-checks then anchor what biology survives: top-100 elements across all three models are $3.3\times$ enriched per model for matching brain eQTLs ($p_\mathrm{emp} < 5\times 10^{-3}$), while a tempting transposable-element regulatory layer and a striking NRXN1+NLGN1 protein-pair convergence both fail proper permutation tests once those tests are constructed. We deliver the diagnostic as a general methodological tool for any ISM-based regulatory study.

---


### 41. [Translate-R1: Cost-Aware Translation Tool Use via Reinforcement Learning](https://arxiv.org/abs/2606.06835)

**<font color=#1a73e8>作者：</font>** Pratik Jayarao, Chaitanya Dwivedi, Himanshu Gupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance gap across languages in LLMs is well documented, and closing it natively requires pretraining or fine-tuning on corpora that, for most languages, do not exist. Translation offers an alternative: converting an input into the model's dominant language unlocks its full capabilities at once. Applying translation to every input, however, is wasteful for languages the model already handles, while leaving the choice to the model fails in the opposite way, as LLMs are overconfident and skip the tool even when they cannot understand the input. Prior work resolves this with language-specific rules, domain heuristics, language identifiers, or external routers, each requiring manual engineering. We instead learn a single policy that decides when to translate from reward alone, developing language- and domain-adaptive introspection that assesses its own comprehension and invokes translation only when it cannot solve a task natively.
Using data built by our answer-preserving translation pipeline, we continue RL on the post-trained Qwen3-4B across 22 languages in 3 resource tiers (High, Low, XLow) and 5 domains, and introduce confidence-gated GSPO for cost-sensitive tool use. The gated policy lifts reward over the baseline by +4.6 on High, +23.5 on Low, and +17.5 on XLow. Against an unconstrained policy that almost always translates, it preserves full reward at 63% of the cost and is Pareto-optimal across 87% of the cost-sensitivity range. Additionally, to simulate behavior on a completely unseen language, we create 2 synthetic languages, where our gated policy improves +18.7 over the overconfident baseline that underutilizes the tool even on these incomprehensible inputs. The policy transfers zero-shot to 9 held-out languages, and we analyze how tool use emerges over training, per language and per domain.

---


### 42. [MotionEnhancer: Leveraging Video Diffusion for Motion-Enhanced Vision-Language Models](https://arxiv.org/abs/2606.06853)

**<font color=#1a73e8>作者：</font>** Yifan Xu, Chao Zhang, Ruifei Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The new era has witnessed a remarkable capability to extend Vision-Language Models (VLMs) for tackling tasks of video understanding. While current VLMs excel at event- or story-level understanding, their ability to capture fine-grained motion details remains limited, primarily due to their focus on high-level static semantic structures and macro-event logic. In contrast, Video Diffusion Models (VDMs) are adept at modeling dynamic motion patterns, benefiting from large-scale video data and the intrinsic requirement of temporal generation. In this paper, we introduce MotionEnhancer, a novel approach that leverages motion priors distilled from a powerful video diffusion model as auxiliary supervision to enhance the motion understanding capability of a VLM via attention alignment. MotionEnhancer comprises two simple parameter-free modules, Motion-sensitive Head Selection (MHS) and Motion-salient Text Token Identification (MTTI), to directly extract and optimize motion-related attentions from the VDM in a computation-only manner. MotionEnhancer provides a scalable solution for motion understanding without additional training parameters, modifications to existing architectures, or tool calling. Extensive experiments demonstrate that MotionEnhancer can achieve consistent improvements over state-of-the-art VLMs on two motion-level video understanding benchmarks, especially on motion-related metrics.

---


### 43. [Interpreting Brain Responses to Language with Sparse Features from Language Models](https://arxiv.org/abs/2606.06857)

**<font color=#1a73e8>作者：</font>** Michael A. Lepori, Kendrick Kay, Greta Tuckute  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central goal of cognitive neuroscience is to characterize the features that are represented by human language cortex. Artificial language models (LMs) have emerged as a powerful tool to address this challenge, but studies relating biological and artificial representations are often criticized as relating one black box to another. The present work introduces Augmented Sparse Encoding Models, an encoding framework that replaces dense LM hidden states with hierarchically-organized sparse autoencoder (SAE) features, while explicitly including surprisal as a predictor. Using this approach, we (i) produce interpretations of neural responses and (ii) test whether model-brain alignment reflects primary or idiosyncratic variation in LM representations. Using a high-field 7T fMRI dataset of eight participants listening to 200 linguistically diverse sentences, we first validate our modeling framework by recovering previous interpretations of voxel populations tuned to processing difficulty and meaning abstractness. We then interpret a previously-uncharacterized (but reliable) voxel population and find that it is tuned to people-related content. Next, we show that the fronto-temporal human language network is predicted by a common set of features across its constituent regions, but find that frontal regions are relatively well-explained by surprisal alone, even in the absence of LM-based features. Finally, we show that brain responses during language processing are not merely predictable from an arbitrary set of LM features. Rather, brain responses are best explained by the features that tend to capture the most general information encoded in LM representations, suggesting a nontrivial correspondence between brain and LM language representation.

---


### 44. [Are Large Language Models Suitable for Graph Computation? Progress and Prospects](https://arxiv.org/abs/2606.06865)

**<font color=#1a73e8>作者：</font>** Yuting Zhang, Yi Han, Kai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been increasingly explored for graph computation, where tasks require reasoning over structured relationships and algorithmic operations. Yet, it remains unclear when LLMs can reliably support such computation and how they should be incorporated into graph-solving pipelines. Existing surveys at the intersection of LLMs and graphs primarily focus on graph learning, text-attributed graphs, or graph-language modeling. To bridge this gap, we provide a comprehensive review of LLMs for graph computation through a role-based taxonomy. Specifically, we identify two major paradigms: i) LLMs as executors, where models directly solve graph tasks from graph descriptions and instructions; and ii) LLMs as planners, where models formulate problems, decompose reasoning steps, and invoke external tools or agents for execution. Based on this taxonomy, we analyze the strengths and limitations of current methods. Our review indicates that LLMs are promising for simple, small-scale tasks, but remain unreliable for large-scale and exactness-demanding tasks. Finally, we summarize available datasets and suggest four future directions.

---


### 45. [Multi-FRuGaL: Multimodal Flexible Redundancy-aware Decomposed Gated Learning for Cancer Diagnosis and Prognosis](https://arxiv.org/abs/2606.06867)

**<font color=#1a73e8>作者：</font>** Sanket Kachole, Siddhesh Thakur, Shubham Innani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern medicine relies on heterogeneous data sources spanning radiology, pathology, text reports, and structured clinical information. However, real-world patient data are frequently incomplete, with missing or sparsely acquired modalities, limiting the effectiveness of standard multimodal fusion approaches. To this end, we propose the Multimodal Flexible Redundancy-aware decomposed GAted Learning (Multi-FRuGaL) framework, a decomposition-aware, adaptive gated intermediate-fusion framework that performs modality-level representation learning under missing data. Multi-FRuGaL integrates per-modality encoders with a signal decomposition layer, an input-conditioned gating network, and an information-aware fusion objective to separate redundant from modality-specific complementary signals, selectively upweighting informative modalities and suppressing redundant or noisy inputs, and remaining well-defined even when multiple modalities are absent. We evaluate Multi-FRuGaL on two multimodal head and neck cancer cohorts: the HANCOCK challenge dataset (N = 763) comprising five modalities and two prognostic endpoints (5-year survival and 2-year recurrence), and the HECKTOR challenge dataset (N = 588) comprising three modalities for human papillomavirus (HPV) status classification. Multi-FRuGaL consistently achieves higher mean performance than the evaluated baselines across multiple tasks, improving AUC from 0.601 to 0.8496 for survival, from 0.672 to 0.8102 for recurrence, and achieving 0.975 AUC for HPV prediction on HECKTOR. For survival analysis, it further achieves a concordance index of 0.6814 for overall survival, 0.7421 for recurrence-free survival, and 0.7143 for progression-free survival on HANCOCK, and 0.7203 for recurrence-free survival on HECKTOR. Qualitative analyses further show that Multi-FRuGaL learns discriminative and robust multimodal representations, even under severe missing-modality conditions.

---


### 46. [Evidence-Based Intelligent Diagnostic and Therapeutic Visualization System with Large Language Models: Multi-Turn Interaction and Multimodal Treatment Plan Generation](https://arxiv.org/abs/2606.06869)

**<font color=#1a73e8>作者：</font>** Yunhan Wang, Yuda Wang, Zhiying Tu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aim: Existing AI-assisted traditional Chinese medicine diagnostic tools suffer from opaque reasoning processes, passive interaction, and limited treatment plan presentation. This
study proposes a knowledge-enhanced visual diagnostic system to improve the transparency and interpretability of syndrome differentiation and treatment.
Methods: The system is built upon a Neo4j knowledge graph comprising 241 syndromes, 1,263 symptoms, and 2,485 relations. It incorporates a four-stage symptom matching pipeline
(exact, semantic, fuzzy, and large language model verification), an information gain-driven proactive questioning strategy optimized with genetic algorithms, and a multimodal
treatment presentation integrating artificial intelligence-generated illustrations, three-dimensional meridian-acupoint models, and evidence-based literature.
Results: Knowledge graph constraints reduced non-standard outputs by 32%. Case studies validated the effectiveness of the interactive workflow across patient self-assessment,
clinician-assisted diagnosis, and traditional Chinese medicine education. Automated paired-comparison evaluation across 30 cases further demonstrated significant improvements in
diagnostic trust (Cohen's d = 1.82, p < 0.001), reduced cognitive load (improvements in four of five dimensions), and higher credibility of evidence-based references (4.21 vs.
2.95).
Conclusions: The proposed system enhances the transparency of traditional Chinese medicine diagnostic reasoning and the interpretability of treatment plans through knowledge
graph-driven visualization and multimodal interaction, offering a practical solution for trustworthy artificial intelligence-assisted traditional Chinese medicine applications.

---


### 47. [EgoPressDiff: Multimodal Video Diffusion for Egocentric UV-Domain Hand-Pressure Estimation](https://arxiv.org/abs/2606.06872)

**<font color=#1a73e8>作者：</font>** Yuan Zeng, Zilue Gao, Yujia Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating hand-surface contact pressure from an egocentric view is crucial for AR/VR devices, robotic imitation, and ergonomic analysis. Existing methods often discretize pressure signal and process frames independently, leading to quantization errors and temporal inconsistencies. We present \emph{EgoPressDiff}, a conditional video diffusion framework that generates UV-pressure maps from visual input. The core of our approach is a multi-modal conditioning strategy, introducing a PoseNet and a Vertex Encoder to efficiently extract features from hand pose and 3D mesh vertices. These signals, along with depth information, guide the generative process to ensure the pressure fields are physically grounded. To effectively fuse these heterogeneous features, we further propose a Distribution-Calibrated Spatial Layer, which aligns their statistical properties before combination. Evaluated on the EgoPressure ego-view setting, EgoPressDiff achieves state-of-the-art results, improving Volumetric IoU by over 34\% relative to prior baseline, while reducing MAE and maintaining high temporal accuracy. Our project page is at this https URL.

---


### 48. [Unified Safe In-context Image Generation in Multimodal Diffusion Transformers via Restricting Unsafe Information Flows](https://arxiv.org/abs/2606.06875)

**<font color=#1a73e8>作者：</font>** Xiang Yang, Feifei Li, Mi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) equipped with multimodal attention (MM-Attn) have become a dominant paradigm for image generation. However, preventing the generation of harmful content remains a critical challenge, particularly in image-to-image (I2I) editing tasks. Existing safety mechanisms are primarily designed for text-to-image (T2I) synthesis or U-Net-based architectures, which limits their effectiveness for unified safety mitigation in DiT-based frameworks. To bridge this gap, we propose Unified Visual Safety Regulator (UVR), a training-free safe generation framework that regulates unsafe semantics in generated images. UVR is grounded in an analysis of attention dynamics from the perspective of information flow in MM-Attn. We identify a task-independent start-up stage, during which unsafe semantics in output patches rapidly emerge and can be accurately localized, followed by task-specific semantic amplification and interference stages, where harmful signals are further propagated and entangled with benign content. Based on these observations, UVR mitigates unsafe generation through unified, targeted attention modulation and explicit restriction of harmful information flow over the identified unsafe output patches. Experiments across various concepts show that UVR achieves state-of-the-art safety performance by achieving 91% and 77% erase rate in image synthesis and editing tasks, while preserving visual quality and fidelity with minimal degradation. Code is available at this https URL.

---


### 49. [GlucoFM-Bench: Benchmarking Time-Series Foundation Models for Blood Glucose Forecasting](https://arxiv.org/abs/2606.06881)

**<font color=#1a73e8>作者：</font>** Baiying Lu, Zhaohui Liang, Ryan Pontius 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Blood glucose forecasting models are foundational for modern diabetes management systems, as reliable short-term predictions can enable proactive interventions, support automated insulin delivery, and reduce the risk of hypo- and hyperglycemic events. From a modeling perspective, glucose forecasting poses unique challenges due to heterogeneous physiological dynamics across diabetes populations. Traditional machine learning and deep learning models have been extensively evaluated for glucose prediction, yet recent time-series foundation models (TSFMs) remain much less studied in this setting. To bridge this gap, we present GlucoFM-Bench, a comprehensive benchmark evaluating state-of-the-art TSFMs alongside supervised deep learning models for blood glucose forecasting. We assess eight representative architectures, including pre-trained TSFMs, time-series large language models, and task-specific deep learning models, across 15 publicly available diabetes-relevant datasets comprising 1,117 individuals with type 1 diabetes, type 2 diabetes, prediabetes, and no diabetes. Models are evaluated under zero-shot, few-shot, and full-shot protocols, with systematic variation in context length and prediction horizon. Across datasets, pre-trained TSFMs, especially Chronos-2 and TimesFM, show strong zero-shot and few-shot transfer, with the best zero-shot model performing within 5% of the best full-shot supervised model. Yet, when task-specific data are abundant, a lightweight LSTM remains strongest, outperforming TSFMs by 4--21% under full-shot training. Stratified analyses reveal persistent challenges in T1D cohorts and hypo-/hyperglycemic ranges, highlighting the need for evaluation beyond aggregate error metrics. Together, GlucoFM-Bench provides a standardized and reproducible foundation for evaluating, comparing, and improving foundation models for blood glucose forecasting.

---


### 50. [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](https://arxiv.org/abs/2606.06888)

**<font color=#1a73e8>作者：</font>** Zhiwei Xu, Shihao Wu, Hanseul Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical scaling laws for language model pretraining balance model size against training dataset size under a fixed compute budget, assuming abundant data and a single pass over the corpus. As training compute grows faster than the supply of natural language data, pretraining is likely to enter a data-constrained, compute-rich regime where models train for multiple epochs over a finite dataset. We study data-constrained pretraining along two axes, regularization and scaling. For regularization, we study masked-input regularization (MIR), an auxiliary next-token prediction loss on randomly masked inputs. MIR tests whether the random masking central to diffusion language models can benefit autoregressive pretraining without architectural changes or inference overhead. Across 72M to 1.4B parameter models, we find that MIR added on top of strong weight decay improves validation loss over autoregressive strong-weight-decay-only models, with downstream gains at 1.4B. For scaling, we propose SoftQ, a scaling law that couples model size and data size to capture their interaction under repeated data. Classical alternatives such as the Chinchilla law use an additive form that decouples these terms, making them misspecified in the data-constrained regime. We find that SoftQ fits data-constrained experiments substantially better than these alternatives, and estimates MIR's gains as equivalent to roughly 1.3 times as much unique training data. We release our code at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-114](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
