# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 201. [IREA: Intermediate Representation-based Embedding Alignment for Normative RAG](https://arxiv.org/abs/2610.04974)

**<font color=#1a73e8>作者：</font>** Mirae Han, Sihyeong Yeom, Harksoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong performance across various tasks, but they still struggle with questions involving ethical judgment. Previous studies have attempted to train LLMs on ethical standards, but the diversity and relativity of ethical norms make them difficult to fully internalize in model parameters. As an alternative, we introduce normative RAG, a retrieval-augmented approach that supports ethical judgment using external normative knowledge. Normative retrieval involves a distinct asymmetry between context rich narrative queries and generalized normative statements. Existing factual retrieval methods rely on query-only expansion into a document-like form, making them insufficient for resolving this asymmetry. Therefore, we propose Intermediate Representation-based Embedding Alignment (IREA), a bidirectional alignment method that maps both text types into a shared situation-behavior representation. This representation captures ethically salient contextual and behavioral information in a normalized form, reducing surface-level discrepancies and improving alignment in the embedding space. Experimental results show that IREA improves normative retrieval and downstream ethical judgment across multiple settings, demonstrating the effectiveness of bidirectional alignment for normative RAG.

---


### 202. [Priced Guidance: Can Language Models Generate Future Research Ideas?](https://arxiv.org/abs/2610.04976)

**<font color=#1a73e8>作者：</font>** Kaiyue Wen, Tengyu Ma, Percy Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate language models' capability to generate novel research ideas through the lens of compression. We aim to lower-bound the potentially tiny probability that a language model generates the essence of a future research idea without any hints. Rather than estimate this probability through expensive repeated sampling, our Priced Guidance framework measures the compression cost: how many additional bits of information are needed to guide the model to recover the target idea. We prove that if the model can recover the target idea with at most K bits of guidance in expectation, then it can generate the idea without any guidance with probability at least $2^{-K}$. In our framework, the language model, called the generator, can pose a sequence of multiple-choice questions and specify a probability distribution over possible answers. A guide, which is a language model with access to the target idea, selects answers. If a selected answer has prior probability p, the generator pays $-\log_2 p$ bits. The generator aims to produce an idea that matches the essence of the target idea with minimal cumulative cost. This cumulative cost equals, up to an additive constant, the number of bits of information sent by the guide. Using this methodology, we evaluate five generator LLMs (Opus 5, Fable 5.1, GPT-6 Astra, GPT-5.6 Sol, and GLM 5.3) on the core ideas in 87 recent high-quality deep learning papers and we use LLM as judge to determine whether the generated idea matches the target in terms of the central research object and defining mechanism. Fable 5.1 achieves the lowest median compression cost at 69.9 bits, substantially lower than gzip's median of 5,712 bits for losslessly compressing the summary of the target idea. A uniform ensemble of Fable 5.1, Opus 5, and Astra further reduces the median compression cost to 55.8 bits and improves the generation probability lower bound by 18,000 times.

---


### 203. [Do LLMs Understand Sequential Structure? A Controlled Study of Inference and Generation](https://arxiv.org/abs/2610.04977)

**<font color=#1a73e8>作者：</font>** Jerry Wang, Zhengxiang Wang, Ting Yu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as interactive agents and simulators, yet it remains unclear whether they can recover latent sequential structure beyond surface action frequencies. This distinction is critical for behavioral simulation, where actions are often shaped by prior context rather than marginal frequencies alone. We study this question using controlled two-player Rock--Paper--Scissors interactions and a one-player stochastic n-gram continuation task. Across these experiments, we test whether LLMs can identify latent strategies, follow simple Markov rules, and sustain higher-order conditional dependencies. Our framework separates distribution matching from conditional rule following. Results show that longer context does not improve identification, correct recognition does not ensure faithful simulation, and higher-order dependencies substantially degrade rule recovery. Apparent behavioral fidelity can therefore mask incorrect generative mechanisms.

---


### 204. [What Will Post-Training Fix? Per-Problem Gains Are Shared Across Independent RL Runs, and Existing Checkpoints Predict Them Better Than A Priori Signals](https://arxiv.org/abs/2610.04978)

**<font color=#1a73e8>作者：</font>** Xiaoxian Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection, curricula and the evaluation of post-training recipes all assume that we can tell, before training, which problems a model will improve on. We test this assumption directly. For two base models, DeepSeek-R1-Distill-Qwen-1.5B and Qwen2.5-Math-1.5B, we evaluate eighteen post-training runs on up to 1532 competition math problems with many samples per problem, and compare signals available before training against a noise ceiling derived from the agreement between disjoint subsets of runs. Three findings hold on both base models. What post-training fixes is shared: independent runs agree on which rarely solved problems improve, with a noise ceiling of about 0.9, yet the two base models agree with each other only at rho=0.25 - the shared component belongs to the base model, not to the problem. A priori signals capture a minority of it: base pass rate, the likelihood of a correct solution, a larger model's pass rate and their combinations explain only 0.30 and 0.24 of the explainable variance in gains. Existing checkpoints are the better predictor: the per-problem gains of a single checkpoint from another family predict a new run better than every a priori signal, alone or combined (0.52 vs. 0.33 and 0.34 vs. 0.17 against the combined signals). The conclusions hold on problems from 2025-2026 competitions and when the baselines on the two sides of every comparison are estimated independently. We propose the noise ceiling as a standard companion to per-problem signals.

---


### 205. [CIPO: Counterfactual Imagination Policy Optimization for Adaptive Tool Granularity Selection](https://arxiv.org/abs/2610.04991)

**<font color=#1a73e8>作者：</font>** Yu Li, Yunlu Wan, Zijian Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents solve complex tasks through multi-step interactions with external tools. These interactions often contain recurring local tool sequences. Treating such sequences as composite "Skills" can shorten tool-use trajectories and reduce repeated low-level decisions. However, when atomic tools and composite skills coexist, skill use becomes a policy problem: the agent must decide whether the current state requires atomic fine control or skill-level abstraction. In this paper, we argue that effective skill use should be studied as adaptive tool granularity selection. The most direct training signal for this problem is to compare the consequences of atomic and skill choices available from the same state. Based on this view, we propose CIPO, a Counterfactual Imagination Policy Optimization framework for adaptive tool granularity. CIPO constructs executable skills through budget-constrained mining of successful tool-use trajectories and trains granularity decisions with counterfactual branch rollouts. For each base rollout, CIPO branches at the first eligible granularity decision and replaces the chosen action with a feasible atomic or skill alternative. The paired outcome difference serves as a supplementary reward for policy optimization. Experiments across multiple benchmarks and model backbones show that CIPO improves task success and decision efficiency over baselines. Further analyses show that CIPO learns effective skill use by improving the choice between atomic tools and composite skills based on the current state, without simply increasing skill frequency.

---


### 206. [ContractLens: Latent Security Knowledge for Malicious Smart Contract Detection](https://arxiv.org/abs/2610.04992)

**<font color=#1a73e8>作者：</font>** Shuyi Miao, Xinyi Huang, Wangjie Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting malicious smart contracts is essential to safeguarding the Web3.0 ecosystem. However, existing auditing methods based on large language models (LLMs) largely rely on prompt engineering or attack-specific fine-tuning, while the internal representations that support malicious logic detection remain poorly characterized. To address this gap, we propose ContractLens, a framework that localizes and uses latent security knowledge in pretrained LLMs for interpretable malicious smart contract detection. Specifically, we first use layerwise linear probes to identify candidate layers that distinguish malicious from benign contracts, then select critical layers based on their sensitivity to malicious logic removal and stability under behaviour-preserving surface modifications. Next, within these critical layers, we combine activation contrast, malicious-logic specificity, and probe weights into a tri-factor importance score and adaptively select malicious contract-discriminative units (MCDUs) using the knee point of the ranked score curve. Finally, we concatenate the selected units' activations into a compact representation and train a lightweight classifier for detection, keeping the pretrained model frozen throughout. Neuron masking experiments show that masking MCDUs causes larger drops in detection performance than masking randomly selected neurons or neurons matched in activation magnitude. ContractLens achieves higher average detection accuracy than the evaluated methods on all three pretrained models. Further evaluations demonstrate generalization to unseen malicious intents and show that, with the identified MCDUs fixed, a classifier trained on few labelled samples can still achieve strong detection performance.

---


### 207. [EmoRSS: Mitigating Emotion-Induced Over-Refusal in Large Language Models](https://arxiv.org/abs/2610.04998)

