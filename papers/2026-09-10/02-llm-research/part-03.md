# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 101. [Beyond Retraining-Free MoE Compression: A Cost-Normalized Study of Post-Compression Adjustment](https://arxiv.org/abs/2609.06076)

**<font color=#1a73e8>作者：</font>** Sieun Hyeon, Jaeyoung Do  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retraining-free MoE compression reduces deployment memory by pruning or merging experts, but often treats the compressed checkpoint as the final artifact. We argue that this view is incomplete: compressed MoE checkpoints are better understood as compressed initializations that benefit from a tiny post-compression adjustment stage. Across two MoE LLM backbones, four pruning/merging methods, three expert-retention ratios, and 28 benchmarks, we compare LM fine-tuning and teacher-based KD under matched small-data budgets and measured GPU costs. Using only 3,000 C4 examples and a single epoch of adjustment, Full FT recovers 37.3% of the original-to-compressed performance gap on average. Moreover, LM fine-tuning is more cost-effective than standard token-level KD, and full-parameter adjustment gives the strongest cost--recovery trade-off among the tested scopes. These results suggest that retraining-free compression should be paired with small post-compression adjustment to recover a substantial portion of the performance lost during compression.

---


### 102. [LayerRoute: Action-Conditioned Mixture-of-Layers Routing for Vision-Language-Action Policies](https://arxiv.org/abs/2609.06079)

**<font color=#1a73e8>作者：</font>** Zheng Lu, Haoran Liao, Wanqi Zhong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) policies leverage pretrained vision-language models (VLMs) to guide action generation for robot control. VLMs provide hierarchical visual-semantic representations that evolve across layers, from local visual geometry to abstract, language-aligned semantics; different manipulation tasks may therefore require different mixtures of layer representations. Meanwhile, the action module maintains intermediate representations that evolve throughout action computation and may provide useful information for subsequent decisions. However, existing VLA interfaces offer limited flexibility in representation access: VLM information is exposed through fixed layer assignments for each action layer, while intermediate action states are only propagated implicitly through residual streams without explicit reuse. We introduce LayerRoute, an action-conditioned representation routing interface that enables adaptive access to VLM layers and action representations. The Layer Mixture Router dynamically forms mixtures of cached VLM representations, while Action-State Reread reuses earlier action representations. Across diverse simulation and real-world benchmarks, LayerRoute consistently improves StarVLA-$\pi$ and $\pi_{0.5}$, achieving up to 7.2 gains on LIBERO Long with only 0.31% / 3.87% additional parameters. Ablation studies validate the benefit of action-conditioned layer routing, while routing analyses reveal structured allocation patterns across action layers and task settings.

---


### 103. [PhenoBench: Mapping What a Deeply Phenotyped Human Cohort Can Tell Us](https://arxiv.org/abs/2609.06080)

**<font color=#1a73e8>作者：</font>** Gal Sapir, Alon Diament, Adva Wolf 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deeply phenotyped cohorts combine clinical, imaging, molecular, and wearable observations across timescales from seconds to years. This breadth can reveal which measurements inform which health-related questions, but heterogeneous analyses are not directly comparable. We present PhenoBench, an executable benchmark built around the Human Phenotype Project, in which more than 13,000 participants have completed the initial visit. Each question fixes the target, eligible population, timing, and allowed information; its evaluation contract specifies the split, metric, baseline, and claim boundary. The benchmark defines 90 clinically grounded tasks across 15 domains and 26 input modalities. Measurements showed question- and representation-dependent predictive value, including positive, near-zero, and negative changes in held-out performance relative to matched baselines. We used PhenoBench to evaluate emerging tabular foundation models across 160 matched regression comparisons spanning 52 tasks. These models ranked above standard task-specific models in aggregate but, averaged across the three pretrained models within each cell, improved on ridge by a median of only 0.004 $R^2$ (95% CI, 0.002--0.006). We then used the same cohort data and evaluation contracts to evaluate 14 language models, collectively covering 40 tasks spanning phenotype recovery, classification, follow-up forecasting, and participant ordering. Without cohort-specific fitting, language models made informative predictions on some tasks, but showed task-specific capability gaps, shared failures of scale, and rarely surpassed models fitted on the same fields. PhenoBench turns a multimodal longitudinal cohort into a versioned, auditable evaluation system where new questions, measurements, and models can be added without redefining existing comparisons.

---


### 104. [Flawed but Memorable: Student Critical Reception of Interest-Personalized GenAI Analogies in Computing Education](https://arxiv.org/abs/2609.06095)

**<font color=#1a73e8>作者：</font>** Seth Bernstein, Naaz Sibia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Motivation: Undergraduate computing students increasingly turn to generative AI (GenAI) tools to understand abstract concepts through analogies. Analogies compare an unfamiliar concept to something familiar, but judging whether the comparison holds requires knowledge of both. GenAI may also embed assumptions about who the learner is. GenAI education research centers on output correctness, leaving students' critical reception of analogies largely unexamined.
Method: We investigate how students evaluate the accuracy, appropriateness, and assumptions in GenAI-generated analogies, and their perceptions of interest-personalized versus generic technical explanations. Ten students with CS2 experience participated in a pre-survey, a think-aloud task with linked-list and recursion explanations, and a semi-structured interview grounded in the Paul-Elder framework. They judged accuracy, clarity, engagement, and trust separately.
Results: Most participants described interest-personalized analogies as more engaging or memorable than generic technical explanations, while trust was mixed. Some trusted the tailored analogies more; others scrutinized them more closely or distrusted the tailoring. Participants with deep source-domain knowledge identified structural flaws requiring that knowledge to recognize. Because personalization and explanation format differed together, these findings do not isolate an effect of personalization alone.
Implications: A familiar source flips the student's role. On the concept they are still learners, but on the familiar source they are the expert, and that is the position from which an analogy can be judged. We call this two-sided analogy auditing. GenAI systems should ask what students know, not just what interests them, and treat a flawed analogy as something to inspect and fix rather than accept.

---


### 105. [VERPO: Verified Evidence Regularized Policy Optimization](https://arxiv.org/abs/2609.06100)

**<font color=#1a73e8>作者：</font>** Haijiang Li, Chengyu Lv, Yi Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verifiable outcome rewards guide language-model post-training, but sequence-level advantages do not identify which token-level decisions should be preserved or revised. Evidence-conditioned Teachers provide denser supervision by replaying sampled trajectories with privileged feedback. Yet indiscriminate imitation risks transferring formatting or reasoning-style shifts that do not support task success. We introduce VERPO, a Verified Evidence Regularized Policy Optimization framework that treats evidence as a proposal for policy correction while retaining the outcome objective. It separates evidence-free reference restoration from signed token-level evidence corrections. Fisher Evidence Contrast attenuates corrections along an estimated evidence-presence direction. A stopped token-wise ZPD controller scales acceptance according to local reward alignment and Fisher movement cost, while the reference channel remains independent of acceptance. Across five scientific-reasoning and tool-use tasks, the best variant on each backbone exceeds the strongest compared baseline in average score. The averages rise from 0.6826 to 0.6857 on Qwen3-4B, from 0.6895 to 0.7058 on Qwen3-8B, and from 0.4751 to 0.5657 on Llama-3.2-1B.

---


### 106. [DataFlex-RL: An Evaluation Platform for RLVR Data Policies](https://arxiv.org/abs/2609.06107)

**<font color=#1a73e8>作者：</font>** Hao Liang, Mingrui Chen, Hengyi Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data policies for reinforcement learning with verifiable rewards (RLVR) determine which rollouts are used, how strongly they are weighted, and which domains contribute to subsequent training batches. We introduce DataFlex-RL, an evaluation platform for comparing these choices under a common GRPO recipe. Our primary experiment evaluates 13 configurations across 12 matched seeds using Qwen2.5-7B-Base and 12 mathematics, logic, and science benchmarks. Uniform GRPO improves the domain-balanced average accuracy by 7.76 percentage points over the untrained checkpoint. None of the eight rollout-selection or reweighting methods achieves a paired 95% confidence interval that excludes zero relative to uniform sampling, and none of the three adaptive mixtures outperforms a fixed equal mixture at the same level of precision. A corrected 12-seed extension on Llama-3.1-8B-Base places the additional methods on the same score scale as the original controls, but does not reveal a consistent winner in terms of observed mean performance. We also quantify evaluation sensitivity by rescoring nine Qwen2.5-7B-Instruct runs using a math-heavy six-benchmark summary, consisting of five mathematics benchmarks and GPQA-Diamond but no logic benchmark, and comparing it with the domain-balanced 12-benchmark summary. The resulting rankings are negatively correlated, with a correlation coefficient of -0.33, whereas summaries that retain all 12 benchmarks largely agree. Across the controlled settings studied here, changing the data policy measurably changes the training process but does not produce a reproducible improvement over uniform training.

