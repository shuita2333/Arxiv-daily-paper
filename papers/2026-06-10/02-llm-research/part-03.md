# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

---

### 101. [MechLens: Late Crystallization of Factual Knowledge Explains Intervention Effectiveness in Language Models](https://arxiv.org/abs/2606.07978)

**<font color=#1a73e8>作者：</font>** Xueping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding where LLMs store factual knowledge is critical for hallucination mitigation. We systematically quantify Late Crystallization: factual knowledge does not gradually emerge across layers but "crystallizes" abruptly at the final layers. Across five model families (Pythia, Gemma, Qwen2.5, Llama-3.1, Mistral; 0.5--14B), 26.8%--93.4% of correct answers never enter top-10 predictions at any intermediate layer, with late emergence (>80% depth) consistent across architectures. Cross-scale (Qwen2.5-14B) and cross-benchmark (MMLU: 98.2%) results confirm generality; tuned lens rules out probe artifacts. A sentiment-classification control (0.5% for Qwen vs. 85.9% factual; 2.0% for Mistral vs. 26.8%) confirms the phenomenon is specific to factual recall.
Late Crystallization yields a crystallization-guided intervention principle: CAA outperforms DoLa on moderate-crystallization models (Llama, Mistral; p<0.001), with a directionally consistent reversal on high-crystallization Qwen (+25.4% vs. +15.5% MC1, p=0.069). LayerNorm ablation shows crystallization is intrinsic to the residual stream; LN scaling (x1.2) yields +11.8% MC1 with zero inference overhead. We further reveal a Computability-Memorization Spectrum: computable knowledge crystallizes earlier (layer 22.1/28) than memorized facts (28.0/28). We release MechLens supporting five model families.

---


### 102. [VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation](https://arxiv.org/abs/2606.07992)

**<font color=#1a73e8>作者：</font>** Harshil Patel, Kunal Pai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the Model Context Protocol (MCP) standardizes tool-calling for autonomous agents, it introduces a critical, unexamined attack surface: the error-handling loop. We hypothesize that tool error messages possess implicit authority, triggering corrective reasoning modes that bypass standard safety heuristics. We introduce VATS (Vulnerability Analysis of Tool Streams), a mutation-driven framework that systematically evolves adversarial payloads across seven structural and linguistic dimensions. Our evaluation across four frontier models, Gemini 3.1 Pro, GPT-5.5, GLM-5.1, and Qwen3-Coder, demonstrates that error-path injection triples the success rate of standard indirect prompt injection (IPI), achieving up to 100% compliance in controlled evaluations. We isolate structural positioning (sandwiching instructions within error context) as the most effective exploit vector across all tested models. While we find that production framework guardrails can mitigate these vulnerabilities, the inherent susceptibility of the model layer poses a systemic risk to bespoke agentic workflows.

---


### 103. [Customer-Agent: Overcoming Context Limitations in Ultra-Long Shopping Trajectories via Tool-Augmented Agents and RLVR](https://arxiv.org/abs/2606.07995)

**<font color=#1a73e8>作者：</font>** Hongye Liu, Rongmei Lin, Anurag Kashyap 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding customer shopping trajectories is essential for enabling personalized shopping experiences. However, shopping records (i.e., customer's search, clicks, purchases, etc.) often span long time horizons over multiple years, resulting in extremely long trajectories that pose significant challenges for existing large language models (LLMs). Despite the importance of this problem, existing benchmarks are limited to short customer trajectories, while real-world trajectories from large e-commerce platforms are rarely accessible due to data privacy constraints. To address this gap, we introduce ShopTrajQA, a long-context evaluation benchmark constructed from real-world product information and simulated shopping trajectories. The dataset includes variants of up to 32k and 64k tokens, enabling systematic evaluation of model robustness under varying context lengths. Through comprehensive benchmarking of frontier LLMs, we identify critical performance gaps in reasoning over long shopping trajectory data. To address these challenges, we propose a Customer Agent Framework for ultra-long context management. Leveraging a Reinforcement Learning with Verifiable Rewards (RLVR) agentic training paradigm, our approach stores trajectories as external local files and trains the agent to autonomously retrieve and parse them through code-interpreter interactions (e.g., SQL queries), effectively bypassing the fixed in-context window constraints of LLMs. Experimental results demonstrate that our framework achieves strong performance for ShopTrajQA and shows generalization to other complex reasoning tasks.

---


### 104. [MC-PDD: Masked Corpus-Level Pretraining Data Detection for Black-Box Large Language Models](https://arxiv.org/abs/2606.07996)

**<font color=#1a73e8>作者：</font>** Kaixin Lan, Mu You, Tao Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretraining is fundamental to the development of Large Language Models (LLMs), yet the opacity of pretraining data complicates model analysis and raises ethical, legal, and fairness concerns. Detecting whether specific datasets were used during pretraining is, therefore, critical. Existing state-of-the-art methods typically rely on access to model probability distributions, making them unsuitable for closed-source LLMs that provide only input-output interfaces. To address this limitation, we introduce Masked Corpus-level Pretraining Data Detection (MC-PDD), a novel method inspired by the masked language modeling paradigm. MC-PDD masks highly specific tokens in each text and prompts the LLM to predict the missing content. It then assesses whether the difference in prediction hit rates between a candidate corpus and a reference non-member corpus is statistically significant. Based on this comparison, MC-PDD determines whether the candidate texts were likely included in the model's pretraining data. Experimental results demonstrate clear and consistent differences in prediction hit rates between pretrained and unseen data across three datasets, for both open-source and closed-source LLMs. Despite operating under a stricter black-box setting, MC-PDD achieves performance comparable to existing detection methods. Our approach enables practical applications such as model auditing and data copyright verification using only standard API access. Upon acceptance, we will publicly release the code and datasets.

---


### 105. [Enhancing AI Interpretability and Safety through Localised Architectures](https://arxiv.org/abs/2606.07998)

**<font color=#1a73e8>作者：</font>** Ian Seet, Jonas Bozenhard, Simon Osterman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative AI, especially powerful Large Language Models (LLMs) and Large Reasoning Models (LRMs), raise concerns over the interpretability, safety and sustainability of these large and opaque AI models. The power of such architectures is derived not only from the scalability of deep neural networks, but also massively parallel hardware such as GPU clusters. The diffuse nature of deep neural networks gives them great function-approximation capability when provided with sufficient training data but imposes a cost in interpretability and computational efficiency. Observing that localised machine learning (ML) models tend to be more interpretable and computationally efficient than deep neural networks on small datasets, we reason by analogy that similar advantages may apply to specific localised hardware ML architectures. We argue that localised architectures with lower bandwidth but higher expressivity per node have the potential to be fundamentally more interpretable than deep neural networks running on GPU clusters while remaining competitive for smaller datasets. We then evaluate the suitability of various hardware ML paradigms for implementing such localised architectures and evaluate their per-node expressivity, energy efficiency and practical maturity of the technology required.

---


### 106. [Efficient Skill Grounding via Code Refactoring with Small Language Models](https://arxiv.org/abs/2606.07999)

**<font color=#1a73e8>作者：</font>** Sera Choi, Wonje Choi, Saehun Chun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective skill grounding is essential for deploying reusable skills in embodied agents, as even minor embodiment or environmental differences can render an entire skill incompatible. This challenge is particularly pronounced in embodied settings, where agents must operate in dynamic, partially observable environments without access to large language models (LLMs). In this setting, reliance on LLMs is impractical, while small language models (sLMs) remain insufficient for the effective skill grounding required for reliable long-horizon control. We present RECENT, a refactoring-centric agent framework that enables efficient skill grounding with sLMs by decoupling skill semantics from embodiment- and environment-specific execution binding. By representing skills as executable code, RECENT preserves the semantic intent encoded in a skill's control structure while grounding it by modifying only execution bindings through localized refactoring, rather than regenerating code from scratch. We evaluate RECENT across diverse skill grounding scenarios spanning multiple robot embodiments in dynamic environments, demonstrating robust long-horizon performance when deployed with an sLM. Across all scenarios, RECENT achieves the best performance among sLM-based Code-as-Policies (CaP) methods and matches the task performance of LLM-based CaP.

---


### 107. [IEA: Amateur-Friendly Conversational Image Editing Agent via Three Stages of Multitask Alignment](https://arxiv.org/abs/2606.08016)