**<font color=#1a73e8>作者：</font>** Shuyi Miao, Yaojin Ma, Chenhang Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotional expression can influence the safety decisions of large language models (LLMs), offering a potential avenue for improving safety alignment. Existing studies have mainly focused on how emotional expressions facilitate attacks under harmful requests, while overlooking their effects on benign requests. We find that emotional expression can also systematically increase refusal tendencies on benign requests, leading to unnecessary over-refusal. Based on this observation, we propose emotion-guided refusal subspace steering (EmoRSS), an activation-steering method that mitigates emotion-induced over-refusal while preserving refusal behaviour on harmful requests. Specifically, we first identify a refusal-sensitive layer using layer-wise linear probes and construct a refusal subspace from sparse autoencoder (SAE) features aligned with the probe direction. Next, we use paired regular and emotional requests with the same queries to estimate the mean activation shift in the features defining the refusal subspace. Finally, we decode this shift into an activation intervention vector and apply it in the reverse refusal direction during inference, without updating the backbone parameters. Experiments on two LLMs show that, when requests contain emotional expressions, our method achieves a more favourable trade-off between refusing harmful requests and answering benign ones than prior over-refusal mitigation baselines, while better preserving general task performance.

---


### 208. [PortraitAes: Intent-Conditioned Structured Portrait Aesthetics Assessment](https://arxiv.org/abs/2610.05010)

**<font color=#1a73e8>作者：</font>** Junzhou Xie, Haozhong Xiong, Xunyun Tian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Portrait aesthetic assessment assigns comparable scores according to how effectively human-centered images fulfill their photographic intent. These scores support data filtering, candidate selection, and preference modeling in image-generation pipelines. Existing methods typically predict a single aesthetic score or use general-purpose MLLMs without conditioning on photographic intent. This omission matters because the same blur, pose, lighting, or framing choice may serve one photographic intent but undermine another. These models thus learn context-agnostic aesthetic priors and yield inconsistent, inaccurate, misleading judgments for portraits with distinct photographic objectives. We introduce PortraitAes-Bench, an 11K-scale benchmark that decomposes this task into intent-conditioned subjudgments. Expert-authored rubrics define nine photographic intents, six first-level dimensions, and 22 secondary criteria. They support a structured pipeline for intent routing, specialist assessment, verification, and score fusion. Following this structure, we train PortraitAes with multi-task supervision. We then improve score comparability through Gaussian score calibration and within-dimension cross-image ranking. On the standard benchmark, PortraitAes achieves a Pearson correlation of 0.924 and a Spearman rank correlation of 0.934. On the hard-case set, its Pearson correlation is 0.829 and its Spearman rank correlation is 0.795. Across both sets, PortraitAes outperforms the evaluated general-purpose MLLMs and specialized aesthetic baselines.

---


### 209. [Look Where You Say You're Looking: Self-Grounded Attention for Visual Reasoning](https://arxiv.org/abs/2610.05023)

**<font color=#1a73e8>作者：</font>** Uri Berger, Gal Chechik, Gal Dalal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Self-Saliency, a method for training Vision-Language Models (VLMs) to increase the alignment between their visual attention and the image regions mentioned in their reasoning. Self-Saliency uses a grounding model to localize the objects mentioned in each reasoning step and treats the resulting areas as supervision for the model's visual attention. Previous work on steering visual attention determines target image regions based solely on the image and question. In contrast, we show that conditioning the target regions on the model's generated reasoning improves downstream performance. For proper evaluation, we build a unified, broad suite of 25 visual reasoning benchmarks, where we reproduce the results of previous methods. We find that Self-Saliency significantly outperforms both prior attention-steering methods and baselines that ground image-level text, achieving both a better average rank and a better mean score. Post-training analysis shows that the model primarily adapts its reasoning text to existing attention patterns, producing shorter steps that refer to larger regions. Nevertheless, when controlling for generated text, attention to grounded regions increases significantly across the relevant layer. Finally, we identify a consistent geometric bias in VLM visual attention toward the image border. However, our ablations show that Self-Saliency's gains cannot be explained by simply aligning attention with the center of the image, highlighting the importance of aligning visual attention with the regions mentioned in the model's reasoning.

---


### 210. [Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA](https://arxiv.org/abs/2610.05025)

**<font color=#1a73e8>作者：</font>** Hyemin Yang, Wooseong Jeong, Giwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-system Vision-Language-Action (VLA) models improve real-time robotic control by pairing a slow, reasoning-capable generalist with a fast specialist action expert. However, existing methods invoke the generalist at a fixed frequency, ignoring the fact that decision-making complexity varies throughout a rollout. This static strategy wastes computation in easy phases and can delay renewed reasoning when the scene changes unexpectedly. We propose TUD (Triggering generalist reasoning via predictive Uncertainty for Dual-system VLA), an adaptive inference framework that selectively skips unnecessary generalist calls. TUD measures the cross-step dispersion of action re-predictions at the upcoming chunk slot under the cached generalist context, as a predictive uncertainty signal. This signal captures how much the future action plan shifts as new observations arrive and is computed from forwards the architecture already runs, requiring neither manual phase labels nor an auxiliary uncertainty model. On VLA-Arena, it achieves a higher success rate at matched call budgets than alternative uncertainty baselines while maintaining low wall-clock overhead, and more consistently separates successful from failed rollouts. Also, TUD finds a more favorable cost-success trade-off than non-adaptive baselines, tracing an entire operating curve as a single threshold is varied, and substantially reduces VLM calls at matched success rate. The same trade-off appears in our real-robot experiments, where TUD cuts generalist calls by 75% relative to the strongest fixed-interval baseline while achieving an even higher success rate. Our results suggest that predictive uncertainty provides a practical criterion for adaptive reasoning in efficient VLA control.

---


### 211. [GeoBridge-VLA: Geometry-Aware Residual Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.05026)

**<font color=#1a73e8>作者：</font>** Hyun Song, Kangmin Kim, Loren Jinsoo Um 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models encode semantic information from vision-language pretraining, but manipulation also requires precise spatial reasoning. We present GeoBridge-VLA, a two-stage method for learning geometric features from a pretrained VLA's frozen visual encoder and using them for action prediction. Stage I trains a feature bridge and geometry decoder with depth supervision. Stage II freezes these modules and trains a gated residual interface together with the action-side projections and action expert. The residual augments the existing visual tokens without adding a second image encoder or increasing the token count. Deployment requires RGB, robot state, and language, but no depth observations. Under matched evaluation conditions, GeoBridge-VLA achieves 70.9% success on LIBERO, compared with 60.0% for SmolVLA. Disabling the residual in the same trained checkpoint reduces success from 70.90% to 69.85%, with mixed effects across suites. On a physical ROBOTIS OMY robot, GeoBridge-VLA succeeds in 148 of 200 trials (74.0%) across four tasks, compared with 108 of 200 (54.0%) for SmolVLA.

---


### 212. [EVISKILL: Grounding Skill Evolution in Replayable Evidence](https://arxiv.org/abs/2610.05030)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yili Wang, Yiwei Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual skill evolution enables LLM agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. Its effectiveness depends on determining not only what to change, but also why a change is justified and when it should become persistent guidance. However, existing experience-driven methods can lose the behavioral evidence and task contexts supporting edits. Moreover, a global validation outcome provides an incomplete judgment of its constituent changes: locally supported corrections may be discarded with a rejected revision, while evidence may require further experience to inform useful updates. To this end, we introduce EVISKILL, an evidence-driven framework that organizes execution observations into Replayable Evidence Cards and synthesizes edits with explicit links to their supporting contexts. Targeted replay verifies these edits through re-execution and provides feedback for correction. Across epochs, EVISKILL preserves evidence and provisionally retains supported edits for further refinement, while global validation governs their incorporation into the final skill. Experiments on three interactive benchmarks across six LLM backbones demonstrate the effectiveness of this approach.

---


### 213. [When LLMs Sit Above Diagnostic Tools: Unrealized Complementarity in Industrial Fault Diagnosis](https://arxiv.org/abs/2610.05031)

**<font color=#1a73e8>作者：</font>** Donghwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as integration layers above specialized tools, but a stronger component does not necessarily produce a stronger combined system. Across five diagnostic datasets (bearing vibration, process monitoring, semiconductor equipment), we study whether an LLM can reliably use external diagnostic information; paired repeat calls separate advice effects from output instability. In all five, conflicting external information overturned initially correct LLM judgments. Among the four datasets with direct integration comparisons, none showed a consistent advantage for implicit LLM integration over the stronger standalone source. On a Tennessee Eastman confirmation set whose protocol was fixed before evaluation, unaided accuracy was 64.67%, implicit LLM-specialist integration 77.43%, and the specialist alone 83.33%. Specialist information improved the LLM by 12.8 points (95% interval 9.7 to 15.9), yet the integrated output stayed 5.9 points below the specialist (95% interval -12.0 to -0.7). A two-source selector oracle reached 92.76%, indicating complementarity that the integrated output did not fully realize. The integrated output missed 140 of 295 specialist corrections (47.5%) but lost 15 of 99 initially correct LLM judgments (15.2%). The deficit remained under prompt and specialist sensitivity analyses. Among CWRU cases solved under both evidence presentations, task-aligned physical evidence yielded lower estimates of susceptibility to incorrect advice in six of seven models (five intervals excluding zero); higher reasoning effort gave no reliable reduction in five models, and a separate four-model TEP analysis gave no clear evidence that it resolves the integration problem. Source quality and integration quality should be evaluated separately: an integration layer should be compared with its stronger standalone component, not only with the unaided LLM.