---


### 107. [MM-SVGEdit: A Multimodal-Driven SVG Editing for UI Design](https://arxiv.org/abs/2609.06116)

**<font color=#1a73e8>作者：</font>** Shibo Yang, Yuqing Gao, Zipeng Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In the field of UI design, Scalable Vector Graphics (SVG) is widely used as a design medium. However, traditional SVG editing techniques have high entry barriers and require cumbersome manual iteration, while LLM-based editing solutions suffer from low accuracy and poor user controllability. To address these issues, we propose MM-SVGEdit, a multimodal-driven SVG editing approach that integrates traditional SVG editing and LLM-based methods. We introduce a two-stage strategy in which visual grounding is followed by modification. Both stages support two interaction modalities: natural language instructions and direct manipulation (mouse and keyboard). We trained and evaluated MM-SVGEdit on a self-constructed dataset of 14,476 question-answer pairs generated from UIs, covering 11 types of editing operations on both single and multiple UI targets. The results show that MM-SVGEdit improves SVG editing accuracy, efficiency, and user-perceived control while reducing token consumption and response time.

---


### 108. [STQA: A Benchmark for Stock-Focused Tabular Question Answering over Historical and Forecasted Data](https://arxiv.org/abs/2609.06117)

**<font color=#1a73e8>作者：</font>** Baoxu An, Wenmian Yang, Zhensheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stock market analysis inherently requires composite reasoning over historical records and future projections, yet existing benchmarks remain fragmented across isolated tasks. We introduce STQA (Stock-focused Tabular Question Answering), an end-to-end benchmark designed to systematically evaluate natural-language question answering over historical data, numerical forecasts, and forecast-based reasoning. Built on a large-scale financial dataset, STQA covers 4,417 stocks and contains 31,400 question-answer pairs derived from expert-crafted templates, accompanied by fine-grained intent and slot annotations. To operationalize this benchmark, we present SQFRS (Stock Query-Forecast-Reasoning System), an agent-based unified framework that orchestrates SQL retrieval and time-series forecasting tools. Experiments demonstrate that while current large language models perform well on historical queries, forecast-based reasoning poses a substantial challenge, revealing critical bottlenecks in tool coordination and reasoning under uncertainty. The dataset and code are available at this https URL. STQA thus serves as a rigorous testbed for future research on trustworthy, tool-augmented financial agents.

---


### 109. [Substrate-Portable Execution for Production LLM Workflows](https://arxiv.org/abs/2609.06128)

**<font color=#1a73e8>作者：</font>** Tarun Gopinath, Atul Kulkarni, Vijay Rajakumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production LLM agents execute tool-calling loops, retrieval chains, and compositional workflows in multiple modes, yet execution semantics are often coupled to one runtime. We encountered this portability problem in Rufus, a conversational AI assistant with a large tool catalog that serves millions of Amazon customers. Rufus supports real-time serving, asynchronous background tasks, and high-volume batch workloads such as evaluation and content pregeneration. Each mode has distinct service-level objectives and typically uses a separate runtime. Reusing streaming orchestration makes asynchronous and batch workloads blocking and prevents use of batch inference APIs, which offer a 50 percent discount at published prices. We present a binding-adaptive agent execution platform that separates workflow definition from execution substrate. Developers define a workflow once as a typed dataflow graph. The platform compiles the graph to in-process streaming for real-time serving, durable AWS SWF orchestration for asynchronous execution, or distributed Apache Flink stream processing for batch inference. No workflow code changes are required. LLM inference is represented as a suspendable graph node whose behavior depends on the substrate: streaming delivery online, durable retry asynchronously, and batched submission offline. We validated dozens of production agent configurations across five orchestration patterns: single-inference RAG, iterative ReAct, compositional PreAct, conditional routing, and multi-agent deep research. Across all three bindings, we found no detectable difference in output quality. Batch execution reduced per-query inference cost in line with published batch API pricing while operating alongside the streaming path at production scale.

---


### 110. [Protocol Compression Changes Which Party Pays: Bilateral Cost in Cross-Organization LLM Agent Communication](https://arxiv.org/abs/2609.06129)

**<font color=#1a73e8>作者：</font>** Janghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents that talk across organizations exchange long messages billed by the token. A shorter notation therefore looks like a saving that costs nothing but an agreement to use it. Recent work reports the saving is conditional. Compressed notation can instead raise total tokens by 8% to 11% over a JSON baseline, when parsing failures force extra model calls. That is measured for one payer. Between two organizations neither side can install a decoder at the other end, and each pays under its own tokenizer, price, and cache state. We measure both sides. A preregistered token-level study covered 198 content-matched item pairs across six vendors, for 2,376 native-usage cells. We then overlay an English baseline, runtime schema negotiation followed by compression, and injected-schema compression on a two-party procurement bargain with an exactly enumerated feasible set. The overlay covers 1,053 completed dialogues of a 1,215-cell grid across 3 model pairs, plus a 405-dialogue rerun of the negotiated condition. Compression amplifies cross-vendor cost dispersion by a factor of 1.078, with a 95% CI of [1.066, 1.091], and two vendor pairs reverse which endpoint is cheaper. Runtime negotiation succeeds as a protocol and fails as a bargain. The parties agree a schema in 121 of 135 headline dialogues, none of them the schema we would have supplied. They settle the task in only 9 of those dialogues, and they reach impasse in 106 of them. The negotiated sessions average 10.8 turns against 17.6, and cost 52% of the English total because sessions end sooner, not because the handshake is repaid. Break-even horizons run from 20 to 70 turns, the low end only under the conditional accounting, and all of them lie above every observed English session. On one cross-vendor pair both parties keep about half their cost. On the other the receiving party pays more at a high cache-hit rate.

---


### 111. [What the Window Does Not Contain: Auditing Provenance in a Document-Grounded Instability Benchmark](https://arxiv.org/abs/2609.06147)

**<font color=#1a73e8>作者：</font>** Seyed Mosayeb Alam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ask a language model the same question about the same document twenty times, and it sometimes returns two different answers. We built Probity, a benchmark of 60 tasks and 470 items from real venture-financing filings, to measure how often this happens. Then we audited our own corpus and found a defect any excerpt-built benchmark can carry: items whose evidence is missing from the window of text the model is shown. The audit flags 36 items and separates two failures a single flag would conflate: evidence genuinely absent from the window and answers that must be computed from numbers the window does supply. Flagged items change their answers far more often, wobbling at 0.255 against 0.087 on the 427 clean items, and excluding them cuts apparent cross-model agreement by about a fifth. Before testing whether the missing evidence explains the instability, we registered a prediction: re-cut each window to hold its evidence, and instability should fall below a set threshold. It failed: the repair moved wobble by 0.058, with an interval containing zero. We report the association as correlational. Almost all measurements sit where instability cannot show, which bounds what a corpus built for accuracy can say about stability. We release the corpus, all 112,800 raw responses, and the audit as a runnable check for any document benchmark.

---


### 112. [SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs](https://arxiv.org/abs/2609.06149)

**<font color=#1a73e8>作者：</font>** Hanna Kim, Jian Cui, Minkyoo Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Script-based malware remains a prevalent attack technique. These scripts often contain indicators of compromise (IOCs) that provide actionable threat intelligence. However, statically recovering such indicators is challenging, as relevant values may be dispersed or transformed within code. Although large language models (LLMs) have shown promise in security analysis, their ability to recover IOCs from malicious scripts remains underexplored.
We present SCRIPTIOC-BENCH, a benchmark for measuring static IOC extraction capability on real-world malicious scripts. The benchmark comprises 634 manually verified JavaScript, PowerShell, and VBScript malware samples covering four IOC types (URLs, domains, IP addresses, and filesystem artifacts). We further stratify ground-truth IOCs by recovery level, distinguishing directly exposed indicators from those requiring decoding or reconstruction. Using this benchmark, we evaluate a broad range of proprietary and open-weight LLMs and show that IOC recovery without execution remains challenging across model scales: the strongest model reaches only 65.4 F1. To characterize how recovery fails, we introduce a false-positive taxonomy and use it to compare the error profiles of the evaluated models. We further study two mitigations on a small open-weight model, deterministic string utilities and task-specific adaptation, finding that they provide complementary recovery gains, raise precision, and shift errors toward sample-grounded mismatches.

---


### 113. [All for 1-Bit: Towards Genuine 1-Bit Post-Training Quantization for LLMs](https://arxiv.org/abs/2609.06161)