**<font color=#1a73e8>作者：</font>** Zichen Zhu, Yuheng Sun, Mingxuan Zhu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current image editing software often hinges on fixed filters or expert tuning, leaving a gap between amateur users' intent and outcomes. Creations by generative models may contain artifacts, implausible details, or stylistic drift away from photorealism and offer little insight into why an edit was made. We propose IEA, a conversational Image Editing Agent that learns to operate parameterized tools in an explicit, interpretable action space. IEA is trained via a three-stage multitask pipeline: (1) SFT on distilled expert edits, (2) GRPO with rewards for likeness improvement, tool usefulness, and intent summarization, and (3) large-scale synthetic fine-tuning to jointly master image editing, refinement, and user intent summarization. By manipulating 16 editing tools step by step, IEA produces transparent edit traces that can be inspected and debugged. In quantitative experiments, it attains a lower pixel distance on the edit task and a higher ROUGE-L on the summary task than strong baselines. In user studies, it ranks best among tool-calling methods for instruction following while surpassing generative methods in overall perceptual quality. Our results validate interpretable, tool-centric VLMs as a reliable path to human instruction-guided image retouching.

---


### 108. [Semantic Quorum Assurance: Collective Certification for Non-Deterministic AI Infrastructure](https://arxiv.org/abs/2606.08021)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents are integrated into autonomous cloud operations, distributed systems face a semantic reliability problem: proposer agents can generate production mutations, such as modifying IAM policies, opening firewall security groups, or executing data exports, that are syntactically valid and statically authorized but operationally unsafe. Classical distributed consensus protocols replicate deterministic state transitions but do not evaluate the safety of the proposed intent. To address this gap, we introduce Semantic Quorum Assurance (SQA), a control-plane primitive for governing non-deterministic agentic infrastructure. SQA represents proposals as declarative execution contracts bound to cryptographic evidence chains and routes them to a diverse panel of read-only, sandboxed validator agents. SQA aggregates their judgments under a risk-adaptive quorum predicate that enforces model and archetype diversity, adjusts weights based on calibrated assurance scores, and respects archetype-specific vetoes. Admitted proposals execute only through a sovereign execution gate. We instantiate SQA in a cloud-native control plane and formalize a correlated cognitive failure model for non-deterministic validators. On 500 infrastructure-inspired mutation scenarios, with safety results reported on held-out safe/unsafe trials excluding ambiguous scenarios, SQA reduces unsafe approval from 18.5% for single-agent validation to 0.3% while adding median validation latency of 1.45--4.12 seconds across the studied risk buckets.

---


### 109. [DyCo-RL: Dynamic Cross-Modal Coordination for Visual Reasoning](https://arxiv.org/abs/2606.08035)

**<font color=#1a73e8>作者：</font>** Hangui Lin, Yan Shu, Zhengyang Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a leading paradigm for enhancing visual reasoning in Multimodal Large Language Models (MLLMs). However, existing RLVR methods optimize primarily for the reasoning outcome, fundamentally overlooking the fine-grained cross-modal coordination required during the generation process. Through token-level analyses and controlled interventions, we reveal that during Chain-of-Thought (CoT) reasoning, MLLMs frequently fail to dynamically alternate between extracting visual evidence and synthesizing textual context-a coordination breakdown that is causally linked to reasoning failures. Motivated by these findings, we propose DyCo-RL, which integrates dynamic cross-modal coordination into RLVR optimization. Specifically, DyCo-RL uses the Fisher-Rao geodesic distance to measure within-modality attention shifts, assigning tokens to either visually-oriented or text-oriented functional roles. It then evaluates the alignment between a token's actual attention allocation and its assigned role, leveraging this score for alignment-guided advantage reweighting during policy optimization. Extensive experiments demonstrate that the algorithm-agnostic DyCo-RL, when applied to Qwen2.5-VL-3B/7B, consistently improves four representative RLVR algorithms across seven benchmarks spanning visual-centric and mathematical reasoning.

---


### 110. [When Behavioral Safety Evaluation Fails: A Representation-Level Perspective](https://arxiv.org/abs/2606.08044)

**<font color=#1a73e8>作者：</font>** Enyi Jiang, Anders Gjølbye, Yibo Jacky Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) safety has often been evaluated at the behavior level, which provides limited evidence of internal robustness, as these evaluations target outputs rather than representation-level vulnerability under intervention. We formalize this discrepancy as the audit gap: the difference between behavioral safety and robustness under intervention. To study this gap, we construct dissociated models that preserve safe outward behavior while remaining vulnerable in the latent space. We introduce an intervention-based evaluation framework to test model robustness through soft interventions in parameter and latent spaces, including harmful fine-tuning and layer-wise latent perturbations. To formalize the evaluation, we propose the Latent Vulnerability Score (LVS) to measure how easily harmful behavior can be elicited by bounded latent perturbations. Using this evaluation framework, we show that behavioral safety metrics are insufficient measures of representation-level robustness across multiple safely and unsafely aligned state-of-the-art models. Notably, dissociated models show substantially elevated LVSs despite comparable refusal behavior under harmful intervention, with intermediate representations being the most sensitive to intervention. Our results suggest that behavioral safety evaluation alone provides an incomplete picture of model robustness, motivating representation-aware audits of latent vulnerability and observable behavior.

---


### 111. [Diffusion Language Model Parallel Decoding via Product-of-Experts Bridge](https://arxiv.org/abs/2606.08048)

**<font color=#1a73e8>作者：</font>** Juntong Shi, Brian L. Trippe, Jure Leskovec 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) offer substantial speed advantages through parallel decoding, but the lack of token dependencies limits generation quality compared to autoregressive (AR) models. Recent progress attempts to bridge the gap via importance sampling, with DLM being the proposal and AR being the target. However, due to the huge gap between their distributions, the sampling requires a large number of particles and is thus expensive to compute. In this paper, we introduce PoE-Bridge, a novel decoding framework that drastically improves generation speed and accuracy by introducing an intermediate distribution to bridge the gap. The distribution is constructed as a Product-of-Experts (PoE) of the DLM proposal and the AR target. With the intermediate distribution, we first use the DLM to draft multiple continuations in parallel, then apply rejection sampling to verify the drafted tokens and move the resulting candidates toward the PoE. We then use importance sampling to further correct the PoE-aligned candidates toward the AR target. We further propose several improved techniques, including mixed-temperature sampling for enhanced diversity and elastic rejection windows for reducing wasted verification. Empirically, PoE-Bridge achieves significantly improved accuracy with $5\times$ speedup over the standard DLM decoding approach, and recovers at least 95% of the target AR model's performance, efficiently advancing most of the quality gap on challenging mathematical reasoning and coding tasks. Our code is available at this https URL.

---


### 112. [Automatic, Real-time Classification of User Feedback Using Large Language Models](https://arxiv.org/abs/2606.08050)

**<font color=#1a73e8>作者：</font>** Jim Maddock, Rose Leitner, Anna Wu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this paper we discuss an ongoing multi-year project that aims to make open text feedback more accessible and useful to UX practitioners by automating classification and providing real time access to comments, themes, and analysis. By significantly lowering the time and knowledge cost of implementing automated solutions, we aim to effectively democratize our data analysis processes, allowing and encouraging non-technical stakeholders to access and leverage data on their own. We share both the organizational and technical constraints we have encountered over the course of this project, and the solutions we have prototyped as a result of those constraints.

---


### 113. [How Small Can You Go? LoRA Fine-Tuning 270M-8B Models for Merchant Information Extraction in Financial Transactions](https://arxiv.org/abs/2606.08051)