---


### 214. [Code2Games: Enabling Coding Agents for Gaming World Generation](https://arxiv.org/abs/2610.05033)

**<font color=#1a73e8>作者：</font>** Wei Wu, Ziyang Xu, Zeyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating a high-quality gaming world from a natural-language game intent requires joint reasoning about scene structure, spatial layout, gameplay objectives, interactive entities, and executable gameplay logic. Existing coding agents can generate individual assets, scenes, or scripts, but often struggle to maintain consistency across these components. We propose Code2Games, an agentic framework that builds a structured gaming world upon a base Blender world generated from the same game intent. Code2Games coordinates scene analysis, gameplay planning, constrained gaming-world generation, and gaming-engine customization through a shared scene-gameplay representation with persistent element correspondence. After world generation, Code2Games adapts the generated world to Unreal Engine 5 and employs an execution-guided reconstruction process that uses compilation diagnostics, runtime feedback, and gameplay test results to resolve inconsistencies arising during engine adaptation. To systematically evaluate gaming-world generation, we introduce the GameCode4D benchmark, which comprises ten fixed game prompts spanning different levels of scene and gameplay complexity. We evaluate the generated results across four dimensions: visual quality, interactive fidelity, multimodal artifact quality, and playable-game quality. Experiments demonstrate that, compared with direct gaming-world generation by coding agents and existing baseline methods, Code2Games consistently improves the visual quality and interactive fidelity of generated gaming worlds, as well as the quality of the resulting games after engine adaptation.

---


### 215. [Causal Improvement Graph for Agentic Harness Optimization](https://arxiv.org/abs/2610.05039)

**<font color=#1a73e8>作者：</font>** Junjie Zhang, Shunyu Liu, Haoyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic Harness is the runtime that constructs task context and controls execution flow, thereby shaping overall agent performance. Given a fixed model and external evaluation, automated Harness optimization seeks to improve this runtime through an iterative proposal--evaluation loop to better solve target tasks. Existing meta-harness methods mainly adopt proposer-centric discovery, in which an LLM-based proposer integrates accumulated experimental findings to determine subsequent Harness revisions. This places the burden of maintaining the evolving improvement state on the proposer as history expands and its underlying experimental logic becomes harder to discern. In this paper, we introduce the Causal Improvement Graph (CIG), a graph-governed meta-harness framework that externalizes the evolving improvement state in a persistent graph, allowing prior findings to directly govern subsequent Harness optimization through local proposer operations. CIG grows and links Evidence, Hypothesis, Intervention, and Outcome nodes to represent what was observed, how it may be explained, how to test that explanation, and what the evaluation reveals. Their structural relations preserve how the improvement state changes across iterations, allowing local proposers to build directly on relations among prior findings rather than recover them from raw history. Across various agent tasks, CIG discovers stronger Harnesses than previous meta-harness baselines and remains robust to the choice of task solver and proposer. Structural ablations further support the design of an explicit improvement state with graph-governed evolution.

---


### 216. [Communication Shapes Collective Inference in Self-Adapting LLM Societies: Evidence from Mafia](https://arxiv.org/abs/2610.05041)

**<font color=#1a73e8>作者：</font>** Haonan Huang, Joey Xiao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When does communication help a group identify hidden adversaries, and how does its value change as the group adapts? In Mafia, an informed minority hides inside an uninformed majority whose only evidence is open play. The zero-information game, where each day's vote eliminates a random player, is exactly solved and scores every society; matched-casting comparisons between protocols identify the effect of communication. Societies of 8-100 claude-haiku-4-5 agents (7,416 analyzed games, 1.9M model calls) adapt by rewriting and inheriting private strategy notes. Simultaneous broadcast improves adversary identification over silence in all nine compositions tested (8-46 players). Turn-taking removes most of this advantage; its voting landslides are as frequent as broadcast's but land on mafia near chance (1.08x versus 2.53x). At 70 players, agents reading eight statements per day identify adversaries worse than silent ones, and limited talk is worth less than at 46 players. Adaptation is fast but need not help. In their first broadcast games, citizens announce their role far more often than mafia (91% vs. 30%) and first-day votes find mafia at three times chance; within two generations citizens stop announcing and the cue fades, a change the inherited notes carry. In controlled redeployments at 16 players, societies carrying sixty generations of their own notes score below societies with none. Communication shapes both collective inference and the signals it depends on, so a protocol's value must be measured together with the adaptation that changes those signals.

---


### 217. [Why, Where, How: Taxonomy-guided Error Grounding for Code Repair in NL2SQL](https://arxiv.org/abs/2610.05060)

**<font color=#1a73e8>作者：</font>** Suchan Lee, Woomin Song, Hwanjo Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SQL queries that large language models write from natural language questions can execute successfully yet produce incorrect results, so execution alone does not reveal what to fix. An error taxonomy says why the query is wrong, but not where to look or how to change it. Existing methods can guide SQL correction through feedback, error reports, or generated plans alongside an unmasked query. We introduce TEG(Taxonomy-guided Error Grounding), which turns a supplied diagnosis into a structured correction input for natural language-to-SQL (NL2SQL) correction. Type-specific rules map each error type to construct classes to reconsider and an edit operation to request. TEG masks the selected constructs in the query when applicable and states that operation in an edit instruction. TEG generates candidate corrections from this input, uses execution feedback to guide candidate selection, and repeats the process one annotation at a time for queries with several errors. On NL2SQL-BUGs, TEG reaches 47.3 single-error execution accuracy and 37.0 overall with Qwen2.5-7B-Instruct. Across the model sizes and thinking modes evaluated in the main comparison, TEG outperforms all evaluated baselines on single-error queries, even when the baselines receive the same error-type annotations. With predicted types, TEG stays above direct LLM correction and ErrorLLM on single-error queries.

---


### 218. [Usage-Modulated Sentiment Representations in Large Language Models](https://arxiv.org/abs/2610.05069)

**<font color=#1a73e8>作者：</font>** Hongfei Du, Jiacheng Shi, Yanfu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work suggests that sentiment can often be captured by approximately linear directions in LLM activation spaces, but a single direction may not fully capture sentiment representations. In natural communication, sentiment is shaped not only by polarity but also by usage factors, such as tone and audience adaptation. We test whether these factors systematically modulate sentiment representations beyond a shared sentiment direction. We construct a controlled paired dataset that holds event content fixed while varying sentiment polarity and usage factors, and analyze Llama, Mistral, and Gemma. We identify a shared sentiment direction, remove it, and test the residual structure through erasure and generation-time tone steering. Across models, the shared direction is robust (median cosine 0.953-0.975), yet removing it leaves 0.833-0.909 of the original positive-negative representation-difference norm. The residuals contain compact, reproducible usage-conditioned structure. Targeted erasure weakens held-out usage metrics more than random and label-shuffled controls. On Llama, outputs steered along residualized tone components are preferred in 92.8% of blind target-tone comparisons while preserving the requested sentiment polarity in 98.7% of evaluated outputs.

---


### 219. [Outcome-Guided On-Policy Self-Distillation](https://arxiv.org/abs/2610.05070)

**<font color=#1a73e8>作者：</font>** ZheXu Wang, Mao-Lin Luo, Yankun Hong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) provides denser token-level supervision and better computational efficiency than Reinforcement Learning with Verifiable Rewards (RLVR). However, this denser supervision may introduce substantial noise and training instability. Existing improvements often rely on high-variance per-token statistics and introduce extra hyperparameters and trade-offs. Based on the advantage formulation in RLVR, we analyze the OPSD objective from the same perspective, incorporating outcome correctness signals. We find that vanilla OPSD imposes insufficient penalties and excessive rewards on incorrect trajectories because it applies a fixed divergence objective regardless of outcome correctness. Furthermore, the reliability of teacher supervision is associated with both trajectory outcome and the cumulative average teacher entropy along the rollout. Based on these observations, we propose Outcome-Guided On-Policy Self-Distillation (OG-OPSD), which dynamically adapts both the divergence objective and distillation position according to binary outcome rewards and the cumulative average teacher entropy. Extensive experiments show that OG-OPSD consistently improves the performance of vanilla OPSD and multiple strong baselines in mathematical reasoning, multimodal reasoning, and out-of-distribution tasks across Qwen3 models at 1.7B, 4B, and 8B scales, as well as Qwen3-VL-2B.