**<font color=#1a73e8>作者：</font>** Zhixiong Zhao, Zukang Xu, Guangyu Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable progress, yet their massive storage and memory-bandwidth demands still hinder efficient deployment. Weight binarization is a promising solution, but existing binarization-based post-training quantization (PTQ) methods usually far exceed the nominal 1-bit storage target due to hidden overhead. To address this gap, we propose All for 1-Bit (AF1), a genuine 1-bit PTQ framework for LLMs. AF1 comprises two complementary components: (1) Null-space-Aware Binary Factorization (NABF) for improving binary reconstruction through Hessian-aware surrogate reparameterization, null-space-aware binary factorization, and scale-only global reconstruction; and (2) Hierarchical Shapley Allocation (HiSA) for assigning structural capacity using hierarchical Shapley sensitivity. Together, they preserve model accuracy under a strict 1.0-BPW budget in the PTQ setting. Experiments on LLaMA, Qwen, and Gemma families show that AF1 consistently outperforms existing binarization-based PTQ methods in perplexity and zero-shot accuracy. Compared with BF16, AF1 achieves an average 2.5 times inference speedup and over 90% memory reduction across evaluated models, providing a practical path toward deployable genuine 1-bit compression for LLMs. The code for reproducibility is available at this https URL.

---


### 114. [MVFA: A Multi-View Text-Guided Multimodal Fusion LLM Adapter for Sentiment Analysis and Emotion Recognition](https://arxiv.org/abs/2609.06188)

**<font color=#1a73e8>作者：</font>** Pengfei Shao, Jisheng Dang, Jiawen Fang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis and emotion recognition in conversations demand effective modeling of heterogeneous interactions across textual, acoustic, and visual modalities. Although large language models (LLMs) offer powerful language understanding, adapting them to multimodal affective computing remains challenging: full-model fine-tuning is computationally prohibitive, while many existing lightweight adapters fail to preserve rich textual cues during cross-modal fusion. To address these limitations, we propose the multi-view text-guided multimodal fusion adapter (MVFA), a parameter-efficient framework that augments frozen LLMs with strong multimodal reasoning capability. MVFA first constructs complementary text views via max pooling, mean pooling, and attention pooling; these views then guide cross-modal interactions with audio and visual features. The fused multimodal representations are subsequently compressed into a compact set of learnable pseudo-tokens through an Enhanced Q-Former Fusion Module. Using ChatGLM3-6B-base as the primary backbone, we further validate MVFA on LLaMA2-7B and Qwen3-8B to examine its portability across multiple frozen LLM backbones. MVFA is evaluated on three challenging datasets: CH-SIMS V2.0, MELD, and CHERMA. Experimental results demonstrate that MVFA achieves state-of-the-art performance on key metrics while updating only a small fraction of parameters. Specifically, it attains 84.62\% Acc2 and 84.59\% F1 on CH-SIMS V2.0, 67.36\% Acc and 66.03\% WF1 on MELD, and 74.66\% Acc on CHERMA. These findings establish multi-view text-guided fusion as an effective and scalable paradigm for parameter-efficient multimodal LLM adaptation in affective computing. The code is publicly available at this https URL.

---


### 115. [One Perturbation Is Not Enough: Identifiability and Blind Baselines for Behavioral AI Evaluation](https://arxiv.org/abs/2609.06190)

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Mariam Sohail, Ahmed Abdala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Behavioral evaluations perturb an input and read the induced change in the output in order to certify that a system uses that input. We show that the number of perturbations such a certificate requires is fixed, and that reporting a single perturbation cannot supply it. Where a response ratio is a property of the policy rather than of the test items, the behavioral record is a linear measurement of an exponent vector recording how much the output depends on each input, so perturbations identify input use exactly when their logarithms span the input space. At least $n$ are needed for $n$ inputs, an incomplete design confuses precisely the policies differing along the kernel of its design matrix, and sharpening a perturbation never substitutes for adding an independent one. We also derive in closed form the score such a test awards a policy that reads nothing, which is far from zero and which none of the probes we survey reports. Instantiating this where the correct response is fixed by dimensional analysis, we run a complete identifying set of three perturbations on three vision--language models reporting a physical quantity from video. All three score far below their own blind bound rather than above it, because each defaults to one of a small set of round calibration values that never matches what the scale asserts; none moves its relabeling response by a single exponent, and none is separable from the same model instructed to ignore the video.

---


### 116. [SCIRIGOR:Evaluating Open-Ended Scientific Analysis Beyond Final Scores](https://arxiv.org/abs/2609.06192)

**<font color=#1a73e8>作者：</font>** Bowen Liu, Shuo Nie, Bodong Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific coding agents produce interdependent code, results, figures, and claims, yet evaluating final
outputs alone does not establish whether their conclusions are scientifically supported. We formulate
evidence-grounded multimodal scientific analysis, requiring agents to produce executable analyses and claims
supported by results and visualizations from the same run. We introduce SciRIGOR, an evaluation framework and
benchmark comprising 100 cases from scientific articles across six domains and 17 subfields. The framework
reconstructs typed evidence graphs, separates artifact fidelity from relational validity, and scores complete
claim-support paths while localizing the earliest unsupported relation. Source-grounded alternative paths
accommodate scientifically equivalent analyses and visualizations. We evaluate 11 agent/model configurations.
On full-benchmark runs, claims agree with faithful and unfaithful results at nearly identical rates (91.8%
versus 91.0%). Yet no system exceeds 62.6% on the soft evidence-chain score or 18.0% strict whole-chain
success. These findings show that internal coherence does not establish scientific correctness: evaluation
must verify support along the complete data-to-claim path.

---


### 117. [From Gaze to Meaning: A Training-Free AI Agent for Unified Grounding and Explanation](https://arxiv.org/abs/2609.06208)

**<font color=#1a73e8>作者：</font>** Shayan Nasiriboukani, Sara Atito, Mohammad Nezamipour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human attention is fundamental for scene interpretation, yet existing approaches often rely on heavily trained models that lack interpretability. Prior methods struggle to jointly reason about gaze targets, attended objects, and visual grounding without extensive supervision. To the best of our knowledge, this work introduces the first training-free Gaze Target Agent (GTA) for gaze-guided reasoning across tasks such as gaze target prediction, attention localization, and object identification. This is achieved by leveraging pretrained vision-language models, augmenting them with visually guided prompts, and employing a memory-based retrieval strategy for high-uncertainty samples to improve performance without additional training. We evaluate our approach using both quantitative metrics and qualitative results. Quantitatively, our method achieves state of the art performance on the GazeFollow and GazeHOI benchmarks. Qualitatively, our agent provides detailed semantic predictions, predicts the correct targets even when ground truth labels are wrong, and remains flexible without vocabulary constraints.

---


### 118. [SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition](https://arxiv.org/abs/2609.06212)

**<font color=#1a73e8>作者：</font>** Jingzhuo Wu, Jiajun Zhang, Liu Yi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have achieved remarkable capabilities in generating language teaching slides. However, a critical mismatch persists between visual polish and actual instructional effectiveness. To address this gap, we introduce SLATE (Slide-based Learning Assessment for Teaching Effectiveness), the first benchmark that evaluates AI-generated language teaching slides through instructional effectiveness and learner knowledge acquisition. SLATE transforms linguistics olympiad puzzles from low-resource languages with negligible web presence into 90 standardized instructional units comprising 1,133 assessable items, paired with a structured course outline and matched near- and far-transfer test sets. This pretest-posttest design eliminates pretrained knowledge leakage, ensuring gains reflect learning rather than prior recall. Using VLMs as scalable learner proxies and directionally supported by a three-system human pilot, our results show that content validity exhibits a weak association with learning gain, while pedagogical design exhibits a robust positive association. Moreover, most systems show a significant gap between near- and far-transfer accuracy, and even frontier models can produce negative learning gains. SLATE reveals a dissociation between artifact quality and instructional effectiveness, calling for a paradigm shift in how generative teaching systems are built, evaluated, and deployed.

---


### 119. [Scratchy: Visual-Scratchpad Multimodal Reasoning for Cryptographic Proof Generation in EasyCrypt](https://arxiv.org/abs/2609.06226)

**<font color=#1a73e8>作者：</font>** Yupeng Ren, Zhaoxuan Li, Rui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently made substantial progress in formal proof generation, yet presenting distinctive challenges in cryptographic area. Computational security arguments posit that a valid proof must coordinate probability, adversarial games, invariants, assumptions and bounds, which can be provided by a machine-checked framework named EasyCrypt. Although all objects may appear in available context, LLMs still struggle because proof-theoretic dependencies are typically implicit in a linear representation and distributed across multiple programs. So, this paper presents Scratchy, a visual-scratchpad approach that exposes these dependencies for multimodal generation. Given the natural-language security description, with formal context and target propositions, the proof objects can be normalized into a typed proof-relation graph. Then a structure-preserving visual compiler transforms the graph into the formula-rich visual proof state that guides a multimodal model in generating the EasyCrypt proof. Also, the Scratchy-eval, a 114-task dataset derived from reliable official EasyCrypt files, has been introduced. It contains 64 security-form proof generations and 50 multiple-choice knowledge tests. After a series of evaluations, covering semantic grounding, relational invariants, and game reductions, classical LLMs like GPT-5.6-Sol and Claude-Opus-5 have gained a clear advantage from Scratchy's structured visual proof states. This contrast suggests that explicit proof structure can make the improvement and multimodal proof-state representation as a promising direction for computer-aided cryptography.