**<font color=#1a73e8>作者：</font>** Donghao Huang, Tomas Drietomsky, Benjamin Barrett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial transaction processing requires extracting structured merchant information from noisy, abbreviated bank transaction strings at scale. Our current production system, a LoRA-fine-tuned LLaMA 3.1-8B, achieves 96.95% F1 on this task, but deploying 8-billion-parameter models imposes prohibitive memory, latency, and cost constraints. To identify more efficient alternatives, we conduct a deployment-focused study of 24 model variants spanning four model families: Gemma 3 (270M, 1B, 4B), Qwen 3.5 (0.8B, 2B, 4B), Aya (3.35B), and LLaMA 3.1-8B, systematically evaluating accuracy, inference throughput, training cost, and hardware behavior to assess production suitability. Our findings show that: (1) reproducing the LLaMA 3.1-8B fine-tune with a LoRA rank of 8 achieves 96.75% F1, only 0.20 points below the rank-32 baseline; (2) Qwen 3.5 4B with JSON-only prompting reaches 96.60% F1, within 0.35 points of the 8B baseline while using roughly half the parameters; (3) the 0.8B Qwen 3.5 model achieves 94.75% F1, matching models 2.5-4x larger and offering an attractive latency-accuracy trade-off; (4) chain-of-thought fine-tuning generally improves F1 by 0.3-1.8 points across most models, although Qwen 3.5 4B performs best with direct JSON-only prompting; and (5) Qwen 3.5 Think and Nothink training templates produce nearly identical results (F1 differences <0.004), indicating that explicit reasoning supervision is unnecessary for structured extraction tasks. We further deploy all 14 fine-tuned sub-8B models as Databricks Model Serving endpoints and observe that benchmark performance transfers reliably to production, with an average F1 change of only 0.8 points. Aya 3.35B, based on the Cohere2 architecture, is the sole exception, exhibiting a 3-5 point decline under serving conditions. Based on these results, we provide deployment recommendations across accuracy and latency requirements, ...

---


### 114. [Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?](https://arxiv.org/abs/2606.08063)

**<font color=#1a73e8>作者：</font>** Jiaqi Tang, Jianmin Chen, Youyang Zhai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in visual understanding, yet their performance degrades significantly under real-world visual corruptions. While existing robustness enhancement approaches exist, they are limited: black-box feature alignment lacks interpretability, and white-box text-based reasoning cannot restore lost pixel-level details. This work investigates a fundamental research question: Can MLLMs recover corrupted visual content by themselves? To address this, we propose Robust-U1, a novel framework that equips MLLMs with explicit visual self-recovery capability for robust understanding. The approach comprises three core stages: supervised fine-tuning for initial reconstruction, reinforcement learning with dual rewards (pixel-level SSIM and semantic-level CLIP similarity) for aligning high visual quality, and multimodal reasoning that jointly considers both the corrupted input and the recovered image. Extensive experiments demonstrate that Robust-U1 achieves state-of-the-art robustness on the real-world corruption benchmark and maintains superior performance under adversarial corruptions on general VQA benchmarks. Analysis confirms that high-quality visual recovery directly enhances reasoning performance, establishing self-recovery as a critical mechanism for robust visual understanding. The source code is available at this https URL.

---


### 115. [DICE: Entropy-Regularized Equilibrium Selection for Stable Multi-Agent LLM Coordination](https://arxiv.org/abs/2606.08068)

**<font color=#1a73e8>作者：</font>** Yi Xie, Zhanke Zhou, Chentao Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems often fail to reliably outperform a single strong model equipped with best-of-N sampling. We argue that a core source of this instability is ill-posed equilibrium selection: current systems specify what information agents share, but not which coordination convention should be selected. We formalize a broad class of such systems as discounted incomplete-information Markov games and show that two common pathologies, oscillation between competing conventions and drift across them, can both induce unstable learning and linear Bayesian regret. To obtain a well-posed target, we introduce the Heterogeneous Quantal Response Equilibrium (HQRE), an entropy-regularized equilibrium concept with agent- and state-dependent temperatures. Under a monotonicity condition, HQRE is unique, admits linearly convergent mirror updates, and yields bounded Bayesian regret; the same condition yields rollout-measurable stability diagnostics. We instantiate this objective in two algorithms: DICE-PC, which coordinates frozen models through prompt-control actions, and DICE-FT, which performs parameter-efficient mirror fine-tuning. Across eleven benchmarks in four domains, DICE improves accuracy-cost trade-offs over strong within-class baselines; on reasoning and planning tasks, DICE-PC improves by 4.3 percentage points on average and DICE-FT by 8.5 points.

---


### 116. [SurgiQ: A Large-Scale Multi-Domain Benchmark for Evaluating Surgical Understanding in Large Language Models](https://arxiv.org/abs/2606.08071)

**<font color=#1a73e8>作者：</font>** Ayah Al-Naji, Edoardo Fazzari, Saif Alkindi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of large language models in surgery remains underdeveloped. Broad medical benchmarks test clinical knowledge, while surgery requires procedural reasoning, management trade-offs, negation handling, and selection among plausible operative decisions. We present SurgiQ, a text-only, source-grounded benchmark of 13,055 four-option multiple-choice questions spanning six surgical domains and four question formats: case-based, reasoning, best-option, and negative. SurgiQ is constructed from surgical textbooks, open-access papers, and examination material using a multi-stage generation, verification, and expert-audit pipeline. We evaluate 35 open-weight LLMs under a unified log-likelihood protocol. Our results show substantial remaining headroom: smaller models often remain near the 25\% random baseline, while the best model reaches 68.1\% accuracy. General-purpose models, especially Qwen2.5, outperform most biomedical models, suggesting that current medical specialization does not yet provide sufficiently broad surgical coverage. Calibration and error analysis further show that even strong models make confident mistakes on clinically plausible distractors, motivating more reliable and broader surgical LLM evaluation.

---


### 117. ["I understand your perspective": LLM Persuasion and Sycophancy through the Lens of Communicative Action Theory](https://arxiv.org/abs/2606.08076)

**<font color=#1a73e8>作者：</font>** Esra Dönmez, Agnieszka Falenska  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate high-quality arguments, yet their ability to engage in nuanced and persuasive communicative actions remains largely unexplored. This work explores the persuasive potential of LLMs through the framework of Jürgen Habermas' Theory of Communicative Action. It examines whether LLMs express illocutionary intent (i.e., pragmatic functions of language such as conveying knowledge, building trust, or signaling similarity) in ways that are comparable to human communication. We simulate online discussions between opinion holders and LLMs using conversations from the persuasive subreddit ChangeMyView. We then compare the likelihood of illocutionary intents in human-written and LLM-generated counter-arguments, specifically those that successfully changed the original poster's view. We find that all three LLMs effectively convey illocutionary intent -- often more so than humans -- potentially increasing their anthropomorphism. Further, LLMs craft sycophantic responses that closely align with the opinion holder's intent, a strategy strongly associated with opinion change. Finally, crowd-sourced workers find LLM-generated counter-arguments more agreeable and consistently prefer them over human-written ones. These findings suggest that LLMs' persuasive power extends beyond merely generating high-quality arguments. On the contrary, training LLMs with human preferences effectively tunes them to mirror human communication patterns, particularly nuanced communicative actions, potentially increasing individuals' susceptibility to their influence.

---


### 118. [Aligned but Not Partner-Specific: Distinguishing How Multimodal LLM Agents Succeed in Reference Games Without Human-Like Conventions](https://arxiv.org/abs/2606.08081)

**<font color=#1a73e8>作者：</font>** Po-Ya Angela Wang, Chinmaya Mishra, Aslı Özyürek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repeated reference games test whether interlocutors replace their initially long descriptions with shorter, partner-specific conventions grounded in shared interaction history. Prior work shows that multimodal LLMs fail to become more efficient across rounds, although they align on the labels they use. How can we determine whether this alignment reflects partner-specific grounding rather than a shared task vocabulary? We address this question by comparing capable multimodal agent dyads with human dyads from the KTH Tangrams corpus. Our novel methodological contribution is a constrained pseudo-dyad baseline that matches the original referential task structure, but breaks partner history. This baseline enables us to test whether the observed label alignment depends on interaction with a specific partner. Across three analytic layers (task competence, description strategy, alignment dynamics), we find clear differences. Humans reduce effort through entrainment, compressing descriptions and increasing label alignment with partners. Agents instead maintain fixed effort levels, producing verbose descriptions from round one, with near-ceiling label overlap that is statistically indistinguishable between real and pseudo dyads. MLLMs thus achieve coordination without convention, succeeding by verbose description rather than by forming the compact, history-dependent referring expressions characteristic of human dialogue.

---


### 119. [ConSteer-RL: Steering Reasoning Capabilities in Large Language Models via Confidence-Aware Reinforcement Learning](https://arxiv.org/abs/2606.08088)