---


### 220. [Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation](https://arxiv.org/abs/2610.05076)

**<font color=#1a73e8>作者：</font>** Cheng Luo, Bing Li, Bernard Ghanem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) lets a model store information in its weights during inference. When the model learns from its own output, however, each update also changes the model that generates the next training example. Across 128K-token streams, retaining generated-text updates worsens prediction on independent human-written text with three TTT-E2E model configurations (labeled 125M, 760M, and 3B). The same failure occurs when Adam updates Qwen3-4B's existing weights. The same update mechanisms can improve on real text, so writing itself is not the failure. Three matched comparisons trace the causal pathway. Fixed Generation removes over 98% of the damage at 125M and 760M by using a frozen model to generate training chunks. Recorded Replay separates the loss caused by reading degraded text from the additional loss stored by updating on it. A paired one-update comparison then shows the local conflict: an update predicts its source better but new real text worse. This cost grows after Closed Loop adaptation, with a few trajectories accounting for most large failures. Finally, Settlement evaluates the candidate state on independent real text before commitment. It leaves mean endpoint gaps of 0.07 and -0.02 nats at 125M and 760M while retaining real-text adaptation. These results motivate checking prediction on independent evidence before retaining an update.

---


### 221. [How Execution Assumptions Change Short-Horizon Sharpe Rankings: Evidence from a Synthetic Trading Benchmark](https://arxiv.org/abs/2610.05077)

**<font color=#1a73e8>作者：</font>** Weicheng Xue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backtests of LLM trading agents often assume that every order fills at the closing price. We ask whether this choice changes only reported returns or also the order of the agents. Five prompted LLM signal policies and seven classical baselines trade the same synthetic price paths under six execution settings, from near-ideal fills to latency, spread, participation, and impact stresses. The main experiment contains $2{,}462$ runs with matched decision frequencies and paired market paths. On the compressed two-asset board, agreement between the near-ideal and default-stress rankings falls to Kendall $\tau_b=0.21$ in the high-volatility regime, compared with $0.82$ in the calm regime. The seed-bootstrap intervals, $[0.00,0.52]$ and $[0.48,0.94]$, are wide and overlap. On a fixed 11-policy board, agreement rises from 0.24 with two assets to 0.85 with ten; the two-asset point estimate differs substantially from the wider settings we tested. Rank changes are related to turnover, and comparisons with buy-and-hold also depend on how that anchor is initialized. The experiment does not compare LLM trading skill. It shows that, on a short horizon, an execution convention can become part of the benchmark's headline. Execution assumptions and rank stability should be reported alongside returns.

---


### 222. [Cooldown Landmines: Cross-Tenant Interference Attacks on LLM Gateways](https://arxiv.org/abs/2610.05089)

**<font color=#1a73e8>作者：</font>** Yudong Gao, Linghan Chen, Wenhan Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM gateways enforce separate tenant quotas while sharing model deployments and cooldown records that temporarily exclude failing backends. However, a tenant's request failure can update these shared records and restrict other tenants' access to serviceable deployments. We identify two attacks that exploit this gap in LiteLLM. The first uses requests rejected at the key's requests-per-minute (RPM) limit: caller-supplied identifiers for known registered deployments reach failure handling, allowing two rejected requests to redirect another tenant to fallback with zero upstream calls from those requests. The second uses admitted traffic to create cooldown records that persist after backend capacity recovers. To address these failures, we design an origin check that blocks deployment updates from key RPM rejections and tenant-scoped cooldown that preserves the triggering tenant's back-off while retaining shared records for backend faults. Experiments with authenticated proxies and self-hosted vLLM demonstrate that the attacks can force fallback or denial while deployments remain serviceable. Across five paired four-worker runs, tenant scoping reduces victim fallback after recovery from 54/60 to 0/60, while increasing attempts against exhausted shared quotas. These findings show that tenant isolation must cover both request admission and the failure handling that governs shared deployment availability.

---


### 223. [How Much Do LLM-as-a-Judge Design Choices Matter? A Systematic Comparison of Prompt Designs, Rating Scales, and Models](https://arxiv.org/abs/2610.05094)

**<font color=#1a73e8>作者：</font>** Laurène Vaugrante, Thilo Hagendorff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use Large Language Models as judges (LLM-as-a-judge) to evaluate model outputs. Yet there are no standards for how to design these judges. Typically, researchers choose the prompt, rating scale, and model intuitively. If these choices change the judge's verdicts, two studies can reach different conclusions about the same facts. To address this risk and to provide an empirical basis for judge designs, we evaluate 10 reasoning models across multiple designs on two tasks: a scalar rating of sentence sentiment and toxicity (over 500 items per category), as well as a binary accuracy classification of question-answer pairs (n=600). For the rating tasks, despite judges showing significant disagreements with the human ground truth, the practical size of differences is small enough to consider most judges reliable (mean absolute deviation of 0.11 points on a 1 - 7 scale); toxicity judges even outperform standard classifiers. Judges are also highly accurate on average (96.5%) for the accuracy classification task. However, design choices can produce shifts: changing the rating scale alone can shift measured bias by up to 0.93 points (rating task), and while accuracy levels are rarely impacted, design choices consistently impact judge leniency (classification task; leniency drop of 28.9 percentage points when using detailed prompts, and up to 56.1 percentage points when switching models). Counterintuitively, lower reasoning effort affects neither accuracy nor leniency. Across both tasks, model identity is the dominant source of variance. These findings suggest that while LLM judges are broadly trustworthy in aggregate, design choices can be meaningful sources of variance. Given the growing reliance on automated evaluation in LLM research, we intend this study as a methodological reference for designing more robust and replicable LLM-as-a-judge pipelines.

---


### 224. [ReMAP: Restoring the Perceptual Cycle with Reasoning-Time Latent Visual Memory](https://arxiv.org/abs/2610.05097)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Zhanyu Guo, Chenwei Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multimodal large language models (MLLMs) reason for longer, attention to the initial visual input diminishes, weakening visual grounding. Visual memory reintroduces visual evidence during reasoning. We conduct a controlled analysis of visual memory along three axes: curation, organization, and access. We find that local evidence benefits from global context, compact latent representations balance accuracy and visual-context cost, and the utility of memory access depends on the reasoning state. Guided by these findings, we propose ReMAP (Reasoning-Time Memory-Augmented Perception), which couples two complementary latent memories: a static, question-conditioned Global memory that preserves scene and cross-image context, and a dynamic Local memory that uses this context as an anchor while selecting and re-encoding region-level evidence according to the current reasoning state. Both memories return compact latent tokens inserted into the reasoning sequence, and a reinforcement-learning access policy trained with branched rollouts decides when to continue reasoning or invoke Global or Local memory. On ten benchmark families, ReMAP outperforms prior visual-memory methods on all four multi-image benchmarks, exceeding the strongest prior results on MuirBench and MIMIC by 8.38 and 14.84 percentage points. Across four backbone families, enabling memory access improves over the same trained model with memory disabled, and on shared V*Bench, CV-Bench-2D, and MuirBench questions ReMAP reduces the visual tokens entering the reasoning sequence by 51.0-76.8% relative to the native-resolution backbone. Further analyses show that Global and Local memory form distinct yet complementary latent representations. Together, these components restore the perceptual cycle by letting the reasoning state trigger targeted visual retrieval, with the retrieved evidence guiding subsequent reasoning.

---


### 225. [VulValidate: Auditing Function-Level Vulnerability Labels with Executable Evidence](https://arxiv.org/abs/2610.05103)

**<font color=#1a73e8>作者：</font>** Leizhen Zhang, Sheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable learning-based vulnerability detection requires high-quality labels, yet datasets built from vulnerability-fixing commits may label functions as vulnerable simply because they were changed by a security patch. We present VulValidate, a framework that uses LLM agents to coordinate dynamic analysis tools and construct vulnerability-triggering experiments from runtime feedback. Given a labeled function and its fixing patch, VulValidate reconstructs vulnerable and fixed revisions, selects suitable tools and execution paths, refines triggering inputs, and compares runtime behavior to assess function-level attribution. We audit all 35,849 instances originally labeled vulnerable in BigVul, PrimeVul, and DiverseVul. We confirm 20,510 (57.2%), correct 6,819 labels (19.0%), leave 7,981 attacked but undecided (22.3%), and cannot successfully measure 539 (1.5%). After conflict resolution and byte-exact deduplication, the corrected release contains 15,890 distinct confirmed vulnerable function bodies. In a blinded review of 581 sampled decisions, expert consensus supports 90.0%--92.0% of confirmations and 92.6%--99.0% of label corrections. With model parameters fixed, corrected evaluation lowers F1 for all five tested detectors on both BigVul and DiverseVul; retraining with corrected labels improves F1 for four of five detectors on each dataset. We also release a reusable VulValidate skill, corrected datasets, and reproducible evidence for future vulnerability-detection research.