---


### 120. [VDiff-Bench: A Challenging Benchmark for Fine-Grained Image Difference Identification](https://arxiv.org/abs/2609.06245)

**<font color=#1a73e8>作者：</font>** Yixin Wan, Tianle Zheng, Kai-Wei Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) perform strongly on general visual understanding tasks such as visual question answering, yet they often struggle with a basic comparative skill: identifying what has changed between two similar images. We introduce VDiff-Bench, a challenging multiple-choice benchmark for fine-grained Image Difference Identification. VDiff-Bench contains 1,756 four-way questions over image pairs and covers 10 change categories: position, motion, regional image color, overall image color, appearance/disappearance, noise/resolution, texture, substitution/size, OCR/text, and illumination. Each question corresponds to two image inputs with 4 choices: the true difference, two hard negative descriptions, and a "no difference" distractor. To make the task challenging, we specifically curate ground-truth-conditioned negatives that require models to distinguish the actual change from nearby semantic alternatives. Experiments with 11 state-of-the-art open- and closed-source MLLMs show that fine-grained visual comparison remains brittle: models exhibit uneven performance across sources and change categories, with persistent failures on subtle low-level changes like noises and textures. For instance, three 7-8B-scale open-source MLLMs score 52.5-70.6% on semantic changes but only 8.7-33.3% on low-level changes like noise and texture, falsely assuming no changes between two image inputs. Surprisingly, despite strong performance of other closed-source commercial models, Grok 4.3 demonstrate remarkable performance drop on identifying noise and texture differences between images, falling significantly behind large open-source models like Kimi K2.5 and K3. Overall, VDiff-Bench provides a targeted diagnostic for evaluating comparative visual understanding in MLLMs, exposing failures that are not captured by standard single-image vision-language tasks.

---


### 121. [It is Not Yet Another Tool: Creating and Deploying an Agentic AI Companion in a Security Operations Center](https://arxiv.org/abs/2609.06250)

**<font color=#1a73e8>作者：</font>** Kritan Banstola, Faayed Al Faisal, Duy Dao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security Operations Centers (SOCs) process large amounts of tickets, most of which are low-interest events not worthy of further investigation. The repetitive nature of this task and similarity of the vast amounts of tickets make it a prime candidate for generative AI-based automation. We created and deployed an agentic AI companion utilizing large language models through fieldwork within a SOC for over one year. The design of the SOC AI companion was driven by researchers' participation and interactions within the SOC's daily work. SOC analysts were invited to use it during the last four months of the fieldwork. We analyzed the analysts' usage of the companion and found that in more than 90% of the cases the companion's outputs were reused by analysts in the ticket's closing report. Our results showed that when designed "in the trenches" with the intended users, a SOC AI companion can go beyond being yet another tool, but rather a system that co-evolves with its human users as it traverses through the various types of workloads. Analysts naturally started to shape the AI companion's behaviors to fit their particular needs. Our data show that the more human analysts shape the AI companion's behaviors, the more they become comfortable trusting the output from the AI system, resulting in improved productivity.

---


### 122. [MobileVLA-R1 2.0: RL-Enhanced Reasoning for Mobile Robot Control](https://arxiv.org/abs/2609.06251)

**<font color=#1a73e8>作者：</font>** Ting Huang, Yue Huang, Zeyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding natural-language instructions into reliable and executable actions remains a fundamental challenge for vision-language-action (VLA) systems on mobile robots, due to the persistent gap between high-level semantic reasoning and low-level locomotion and manipulation control. Existing approaches often rely on implicit reasoning or monolithic action prediction, making it difficult to maintain coherent long-horizon decision making while producing precise and adaptable robot actions. To address this challenge, we propose MobileVLA-R1 2.0, an RL-enhanced VLA framework that explicitly couples structured embodied reasoning with executable mobile robot control. The framework learns multi-granularity reasoning over embodied trajectories through supervised Chain-of-Thought (CoT) alignment and reinforcement learning, improving reasoning-to-action consistency beyond purely behavioral supervision. To support both locomotion and manipulation, we further introduce a reasoning-conditioned action decoder that maps multimodal reasoning representations to task-level action targets, which are subsequently translated into embodiment-specific commands by robot controllers. This design provides a unified perception-reasoning-action interface while decoupling high-level action generation from robot-specific actuation. We conduct extensive evaluations on language-guided navigation, quadruped control, and humanoid mobile manipulation, covering VLN-CE, QUARD, and real-world deployments on Unitree Go2 and G1 robots. MobileVLA-R1 2.0 consistently outperforms strong VLA baselines, achieving an average 1.6 point improvement in SR on VLN-CE and a 10.0 point improvement in full-task success on real-world G1 mobile manipulation tasks over MobileVLA-R1, while demonstrating robust long-horizon instruction following and closed-loop execution across different robotic platforms.

---


### 123. [Beyond the Flag: Clinical Framing Closes the Moderation Gap in Suicide Risk Measurement](https://arxiv.org/abs/2609.06263)

**<font color=#1a73e8>作者：</font>** Shreyas Krishnan, Gun Ahn, Jungjin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Moderation APIs are built to flag policy-violating content, not to measure graded clinical risk. But a platform's duty does not end at detection: the response owed to passive distress differs sharply from the response owed to active planning with means access, and emerging regulation (e.g., California Senate Bill 243) is turning that distinction into a compliance requirement. We therefore ask how well deployed safety signals recover clinically meaningful severity. We release a benchmark of 516 r/SuicideWatch posts rated by a licensed psychiatrist on a four-level ordinal schema (Indicator, Ideation, Behavior, Attempt) grounded in the Columbia Suicide Severity Rating Scale, and evaluate moderation APIs, prompted LLMs, and supervised baselines under seven ordinal-aware metrics. Three findings. Vendor moderation APIs separate low- from high-severity posts well (0.860 high-risk F1) but measure severity poorly (0.395 macro F1), systematically over-predicting the most severe category. Clinically grounded zero-shot prompting recovers much of that gap (0.562 macro F1), and expert-authored framing (not fine-tuning, added reasoning, or naive multi-agent aggregation) is the effective lever. The value of reasoning depends on register: it hurts on long, noisy Reddit posts and helps on short, clinician-authored statements. We argue graded severity, not a binary flag, is what a proportionate duty of care requires, and release our evaluation framework to support that measurement.

---


### 124. [Adaptive Ecological Momentary Assessment with a Hybrid Language Model: Formative Expert Review and Retrospective Evaluation](https://arxiv.org/abs/2609.06269)

**<font color=#1a73e8>作者：</font>** Arash Ahmadi, Dingjing Shi, Yaser M. Banad  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ecological momentary assessment (EMA) measures experience in daily life, but fixed questionnaires and schedules collect information of uneven value and can interrupt participants. We present and retrospectively evaluate EMA-E4B, a hybrid framework for question selection and prompt timing. Separate ridge models propose an item set and delay; a supervised Gemma 4 E4B language layer produces the final structured response and explanation. Evaluation distinguishes proxy action performance, output conformity, and formative judgments of response quality. The data contain 4,372 records from 79 participants and yield 3,516 sequential cases under a participant separated split. One involved domain expert preferred the complete hybrid response in 15 of 20 decisive comparisons, with two ties among 22 reviews. On 75 reused development cases, hybrid question utility and timing similarity were 0.832 and 0.818; the head alone reached 0.852 and 0.818. A separate 60 case comparison with untouched E4B under the same head gave action differences of -0.0031 and -0.0105. Thus, the language layer produced structured responses with action scores comparable to or slightly below the reference configurations, while the expert feedback favored the complete hybrid response. These observations establish a concrete, inspectable framework and clarify the distinct roles of action scoring and response review. Repeated adaptive administration and practical effects on measurement and participant burden remain future research.

---