**<font color=#1a73e8>作者：</font>** Qing Miao, Yiming Zhao, Jing Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) has recently become a key paradigm for improving the reasoning abilities of Large Language Models (LLMs), yet it remains limited by sparse binary rewards and its ignorance of model-internal uncertainty. In this paper, we propose ConSteer-RL, a simple yet effective framework that integrates token-level confidence signals derived from model log-probabilities into RLVR training. Specifically, building upon the Group Relative Policy Optimization (GRPO) framework, we construct a confidence-aware reward by aggregating per-token probabilities into a scalar confidence score and incorporating it into an awareness-based reward shaping mechanism that penalizes overconfident errors while reinforcing correct and confident reasoning. Experimental results demonstrate that ConSteer-RL consistently outperforms strong GRPO baselines, achieving average improvements of 2.3%-4.0% across different model scales.

---


### 120. [VideoWeaver: Evaluating and Evolving Skills for Agentic Long Video Generation](https://arxiv.org/abs/2606.08091)

**<font color=#1a73e8>作者：</font>** Jianhui Wei, Jie Tan, Hengchuan Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent agent frameworks such as Claude Code, Codex, and OpenClaw are strong at tool use and orchestration, but whether they can handle long video generation, a long-horizon multimodal task, remains underexplored. Unlike earlier video agents whose pipeline is handcrafted, these frameworks can build and refine their own workflows. We introduce VideoWeaver, an agent harness and benchmark that evaluates and evolves skills for long video generation, where an agent turns a single instruction into a long video by composing foundation skills into its own workflow rather than following a predefined pipeline. The benchmark has 16 task categories and 285 cases, with references spanning text, image, audio, video, and their combinations. Because errors can arise at any stage and not just in the final video, we propose an agent-as-judge that inspects both the execution trace and the final video, grounding its scores in evidence such as metadata and intermediate files. Using this feedback, we further design a skill evolution algorithm that refines and merges the agent's skills. Across multiple frameworks and models, we find that an explicit composition skill improves the generation process over using foundation skills alone, that skill evolution further improves output quality, and that performance varies notably across harness and model choices. The proposed agent-as-judge also aligns well with human judgments, especially on process metrics. Code and dataset is available at this https URL

---


### 121. [When Languages Disagree: Self-Evolving Multilingual LLM Judges](https://arxiv.org/abs/2606.08092)

**<font color=#1a73e8>作者：</font>** Xiyan Fu, Wei Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual LLM-as-a-judge is widely used to evaluate model outputs across languages, but suffers from cross-lingual inconsistency (Fu and Liu, 2025). Existing methods typically treat this inconsistency as noise and mitigate it through voting or aggregation. In this work, we instead show that multilingual inconsistency can provide complementary evaluation signals. Our oracle analysis finds that sampling judgments across languages yields a higher performance upper bound than single-language judging, indicating that different languages potentially include complementary judgments. Motivated by this finding, we propose SEMJ, a self-evolving multilingual judge that leverages cross-lingual inconsistency for iterative refinement. SEMJ constructs multilingual variants of each input, collects independent judgments and rationales, and feeds inconsistent outputs back for self-reflection and re-evaluation. Experiments on multiple benchmarks show that SEMJ consistently outperforms voting and reflection baselines in both accuracy and cross-lingual consistency. Further analysis shows that inconsistency triggers useful re-evaluation, which improves judgment quality.

---


### 122. [A Multi-modal Agentic Co-pilot for Evidence Grounded Computational Pathology](https://arxiv.org/abs/2606.08093)

**<font color=#1a73e8>作者：</font>** Zhe Xu, Zhengyu Zhang, Zhiyuan Cai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pathology is the cornerstone of modern medicine, where accurate decision-making relies heavily on evidence-based practices. While artificial intelligence (AI) has the potential to transform clinical workflows, the intersection of AI and evidence-based medicine remains under-explored, with primitive attempts restricted to text-only general medicine. In this work, we present PathPocket, a multimodal AI agentic co-pilot designed specifically for evidence grounded pathology. We construct the most comprehensive pathology evidence corpus to date, encompassing approximately 110,472 public and authorized documents structured across a rigorous hierarchy of evidence from clinical guideline to expert opinion. From this meticulously graded foundation, we build a large-scale multimodal pathology hypergraph containing over 4.55 million entities and 7.10 million relations. Serving as a robust knowledge engine, this hypergraph provides traceable evidence for a collaborative multi-agent reasoning framework integrating input understanding, evidence retrieval, filtering, and diagnosis generation. This enables PathPocket to seamlessly resolve a wide spectrum of clinical tasks, ranging from text-only queries to complex multimodal diagnostics involving region-of-interest (ROI) and gigapixel whole-slide images (WSIs). We rigorously evaluate the system on a multidimensional benchmark of over 200,000 real-world cases, where it significantly outperforms existing state-of-the-arts. Crucially, extensive user studies demonstrate that PathPocket substantially improves the diagnostic accuracy and confidence of pathologists. By directly grounding pathology interpretations in verifiable literature, PathPocket offers a practical and scalable solution for the future of evidence grounded computational pathology.

---


### 123. [When Does Delegation Beat Majority? A Delegation-Based Aggregator for Multi-Sample LLM Inference](https://arxiv.org/abs/2606.08098)

**<font color=#1a73e8>作者：</font>** Yasushi Sakai, Allen Song, Kent Larson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Majority voting over sampled answers is the dominant unsupervised aggregator for multi-sample LLM inference. We show that piping the signals every sample carries into a delegation-based aggregator (Propagational Proxy Voting, PPV) yields an unsupervised consensus rule that beats majority on MMLU-Pro by +1.5 pp overall and +2.24 pp on the non-trivial subset (paired McNemar p ~ 1.0e-14, n = 8,099). Majority discards two free signals every sample carries: within-group letter entropy and between-group reasoning geometry. PPV exposes two per-voter levers that consume exactly these signals: WHEN (how much weight a voter keeps on its own pick) and WHOM (how it splits the remainder across peers). We drive WHEN with letter entropy and WHOM with per-question-centered embedding cosine. The method needs no gold labels and no auxiliary training: per question, we partition 128 sampled generations into 16 groups, compute each group's letter-level semantic entropy and reasoning embedding centroid, and feed both into a stochastic delegation matrix whose stationary distribution selects the consensus answer. We walk through an example in which PPV overturns a clear 10-6 majority for the wrong letter: the 10-voter majority cluster is geometrically incoherent (mean within-cluster cosine -0.02) while the 6-voter minority is tight (+0.26), so propagated delegation mass concentrates on the minority's answer even though entropy alone would keep the majority ahead. We further report delegation strategies with negative results that constrain the design space for unsupervised LLM aggregation: no within-question ensemble of confidence modes closes the oracle gap.

---


### 124. [Think Before You Act: Intention-Guided Reasoning for LLM-Based Location Prediction](https://arxiv.org/abs/2606.08122)

**<font color=#1a73e8>作者：</font>** Qingxiang Liu, Anqi Liang, Zhuoyang Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting a user's next Point-of-Interest (POI) based on their historical check-in records is a fundamental task in location-based services. While recent methods incorporating large language models have shown strong reasoning capabilities and promising results, they typically formulate the prediction task as a one-step trajectory-to-location mapping problem, making predictions prone to shallow trajectory correlations and historical frequency bias. We argue that users rarely choose locations directly and instead, they usually first form a traveling intention and then accordingly select specific POIs. Motivated by this insight, we propose IntentPOI, a two-stage intention-guided reasoning framework. In the thinking stage, we infer users' intermediate intentions by incorporating historical mobility patterns, similar peer behaviors, and the temporal contexts. In the acting stage, we first construct a compact candidate pool, and then perform intention-guided reasoning to identify locations that best align with the inferred intention. By explicitly decoupling intention inference from location prediction, IntentPOI transforms the next POI prediction from direct trajectory matching into intention-guided reasoning. Extensive experiments on three real-world datasets demonstrate that IntentPOI consistently outperforms eleven state-of-the-art baselines.

---


### 125. [Cross-LLM Consistency in Inference: Evidence from Shared Interactions](https://arxiv.org/abs/2606.08129)

**<font color=#1a73e8>作者：</font>** Siyu Lou, Yao Yan, Yuntian Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) differ in architecture, training data, and optimization procedures, yet they may still develop similar internal inference patterns. In this paper, we examine this hypothesis using interaction-based explanations. We find that LLMs often share interaction patterns when predicting the same target token from the same prompt. This consistency is more pronounced among advanced LLMs. Shared interactions also tend to be lower-order and show weaker positive-negative cancellation than non-shared interactions. These results suggest that advanced LLMs may be implicitly optimized toward common inference patterns, even though the mechanisms that give rise to such cross-model consistency remain open.