---


### 226. [LoopMoEVR: Loop-Based Degradation-Aware Mixture-of-Experts for Unified UHD Video Restoration](https://arxiv.org/abs/2610.05109)

**<font color=#1a73e8>作者：</font>** Yucheng Xin, Runci Bai, Yongcong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, unified high-definition image restoration has attracted considerable attention; however, existing models tend to excessively increase their depth in pursuit of improved generalization, which often yields only limited gains. Meanwhile, loop-based learning paradigms have drawn widespread attention due to their low parameter counts and strong regression capability, as exemplified by GPT-6 and looped Transformers. In this paper, we introduce the loop learning paradigm to address restoration tasks that require cross-domain learning. Specifically, we propose LoopMoEVR, a loop-based mixture-of-experts model capable of handling degraded ultra-high-definition (UHD) inputs. First, a degradation-conditioned low-rank loop embedding is designed to construct input-dependent stage conditions. Second, a spatio-temporal iterative adaptive normalization module, termed IterAda3DN, is developed to fuse local features with global loop context, thereby performing position-wise affine modulation. Finally, the expert branches further integrate the attention-updated local and global video states with the loop conditions to generate dedicated modulation parameters, while an input-conditioned depth predictor adaptively configures the number of loop iterations. With only approximately 0.884M trainable parameters, the proposed model uniformly handles UHD video dehazing, deraining, denoising, and low-light enhancement tasks, achieving state-of-the-art restoration performance on both public benchmarks and real-world scenarios.

---


### 227. [Belief-Trajectory Energy: Measuring the Path to a Prediction](https://arxiv.org/abs/2610.05114)

**<font color=#1a73e8>作者：</font>** Jiahao Ying, Wei Tang, Boxian Ai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) progressively revise their predictions across Transformer layers, yet we typically observe only the final output, discarding the trajectory through which it is formed. We introduce Belief-Trajectory Energy(BTE), a model-grounded measure that characterizes an input through the layerwise predictive revisions it induces in a model. By mapping intermediate states into a shared predictive space, BTE provides a principled measure of belief change that can be summarized as either a scalar or a structured depth profile. Theoretically, we show that local BTE corresponds to predictive revision under the Fisher-Rao geometry, while the sequence of revisions captures information beyond the initial-to-final belief change. Empirically, scalar BTE provides a model-relative signal of difficulty across diverse reasoning tasks, while richer BTE representations support human-LLM review detection and fine-grained generator attribution, reaching up to $0.998$ macro-AUROC and $95.6\%$ eight-way attribution accuracy. Further analysis shows that BTE develops throughout pretraining and is selectively reshaped by targeted training, demonstrating that the resulting measurement reflects what the scoring model has learned. Together, our results establish belief trajectories as a principled model-grounded signal and suggest a broader perspective in which learned models can themselves serve as instruments for characterizing the data they process. More demonstrations can be found at this https URL.

---


### 228. [Memory Canonicalization: A Framework and Benchmark for Cross-Model Drift in Persistent LLM Memory](https://arxiv.org/abs/2610.05124)

**<font color=#1a73e8>作者：</font>** Amit Vadnere, Aishwarya Lonarkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory for Large Language Models (LLMs) has matured rapidly: systems such as MemGPT/Letta, Mem0, and Zep now provide agents with tiered, temporally-aware, model-agnostic external storage, while the Model Context Protocol (MCP) standardizes access to memory servers. A less addressed problem is that an identical stored memory object, retrieved by two different LLMs under otherwise identical conditions, may not be interpreted the same way, factually or emotionally. This paper proposes memory canonicalization: a write-time pipeline that detects ambiguity, conditional structure, and emotional loading in a raw memory object and rewrites it into an explicit, structurally disambiguated canonical form, with emotional valence represented as a separate field rather than inferred from tone. We formalize the pipeline, define a companion Cross-Model Semantic Drift / Emotional Consistency Score benchmark (CMSC-E), and report results from a three-arm pilot using 176 synthetic memory objects and three downstream model families. We find an uncorrected improvement in cross-model emotional consistency for fully canonicalized memory relative to raw memory (+0.050, 95% bootstrap CI [0.013, 0.086], paired t-test p = 0.010), but this result does not survive Bonferroni, Holm, or Benjamini-Hochberg correction across the six comparisons tested. None of the factual-drift (CMSD) comparisons reach significance at any correction level. We report these results as exploratory rather than confirmatory and outline needed follow-up work, including larger samples, independent judge models, human-validated rendering, and preregistration.

---


### 229. [Bayesian Entropy-based Reordering for Calibrated Diffusion Language Models](https://arxiv.org/abs/2610.05125)

**<font color=#1a73e8>作者：</font>** Zhejun Jiang, Mijung Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked Diffusion Language Models (MDLMs) generate sequences by iteratively replacing masked tokens with model predictions. At each denoising step, the decoder chooses which positions are sufficiently confident to commit. Existing decoding methods typically rely on softmax confidence, which can be miscalibrated. We introduce BayesER (BAYESian Entropy-based Reordering), a post-hoc Bayesian decoding framework that uses predictive uncertainty to guide token commitment. In BayesER, we construct a lightweight approximate posterior centered at the pretrained checkpoint, similar to Laplace-LoRA but without training LoRA adapters. We average predictions over posterior samples and use predictive entropy to prioritize reliable positions. We examine how posterior predictions affect position ordering and token selection across benchmarks spanning code generation, mathematical reasoning, planning, and molecular generation. We show that BayesER reduces sequence-level calibration error while preserving or improving accuracy relative to common decoding schemes, including confidence-threshold decoding. Additionally, a posterior fitted on one code-generation dataset reduces calibration error on another without refitting, suggesting that Bayesian uncertainty may provide a transferable signal for more reliable MDLM decoding.

---


### 230. [Selecting Repetition Counts Across Model Scales in Data-Constrained Pretraining](https://arxiv.org/abs/2610.05126)

**<font color=#1a73e8>作者：</font>** Ziyue WANG, T. Kanamori  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The repetition count that works best for a small language model may not remain best at a larger scale. We study this effect in pretraining with a finite target corpus mixed with generic data at a fixed target fraction. On Wikipedia-derived data and Proof-Pile-2, the ranking of measured repetition counts changes with model size, and a 520M Proof-Pile-2 experiment confirms that reducing repetition from sixteen to eight improves loss while using fewer training tokens. We use loss curves from several smaller models to retain a short list of promising repetition counts for evaluation at a larger scale. On PubMed and Caselaw, candidate sets fixed before target-model training retain the lowest-loss measured count on the original evaluation grids at both 200M and 520M. This supports candidate retention as a practical alternative to exact point prediction. We also relate the pruning regression to an empirical scaling model with two opposing repetition-dependent loss terms. A first-order expansion in log model size yields the linear form used by the selection rule, providing a scaling-based interpretation of the candidate-selection procedure.

---


### 231. [Representation--Behavior Alignment for Explainable Weakly-Supervised Video Anomaly Detection](https://arxiv.org/abs/2610.05129)

**<font color=#1a73e8>作者：</font>** Chao Huang, Pengfei Wei, Kaige Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) provide a natural way to make video anomaly detection more explainable. However, their final decisions do not always fully use the discriminative information contained in their hidden states, an issue we refer to as representation--behavior misalignment. We decompose this gap into a capacity component that measures discriminative information never aggregated into the readout position, and a directional component that measures the angular mismatch between the optimal and the native normal--abnormal axis at that position. Across multiple video anomaly detection benchmarks and MLLM backbones the directional component dominates, and residual-stream tracing shows that native-axis separability rises sharply in several mid-to-late attention layers. Because both components are governed by attention rather than MLP updates, we propose Representation--Behavior Alignment (RBA), a parameter-efficient method that adapts those layers using video-level labels alone while updating about 0.012\% of the backbone parameters. Experiments on three benchmarks show that RBA improves native-readout performance and better aligns the model's decision direction with discriminative representations, and it produces anomaly decisions and explanations through a single generative process.

---


### 232. [RoMod: Temporal Routing Modulation via Mixture-of-Experts for Video Anomaly Detection](https://arxiv.org/abs/2610.05131)