### 125. [Steering Geometry: Validating Human Value Geometry in LLM Steering Space](https://arxiv.org/abs/2609.06289)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Abootorabi, Armin Saghafian, Ali Bazshoushtari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in alignment-sensitive contexts, activation steering has emerged as a lightweight, inference-time alternative to fine-tuning methods (e.g., RLHF, DPO) for behavioral control. However, existing work typically validates steering on isolated behaviors, leaving it unclear whether steering vectors encode coherent semantic structure or merely exploit behavior-specific shortcuts. We investigate whether the latent geometry of LLM steering vectors reflects theory-specified structure in human values and morality. Using Schwartz's Theory of Basic Human Values as our primary fine-grained framework, we introduce a 26K-sample benchmark covering 20 human values and analyze distribution-driven methods (e.g., CAA, SphericalSteer, ODESteer) and behavior-centric approaches (e.g., COLD-Steer, BiPO) across diverse model families and sizes. We find that distribution-driven methods recover human value topologies aligned with theoretical predictions (Spearman $\rho$ up to 0.51, $p < 10^{-13}$). In contrast, behavior-centric methods achieve comparable steering performance but show little correlation with the expected value geometry. Geometric fidelity improves with model scale but drops after instruction tuning. Finally, better geometric alignment also leads to more human-consistent transfer across values: steering one value correctly lifts compatible values and suppresses opposing ones. Code and data are available at: this https URL.

---


### 126. [Reliability, validity, and diagnostic evidence for multi-model LLM short-answer scoring](https://arxiv.org/abs/2609.06315)

**<font color=#1a73e8>作者：</font>** Chunyi Zhao, Chao Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used or proposed for educational scoring, but single-model and single-run evaluations provide limited evidence for assessment use. Short-answer scoring requires evidence about reliability, validity, severity, diagnostic value, and failure cases. This study evaluated repeated multi-model OCG-PRES guided LLM scoring for short-answer assessment. The analysis used 996 SciEntsBank responses. GPT, DeepSeek, and Qianwen each scored every response across three independent runs using five OCG-PRES dimensions: concept coverage, relation accuracy, reasoning completeness, contradiction control, and domain relevance. Scores were evaluated against official binary and five-category labels and compared with non-LLM baselines based on answer length, Jaccard keyword overlap, TF-IDF cosine similarity, and a combined traditional logistic model. Repeated-run reliability was high for all models, with ICC(3,k) = .977 for GPT, .992 for DeepSeek, and .981 for Qianwen. DeepSeek was the most stable across runs. GPT showed the strongest official-label alignment by AUC (.909), while Qianwen was stricter, with higher precision but lower recall under the fixed threshold = 3.0 rule. OCG-PRES scores followed expected diagnostic patterns across five official categories and outperformed all non-LLM baselines in AUC and F1. Repeated multi-model OCG-PRES scoring provides reliability, validity, and diagnostic evidence for LLM-assisted short-answer scoring. The findings support cautious, evidence-based use as a scoring support tool rather than a replacement for human judgement.

---


### 127. [A Ticket from Marginals to Joints: Coupled-Noise Distillation for One-Step Block Generation in Diffusion Language Models](https://arxiv.org/abs/2609.06324)

**<font color=#1a73e8>作者：</font>** Lin Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models commit one token per forward pass; diffusion language models commit a block of tokens over several steps. We ask whether a block can be committed in a single forward pass. We study this with a noise-conditioned masked denoiser: a data-independent Gaussian noise field is added to the mask embeddings so that, in principle, each sampled field selects one joint mode of the block. The established way of training such a model is to sample several fields per example and let them compete for the data, by winner-take-all or importance weighting. This gives the noise only coarse control: in our experiments, the information it carries grows roughly with the logarithm of the number of competing fields, and one-step outputs remain rarely coherent across the model sizes tested. We propose CONDOR (Coupled-Noise Distillation for One-Step Readout). A noise-conditioned teacher is trained with a random number of masked positions and winner-take-all. A student proposes a one-step block, retains selected tokens, and learns from the block obtained when the teacher refills the other positions in several steps under the same noise field; a noise-free masked-LM term on the ground truth anchors the student. Human evaluation on TinyStories shows a large gain in one-step legality while different noise fields still yield different blocks, at one forward pass per block.

---


### 128. [Beyond QA Matching: Perturbation-Response Fingerprinting via Probability Distributions for Large Language Models](https://arxiv.org/abs/2609.06330)

**<font color=#1a73e8>作者：</font>** Jichao Zeng, Yanli Chen, Hanzhou Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are often instruction-tuned, specialized, quantized, or otherwise transformed, making fine-grained provenance difficult. In this paper, we introduce BReF, a training-free fingerprint that compares how probability distributions over four answer-option labels A/B/C/D move under controlled textual perturbations. For each pair of models, BReF selects 25 jointly responsive probes and compares their perturbation log-ratio (PLR) response directions by global cosine similarity. On a unified benchmark with 34 checkpoints, 22 documented direct-parent relations, and 411 suspect-candidate pairs, BReF retrieves the documented parent in 22/22 cases (MRR=1.0000), with DP-DF AUC 1.0000. Same-family discrimination is harder (DP-SF AUC 0.8969), and paired tests show a significant exact-retrieval gain over a magnitude-only Top-25 control. Together with static, random-probe, permutation, calibration, and transformation-level controls, the results show that strong pooled separation does not guarantee correct parent ranking among closely related checkpoints, verifying the superiority of our work.

---


### 129. [Linear Algebra Foundations of Efficient Attention: A Phase Reversal in Rank Collapse Under SVD Compression](https://arxiv.org/abs/2609.06341)

**<font color=#1a73e8>作者：</font>** Anjaneya Teja Sarma Kalvakolanu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear algebra provides the framework of concepts (matrix rank, singular value decomposition (SVD), and eigendecomposition) that modern artificial intelligence employs to encode, compress, and propagate information through neural networks. This paper unifies fourteen separate peer-reviewed works analyzing the usage of these techniques in the context of transformer-based foundation model research, focusing on three areas of the topic: derivations and properties of self-attention matrices' output rank, compression methods that purposefully utilize this phenomenon, and the low-rank key-value (KV) cache projection and its semiseparable-matrix duality to linear attention and state-space structured models. We were motivated to conduct this work after observing an open problem in this literature: the interplay of the mentioned compression methods with natural rank collapse of the network. With this paper, we report an original finding that using SVD compression of attention projections actually has the opposite effect on the rank collapse of the network: while it strongly suppresses it at initialization, it accelerates on pretrained models (for GPT-2 124M, GPT-2 Medium 355M, and Pythia-160M) with minimal risk of object aliasing artifacts appearing (verified on all compression ratios) and is consistent across four rank estimation methods. A controlled causal decomposition of the effect in both settings showed that the reason for this behavior can be explained by the choice of the subspace SVD makes when compressing the matrix better than the reduction of the operator norm it achieves, explaining roughly 76% of the effect at initialization and 83% on the pretrained weights, providing a refinement to the calibration-aware compression viewpoint and an explanation of why it outperformed naive SVD truncation.

---


### 130. [NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection](https://arxiv.org/abs/2609.06360)

**<font color=#1a73e8>作者：</font>** Wei-Chih Yin, Yun-Ching Kao, Cheng-Kuan Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free zero-shot video anomaly detection (ZS-VAD) leverages vision-language models (VLMs) to localize anomaly instances from a predefined anomaly vocabulary, without providing any video. Existing CLIP-based methods often emphasize anomaly-side semantics, while the competing normality side remains less carefully formulated. We identify two key limitations in existing solutions: (i) blurred decision boundary: normal prompts may contain ambiguous verbs, such as running, that are semantically close to anomalies, reducing normal and abnormal separation in the VLM embedding space; and (ii) modality gap: poor alignment between features of textual normal anchors and visual frames. We propose NOVA, a training-free ZS-VAD framework that strengthens the normal side at both linguistic and visual levels. NOVA introduces Normality-Aware Prompt Construction (NA), which excludes anomaly-adjacent verbs and biases normal descriptions toward static, low-motion scenes. To overcome the text-vision modality gap, NOVA constructs a Visual Normality Anchor (VNA), which creates a weighted visual normal anchor from the initial frames of each test video, providing a video-specific normal reference without task-specific training or annotations. NOVA achieves 89.86 percent AUC on UCF-Crime and 95.07 percent AUC and 84.82 percent AP on XD-Violence, reaching state-of-the-art performance among comparable training-free zero-shot methods.

---


### 131. [AutoKD: Autonomous Knowledge Discovery](https://arxiv.org/abs/2609.06366)

**<font color=#1a73e8>作者：</font>** Qinwen Ge, Bo Ni, Haowei Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery in data-rich domains is currently constrained by human bandwidth: the growth in the volume and complexity of real-world data far outpaces the rate at which researchers can read, reason, and synthesize. Recent LLM-based multi-agent systems have begun to automate portions of the research cycle, but they target hypothesis generation in settings where validation cannot itself be automated, and each run is one-shot, with no mechanism for findings to accumulate or steer subsequent inquiry. This paper introduces AutoKD, a multi-agent framework for autonomous knowledge discovery that is both computational and cumulative, allowing validated findings to persist and inform subsequent inquiry. Six coordinated LLM agents collaborate in an open-ended discovery loop, where accepted findings are stored in a persistent insight graph that serves as both long-term memory and an exploration-steering mechanism. We evaluate AutoKD on three diverse datasets from two perspectives: Open-ended Quality against published findings, and Conditioned Quality via literature-derived queries. Across both evaluation perspectives, AutoKD covers known findings and surfaces substantive discoveries that complement human-driven research. Our code is available at this https URL.