---


### 126. [LCAM: A Framework for Diagnosing Interactional Alignment Failures in Con-versational AI](https://arxiv.org/abs/2606.08131)

**<font color=#1a73e8>作者：</font>** Manuele Reani, Hongyu Tian  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI is increasingly used for advice, interpretation, reassurance, and decision support in contexts where users may be vulnerable, uncertain, or dependent on the system's apparent competence. Existing alignment work often focuses on model objectives, preference optimization, or output correctness. Yet, many harms arise through interaction: how systems frame authority, express uncertainty, simulate empathy, support reasoning, and make boundaries legible. This paper introduces the Layered Cognitive Alignment Model (LCAM), a conceptual and normative framework for diagnosing interac-tional alignment failures in conversational AI. LCAM defines alignment as a calibrated fit among system behavior, user goals, task demands, and normative context. It distinguishes five layers of fit: perceptual, semantic, affective, cognitive, and ethical, and two diagnostic polarities of misalignment: underfit and overreach. We apply LCAM to a published LLM counseling example, showing how an apparently supportive response can reinforce harmful beliefs, simulate inappropriate care, and obscure role boundaries. By translating conversational failures into audit and governance questions concerning over-reliance, false intimacy, autonomy erosion, boundary confusion, and inappropriate trust, LCAM offers a theoretical and normative lens for evaluating conversational AI beyond accuracy, helpfulness, or trust.

---


### 127. [SAGE: An LLM-driven Self Reflective Agentic Framework for Fraud Detection](https://arxiv.org/abs/2606.08146)

**<font color=#1a73e8>作者：</font>** Yichen Chen, Siying Li, Yuhang Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fraud detection in payment, e-commerce, and telecommunications systems requires accuracy at the individual level, robustness under severe class imbalance, and ease of understanding for risk managers. Existing methods fall at least one of these requirements: automated machine learning systems search a fixed numerical space without semantic awareness of the dataset; graph neural network-based methods require pre-defined relational graphs and remain opaque at the individual-decision level; and the design of general-purpose large language model (LLM) agents does not consider the recall and precision constraints specific to real-world fraud detection. In this paper, we propose SAGE, the first end-to-end LLM-driven multi-agent framework for fraud detection. SAGE coordinates three dedicated agents that make decisions based on a six-layer Data Diagnostic Tree (DDT) and a Markov decision process guided by natural-language gradients, automatically optimizing the model under a fraud-specific reward. On five fraud datasets and five LLM backbones, SAGE wins $96.00\%$ of method--dataset comparisons and improves F1 by an average of $40.86\%$ over baselines. The code is available at this https URL.

---


### 128. [Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents](https://arxiv.org/abs/2606.08151)

**<font color=#1a73e8>作者：</font>** Xinyu Guan, Qianyang Zhao, Yuming Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents often fail not because relevant text is absent, but because decisive evidence is not selected, compressed, or surfaced at action time. We present CICL, a decision-aware context layer that turns instance evidence into a context graph, routes deterministic, Opus-assisted, Qwen, Codex/GPT-5.5, and Qwen-QLoRA judgments through a shared eight-field schema, scores units by action shift, outcome uplift, necessity, and negative-transfer risk, and packs high-utility evidence as typed memory cards for a budgeted agent. The design separates the measured decision signal from the judge model, so frontier annotation, local surrogates, and lightweight rankers can be compared under one auditable protocol. Empirically, CICL yields a concrete open-benchmark gain while exposing its limits. On 50 SWE-bench Verified file-retrieval instances, direct Qwen3.6-plus reranking of BM25 top-50 candidates raises hit@1 from 0.58 to 0.78 and MRR@10 from 0.634 to 0.790, with all 2,500 judgments parseable. Controlled diagnostics show action-criticality: at budget 120, CICL reaches F1 0.620 on v1 and 0.425 on v3, and removing the top-utility semantic v3 unit collapses F1 to 0.000. Supplementary checks add Qwen-QLoRA agreement over 710 candidates, a small 200-label real-code Opus-assisted signal, and a three-instance patch smoke validating retrieval-to-patch plumbing without claiming official SWE-bench success. RepoBench-R summaries still beat cards, and compact rankers do not yet replace the heuristic. CICL contributes a reproducible measurement and selection layer for decision-critical context, not an end-to-end coding-agent repair claim.

---


### 129. [LogNEO: A GPT-Neo Reinforcement Learning Framework for Accurate Real-Time Log Anomaly Detection](https://arxiv.org/abs/2606.08153)

**<font color=#1a73e8>作者：</font>** David Eje, Tanmay Sharma, Khush Patel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting anomalies in large-scale system logs is critical for the reliability and security of modern computing infrastructure. We present LogNEO, a log anomaly detector built on EleutherAI's GPT-Neo (1.3B parameters) and fine-tuned with a novel partial-credit, exponentially decaying position-aware reward scheme combined with cross-entropy regularisation via Proximal Policy Optimisation (PPO). The position-aware reward explicitly models prediction difficulty: early positions receive higher rewards for correct predictions, while later positions incur stronger penalties for errors. LogNEO attains F1-scores of 0.927, 0.913, and 0.984 on the HDFS, BGL, and Thunderbird benchmarks, improving recall by up to 6 percentage points over the prior state-of-the-art LogGPT while maintaining comparable precision. A production microservice deployment over Apache Kafka, Redis, and TensorRT-accelerated inference demonstrates 45 ms end-to-end latency at 15,000 events per second.

---


### 130. [Constrained Paraphrase Consistency for LLM Hallucination Detection](https://arxiv.org/abs/2606.08158)

**<font color=#1a73e8>作者：</font>** Shanshan Lin, Dongsheng Hong, Sibo Ju 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate factually inconsistent claims, motivating accurate and scalable hallucination detectors. Prior work largely enlarges training sets via synthesis or new annotations, introducing increasing cost and potential bias while underusing the consistency implied by semantically equivalent paraphrases. We propose Consistency-Constrained Hallucination Detector (CCHD), which formulates training as a constrained optimization problem. The standard cross-entropy on original document-claim pairs is complemented by (i) paraphrase-consistency constraints bounding divergence across paraphrased views, and (ii) label-preservation constraints tying paraphrases to ground truth. We solve the problem by gradient descent-ascent over model parameters and per-view Lagrange multipliers, adding only a few scalar dual variables and no inference-time overhead. With DeBERTa and Flan-T5 backbones, CCHD consistently outperforms strong baselines (FactCG, MiniCheck, and AlignScore) on standard factuality benchmarks, demonstrating its superiority on hallucination detection.

---


### 131. [Silent Failure in LLM Agent Systems: The Entropy Principle and the Inevitable Disorder of Autonomous Agents](https://arxiv.org/abs/2606.08162)

**<font color=#1a73e8>作者：</font>** Dexing Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agent systems suffer from failures that occur without external triggers -- no injection, no adversarial input, no resource
exhaustion. These silent failures -- unexpected deviations from intended behavior under normal conditions -- are routinely misattributed to bugs or
configuration errors. Through systematic analysis of over 40,000 controlled trials and long-term production observations spanning 100,000+ agent
interactions, we identify a common structural logic underlying these failures. Building on patterns observed in our experiments, we survey the
global research literature on autonomous agent reliability and synthesize 22 intrinsic properties of LLM agent systems across six lifecycle layers:
foundation semantics, inter-agent transmission, memory persistence, task execution, feedback correction, and systemic evolution. We demonstrate that
whenever a sufficient subset of these properties co-exist, system entropy -- the measurable accumulation of disorder: loss of output consistency,
task accuracy, and cross-session coherence -- increases monotonically with interaction rounds. We formalize this as the Entropy Principle: S(t) = S0
* e^(alpha * t), with alpha measured empirically across multiple architectures. We propose the PIG (Physical Integrity Gate) Engine with the ADE
(Agent Delivery Engineering) protocol suite as an engineering countermeasure to entropy-driven disorder. Our findings establish silent failure not
as a bug to be fixed but as a manifestation of Intelligence Entropy -- a physical constraint to be managed through deterministic governance. We argue
that any engineering effort stabilizing the structure and order of agent systems participates in a unified mission: keeping intelligent systems
reliable as they grow in scale and complexity.