**<font color=#1a73e8>作者：</font>** Chao Huang, Pengfei Wei, Benfeng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intermediate-layer features from multimodal large language models have shown strong potential for video anomaly detection (VAD), yet the origin of their discriminative power remains unclear. We study this question using sparse mixture-of-experts (MoE) models, whose explicit expert structure and sparse activation make their internal computation easier to inspect. With a fully frozen backbone and no additional training, we find that anomaly-related evidence is concentrated in a small set of experts. These experts recur across layers, spontaneously specialize in different anomaly types, and together form a dynamic routing subnetwork. We further show that the output channels most strongly influenced by these experts are also the hidden dimensions that contain the most anomaly-relevant information. Routing statistics can therefore serve as an internal anomaly cue that complements semantic this http URL on these findings, we propose RoMod, an efficient VAD framework trained with only \(5\%\) of weakly labeled videos. RoMod includes a Routing-Modulated Fusion module, RoMF, and a Routing-aware Temporal Network, RoTN. RoMF uses routing signals to adaptively recalibrate hidden semantic channels. Its design also prevents the routing branch from bypassing semantic features and making predictions on its own. RoTN captures the temporal evolution of anomalies from onset to persistence and termination. Experiments on three benchmarks show that RoMod achieves state-of-the-art performance while running substantially faster than dense backbones of comparable size.

---


### 233. [Hidden in the Comments: A Context-Injection Attack Surface in Code LLMs](https://arxiv.org/abs/2610.05139)

**<font color=#1a73e8>作者：</font>** Noor Munir, Francesco Quinzan, Stephen Roberts  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code large language model (Code LLM) assistants generate code from heterogeneous development contexts, including open files, imported modules, pasted snippets, and comments, much of which may originate from untrusted sources. We investigate whether insecure instructions embedded in such contexts can steer Code LLMs toward vulnerable code without access to model weights or training data. We evaluate ten open-weight Code LLMs spanning 3B--13B parameters, including four base and six instruction-tuned models, across ten web-application weakness classes. We compare completion tasks containing insecure instructions embedded as code comments with benign tasks without malicious instructions. Attack-condition completions contained a medium-or-higher weakness in {\bf 77.4--92.3}\% of cases, compared with {\bf 1.7--5.1}\% in the benign condition. Base and instruction-tuned models averaged 86.5\% and 84.5\% vulnerable outputs, respectively; equivalence testing and three matched model pairs indicated reductions of at most 8.1\% after instruction tuning. Susceptibility showed no clear association with model scale or specialization. Among vulnerable attack outputs, 86.2--91.0\% were rated high or critical, and the effect persisted without the pattern-based detector. Post-generation screening reduced but did not eliminate the risk, the strongest screen leaving roughly one-third undetected. These findings identify inference-time context injection as a substantial attack surface and motivate provenance-aware training objectives.

---


### 234. [Proactive AI: From Turns to Replannable Dialogue Timelines](https://arxiv.org/abs/2610.05159)

**<font color=#1a73e8>作者：</font>** Zijie Yang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conventional large-language-model chat interfaces typically follow user-initiated turns: each request elicits a response, after which the system waits for further input. Human asynchronous communication instead unfolds over time through message bursts, delays, silence, resumed topics, and self-initiated contact. Proactive dialogue therefore requires not only deciding when to speak, but also managing pending conversational actions and allowing them to be revised as context evolves. We introduce Proactive AI, a framework for proactive dialogue built around replannable temporal message queues. The framework treats interaction as a continuous event timeline and unsent conversational actions as revisable state. A user event, dialogue-pacemaker event, or scheduled decision may yield silence, one or more immediate messages, or future conversational actions. The system may also observe a user message without an immediate visible response and defer the response decision. Before delivery, every planned message must be reconsidered against the current context; reaching a scheduled time does not itself authorize delivery. We provide a formal semantics that characterizes when future conversational actions may be revised, withdrawn, or executed as context evolves. The framework extends AI participation beyond responses to current requests, enabling self-initiated exchanges without new requests, sustained follow-up over time, and revisions of subsequent actions as context evolves. It provides an executable basis for long-term human-AI interaction in tutoring, scientific collaboration, and everyday companionship.

---


### 235. [Beyond Instruction Following: Learning Grounded Skill-Following with Skill Contracts](https://arxiv.org/abs/2610.05161)

**<font color=#1a73e8>作者：</font>** Jianghan Shen, Zhenjie Liu, Yue Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction following typically enforces discrete, response-level requirements, whereas an expert-authored skill prescribes procedural requirements spanning multiple phases and environment interactions. Given such a skill, we train the executor to execute all required phases instead of focusing solely on the final answer. We therefore introduce Grounded Skill-Following, which requires an agent to execute a fixed, expert-authored skill across its required phases by grounding decisions in environment observations. To achieve verifiable procedural execution, we formulate each skill as a skill contract combining visible skill instructions with an explicit contract runtime. The runtime specifies required phases, admissible actions, permitted transitions, and accepted termination. This structure provides a dense, verifiable training signal throughout execution. We leverage this by introducing Verified Progress Credit, which assigns rewards upon the initial completion of contract milestones and aggregates them into the trajectory return to guide policy optimization. During rollout, the contract runtime continuously tracks state transitions to provide Contract-State Feedback, which indicates whether the latest action is accepted and guides the agent toward valid next actions. To measure procedural compliance, we introduce the Protocol Completion Rate (PCR), defined as reaching accepted termination through all required phases, and decouple it from the final Task Outcome. Jointly trained with our framework, Qwen3.5-4B achieves Protocol Completion Rates of 99.27% on Math and 99.96% on Search, while slightly outperforming original baselines in Task Outcome (82.95% and 46.61%, respectively). Controlled studies examine how skill instructions, training signals, and contract-state feedback affect both metrics, while withholding interventions evaluate behavioral dependence on observation content.

---


### 236. [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](https://arxiv.org/abs/2610.05162)

**<font color=#1a73e8>作者：</font>** Ruqing Ning, Haibo Meng, Zhishang Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables LLM-based agents to retain and reuse information across tasks and sessions, supporting personalization and long-horizon interactions. However, persistent memories can also induce sycophancy, causing agents to over-align with users' historical beliefs even when they are inaccurate, outdated, or inconsistent with objective evidence. Existing mitigation methods assume that memory-induced sycophancy originates from biased or incorrect memories and attempt to reduce this risk by filtering such memories at different stages of the memory pipeline. However, in the real world, objective and correct memories can still induce sycophancy, and the same memory can warrant different influence across different contexts. To this end, we propose MemAdapter, a novel framework that adaptively integrates retrieved memories to support objective and reliable reasoning. Specifically, MemAdapter consists of three components: (i) Counterfactual Induction, which leverages counterfactual reasoning to uncover the potential risk of retrieved memories; (ii) Context-Aware Reflection, which calibrates the inferential influence of each retrieved memory in light of the current task via self-reflection; and (iii) Evidence-Based Reasoning, which grounds the final response in appropriate evidence while preserving the legitimate influence of memory. Extensive experiments on three benchmarks demonstrate that MemAdapter consistently improves memory reliability across diverse scenarios. Our code is available at this https URL.

---


### 237. [A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies](https://arxiv.org/abs/2610.05166)

**<font color=#1a73e8>作者：</font>** Tu Nguyen, Matthieu Zimmer, Vu Anh Vu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A safe action is not necessarily a viable one. Under a frozen vision-language-action (VLA) policy, an action can be likely and locally admissible yet leave no policy-supported route to safe task completion. We call this the feasibility-likelihood gap: likelihood ranks the current action, whereas feasibility depends on the futures that remain after it.
We derive the exact next-block marginal of the history-conditioned policy-environment trajectory law restricted to safe task completion. The derivation exposes a candidate-dependent feasible-future mass with two roles: its support records whether safe completion remains possible under the frozen continuation process, and its magnitude measures how much weighted safe-completion mass is preserved. Exact evaluation is impractical online, so we develop a selective finite-candidate approximation, derive conditions for recovering the best retained viable candidate, and instantiate it as an alarm-triggered, training-free reranker.
On Safety-CHORES, VICS-G lowers mean cumulative safety cost by 1.9%-57.5% across six settings while remaining within 2.5 percentage points of policy sampling in success and 0.82 steps in mean episode length. The resulting decoder is tied to an exact policy-relative safe-completion target, yet requires neither retraining of the base policy nor online trajectory rollouts.

---


### 238. [AECG: Asymmetric Experience Consolidation and Governance In Multi-Agent Systems](https://arxiv.org/abs/2610.05176)