---


### 132. [Robust Conformal Consensus: Multi-Agent LLM-as-a-Judge Interval Evaluation with Conformal Prediction](https://arxiv.org/abs/2609.06367)

**<font color=#1a73e8>作者：</font>** Lihui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge has emerged as a promising paradigm for evaluating natural language generation. However, the uncertainty associated with such evaluations remains largely unexplored, which limits their reliability in real-world applications. Although conformal prediction offers a principled framework for uncertainty quantification, existing approaches typically apply it to a single LLM judge, overlooking the variability introduced by using different LLM evaluators. In this work, we propose a robust uncertainty estimation framework for multi-agent LLM-as-a-Judge evaluation. Our approach constructs conformal prediction intervals for LLM-based scores from multiple LLMs. By considering intervals from different LLM judges, we obtain more stable and reliable uncertainty estimates. Extensive experiments demonstrate that our method produces valid prediction intervals with coverage guarantees, and that interval-based aggregation across multiple judges leads to more stable evaluation outcomes.

---


### 133. [An Integrated Video-AI Platform for Action-Level Microanastomosis Training and Performance Feedback](https://arxiv.org/abs/2609.06380)

**<font color=#1a73e8>作者：</font>** Yan Meng, Daniel A. Donoho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing microanastomosis skill requires repeated practice with timely, action-specific feedback, yet expert review of lengthy microscope videos does not scale to frequent or distributed training. We present an integrated video-AI platform that turns a complete simulated procedure into inspectable, interactive feedback through three connected modules. First, a proposed transformer segments the video into six surgical actions. Second, object detection and tracking localize instrument tips within each action; the resulting kinematic features and action statistics drive supervised classification of five NOMAT-aligned performance dimensions. Third, a grounded large language model (LLM) uses these structured outputs to answer user questions about the current scene, actions, motion, and predicted performance through a unified interface. In a two-site study, 17 participants completed 72 procedures comprising 576 suture placements. The action-segmentation module achieved 87.66\% accuracy and 82.86\% F1, increasing to 93.62\% and 88.32\% after workflow-aware refinement. The five performance classifiers achieved 76.0\% mean accuracy, with Cohen's $\kappa$ from 0.63 to 0.93. Although the language interface and educational benefit require prospective evaluation, these results establish the technical basis for an expert-supervised platform that can shorten review, expose the evidence behind performance estimates, and support scalable formative microsurgical training.

---


### 134. [Cross-Lingual Representation Alignment by Token-Level Optimal Transport in a Language-Agnostic Space](https://arxiv.org/abs/2609.06381)

**<font color=#1a73e8>作者：</font>** Taisei Yamamoto, Ryoma Kumon, Danushka Bollegala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual alignment (CLA) aims to align the representations of large language models (LLMs) across languages, enabling cross-lingual transfer to improve multilingual capabilities. Previous CLA methods often ignore language-specific information encoded in representations and only consider sentence-level alignment, which may lead to suboptimal performance and input-output language mismatch. We propose CAROT (Cross-Lingual Alignment of Representations in a Language-Agnostic Space via Optimal Transport), which consists of two steps: identifying language-specific representations in LLMs' internal states and aligning language-agnostic representations across languages at the token level by optimal transport, while explicitly preserving language-specific representations. Inference-time steering experiments show that the representations computed by CAROT are effective alignment targets, improving multilingual performance by up to 11.2 points in accuracy while maintaining input-output language consistency. We further use the representations obtained by CAROT as training targets, internalizing the aligned representations. The trained models outperform existing CLA methods in 11 of 18 evaluation settings (3 models $\times$ 3 tasks $\times$ ID/OOD languages). Our work provides insights into what constitutes effective alignment targets for CLA in LLMs. Code is available at this https URL

---


### 135. [Are Verifier Errors Independent Within a GRPO Group? Evidence from Qwen2.5 Rollouts](https://arxiv.org/abs/2609.06386)

**<font color=#1a73e8>作者：</font>** Esther Xin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning with verifiable rewards (RLVR) scoresmultiple completions per prompt using automatic verifiers. Analysesbased on independent verifier errors may overlook dependence associatedwith shared answer formats. We investigate this dependence in24,998 groups of eight completions generated by Qwen2.5-1.5B onMATH, GSM8K, and DeepMath-103K. We estimate a pooled within-groupverifier-error correlation of 0.530 (95% confidence interval:0.500--0.560). Under an exchangeable-error model, this correspondsto a design-effect-adjusted effective sample size of 1.70 for aneight-completion group. Dependence varies substantially across answerforms: fractions, radicals, symbolic expressions, and intervals exhibitstronger clustering than unit annotations and percent signs. Replayinggroup-relative advantages across four rule-based verifier configurationsidentifies at least one advantage-sign disagreement in up to 0.83% ofgroups. Because a group is repeated sampling for one prompt, thiswithin-group clustering may reflect shared prompt difficulty as well asshared answer form, and we do not attempt to separate the two this http URL studies of correlated judgments across multiple evaluators, ouranalysis examines dependence across completions scored by the sameverifier. These findings motivate prompt- and answer-form-aware analysesof verifier noise rather than characterizations based solely onaggregate error rates.

---


### 136. [Building Trustworthy Graph-Agentic RAG for Social Good: Architectures, Failure Propagation, and Assurance by Construction](https://arxiv.org/abs/2609.06391)

**<font color=#1a73e8>作者：</font>** Vijay Bommireddy, Raviteja Bommireddy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-agentic retrieval-augmented generation combines structured evidence with adaptive controllers that can plan retrieval, traverse relations, verify intermediate claims, delegate subtasks, and use tools. This combination is useful when answers depend on relations across documents, entities, time, or institutions, but it also creates coupled failure paths: a defect in graph construction can become retrieved evidence, alter later control decisions, and propagate toward a consequential outcome. We examine how such systems should be designed and evaluated for social-good settings in which freshness, authorization, traceability, oversight, and recourse matter alongside answer quality. We organize the literature by graph substrate, graph lifecycle, agent function, coordination pattern, and authority boundary, and distinguish graph-based retrieval from observation-dependent graph control. We then synthesize reported risks as an evidence-to-action failure chain and propose an assurance-by-construction blueprint comprising five interface contracts for evidence, retrieval, reasoning, capability and delegation, and outcome. These contracts make provenance, temporal validity, authorization, uncertainty, and recoverability explicit at system boundaries. An illustrative public-benefit information design shows how the framework constrains graph structure, permissions, abstention, and operating authority. Finally, we derive an evaluation agenda spanning graph assertions, trajectories, claims, coordination, and outcomes.

---


### 137. [From Concentration to Differentiation and Back: Routing Effective Rank in MoE Reasoning Cohorts](https://arxiv.org/abs/2609.06403)

**<font color=#1a73e8>作者：</font>** Kang Chen, Sihan Zhao, Yixin Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling produces cohorts of reasoning rollouts, yet there is no standard label-free account of how their internal computation reorganizes as inference unfolds. We introduce routing effective rank deff, the entropy-effective dimensionality of a cross-rollout graph built from MoE expert-routing similarity. Across ten MoE configurations and five math/science benchmarks, deff exhibits a reproducible low-high-low trajectory, with a prominent interior maximum in 98.5% of 3,105 model-question cohorts: routing similarity is concentrated early, maximally differentiated at intermediate budgets, and reconcentrated later, and the timing of this maximum varies systematically with architecture and reasoning effort. An exact decomposition separates cohort-wide common-mode mass from residual spectral dimensionality: common-mode reallocation accounts for about two thirds of the trajectory, while the residual spectrum contributes about one quarter and retains substantial variation beyond the common mode. The decomposition further localizes behavior: among non-unanimous cohorts, increases in common-mode concentration strongly predict same-answer recoverability, and higher reasoning effort delays the maximum by 2.59 octaves (doublings of the token budget) and consistently expands the high-rank period across all four tested architectures, locating the effort effect in timing and duration rather than peak amplitude. Correctness comparisons separate structural monitoring from answer selection, positioning routing effective rank as a decomposable, label-free diagnostic of cohort organization - a principled spectral lens on how MoE reasoning cohorts differentiate and reconcentrate over inference time.

---


### 138. [Visual Search Augmented Chain-of-Thought Reasoning for Attribute Value Extraction from Product Videos](https://arxiv.org/abs/2609.06410)