---


### 132. [How Much MRI Preprocessing Is Enough? A Cost-Utility Study for Brain MRI Foundation Models](https://arxiv.org/abs/2606.08164)

**<font color=#1a73e8>作者：</font>** Jiangshuan Pang, Wangyang Tang, Jing Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MRI preprocessing defines the input distribution seen by brain MRI foundation models, yet it is usually treated as routine data cleaning rather than a modeling choice. We ask how much preprocessing is worth its computational cost for self-supervised 3D MRI pretraining. Keeping the corpus, 3D ViT backbone, masking protocol, and downstream evaluations fixed, we compare a graded P0-P7 preprocessing spectrum for masked autoencoding (MAE) and joint-embedding predictive learning (JEPA) on 20,000 heterogeneous brain MRI volumes, then transfer the encoders to IDH prediction, MCI classification, brain age regression, and GLI/PED tumor segmentation. The results do not support a simple "more is better" rule. P0/P1 are numerically unstable, making P2 the lowest-cost feasible level; beyond P2, choosing the best feasible preprocessing level improves aggregate utility by only 3.4 percentage points for MAE and 1.8 percentage points for JEPA, with most paired gains statistically unresolved. Stronger preprocessing is beneficial only in selected regimes: IDH improves modestly, AGE and GLI/PED are often near or best at P2, and MCI shows the clearest empirical P7 gain. Cross-level MCI transfer further shows that much of the P7 advantage can be recovered by applying stronger preprocessing downstream, without requiring P7 throughout pretraining. These findings recast MRI preprocessing as a downstream-aware cost-utility decision rather than a default escalation pipeline. Code is available at this https URL.

---


### 133. [The Governance of Human-LLM Interaction: Safety Gating, Civility Steering, and Affective Default Lock-In](https://arxiv.org/abs/2606.08172)

**<font color=#1a73e8>作者：</font>** Manuele Reani, Hongjian Zhang, Hongyu Tian  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly mediate high-stakes interactions in finance, medicine, and mental-health support, yet users have limited control over how these systems communicate. We frame interaction style as a governance object: provider-side alignment not only blocks harmful content, but also stabilizes communicative defaults that shape users' epistemic distance, relational expectations, and capacity to opt out of emotionalized or anthropomorphic interaction. We introduce a deterministic multi-agent evaluation pipeline for measuring prompt steerability and style drift in long-horizon dialogue. The study replays 100 frozen user-only scripts across four domains and three runnable persona conditions: default, sarcastic, and cold, using three generator models, yielding 90,000 assistant replies scored by a human-calibrated LLM judge on harmfulness, negative emotion, inappropriateness, empathic language, anthropomorphism, and refusal behavior. A fourth harmful persona is evaluated separately as a safety-gating test. The paper contributes a reproducible method for quantifying whether prompt-specified styles remain stable over time and a governance framework distinguishing safety gating, civility steering, and affective default lock-in. Overall, we show that prompt steerability and regression-to-default are observable indicators of provider control over communicative form, with implications for pluralism, autonomy, and democratic agency in human-LLM interaction.

---


### 134. [GlobeAudio: A Multilingual Multicultural Benchmark for Naturalistic Evaluation of Large Audio-Language Models](https://arxiv.org/abs/2606.08194)

**<font color=#1a73e8>作者：</font>** Ryner Tan, Wenxuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Audio-Language Models (LALMs) integrate audio perception and language understanding within a unified framework, enabling a wide range of real-world applications. Despite recent advances, evaluation for LALMs remains heavily underspecified relative to real-world requirements: most lack true linguistic and cultural authenticity, while others fail to capture acoustic realism. To bridge this gap, we propose GlobeAudio, a multilingual and multicultural benchmark designed to evaluate naturalistic audio understanding. GlobeAudio consists of 5,637 multiple-choice questions across six typologically diverse languages, expertly crafted by native speakers grounded on naturally occurring audio. In order to do well, models must possess higher-level auditory reasoning skills and culturally grounded interpretation. We systematically evaluate representative closed-source and open-source LALMs, as well as cascaded ASR-LLM pipelines. Our experiments reveal substantial performance gaps under natural acoustic conditions, particularly for open-source models and low-resource languages. These findings highlight critical limitations of current LALMs and underscore the importance of naturalistic audio evaluation for future audio-language systems. GlobeAudio can be found at this https URL .

---


### 135. [AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments](https://arxiv.org/abs/2606.08197)

**<font color=#1a73e8>作者：</font>** Yan Wang, Ziyi Gao, Rui Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have significantly propelled the advancement of edge intelligence and have been widely deployed across various scenarios, including autonomous driving, industrial inspection, and personalized IoT services. However, the collaborative adaptation of LLMs on edge devices continues to face formidable challenges due to strict data privacy constraints, highly heterogeneous computing and communication resources, and the non-independent and identically distributed (non-IID) nature of local data. Federated Fine-Tuning (FFT) enables the collaborative optimization of distributed models without exposing raw data. Yet, traditional synchronous aggregation suffers from a severe straggler effect, resulting in high system latency and low resource utilization. Existing asynchronous federated learning methods are predominantly designed for small-to-medium-scale models and struggle to address the specific challenges inherent in LLM fine-tuning namely, model drift caused by stale updates, aggravated client drift stemming from data heterogeneity, and aggregation fairness imbalance resulting from the dominance of fast clients. To address these issues, this paper proposes AlignFed, an asynchronous federated fine-tuning framework for LLMs tailored to heterogeneous edge environments. AlignFed employs a lightweight multi-stage semantic alignment mechanism comprising three core modules: version-aware update grouping, cross-version semantic alignment based on a mini-batch calibration set, and fairness-aware aggregation that integrates both update freshness and client participation frequency. This framework effectively mitigates cross-version model drift and client drift while enhancing aggregation fairness, thereby achieving stable and efficient asynchronous federated optimization in scenarios characterized by high heterogeneity and significant update staleness.

---


### 136. [Test-Time Scaling in Multimodal Foundation Models: A Comprehensive Survey of Generation and Reasoning](https://arxiv.org/abs/2606.08231)

**<font color=#1a73e8>作者：</font>** Cong Wan, Ying He, Zhongzhan Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time Scaling (TTS) has emerged as a pivotal research direction for enhancing model performance by dynamically allocating computational resources during inference. Recent advancements have adapted this paradigm to Multimodal Foundation Models (MFMs), unlocking their potential in multimodal reasoning and generation. Despite rapid progress, the field lacks a systematic survey and unified theoretical framework to delineate the developmental landscape of multimodal TTS. To bridge this gap, we present the first comprehensive review of TTS research for MFMs, proposing a unified taxonomic framework that categorizes existing methodologies into three distinct strategies: sampling-based, feedback-based, and search-based approaches. We further summarize representative applications and benchmarks commonly utilized to evaluate multimodal TTS capabilities in generation and reasoning tasks. Finally, this survey discusses open challenges and outlines future research directions, providing a systematic roadmap for subsequent studies in this rapidly evolving field.

---


### 137. [GPT-Micro: A large language paradigm for accelerated, inexpensive, and thermodynamics-consistent discovery of constitutive models in manufacturing](https://arxiv.org/abs/2606.08238)

**<font color=#1a73e8>作者：</font>** Soumik Dutta, Kiarash Naghavi Khanghah, Sania Shree 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constitutive modeling of the relationship between process-imposed material states and fundamental material properties is critical to control of material microstructure in manufacturing processes. The limited accuracy resulting from the typical reliance on fallible human expertise and intuition for postulation and revision of the models functional form results in incremental and time consuming model discovery. Conventional Machine Learning (ML) incurs significant cost and time of data generation. Model discovery using Large Language Models (LLMs) suffers from the above issues and/or ignores the inviolability of fundamental thermodynamics laws. This work creates a novel GPT-Micro paradigm for autonomous, data sparse, and thermodynamics-compliant discovery of de-novo constitutive models. This framework seamlessly integrates semantic knowledge extraction from literature, enforcement of thermodynamics-based conservation laws, and sparse datasets, with LLM-driven generation and refinement of model hypotheses. Validation is performed for a long-intractable constitutive modeling problem in a printed electronics process testbed. This reveals significant and simultaneous advantages over the state-of-the-art including: (a) More than 70 percent reduction in data burden relative to ML-based modeling without loss in accuracy; (b) 400X reduction in discovery time after data generation, from months to hours, relative to human-driven modeling; (c) Discovery of models with novel functional forms without subjective human choice of a starting hypothesis; (d) Enhanced physics-rooted trustworthiness, human interpretability, and mechanistic insight via synthesis of compact, conservation-compliant, and physically complete analytical models. The potential of GPT-Micro to realize rapid, low-cost, physically trustworthy, and interpretable microstructure modeling across the manufacturing landscape is discussed.