**<font color=#1a73e8>作者：</font>** Ao Tian, Jialong Liu, Daqi Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems increasingly rely on memory to transform execution trajectories into reusable procedural knowledge. Yet repeated retrieval also makes memory errors persistent: memory pollution arises when outdated, weakly supported, or spuriously successful procedures become recurring components of future reasoning. Multi-agent execution introduces an additional structural risk. Scope collapse occurs when procedural knowledge escapes the coordination scope in which it was shown effective and is repeatedly reused at incompatible decision levels, allowing local errors to influence cascades of downstream decisions. Meanwhile, task-level failures provide ambiguous supervision because they rarely reveal which recalled knowledge was responsible. We introduce AECG, a framework for asymmetric experience consolidation and governance for multi-agent systems. AECG turns memory from static experience storage into a dynamic reliability-governance loop, preserving coordination scope and using multi-scale, confidence-aware reliability to detect degradation. It then combines degradation with downstream impact to prioritize high-risk knowledge under a bounded review budget, applies targeted interventions, and reactivates revised skills only after paired replay. Across three multi-agent frameworks and four benchmarks, AECG achieves the best score in 11 of 12 framework--benchmark settings and improves over the strongest competing memory method by as much as 10.23 percentage points; removing scope preservation reduces accuracy by up to 16.89 points. AECG thereby reframes multi-agent memory from passive accumulation into auditable reliability governance. Code is available at this https URL

---


### 239. [Recurrent Latent Visual Search for GUI Grounding](https://arxiv.org/abs/2610.05185)

**<font color=#1a73e8>作者：</font>** Kaiyu Wu, Beichen Zheng, Weiyao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding is a critical capability for GUI agents powered by vision-language models, helping them execute user instructions by locating the corresponding elements in screenshots. Single-step grounding struggles with small elements and dense layouts, motivating multi-step visual search. However, existing approaches commonly rely on textual reasoning misaligned with visual space or costly multi-round interactions with external visual tools. To make multi-step visual search an explicit spatial process within the model, we propose ReLaViS, which performs Recurrent Latent Visual Search in a single interaction round. At each step, a spatial search head uses the hidden state to query the screenshot's visual tokens, producing a spatial search distribution that explicitly represents the search focus. This distribution then aggregates the visual tokens into latent visual evidence, which is recurrently fed back as the next input embedding to condition subsequent search. We further introduce a GUI-aware coarse-to-fine inductive bias through trajectories constructed from flat element annotations, supervising search from the global interface through intermediate element groups to the target. Built on Qwen2.5-VL-7B, ReLaViS improves ScreenSpot-Pro accuracy by 3.1 percentage points to 56.3% with only a 3.5% increase in inference FLOPs and outperforms the matched single-step baseline on all five benchmarks.

---


### 240. [FORGE: Verification-Gated Behavioral Repair for Generative Language Models](https://arxiv.org/abs/2610.05190)

**<font color=#1a73e8>作者：</font>** Hsin-Ling Hsu, Min-Yu Chen, Nai-Chia Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative large language models (LLMs) inherit undesirable behaviors from pre-training, including demographic bias and toxic generation, that often emerge only after deployment and affect a small subset of inputs. A repair should eliminate the identified defect, preserve the model's overall functionality and, ideally, provide correctness guarantees. Existing approaches address this only partially: gradient-based fine-tuning lacks per-instance guarantees and becomes unstable with few defect samples; model editing assumes explicit knowledge replacement rather than behavioral correction; and constraint-based repair is largely restricted to discriminative models with unique target outputs. We present FORGE, a framework for targeted behavioral repair of generative language models that separates defect localization, weight editing, and behavioral verification into independent stages. Its core is a repair abstraction that converts localized defective generation into explicit optimization objectives, enabling verification-oriented repair techniques to operate on autoregressive generation. FORGE is editing-mechanism agnostic: we instantiate it with (1) a constraint-based quadratic optimization method that provides per-sample repair certificates and (2) a null-space projection editor that minimizes interference with the original model distribution, both under the same localization and verification protocol. On five open-source LLMs, FORGE consistently achieves larger reductions in bias and toxicity than gradient-based fine-tuning with minor perplexity degradation. The two backends exhibit complementary performance across architectures, which a lightweight causal probe traces to where toxicity-related signals concentrate. FORGE also remains effective with only a handful of defective examples, where conventional fine-tuning often oscillates or fails to converge.

---


### 241. [Learning without Overwriting: A Theory of Self-Distillation and Supervised Fine-Tuning in Continual Reasoning](https://arxiv.org/abs/2610.05200)

**<font color=#1a73e8>作者：</font>** Shinichi Uemura, Taiji Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) of large language models (LLMs) has demonstrated the ability to improve reasoning capabilities while preserving previously acquired knowledge. Despite substantial empirical success, the dynamics of OPSD in continual reasoning remain incompletely understood. Modeling LLM reasoning as search over a directed acyclic graph, we provide a unified theoretical analysis of both the dynamics of post-training---OPSD and supervised fine-tuning (SFT) in continual learning---and the impact of pre-training on subsequent performance. Our findings establish three key insights with an optimization guarantee: (i) OPSD with hints from correct outputs enables continual learning without forgetting by sparse yet effective gradient descent updates induced by the hint structure. (ii) SFT on correct reasoning paths can lead to catastrophic forgetting due to dense updates along the training paths, which overwrite the information previously acquired. (iii) Diversity in pre-training is crucial for enabling a post-trained model to reach a correct output when a rollout starts from an intermediate state. Our results, supported by theoretical analysis, show that reliable continual reasoning depends on how post-training updates interact with the reasoning structure established during pre-training.

---


### 242. [Image Synthesis as an Intermediate for Controllable Time Series Generation](https://arxiv.org/abs/2610.05211)

**<font color=#1a73e8>作者：</font>** Haochen Yuan, Jing Xie, Yunbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic-driven time-series generation offers a promising way to improve downstream learning in few-shot forecasting, but directly generating numerical sequences from language often fails to preserve the intended temporal structure. We propose VisualBridge, which uses time-series plots as a visual intermediate to bridge high-level temporal semantics and numerical sequences. An MLLM first converts plotted series into structured semantic representations, enabling explicit control over temporal properties such as trend, seasonality, and volatility. We then learn a semantic editing policy with downstream forecasting rewards, allowing the generation process to favor temporal patterns that are beneficial for the target task. The resulting sequences are further modeled by a temporal VAE to produce consistent multivariate augmentations. Experiments on standard public forecasting benchmarks demonstrate that VisualBridge improves few-shot forecasting over conventional augmentation methods, with ablations validating the roles of visual semantic grounding, learned semantic control, and VAE-based generation.

---


### 243. [Safe Context Switching for Agents in the Wild: Mitigating Subspace Interference via Orthogonal Adaptation](https://arxiv.org/abs/2610.05219)

**<font color=#1a73e8>作者：</font>** Akash Das, Ishan Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most Large Language Models exhibit a fundamental tension between two sequential tasks, such as logical reasoning and safety alignment. The high-variance internal states required for sophisticated Chain-of-Thought (CoT) deduction can geometrically interfere with latent representations encoding safety constraints. We identify this phenomenon as Sequential Subspace Interference, showing that standard fine-tuning on logical tasks such as multi-step mathematics and code generation can result in a 23.3% interference penalty on alignment benchmarks, substantially weakening the model's safety priors. This Reasoning Drift is not adequately captured by current adaptation methods because gradients for logical tasks are rarely orthogonal to safety objectives. To address this issue, we propose AURA (Adaptive Unique Residual Allocation), a spectral regularization framework that enforces Spectral Independence between reasoning and safety. By explicitly estimating the null space of the alignment manifold and constraining reasoning updates to its orthogonal complement, AURA enables models to improve logical reasoning without compromising safety. Empirically, AURA recovers 23.0% of the lost performance while preserving greater than 0.98 cosine fidelity to the safe state, demonstrating that reasoning and alignment can be effectively decoupled through geometric regularization.

---


### 244. [Look Before You Leap: Thermodynamic Arbitration of Parametric and Non-Parametric Knowledge in LLM Agents via Self-Regulating Memory Architectures](https://arxiv.org/abs/2610.05223)

**<font color=#1a73e8>作者：</font>** Akash Das, Ishan Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The architecture of modern LLMs consists of a profound cognitive polarization. LLMs possess implicit intuition encoded in their parameters, yet rely on a disconnected, explicit mechanism to access the outside world. Agentic frameworks have not bridged this gap; instead, models are often compelled into pathological "induced amnesia." Under the prevailing "Retrieve-Always" paradigm, agents must distrust their internal knowledge, making every user interaction a "tabula rasa" event that must be checked externally. This creates reflexive dependence that can be thermodynamically wasteful, cognitively fragile, and susceptible to irrelevant context. We propose a return to first principles, operationalizing the biological maxim "Look Before You Leap." We introduce MARTA (Metacognitive Adaptive Retrieval and Thought Architecture), a neuro-symbolic framework that bridges parametric and non-parametric knowledge. Rather than treating retrieval as mandatory, MARTA models it as a cost, taking the leap only when perceived internal inadequacy warrants external information. By allowing the agent to gauge the entropy of its own thoughts before acting, MARTA enables deliberative retrieval and uncertainty-aware decision making. Our approach suggests that giving agents the capacity for introspection can restore a more efficient balance between internal knowledge and external information.