**<font color=#1a73e8>作者：</font>** Tong Wu, Ming Cheng, Jiazhen Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing approaches to visual attribute value extraction (AVE) primarily rely on static product images, failing to capture temporal cues, multi-angle views and fine-grained visual details. Directly applying video vision-language models (VLMs) to product AVE results in limited performance due to the lack of domain knowledge, and fine-tuning them requires extensive high-quality data and substantial computational resources. Thus, we propose visual search augmented chain-of-thought reasoning (ViS-CoT), a training-free, plug-and-play pipeline that can be easily applied to any open-source video VLM for video-to-text AVE in e-Commerce. Specifically, ViS-CoT employs visual clustering to identify representative frames, followed by visual search to retrieve semantically similar product knowledge that can enrich attribute cues. Next, an interleaved CoT reasoning module iteratively refines reasoning through visually-aligned auxiliary texts derived from captioning and automatic speech recognition. Finally, the integrated information guides the model toward accurate and fine-grained attribute predictions. Extensive experiments across 14 product categories on the VideoAVE dataset show that ViS-CoT consistently enhances multiple state-of-the-art video VLMs, achieving an average improvement of 17.91 percentage points in micro-F1.

---


### 139. [Separating Capability from Confidence: Grounded Dual-State Calibration for GRPO-Trained Medical Vision-Language Models](https://arxiv.org/abs/2609.06419)

**<font color=#1a73e8>作者：</font>** Yangyang Xie, Ke Hao, Jiaqi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) require confidence that reflects both answer correctness and patient-specific visual evidence. Recent GRPO-based methods optimize verbalized confidence together with answer generation. However, this joint optimization may interfere with answer learning and drive confidence toward near-binary values. Verbalized confidence also provides no explicit assessment of visual support. We therefore separate capability learning from confidence estimation and propose \textbf{DualRead}. DualRead builds on the insight that reliability can be read from the actor's internal states at critical moments in the answering process. It freezes the GRPO-trained actor and combines pre-answer solvability with a post-answer assessment of the generated answer and its visual support. To further assess whether confidence reflects visual grounding, we introduce \textbf{Counterfactual Confidence Grounding AUC} (CCG-AUC). It measures whether confidence decreases when real-image substitution changes the actor from correct to incorrect. Across two VLM backbones and both in- and out-of-distribution medical VQA benchmarks, DualRead improves correctness discrimination and calibration over verbalized confidence while preserving answer accuracy. CCG-AUC reveals whether confidence responds to answer-relevant visual evidence rather than primarily to non-visual cues.

---


### 140. [InsightChain: Optimized Chain-of-Insight Analytics for LLM-driven Data Visualization](https://arxiv.org/abs/2609.06438)

**<font color=#1a73e8>作者：</font>** Hanya Sun, Chen Zhang, Sheng Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for automated data visualization, yet existing approaches often frame visualization generation as a single-step mapping from user query to figure or code, overlooking the iterative analytical reasoning process of expert analysts. We present InsightChain, a four-stage visualization prompting pipeline (Explore--Focus--Test--Present) that emulates expert analytical workflows, together with VG-COPRO, a vision-guided automatic prompt optimization (APO) method adapted to jointly optimize such multi-stage, executable pipelines. To address the evaluation gap for complex data visualization, we introduce the Insight Progression Metric (IPM), a rubric combining four text-based dimensions with a vision-based dimension. We assess IPM through a 100-chain human pilot and an expanded 300-chain agent-based evaluation spanning all ten domains. Experiments on public datasets show that InsightChain consistently outperforms competing prompting baselines. Existing APO methods fail to yield consistent gains on this multi-stage task, whereas VG-COPRO improves performance in both in-domain and cross-domain settings.

---


### 141. [Decomposing LLM-Judge Uncertainty to Target Expert Labels](https://arxiv.org/abs/2609.06444)

**<font color=#1a73e8>作者：</font>** Ryan Lail  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM judge evaluates outputs at scale. Experts should label only where it is least sure. Its natural escalation signal conflates two uncertainties: aleatoric, real disagreement in the expert pool, which labels cannot reduce, and epistemic, the judge's ignorance, which labels do reduce. A small Bayesian model separates them: a regression on labels already collected learns how far to trust a black-box judge's prediction. Both components follow as simple formulas, with no sampling or further judge calls. The components isolate on a real LLM judge against exactly known truth, and stated confidence is no guide to its actual error. On real human disagreement (ChaosNLI) the epistemic ranking removes 83% more error than total uncertainty for the same expert labels, though simply escalating the least-labelled items does as well there. We demonstrate we can estimate where a judge is ignorant rather than where experts genuinely disagree, and propose using this to direct expert labelling.

---


### 142. [One Step, One Lead: Mitigating Higher-Order Interference in Multi-Domain Reinforcement Learning via Cross-Step Control](https://arxiv.org/abs/2609.06469)

**<font color=#1a73e8>作者：</font>** Zihan Lin, Xiaohan Wang, Jie Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) across multiple domains can broaden the reasoning capabilities of large language models (LLMs), yet joint training often degrades individual-domain performance and can destabilize optimization. Existing work typically diagnoses such interference from a single-step view using first-order gradient alignment or curvature-based proxies. We show that this view can miss a critical form of sequential interference: same-point domain gradients may remain nearly orthogonal even when consecutive realized updates partially reverse one another in output space. We further show that consecutive token log-probability footprints recover this interaction directly from adjacent checkpoints as a local second-order interaction in output space, without explicitly reconstructing same-step curvature. Building on this insight, we propose OSOL, which designates a focus domain at each iteration, uses the preceding checkpoint footprint to rank token-level rebound risk, and applies a drift-ranked, adaptively scaled correction within the standard GRPO update. Our analysis shows that this correction suppresses the targeted cross-step output backtracking component. Controlled studies further show that cross-step backtracking is more strongly associated with subsequent task damage than same-point gradient diagnostics, while the preceding footprint ranks future rebound risk more accurately than Hessian-based proxies. On Qwen3-30B-A3B, OSOL reaches a domain-macro average of 0.4822, improving by 5.7% over the strongest compared baseline, without explicit higher-order differentiation.

---


### 143. [Steering Under Compression: Dose-Response, Capability Cost, and Failure Asymmetry in Quantized LLMs](https://arxiv.org/abs/2609.06473)

**<font color=#1a73e8>作者：</font>** Saurav Bhandari, Benjamin Wade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time activation steering enables behavioral control of large language models without parameter modification, while post-training quantization reduces memory and compute costs for deployment. Despite their growing convergence in practice, the interaction between these two techniques remains uncharacterized. We systematically study activation steering under weight-only quantization (INT8 and NF4) across four open-weight 7-9B models and two behavioral targets: judged sentiment and judge-free reasoning length. Using an iso-effect framework that compares capability costs at matched behavioral effect, we find that sentiment steering survives quantization intact. After correcting a GSM8K parser artifact with a uniform v2.3.1 rescore, the pooled INT8 contrast is -0.010 (90% CI [-0.026, +0.007]), descriptively Equivalent under the preregistered three-label rule, while NF4 remains Inconclusive at -0.017 ([-0.067, +0.033]). In contrast, reasoning length exhibits a surprising asymmetric dose-response: lengthening is graded but terminates in cap-runaway and collapse, while shortening is a step function with only 12-30% shortening (model-dependent) before discontinuous failure. We expose a methodological pitfall: the naive iso-effect ladder anchors on the collapse floor for floor-bounded targets, and we introduce a censored construction that restores interpretable crossings. We also quantify a substantial baseline capability shift for Mistral-NF4 (0.545 to 0.365 GSM8K at alpha=0), demonstrating that compression can dominate the steering intervention. Despite this, steering vectors remain highly collinear with their FP16 siblings (cosine similarity 0.989-0.998 for INT8, 0.945-0.990 for NF4), confirming that the behavioral direction survives quantization even when the cost structure does not. All code and data are released.

---


### 144. [Thinking with Cameras: Active Visual Reasoning via Dynamic Viewpoint Control for Surveillance Video Understanding](https://arxiv.org/abs/2609.06475)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Wang Zeng, Sheng Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have recently achieved remarkable progress in general-purpose video understanding. However, their application to surveillance videos remains challenging due to the lack of large-scale domain-specific datasets and the limitation of passive observation from fixed viewpoints. In surveillance scenarios, critical visual evidence can be easily missed when targets are distant, small, occluded, or move beyond the current camera view. In this work, we introduce CamVLM, a new framework for Thinking with Cameras, which enables LVLMs to actively acquire visual evidence through dynamic viewpoint control rather than passively analyzing fixed video streams. We first construct CCTV-Anomaly, a large-scale surveillance video understanding dataset containing 14,459 videos across 10 anomaly categories, with detailed captions and event annotations. We further formulate viewpoint control as an active visual perception problem and build CamTrack-53K, an object-centric viewpoint trajectory dataset for learning camera actions. Moreover, we propose a reinforcement learning based viewpoint policy optimization framework, which models camera control as a sequential decision-making process and learns long-horizon observation strategies beyond supervised trajectory imitation. Extensive experiments demonstrate that CamVLM achieves state-of-the-art performance under both passive observation and dynamic viewpoint settings, validating the effectiveness of active camera-based reasoning for surveillance video understanding. Our datasets, model, and code will be available at this https URL .