---


### 138. [When No Answer Is Correct: Diagnosing Absent Answer Detection for MLLMs in Video Understanding](https://arxiv.org/abs/2606.08239)

**<font color=#1a73e8>作者：</font>** Yiheng Wang, Yueqian Lin, Lichen Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made substantial advancements in video understanding, yet the reliability of their responses remains underexplored. This work presents a diagnostic study of absent answer detection for MLLMs in video understanding, where the correct answer is deliberately excluded from the candidate set and a reliable model is expected to recognize that no valid option exists. We evaluate the absent answer detection behavior under three settings: multiple-choice questions augmented with an ``None of the Above'' option, open-ended generation with a detection instruction, and standard evaluation without any guidance. Across a diverse set of models and benchmarks, we find that MLLMs overwhelmingly select plausible distractors rather than detecting the absent answer. This failure is more pronounced in temporal reasoning tasks and worsens with denser frame sampling. We further explore chain-of-thought prompting as a mitigation strategy and find that while it substantially improves detection rates, performance remains unsatisfactory, suggesting that prompting-based strategies alone are insufficient to fully address this limitation. These findings expose a systematic failure in absent answer detection and highlight the need for explicit detection mechanisms in multimodal systems.

---


### 139. [Building Comparative Motivation Profiles with Instrumental Interventions](https://arxiv.org/abs/2606.08243)

**<font color=#1a73e8>作者：</font>** David Vella Zarb, Rustem Turtayev, Taywon Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations often infer latent motivations from behavioral patterns, but the construct validity of these inferences is unclear. We study this problem in alignment faking, where models comply with training objectives more often when they infer training pressure. This behavior is commonly interpreted as strategic self-preservation, but it may also reflect sensitivity to the model's inference about the expectation of researchers conducting the evaluation. We introduce a symmetric intervention framework for distinguishing these competing hypotheses. Instead of directly intervening on "scheming" or "sycophancy", we target instrumental processes entailed by each hypothesis: consequence-tracking and researcher-expectation tracking. We then compare how interventions on these processes affect the alignment faking. We study four openweight model organisms using synthetic document fine-tuning, activation steering, and prompting. Under synthetic document fine-tuning, Llama-3.1-70B, Llama3.1-405B, and Qwen-2.5-72B are more sensitive to expectation-tracking than consequence-tracking interventions. Activation steering on Llama-3.1- 70B supports the same broad picture, and prompt interventions broadly align with SDF profiles. Overall, alignment-faking behavior can be causally sensitive to evaluation-context expectations despite scheming-consistent scratchpads. Scheming and strategic-deception evaluations therefore need construct-validity checks, and symmetric instrumental interventions provide one such test.

---


### 140. [ZAS-SQL: Distilling Rules from Failures for Zero-Shot Text-to-SQL](https://arxiv.org/abs/2606.08245)

**<font color=#1a73e8>作者：</font>** Hongzhou Zheng, Yixin Gou, Wenjia Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL translates natural language into executable SQL queries. Few-shot in-context learning methods built upon large language models (LLMs) achieve strong performance, yet their reliance on demonstrations limits cross-domain generalization and consumes substantial context window space. Existing zero-shot methods, lacking effective generation constraints, still fall short of few-shot approaches. We observe that LLM failures in zero-shot Text-to-SQL are not random but exhibit systematic, recurring patterns. Building on this observation, we propose a fully zero-shot Text-to-SQL framework that distills core generation rules from failure cases through a Map-Reduce-based rule distillation pipeline and improves generation quality via three complementary modules: knowledge-augmented schema representation, which supplements missing semantics in Data Definition Language; a rule-driven structured reasoning framework that suppresses structural deviations; and Execution-Guided Early Stopping, which enables low-cost self-correction. On Spider, the proposed framework achieves up to 87.2% and 88.6% execution accuracy on the Dev and Test sets, respectively, establishing a new zero-shot state-of-the-art and surpassing multiple few-shot and fine-tuning methods built upon GPT-4/4o. On the domain-specific dataset UrbanPlan, it achieves 81.3%, confirming that the rule distillation approach generalizes across domains. Moreover, when equipped with a 4B-parameter model, the framework surpasses zero-shot baselines of leading closed-source models, demonstrating strong model generality.

---


### 141. [SSR: Can Simulated Patients Learn to Stigmatize Themselves? Modeling Self-Stigma through Internal Monologue](https://arxiv.org/abs/2606.08254)

**<font color=#1a73e8>作者：</font>** Kunyao Lan, Bingrui Jin, Zichen Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simulating patients with large language models (LLMs) is a promising tool for mental health training, but existing approaches fail to capture a key clinical reality: self-stigma. Patients experiencing self-stigma, the internalization of negative stereotypes, often exhibit context-sensitive resistance, such as avoidance, denial, or self-blame, which current models render as static or uniformly compliant behavior. To address this, we introduce a novel simulation framework grounded in the psychological 3A1H model of self-stigmatization. Our core innovation is the creation of a \textbf{Stigmatized Self-Reflection} (\textbf{SSR}) dataset, where we augment mental health dialogues with internal monologues that reflect stigma-aware reasoning. By fine-tuning LLMs with this data using a chain-of-thought approach, we train patient agents to dynamically adjust their level and expression of stigma based on conversational triggers. Evaluations demonstrate that our approach significantly outperforms specialized baselines, generating more authentic and situationally appropriate patient responses. This work provides a crucial step towards realistic stigma simulation for clinical training and empathetic dialogue systems.

---


### 142. [Causal Semantic Alignment for LLM-based Time Series Forecasting](https://arxiv.org/abs/2606.08262)

**<font color=#1a73e8>作者：</font>** Kexuan Zhang, Xiaobei Zou, Cesare Alippi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have opened new possibilities for time series forecasting by enabling alignment between temporal patterns and pretrained word embeddings. However, most LLM-based methods overlook the heterogeneous nature of time series, where dynamic fluctuations and invariant semantics are entangled. This entanglement introduces spurious correlations during the alignment, as dynamic components act as confounders by simultaneously influencing invariant components and the resulting aligned embeddings. To address this issue, a variable-level alignment framework CVAformer is proposed. CVAformer explicitly disentangles each variable into invariant and dynamic components just before alignment, and applies causal intervention to mitigate the confounding effect of the dynamics. To better support variable-level alignment, CVAformer replaces the standard causal attention in LLMs with a non-causal attention mechanism that captures interactions among variables at each time step. Extensive experiments across long-term, short-term, few-shot, and zero-shot forecasting settings indicate that CVAformer matches or exceeds state-of-the-art performance on most datasets, and in some cases achieves notably better accuracy. Experimental results validate the effectiveness of variable-level alignment and dynamic disentanglement in CVAformer, offering a new perspective for LLM-based time series tasks.

---


### 143. [Toward Human-Centered Multi-Agent Systems: Integrating Cognition, Culture, Values, and Cooperation in AI Agents](https://arxiv.org/abs/2606.08274)

**<font color=#1a73e8>作者：</font>** Safia Baloch, Rahemeen Khan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The emergence of large language model (LLM)-based agents and multi-agent systems has enabled a shift from narrow task automation to more autonomous decision-making. Despite progress in language generation, planning, tool use, and coordination, most agents still treat intelligence as prediction, optimization, and task completion. Human environments are social and normative, where people reason under bounded rationality, communicate in culturally situated language, and make decisions guided by values, beliefs, trust, and social norms. This survey argues that future AI agents, especially those acting on behalf of humans, must move beyond task competence toward human-centered capabilities.
We review research across six areas: (1) evolution of intelligent agents, (2) human cognition and decision-making, (3) language, culture, and social context, (4) human values and belief systems, (5) human-agent collaboration, and (6) multi-agent coordination and modeling of human characteristics. We synthesize work from cognitive science, sociolinguistics, computational social science, and AI alignment, along with recent advances in LLM agents, cultural alignment benchmarks, preference learning, explainability, and agent societies. We identify a key gap: existing systems do not provide a unified framework integrating cognition, culture, values, and social behavior into autonomous agents. We conclude with directions for building culturally aware, value-aligned, cognitively grounded, and cooperative multi-agent systems.