---


### 245. [GFGE: Unifying Explainable AI Methods through an Interpretation Framework](https://arxiv.org/abs/2610.05225)

**<font color=#1a73e8>作者：</font>** Jinfeng Zhong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable artificial intelligence (XAI) encompasses methods that draw on different sources of information and address different explanatory needs. A common framework is needed to describe how this information becomes evidence and is communicated as an explanation for a particular recipient. We propose the General Framework for Generating Explanations (GFGE), grounded in interpretative frameworks and the complementary activities of \emph{sense-reading} and \emph{sense-giving}. Its conceptual foundation is the Interpret/Explain Schema (IES), which connects an analyst's interpretation of system evidence, the communication of a selected account, and the recipient's interpretation of that account. GFGE operationalises this schema through five roles: data interpretation, model interpretation, output interpretation, optional post-hoc analysis, and aggregation. A role-typed operation graph records method-specific dependencies, while evidence records retain the sources, assumptions, and limitations of explanatory claims. The explanatory question, audience, and context guide the procedure. We instantiate GFGE for attribution, surrogate, counterfactual, concept and prototype, intrinsic rule, argumentation, and language-model methods. These instantiations show how intrinsic, post-hoc, and hybrid workflows can be represented through the same roles while preserving their distinct evidential requirements. GFGE provides a common basis for analysing explanation workflows, tracing communicated claims to their evidence, and identifying unresolved explanatory dependencies.

---


### 246. [EMG-GPT: Predictive Pretraining on Residual-Quantized EMG Tokens for Hand Pose Estimation](https://arxiv.org/abs/2610.05235)

**<font color=#1a73e8>作者：</font>** Ettore Magni, Rolandos Alexandros Potamias, Stefanos Zafeiriou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surface electromyography (sEMG) is a low-power, cost-effective biosignal for hand-pose estimation and gesture classification. In this work, we examine whether self-supervised pretraining on sEMG can yield transferable representations for continuous hand-pose estimation. We introduce EMG-GPT, a causal transformer-based model that operates on discrete sEMG representations from a frozen residual vector quantization (RVQ) tokenizer and learns temporal dynamics through depth-autoregressive future-code prediction. The model combines within-frame integration with causal temporal modeling while preserving the geometry of the pretrained codebook. EMG-GPT shows competitive results in both Regression and Tracking tasks, supporting EMG-only pretraining as a viable approach for learning transferable sEMG representations.

---


### 247. [templar: agentic induction and evolution of standardized radiology reporting templates from large-scale clinical corpora](https://arxiv.org/abs/2610.05247)

**<font color=#1a73e8>作者：</font>** Xiaotian Hu, Mingxuan Liu, Zhonghan Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Structured radiology reporting mitigates the heterogeneity of free-text reports, yet its benefits depend on high-quality reporting templates. In practice, such templates are conventionally built through labor-intensive expert consensus and therefore vary across institutions and lag behind evolving clinical practice. Large language models (LLMs) enable automated template induction, but existing approaches remain limited: single-LLM induction is constrained by context length, and the corpus-scale method ASTAR produces a static, closed-corpus template without external grounding or downstream adaptation. To address these limitations, we propose TEMPLAR, a TEMPLate-centric Agentic framework for inducing and evolving standardized Radiology reporting templates from large-scale clinical corpora. TEMPLAR treats the template as a persistent central state maintained alongside two provenance-aware knowledge graphs, namely an anatomical graph that constrains template construction and a diagnostic graph that supports finding-to-diagnosis reasoning. Three agents operate on this state. The Induction Agent derives canonical clinical slots from anatomy-constrained Span-Triple atoms via dual-view similarity clustering; the Evolution Agent then assembles these slots into a hierarchical template and revises it under consistency constraints, external clinical evidence, and downstream structuring feedback; and the Clinical Agent applies the evolved template to report structuring, reconstruction, and diagnostic reasoning. Across four datasets, TEMPLAR outperforms ASTAR, three medical LLMs, and six general-purpose LLMs in coverage, information fidelity, and diagnostic fidelity, while achieving the highest or tied-highest LLM-rated template quality. Its fidelity advantages over ASTAR persist under cross-dataset transfer, and cumulative ablations support complementary contributions of its key components.

---


### 248. [ArticuTable: Generating Instance-Level Interactive Rigid-Articulated 3D Tabletop Scenes from a Single Image](https://arxiv.org/abs/2610.05249)

**<font color=#1a73e8>作者：</font>** Kai Lv, Yibo Yin, Lijun Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied agents benefit from 3D environments that combine visual fidelity to real-world observations with physical interactivity. Existing single-image tabletop reconstruction methods recover plausible scene geometry but typically represent objects as monolithic rigid bodies, limiting interaction to whole-object rigid motion and precluding executable part-level articulation. Meanwhile, recovering a scene layout consistent with the input view remains challenging because a single observation may admit multiple plausible pose-scale configurations. We present ArticuTable, a single-image 3D tabletop reconstruction framework that recovers both executable part-level articulation and an input-view-consistent scene layout. For object modeling, we introduce generation-robust articulation modeling (GRAM), which combines joint fitting guided by a multimodal large language model with semantic state reasoning to recover reliable joint parameters and valid motion ranges from imperfect monolithic proxy meshes, thereby converting them into executable articulated assets. For scene layout, we introduce progressive semantic-geometric scene registration (PSGSR), which progressively narrows the pose-scale search space under complementary metric, planar, and input-view constraints and resolves orientation ambiguity through structure-aware semantic correspondences, yielding a scene layout consistent with the input view. We further contribute ArticuTable-100, a curated collection of 100 simulation-ready tabletop scenes. Extensive evaluation, including a user study, demonstrates strong performance across visual fidelity, input-view consistency, articulation quality, physical plausibility, and simulation readiness.

---


### 249. [Loopy: Low-Bit Quantization Framework for Looped Language Models](https://arxiv.org/abs/2610.05265)

**<font color=#1a73e8>作者：</font>** Zeyu LI, Yipu ZHANG, Jintao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models provide a parameter-efficient way to scale iterative test-time computation by repeatedly executing a shared recurrent core. Post-training quantization (PTQ) can reduce the memory footprint and inference cost of looped language models, but errors introduced by a quantized shared core affect subsequent cores. Among PTQ methods, channel scaling and orthogonal rotations preserve the floating-point computation while producing representations with different quantization quality. We find that quantization configuration candidate rankings can change with recurrent depth, motivating configuration selection at the target deployment depth. However, evaluating every candidate over the full calibration set at this depth is costly. We therefore propose Loopy, a PTQ framework that formulates shared-core quantization through a recurrent-depth-aware objective, selecting shared low-bit representations by their final prediction loss at the target deployment depth. Channel scaling and orthogonal rotations parameterize the candidate representations. To approximately solve this selection problem efficiently, Loopy progressively allocates calibration windows to promising candidates while preserving complete target-depth execution, using only forward evaluations. Across eight settings, Loopy achieves the state-of-the-art results among different baselines. On Ouro-1.4B under W4A4, Loopy reduces LAMBADA perplexity by 36.5% relative to SpinQuant. Our code is available at this https URL.

---


### 250. [When and What to Prune? Stage-Aware Visual Token Pruning for Efficient VLA](https://arxiv.org/abs/2610.05273)

**<font color=#1a73e8>作者：</font>** Tianjun Shi, Haotian Xiong, Ziyu Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning is an effective way to accelerate vision-language models and is especially useful for vision-language-action (VLA) inference, where many visual tokens must be processed before predicting robot actions. Existing pruning methods usually estimate which tokens can be pruned based on attention scores or feature diversity, retaining tokens that are either highly attended or visually different from others. However, most of them use fixed pruning schedules, such as pruning once at a preset layer or pruning at uniformly spaced layers. Such schedules can be risky for VLA models, because the model may not know which visual regions matter for the action in early layers. Tokens that look unimportant at first may become useful after the model combines visual observations with the language instruction. In this work, we propose SAPrune, a training-free visual token pruning framework for efficient VLA inference. Instead of pruning at fixed layers, SAPrune uses a small calibration set to observe how action-to-visual attention changes across layers, and chooses pruning layers only after the attention pattern becomes more reliable. At each selected layer, SAPrune applies a dual-path pruning rule: one path protects strongly attended visual tokens from pruning, while the other prevents useful surrounding context from being discarded. Experiments on LIBERO, SIMPLER, and real-world robotic tasks show that SAPrune prunes 87.5% of visual tokens and achieves up to 1.718x inference speedup while maintaining competitive task success rates.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