---


### 145. [One MLLM, One Call: Efficient Zero-Shot Vision-and-Language Navigation via Spatial-Aware Waypoints](https://arxiv.org/abs/2609.06476)

**<font color=#1a73e8>作者：</font>** Shiqi Pan, Qi Zheng, Hanqin Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to navigate unseen environments by following natural language instructions. Current zero-shot VLN-CE methods either rely on pre-trained waypoint predictors or require multiple queries to large models per step. To address prohibitive inference latency and computational overhead, we propose O2C-Nav, an efficient zero-shot navigation framework that calls only a single large model once per decision step. Our approach introduces a training-free structured waypoint generator and a novel abstract representation that projects sparse, history-aware candidate waypoints directly onto RGB images as visual markers. The MLLM selects a waypoint or generates a fallback target bounding box at each step, while a low-level Fast Marching Method (FMM) planner converts the selected target into an executable collision-free path. This paradigm provides the model with concrete spatial perception and explicit memory while significantly reducing the visual processing load. Extensive evaluations on the R2R-CE and RxR-CE benchmarks demonstrate that O2C-Nav outperforms current state-of-the-art zero-shot methods, highlighting its great potential for real-time robotic deployment. Code is available at this https URL.

---


### 146. [DFlow: Enabling Verifier Information Flow in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2609.06498)

**<font color=#1a73e8>作者：</font>** Yaojie Zhang, Linfeng Zhang, Bin Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block diffusion speculative decoding improves LLM inference efficiency by proposing a block of future tokens in parallel and verifying them with a single forward pass through the target model. However, existing methods retain only the accepted prefix and discard the rejected suffix, preventing the computation spent on these positions from benefiting subsequent drafting rounds and forcing the drafter to repeatedly reconstruct representations for future tokens from scratch. We observe that rejection only determines whether a proposed token can be committed, while the verifier representations at rejected positions can still provide useful information for subsequent predictions. Based on this observation, we propose DFlow, a simple yet effective framework that enables verifier information to flow across drafting rounds. DFlow reuses the hidden states produced by the target verifier for the rejected suffix to guide subsequent drafting without additional target computation. To effectively learn this information flow across drafting rounds, we introduce a self-condition train strategy that feeds verifier representations from earlier predictions back into subsequent predictions. Experiments on Qwen3 models across diverse benchmarks demonstrate that DFlow consistently improves draft quality and acceptance length over DFlash.

---


### 147. [CAM: Question Answering on Entity-Centric Videos with Continuous Extraction and Adaptive Querying](https://arxiv.org/abs/2609.06504)

**<font color=#1a73e8>作者：</font>** Yizhou Tian, Zizhe Chen, Shiyuan Deng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory facilitates question answering over long videos by extracting and retrieving facts to fit within the limited context windows of multimodal LLMs (MLLMs). Existing solutions typically extract independent memory entries from fixed-length video clips and thus cannot capture high-level semantics that need to be summarized over extended time periods, such as character traits and relations. Moreover, they rely solely on similarity-based retrieval and may fail to retrieve the fine-grained details required for question answering. To tackle these problems, we propose CAM, featuring continuous extraction for high-level semantics and adaptive querying for fine-grained details. In particular, CAM stores the entities and relations extracted from video clips in a knowledge graph. To capture the high-level semantics of each entity or relation, CAM summarizes the local subgraph of the target entity or relation once the subgraph reaches a predefined size. To retrieve the fine-grained details required for question answering, CAM supports multiple search methods, including knowledge graph traversal, video re-watching, and audio listening. It utilizes a planner-executor-verifier pipeline to adaptively compose these search methods according to question intent. Evaluations on three benchmarks show that CAM outperforms SOTA baselines and improves their accuracy by up to 23 percentage points. Code is available at this https URL.

---


### 148. [ProcArena: A Multi-Scenario Benchmark for LLMs on Direct and Interactive PL/SQL Development from Natural Language](https://arxiv.org/abs/2609.06527)

**<font color=#1a73e8>作者：</font>** Hang Zhang, Chaokun Wang, Yuzhi Pan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for translating natural-language (NL) requirements into PL/SQL programs, attracting increasing attention from the database community. However, existing NL-to-PL/SQL efforts primarily focus on directly generating PL/SQL from complete NL requirements. In practice, PL/SQL development involves diverse scenarios, such as from-scratch development, code modification, debugging, and optimization, and may require either direct generation or multi-turn interaction. Yet, no comprehensive benchmark evaluates multi-scenario, direct and interactive, and multi-dialect NL-to-PL/SQL development. In this paper, we present ProcArena, an execution-based benchmark covering both Direct and Interactive modes. ProcArena comprises 3,998 executable tasks over 157 databases, spanning nine development subscenarios in PostgreSQL and Oracle. We construct challenging Direct tasks through Iterative Logic Enhancement and scenario-specific adapters, and derive paired Interactive tasks through Knowledge Integration and Requirement Perturbation while preserving executable targets. We further design a controlled Solver-User Simulator protocol that allows models to clarify user intent and inspect the database environment without exposing hidden execution feedback. Evaluating seven language models, we find that the best average scores are only 62.2% and 57.8% in Direct and Interactive, respectively, demonstrating that realistic NL-to-PL/SQL development remains challenging, particularly in interactive settings.

---


### 149. [3DHarnessBench: Probing Agentic 3D-to-Code Capabilities of Frontier Vision-Language Models](https://arxiv.org/abs/2609.06535)

**<font color=#1a73e8>作者：</font>** Ling Liu, Bingchen Gong, Amal Dev Parakkat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce 3DHarnessBench, a benchmark that evaluates the agentic ability of frontier vision-language models (VLMs) to recover 3D geometry as Blender Python code from a variety of inputs. Unlike previous frameworks that prompt the VLMs with a fixed input (e.g., a single rendering or a text description), 3DHarnessBench evaluates four separate harness settings that progressively enable active agentic exploration, facilitated by recent Blender MCP functionality. Our hierarchy from Single-view, Multi-view, Active Visual (arbitrary viewpoint access), and Full 3D Interaction (complete access to the target object through Blender function calls) probes the models' abilities in both visual perception and active inference, tool calling, and self-correction. We observe that the ability of all frontier models to recover 3D geometry improves significantly with richer function call access, although the improvements are strongly model-dependent, revealing highly uneven agentic 3D-to-code capabilities. We will release the benchmark, code, outputs, and agent trajectories for reproducible 3D evaluation.

---


### 150. [SRD-GUARD: A Defense Framework of LLMs via Semantic Rewriting and Joint Multi-Model Scoring for Latent Intent Exposure](https://arxiv.org/abs/2609.06540)

**<font color=#1a73e8>作者：</font>** Qi Wang, Chengcheng Wan, Jiangtao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in safety-critical applications, yet jailbreak attacks can conceal harmful intent through role-playing, fictional scenarios, or seemingly benign motivations. Existing inference-time defenses may miss disguised attacks or excessively refuse legitimate requests. We propose SRD-GUARD, a parameter-free, black-box defense framework that exposes concealed intent through semantic rewriting and consensus-based risk assessment. Given an input prompt, SRD-GUARD generates five semantically related rewrites that preserve the underlying objective while removing unnecessary contextual packaging. The original prompt and rewrites are jointly evaluated by multiple independent LLM-based safety scorers on a continuous risk scale. A decision module combines absolute risk thresholds with relative risk changes between the original and rewritten prompts to adaptively intercept, preserve, or warn on requests.
We evaluate SRD-GUARD against UNIATTACK, CIPHER, and DeepInception on Llama-3-8B-Uncensored and DeepSeek-V4-Flash using AdvBench and OR-Bench-Hard. SRD-GUARD achieves average DSRs of 91.44% and 100%, with ORRs of 8.00% and 12.00%, respectively. Compared with evaluated baselines, it provides a more favorable DSR--ORR trade-off. Ablation studies show that rewriting exposes concealed harmful intent, joint scoring improves robustness to individual evaluator behavior, and risk-adaptive decision making enables selective handling of ambiguous inputs. These results demonstrate that semantic intent exposure, consensus-based risk assessment, and relative-risk-aware routing provide an effective and selective approach to black-box jailbreak defense. The artifact is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