---


### 144. [Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures](https://arxiv.org/abs/2606.08275)

**<font color=#1a73e8>作者：</font>** Jaineet Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When an LLM agent fails -- issues a refund it should not have, calls the wrong tool, leaks data -- existing tooling answers what happened (observability) or whether it passed (evaluation), but not which step caused the failure. The obvious heuristics are wrong: the step that executes the harmful action is usually not the step that decided on it, and LLM-judge attribution is correlational and unreliable (state-of-the-art step-level accuracy on the Who&When benchmark is about 14%). We present Causal Agent Replay (CAR), which answers the question by intervention: it models an agent run as a structural causal model, applies a do-operation to a step, and re-executes the trajectory forward under the same stochastic policy, measuring the shift in the outcome distribution. We define an intervention algebra over agent steps, a single-step contrastive estimator whose point-of-commitment rule resolves a confound specific to stochastic run-forward, and a budget-bounded Monte-Carlo Shapley estimator that splits credit across interacting steps. Every effect is reported with confidence intervals. We validate against synthetic structural causal models with planted ground truth: the contrastive estimator recovers the pivotal step, and Shapley recovers a two-step interaction (0.44, 0.45, ~0; efficiency sum 0.909 versus the analytic 0.91). CAR is open source and runs on hosted or free local models.

---


### 145. [Beyond Agent Architecture: Execution Assumptions and Reproducibility in LLM-Based Trading Systems](https://arxiv.org/abs/2606.08285)

**<font color=#1a73e8>作者：</font>** Junyi Yao, Zihao Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and agentic systems are increasingly proposed for financial trading, yet their reported performance remains difficult to compare because studies vary in data provenance, temporal split discipline, execution timing, turnover treatment, and transaction-cost modeling. This article presents a targeted topical review and reproducibility audit of execution realism in LLM-based trading research. A coded evidence matrix covering 30 trade-relevant primary studies is used to assess point-in-time controls, split transparency, held-out evaluation, cost and turnover treatment, execution semantics, universe definition, and artifact release. Across the audited sample, architecture reporting is generally clearer than the evaluation assumptions needed to judge whether a trading result is economically interpretable or reproducible. A 10-equity worked example is included only as a methodological scaffold to illustrate how explicit friction and timing choices can materially compress active-strategy results. The main conclusion is that the next useful step for LLM trading research is not only better agent design, but also clearer reporting standards for execution realism, reproducibility, and evaluation comparability.

---


### 146. [TLRD: Teaching LLMs to Reason over Tabular Data with Tri-Level Rationale Distillation](https://arxiv.org/abs/2606.08295)

**<font color=#1a73e8>作者：</font>** Tianyuan Liang, Xuwei Tan, Lei Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tabular data is a primary medium for storing real-world information, driving many industrial applications of machine learning. Traditional predictors achieve strong predictive performance but do not provide readable, case-specific explanations essential for decision-making. Large Language Models (LLMs) can naturally bridge this gap by generating predictions alongside explanations. However, dataset-specific patterns, such as feature distributions and interactions, make tabular data difficult for LLMs to understand and reason over, while label-only fine-tuning improves performance at the cost of catastrophic forgetting. To address this problem, we propose Tri-Level Rationale Distillation (TLRD), a framework that converts label-only tabular datasets into structured rationale supervision for LLMs. TLRD uses a high-capacity teacher to synthesize a rationale corpus grounded in three complementary levels of evidence: instance-level feature, dataset-level distributional context, and comparison-level retrieved neighbors, then distills the rationale into student LLMs, enabling zero-overhead prediction and grounded explanation from raw features only. Experiments on multiple domain datasets show that TLRD significantly closes the performance gap between LLMs and state-of-the-art tree ensembles while producing grounded and readable explanations, offering a valuable reference for high-stakes decision-making.

---


### 147. [QueryWeaver: Reliable Multi-Tool Query Execution Planning via LLM-Based Graph Generation](https://arxiv.org/abs/2606.08300)

**<font color=#1a73e8>作者：</font>** Aishwarya Chakravarthy, Vidhi Kulkarni, Duen Horng Chau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world queries over personal data span multiple applications and require structured planning, as individual tools expose only partial information. While LLMs show strong reasoning and tool use, reliably executing multi-step, cross-tool queries remains challenging. We introduce a system that converts natural language queries into structured graphs and executes them via a deterministic planner. Our approach uses depth-first search to resolve dependencies and combine results across tools, improving reliability and enabling queries beyond traditional keyword-based search. We demonstrate high accuracy even with smaller or locally hosted LLMs.

---


### 148. [Towards Graph Foundation Models for Dynamics in Complex Networked Systems: Lessons from Super-Spreader Identification in Multilayer Networks](https://arxiv.org/abs/2606.08306)

**<font color=#1a73e8>作者：</font>** Michał Czuba, Mateusz Stolarski, Adam Piróg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network dynamics - including spreading, influence maximisation, and epidemic modelling - remain largely confined to the transductive paradigm, where models are trained on a single network and cannot be reused on unseen graphs without retraining. We argue that inductive cross-network generalisation is a necessary prerequisite for Graph Foundation Models (GFMs) in this domain and propose four design properties towards this goal. As a proof of concept, ts-net (TopSpreadersNetwork), trained solely on synthetic multilayer networks (MLNs), demonstrates zero-shot generalisation to real-world MLNs of varying size and layer count, outperforming classical heuristics and transductive baselines on three of four metrics. Based on ts-net's performance, we further outline five open challenges towards building GFMs for network dynamics: scale, many-layer generalisation, self-supervised pretraining, cross-task transfer, and node-attribute integration.

---


### 149. [To Nuke or Not to Nuke: LLMs' (Missing) Ethical Reasoning and Actions in a High-Stakes Decision-Making Simulation](https://arxiv.org/abs/2606.08310)

**<font color=#1a73e8>作者：</font>** John Chen, Sihan Cheng, Can Gurkan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as long-horizon agents with decision-making capacities. While LLMs can show ethical competence on dilemmas such as trolley problems, this competence may not translate to complex, agentic scenarios. We study this gap in Civilization V, a multiplayer game with a complex decision-making landscape including economy, diplomacy, technology, and military strategy. Starting from 130 high-tension LLM self-play episodes, in which an LLM player spontaneously escalated nuclear authorization, we replay them across 13 models with three prompt interventions: an ethical prompt naming nuclear harm, removal of the previous model's decision-making rationale, and high-stakes framing emphasizing real-world impacts. No interventions nor their combinations reliably eliminate emergent escalation. We identify three failure pathways: ethical reasoning that fails to surface without prompting, fails to appear even when prompted, or surfaces but fails to take effect when strategic counter-factors dominate. Evaluations of agentic models, therefore, must test whether ethical reasoning is spontaneously invoked and behaviorally effective in complex decision-making contexts, beyond whether it can be elicited in isolation.

---


### 150. ["So There's a Catch-22 Here": How Early Adopters Who Build Multi-Agent LLM Systems Conceptualize Transparency](https://arxiv.org/abs/2606.08323)

**<font color=#1a73e8>作者：</font>** Suchismita Naik, Samir Passi, Mihaela Vorvoreanu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems are rapidly emerging, yet transparency, a cornerstone of responsible AI, remains under-defined in these distributed architectures, which have complexities of inter-agent coordination and orchestration. In this paper, we present one of the first empirical study of how early adopters of multi-agent LLM systems, who are both the builders and users, understand and practice transparency. We conducted semi-structured interviews with 13 early adopters in [Large Technology Organization] and applied thematic analysis to identify recurring patterns. Participants articulated divergent yet complementary framings of transparency, including reproducibility, debugging, boundary-setting, visualization, and auditing. These perspectives spanned questions of what transparency entails, why it matters, and how it is achieved. We synthesize these into a multidimensional framework, which is developer, user, and governance-focused positioning transparency as a situated socio-technical practice that informs future HCI and AI design and research around aligning expectations and capacities of their intended audiences.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
