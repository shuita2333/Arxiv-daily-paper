# 🧠 大模型相关研究 | 2026年11月26日

> 本类共 **299** 篇论文：已确认 **280** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-299](./part-06.md)

---

### 201. [Evaluating Latent Knowledge Stability in Multimodal Large Language Models](https://arxiv.org/abs/2611.32566)

**<font color=#1a73e8>作者：</font>** Chuancheng Shi, Shangze Li, Wenhua Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Changes in image viewpoint and question formulation can alter latent knowledge representations in multimodal large language models (MLLMs). However, output correctness and overall representational drift provide limited insight into how these changes affect model decisions. We therefore evaluate latent knowledge stability across visual and linguistic elicitation conditions from two complementary perspectives: answer preference and internal support. Specifically, we devise the margin retention score (MRS), which measures the first-order projected degradation of the initial answer's logit margin over competing options across conditions and assesses how changes in latent knowledge representations affect this margin. We also present latent knowledge support-structure stability (KSS), which evaluates reference-correct items by comparing internal support profiles constructed using the margin gradient under the reference condition, which jointly reflects changes in how internal support is distributed and changes in total support magnitude. We further construct MMStableBench, comprising 19,452 knowledge items (facts), each probing the same latent knowledge across varied image viewpoints, semantically equivalent question formulations, and answer-option permutations. Experiments across 15 MLLMs show that MRS and KSS reveal latent knowledge instability not captured by accuracy, while an MRS-inspired regularizer further improves the generalization of edited latent knowledge.

---


### 202. [Understanding the Importance of Massive Activations through Adversarial Robustness](https://arxiv.org/abs/2611.32585)

**<font color=#1a73e8>作者：</font>** Tigran Fahradyan, Riccardo Ali, Sergio Calvo-Ordoñez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common occurrence in Large Language Models (LLMs) is the emergence of so-called massive activations. This phenomenon is well known in the literature and has been connected to attention sinks, representational compression, as well as signal propagation. However, the reasons and consequences for their appearance are not yet well understood. In this paper, we explain the role of massive activations in deep learning by showing that they are connected to the region migration phenomenon in delayed robustness. Under the spline theoretic interpretation of deep networks, we show that massive activations push the representations away from the nonlinearity boundaries of the network, decreasing the complexity of its input-output map around data points. Furthermore, we uncover for the first time that this phenomenon is not unique to transformers and actually appears in a number of common architectures performing simple supervised learning tasks. We validate this connection through extensive experiments on a diverse set of architectures including residual MLP, ResNet18, Vision Transformers and GPT and datasets including MNIST, CIFAR10, Imagenette and Shakespeare Text. We consistently observe that massive activations and region migration co-occur with adversarial robustness. Furthermore, we illustrate that this connection holds in the large-scale pretraining of LLMs by showing that the rise of massive activations in LLMs closely tracks the adversarial accuracy of the model under perturbations of the token embeddings.

---


### 203. [Gated Concept Adapters: Layer-Wise Concept Bottlenecks for Auditable Text Understanding](https://arxiv.org/abs/2611.32600)

**<font color=#1a73e8>作者：</font>** Niloofar Ranjbar, Saeedeh Momtazi, Mohammad Mehdi Homayounpoor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human-facing text understanding systems are used to infer affect, moderate harmful content, and support socially sensitive decisions. However, Transformer predictions are difficult to audit because they are produced from high-dimensional hidden states that do not provide a compact, inspectable interface for human analysis or intervention. We introduce Gated Concept Adapters (GCA), a layer-wise concept bottleneck framework that attaches gated, low-dimensional concept-producing readout adapters to selected outputs of pretrained Transformers. Token representations are mapped into concept activations, filtered by learned gates, pooled into layer-level summaries, and exposed to the prediction head as a concept-mediated interface. The dimensions can be inspected through usage statistics, signature n-grams, post-hoc concept names, and targeted concept interventions. We evaluate GCA on fine-grained emotion classification, toxicity detection, topic classification, and a controlled verb-cloze stress test. In the affective and safety-relevant classification settings, GCA learns comparatively low-redundancy and intervention-sensitive concept representations while retaining useful predictive performance. On toxicity detection, it remains close to an unconstrained ModernBERT baseline while enabling concept-level inspection, targeted intervention, and lightweight post-hoc control. On GoEmotions, the end-to-end concept model incurs a macro-F1 cost relative to unconstrained RoBERTa, while a task-initialized frozen variant substantially reduces this gap. On AG News, GCA remains competitive with recent concept-based baselines, and the Qwen verb-cloze experiment clarifies the limits of concept-mediated full-vocabulary prediction. Overall, GCA provides a neural concept interface for auditable text understanding, prioritizing transparency, diagnosis, and intervention over unconstrained accuracy maximization.

---


### 204. [Recursive Collective Intelligence: Emergence on an Equal-Budget Ladder in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.32606)

**<font color=#1a73e8>作者：</font>** Lixuan He, Shengqu Cai, Fang Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly work as teams of agents, and a team is expected to solve problems beyond the reach of any single member. Most evaluations credit a team for outperforming a single agent, without accounting for the additional computation: a team may consume many times the tokens of one agent, and a plain vote over independent answers already explains most of the reported gain. Two questions therefore remain open: When does interaction itself make a group smarter, and can a group improve its next generation by learning from its own work? We answer both with the equal-budget ladder, which grades a group against independent agents at three levels: outperforming a single agent, a compute-matched majority vote, and compute-matched pass@n. On this ladder we define Recursive Collective Intelligence (RCI) as a group whose own output, without a teacher or external labels, makes its next generation smarter at equal cost. Three findings follow. First, interaction improves collective intelligence when it moves information across agents: forwarding split facts lifts groups above pass@n at three model scales, by about a third at 27B. Second, organization emerges spontaneously: identical 27B agents form hubs and improve accuracy by 18 percentage points; encoding their organization in a prompt enables them to reach level 3 at less than half the token budget in a descriptive comparison. Third, groups recursively improve themselves: Two label-free generations progressively climb the ladder, the second 9B generation surpassing both pass@$n$ and a control trained on base-model turns; on PlanBench, HiddenBench and Hanabi, each generation outperforms its predecessor on unseen problems for four to six generations. A group therefore outperforms its members when it forwards useful information more efficiently than it spends tokens on coordination, and learns to do so from its own work.

---


### 205. [Privacy Disclosure Control Benchmark (PDC-Bench): How Faithfully Do LLMs Keep Privacy Constraints on In-Context Disclosure Granularity?](https://arxiv.org/abs/2611.32610)

**<font color=#1a73e8>作者：</font>** Kosuke Fujita, Daiki Nishiyama, Jun Sakuma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In LLM task execution, a constraint on the permitted disclosure granularity of personal attributes is sometimes imposed on the output. For example, if a person's private attribute is their location (San Francisco) and disclosure is permitted only at the country level, an output at the state level (California) violates the constraint. Detecting such violations requires capturing not only direct privacy leakage (San Francisco) but also semantic leakage (California). However, existing benchmarks cannot measure the degree of leakage with respect to a given semantic constraint such as the country-level limit. We therefore formalize disclosure control as a constraint on the permitted ceiling over the hierarchy of a knowledge graph. Building on this formulation, we construct PDC-Bench, a benchmark of 16,105 samples covering geography, age, race and ethnicity, and occupation. In our experiments applying PDC-Bench to eleven LLMs, 62% of the constraint violations were semantic leakage. We further found that semantic leakage depends less on the model than on the permitted disclosure granularity and the task's need for the private attribute; reliable auditing must therefore target semantic leakage together with these two factors. Data, prompts, and code are available at this https URL.

---


### 206. [VenusOCR2.0: Towards Efficient and Effective Document Parsing](https://arxiv.org/abs/2611.32617)

**<font color=#1a73e8>作者：</font>** Lei Li, Zheng Wei, Yi Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VenusOCR2.0, a compact 1B-parameter vision-language recognizer designed for both high-accuracy and high-throughput document parsing across text, tables, and formulas. To continuously improve recognition quality without self-training collapse, we build a bounded recursive self-improvement (RSI) data engine where the model acts strictly as a weakness probe, while external multi-expert medoid consensus, VLM visual verification, and factorized synthesis supply reliable supervision across pretraining, curated SFT, and RLVR. VenusOCR2.0 couples a dynamic-resolution SigLIP2 encoder and 2x2 spatial token merging with a Qwen3-0.6B decoder, adopting compact atomic OTSL tokens to shorten table sequences and reduce structural errors. To further eliminate the autoregressive decoding bottleneck, we introduce PTPv2, a lightweight ($\sim$67M) decoupled parallel draft module that combines frozen multi-layer verifier conditioning, a standalone learned mask, and block-causal all-position next-token prediction. On OmniDocBenchv1.6, VenusOCR2.0 achieves an overall score of 96.45 and a state-of-the-art 98.57 formula CDM, substantially outperforming massive general-purpose VLMs such as Gemini-3-Pro (92.91) and Qwen3-VL-235B (89.78). Deployed in vLLM on a single H20 GPU, PTPv2 delivers a 2.96x single-request speedup and up to 2.36x higher batched throughput while guaranteeing lossless, token-for-token equivalence with standard autoregressive decoding.

---


### 207. [ShapeQuest: Towards Granularity-Controlled Edit-Conditioned 3D Asset Retrieval](https://arxiv.org/abs/2611.32621)

**<font color=#1a73e8>作者：</font>** Faris Abu-Ali, Sankalp Sinha, Didier Stricker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a reference asset and an instruction such as "remove one armrest," a retriever must find variants that make the edit and preserve the other parts. This search is well established for images but remains underexplored for individual 3D assets. To study this problem, we introduce ShapeQuest and ShapeQuester, a new benchmark and model for edit-conditioned 3D asset retrieval. ShapeQuest's open-source pipeline edits textured meshes through part additions, removals, and material and colour changes. It controls edit granularity across five levels, defined by the fraction of the object's surface area each edit affects. It constructs multiple valid targets when an instruction leaves the choice of part open. A vision-language model judges each edit from views chosen to expose the edited parts, and human raters audit its judgments. ShapeQuest has 87,824 queries in 50 categories and a 50,919-shape gallery with competing edits. To distinguish these variants, ShapeQuester learns retrieval alongside reconstruction of the edited point cloud, with part masks supervising changed and preserved regions. With a frozen pretrained point encoder, ShapeQuester reaches 50.4 operation-macro mAP@10 on the test split, against 47.2 for the fusion baseline with the same inputs and 48.6 for the strongest baseline. Reconstruction adds 6.5 points on the validation split when the point encoder is trained from scratch, including 3.3 from part masks.

---


### 208. [HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization](https://arxiv.org/abs/2611.32624)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhang, Yanzhao Li, Hui Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block floating-point (BFP) quantization is widely adopted for efficient low-bit large language model (LLM) inference, where the choice of block scales plays a critical role in quantization accuracy. HiFloat4 (HiF4) employs a hierarchical scale encoding scheme consisting of a global E6M2 scale and two levels of binary scale extensions. However, its conventional rounding rule and fixed scale extension thresholds may not fully capture the statistical characteristics of the quantized tensors in practice, leading to suboptimal scale representations. In this work, we propose HiCal, an offline calibration approach that improves HiF4 quantization accuracy by refining the encoding decisions across all three scale levels. Specifically, we introduce a calibrated rounding bias for the Level-1 E6M2 scale and optimize the scale-extension thresholds at Levels 2 and 3 based on the empirical distributions of local group magnitudes. The resulting calibration parameters are determined offline and remain fixed during inference, while the hierarchical encoding continues to adapt to individual blocks through their local values. This design eliminates the need for per-block multi-candidate scale search while preserving the original deterministic HiF4 encoding procedure. Experiments across five synthetic and real activation distributions show that the proposed method reduces quantization MSE by 9.91%-23.50% relative to the original HiF4 scheme, including a 13.00% reduction on real Qwen3-8B activations. End-to-end evaluations across six benchmarks further show average-score improvements of 0.91 and 1.25 percentage points on Qwen3-8B and Qwen3-30B-A3B, respectively, without per-block multi-candidate search during inference.

---


### 209. [MargEmbed-Akan: Bridging Twi Questions and English Knowledge through Cross-Lingual Score Distillation](https://arxiv.org/abs/2611.32630)

**<font color=#1a73e8>作者：</font>** Prince N. Y. Annan, Ali A. A. Aziz, Stephen E. Moore  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most information sought online by Twi (Akan) speakers is written in English, making cross-lingual retrieval essential. We evaluate eight systems: BM25, five open embedding models, and two proprietary models (gemini-embedding-001 and OpenAI text-embedding-3-large) on two Twi-English tasks. AfriQA contains 1,221 natively written Asante Twi questions that must retrieve their answering English Wikipedia passages. Bible translation retrieval requires a Twi passage to retrieve its English translation from 6,195 candidates.
We introduce MargEmbed-Akan, a 560M-parameter open query encoder trained from AfriE5-Large-instruct using cross-lingual score distillation. The frozen base model scores each English training question against its answer passage and seven hard negatives. The student learns to reproduce these scores from both an NLLB-200 Twi translation that passes a round-trip translation check and the original English question, preserving English behaviour. During training, passages are encoded by the frozen base model; at evaluation, MargEmbed-Akan encodes questions and passages.
On AfriQA, base AfriE5 and gemini-embedding-001 both achieve 66.6 nDCG@10; EmbeddingGemma 2, Qwen3-VL-Embedding-2B, and OpenAI text-embedding-3-large achieve 56.6, 51.3, and 53.4, respectively. MargEmbed-Akan achieves 71.5, outperforming gemini-embedding-001 by 4.9 points, its base model by 5.0, and OpenAI text-embedding-3-large by 18.1. Its largest gain is on Twi typed without E and O (+7.5 over gemini-embedding-001). English retrieval does not differ significantly from the base model, although both proprietary models score 1.5-2.2 points higher. On Bible translation retrieval, MargEmbed-Akan and gemini-embedding-001 are statistically tied on standard Twi (97.2 vs. 96.5 nDCG@10); MargEmbed-Akan performs better on diacritic-free Twi (92.7 vs. 84.9). No AfriQA data was used for training or model selection.

---


### 210. [Generating Schema-Aligned Synthetic Dialogues and Measuring Their Diversity](https://arxiv.org/abs/2611.32631)

**<font color=#1a73e8>作者：</font>** Konrad Stolte, Toni Fetzer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training or evaluating a model that turns a conversation into a structured record requires paired data, meaning a transcript together with the exact record it should be converted into. Such pairs are expensive to annotate, and in sensitive domains they are also difficult to obtain at all. We therefore build them in the opposite order by sampling a schema-valid record first, then writing a dialogue from it, and optionally synthesizing speech from the dialogue, so the label exists before the text and we need no annotation step. Naively prompting a language model for such dialogues yields small variations of a single conversation, so we add a sampled variation configuration, personas, and a topic plan that orders the fields of the record as explicit mechanisms for variation. We measure the variation that reaches the output through embedding space, where the embedding variance spreads over about two and a half times as many independent directions with our full configuration compared to without (participation ratio 23.3 against 9.2). Two corpora of medical dialogue give values of the same order, with sample size, text length and language being additional factors there. We also show the positive effect of our method in a downstream test, where an 8B extraction model reaches 64.8% field accuracy when fine-tuned on dialogues from our method, against 57.5% from naive generation. We release the generation library and the generated corpus of German clinical dialogues with aligned records.

---


### 211. [A Text-to-SQL Benchmark for Official Statistics](https://arxiv.org/abs/2611.32646)

**<font color=#1a73e8>作者：</font>** Lucas Lageweg, Karen Goes, Tom van den Broek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Official statistics are critical datasets for a wide variety of actors, including policymakers and businesses. For providers of official statistics, improving accessibility, governance, and disclosure of their data is of key importance. This can be improved by providing question-answering systems based on text-to-SQL approaches. However, existing text-to-SQL benchmarks do not resemble this setting. Official statistics are published as open-domain catalogs of thousands of wide tables whose columns and values are codes, and whose meaning is recorded in separate metadata rather than in a relational schema. To address this gap, we introduce LOCuST, a text-to-SQL benchmark that pairs over two thousand English and Dutch tables from Statistics Netherlands with a semantic knowledge graph. The graph describes the tables, measures, and dimension codes through labels, definitions, hierarchies, and units, and is the external knowledge a system needs to find the right tables and ground a question in the right codes. The benchmark includes expert-annotated questions for different query and aggregation types, including raw value retrieval, summations, proportion calculations, and joins. Alongside standard evaluation measures, we introduce an observation F1 metric that measures how close a query is to the ground truth even when the answers are different. We evaluate a variety of state-of-the-art LLMs and find that they struggle to write SQL that answers the questions correctly.

---


### 212. [ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649)

**<font color=#1a73e8>作者：</font>** Qingle Liu, Jieming Li, Pei-lin Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline, rely on text or static images, and risk training-data contamination, while robot evaluations are limited to method-level ablations. We present ICLWorld, an online benchmark that evaluates the ICL of agents from digital to physical worlds, covering computer use and robot use, together with UIverse, a unified harness that turns every environment into a user interface. We build 30 environments, record 630 demonstration videos (10+ hours), and design 160 tasks with customized, often counter-intuitive rules that cannot be satisfied without learning from the context. Each task comes with three rule versions, given as text or video, and we test generalization at three levels, from replaying the demonstration to new instances and unseen environments. Across six frontier models, the strongest agents, Claude Opus 5.5 and GPT-6 Astra, succeed on 82% and 76% of computer-use runs but only 27% and 26% of robot-use runs, and a no-rule control reduces success to at most 8%. GPT-6 Astra succeeds under all three rule versions on only 38% of computer-use tasks, half its rate under a single rule, and answers 98% of robot rule questions correctly yet completes only 20% of these tasks. Frontier agents learn rules comparably well from video and from text and transfer them across environments, whereas weaker agents rely on text and lose most of their video-based success once the demonstrated situation is resampled. These findings reveal substantial gaps between the digital and the physical world and between identifying a rule and acting on it.

---


### 213. [Economic World Model](https://arxiv.org/abs/2611.32663)

**<font color=#1a73e8>作者：</font>** Qirui Mi, Yujia Ming, Bo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an economic system works, enabling counterfactual simulation and decision-making under resource constraints. We then propose a general framework for studying EWMs that links three tasks: simulating agent behaviour, learning economic transitions and systematically evaluating the dynamics. As an initial implementation, we learn household policies from microeconomic data and calibrate a structural economic transition model using macroeconomic data, linking individual decisions to aggregate dynamics. Our micro-to-macro evaluation framework compares simulated individual actions and group distributions with observed microdata and assesses macroeconomic dynamics through forecasting and counterfactual experiments. Results show that simulated and observed household consumption distributions overlap by 94.9%, while EWM forecasts closely track real GDP and several other aggregate levels. In government-borrowing counterfactuals, the EWM reproduces the benchmark life-cycle model's short-run transmission from borrowing to consumption. For ex ante planning, the EWM enables an LLM agent to achieve 10.29% higher simulated GDP under the epidemic shock than direct LLM decisions. This initial EWM is only a starting point. We invite economists and AI researchers to build a stronger EWM together. Economists can contribute richer economic models and knowledge, while AI researchers can develop stronger data-driven methods for simulating agent behaviour and learning economic transitions. Together, we aim not only to reproduce real economic dynamics, but also to discover and test new mechanisms that support better decisions and benefit society.

---


### 214. [Text Is Just Another Shot in Vision-Language Models: Simple Probes on Frozen Encoders Do It](https://arxiv.org/abs/2611.32672)

**<font color=#1a73e8>作者：</font>** Reda Bensaid, Ismail Ben Ayed, François Leduc-Primeau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot adaptation of vision-language models has produced increasingly elaborate methods built on CLIP and on one shared principle: the zero-shot text classifier is the anchor, and labeled images only correct it. We argue that this principle reflects CLIP's visual features rather than a property of the task. We provide a simple Bayesian interpretation, in which a class name is worth exactly kappa = sigma^2 / tau^2 labeled images, the ratio between the visual spread of a class and the misalignment of its name. The Bayes classifier of this model counts text as kappa more samples. With modern frozen encoders, few-shot adaptation then reduces to a well-regularised convex probe. Specifically, we introduce TASP, a simple convex logistic regression on frozen features that incorporates class-name embeddings as weighted training examples and as a regularization prior. On the standard 11-dataset benchmark, TASP with frozen PE-Core-L features achieves 87.1% accuracy at 1 shot and 91.4% at 16 shots, outperforming state-of-the-art few-shot vision-language adaptation methods by 4.6 to 11.0 percentage points. While stronger representations explain much of this improvement, controlled comparisons on matched features show that existing frozen-encoder adaptation methods do not materially improve on this probe. We further find that the weight assigned to text matters more than how it is incorporated, and that combining self-supervised visual features with vision-language representations is most beneficial for weaker visual encoders. Together, these findings suggest that progress in few-shot vision-language adaptation depends more on representation quality and the appropriate use of text supervision than on increasingly complex adaptation mechanisms.

---


### 215. [Social Bias Neurons in Multilingual Language Models: A Mechanistic Interpretability Analysis](https://arxiv.org/abs/2611.32685)

**<font color=#1a73e8>作者：</font>** Lance Calvin Lim Gamboa, Yue Feng, Mark Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual models exhibit social bias when processing inputs pertaining to societal stereotypes. We adapt emerging mechanistic interpretability methods to pinpoint and characterize model components that encode this bias. We conduct our analysis across three instruction-tuned models, four languages, and seven bias dimensions. Specifically, we leverage multilingual bias benchmarks in implementing two methods for identifying social bias neurons: activation probability entropy and integrated gap gradients. We find the latter method to be more effective, as the neurons it isolates (which are largely concentrated at the model's deepest layers) lead to sharper decreases in model bias when suppressed. Further analysis reveals neuron distribution patterns differ between high- and low-resourced languages, suggesting that a language's representation in pretraining data influences how its biases are represented within model internals. Our results also indicate that neurons linked to gender, nationality, and social class biases overlap the most with neurons related to other bias dimensions, pointing to the pivotal role these three dimensions play in how models learn and handle bias.

---


### 216. [CAPTA: Identifying LLMs Behind AI Agents](https://arxiv.org/abs/2611.32686)

**<font color=#1a73e8>作者：</font>** Kailun Yan, Yue Huang, Sisi Duan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents access remote services through tools to complete user tasks, often via API calls. In this setting, a remote service may want to identify the backend LLM of an agent to launch model-specific attacks, including prompt injection or selective delivery of manipulated content. However, the service cannot directly query the backend model and must instead collect observable responses through its interactions with the agent, making identification challenging.
In this paper, we present Completely Automated Preference Test to tell LLMs Apart (CAPTA), a model identification approach inspired by CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart), which distinguishes humans from automated programs. CAPTA presents multiple-choice questions as verification challenges, using differences in models' selection preferences to identify the backend LLM. It selects questions based on cross-model option-generation diversity and uses LLM-guided search to optimize their option sets. Our evaluation shows that CAPTA achieves 99.0% mean identification accuracy with only 10 questions across 25 LLMs from 10 model families. We further evaluate CAPTA with four widely used agents and seven representative LLMs, achieving 99.7% mean identification accuracy across all 28 agent-LLM combinations with 30 submitted answers.

---


### 217. [Are We Rewarding the Wrong Module? Module-Specific Policy Optimization for Multimodal Reinforcement Learning](https://arxiv.org/abs/2611.32687)

**<font color=#1a73e8>作者：</font>** HuiSeong Cho, Jun Yeong Park, Yu Rang Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) based on Group Relative Policy Optimization (GRPO) has been widely adopted to enhance the multimodal reasoning of multimodal large language models (MLLMs). However, existing methods share a common limitation of Module-Level Credit Entanglement, in which the vision encoder, projector, and LLM modules are jointly optimized using the same advantage signals even when perceptual correctness and final-answer correctness differ. To address this limitation, we propose Module-Specific Policy Optimization (MSPO), a framework that separates perceptual and outcome-based learning signals across model modules. Specifically, MSPO uses responses to perception checklists comprising auxiliary questions about visual information to derive an advantage for training the vision encoder. From these responses, MSPO computes the Confidence-aware Perception Reward (CaPR), using a perception sign obtained by thresholding checklist accuracy to determine reward direction and posterior confidence from a Beta distribution over latent perception accuracy to scale reward magnitude. We then derive the vision advantage through group-relative normalization of CaPR and scale it using main-task success rates. This advantage guides updates to the vision encoder, while the projector and LLM retain outcome-based GRPO updates. Extensive experiments on seven mathematical and general reasoning benchmarks demonstrate that MSPO outperforms existing RL-tuned models on average at both the 3B and 7B scales.

---


### 218. [Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs](https://arxiv.org/abs/2611.32705)

**<font color=#1a73e8>作者：</font>** Dan Zlotnikov, Nadav Alali, Ohad Ben-Shahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models (VLAs) enable simultaneous processing of egocentric video and textual target descriptions to produce action commands for embodied tracking platforms. However, these platforms rarely move exactly as commanded, in part due to unexpected environmental disturbances such as wind, unleveled terrain, and road bumps. Here we study how such models handle uncommanded egomotion. First, we explore performance across diverse disturbances by benchmarking three tracking VLAs on three datasets. We find that models differ in which environmental disturbances hurt them most, but all are sensitive to sudden target loss. Tracing egomotion from pixels to emitted actions, we identify two gaps. In representation, motion is reliably recovered through explicit relations between frames, but aggressive compression of past frames weakens small-motion readouts. In action, large rotations do reach the decision state, yet the decoded direction carries only a few percent of a mirrored rotation's effect on the turn. Targeting both gaps, we fine-tune one model, Uni-NaVid, on data amounting to just 1.7% of its original training set in a ladder of analysis-motivated variants. These gain 5-22 points after target-loss without degrading clean success; after a smooth loss, the best one improves success by 72% (relative), recovering 76% of its gap to clean. We also show that targeted fine-tuning improves recovery partly via a text-mediated action dependency, without new architecture, large-scale data collection or training from scratch.

---


### 219. [ASCENT: A Benchmark for Evaluating and Advancing Stepwise Diagnostic Reasoning in Large Language Models on Common Clinical Scenarios](https://arxiv.org/abs/2611.32734)

**<font color=#1a73e8>作者：</font>** Yera Choi, Yeong Hwa Kim, Jaedeok Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at medical question answering yet are rarely evaluated on the stepwise diagnostic reasoning that defines real clinical workflows, where impressions are revised as information accumulates. We build Annotated Stepwise Clinical rEasoning for NaturalisTic Diagnosis (ASCENT), a clinician-annotated benchmark and training resource of 3,078 stepwise problems derived from MedQA-USMLE that decomposes each vignette into EMR-aligned steps (Findings, Impression, supporting Rationale), enabling evaluation of intermediate reasoning under incomplete information.
Experiments and training with ASCENT revealed insights into how current LLMs handle stepwise diagnostic reasoning. Even strong reasoning models that perform well on MedQA-USMLE leave substantial headroom on ASCENT, and general-purpose frontier models trail further, exposing a persistent gap between fully informed and stepwise diagnosis. Fine-tuning Qwen2.5-7B and 32B on ASCENT yields measurable F1 gains over both pre-trained and HuatuoGPT-o1 CoT-trained baselines, with gains driven primarily by precision. Complementary robustness analyses (counterfactual perturbation, format-vs-content control, judge agreement, and rollout) further show that ASCENT-fine-tuned models rely on the diagnostic content of prior impressions rather than imitating their output format, while error propagation under rollout remains a key challenge for clinical deployment.

---


### 220. [Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation](https://arxiv.org/abs/2611.32736)

**<font color=#1a73e8>作者：</font>** Zihao Liu, Zekai Zhang, Shengming Yin 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a generator on a complete high-resolution canvas requires long image sequences and substantial computation, yet local regions can still exhibit unnatural repetitive stripes when training resources are limited. We introduce Qwen-Image-HD, which adapts Qwen-Image 2.0 to high-resolution synthesis through local training and blockwise autoregressive generation. Each prediction covers a target tile at 1K scale, conditioned on high-resolution upper and left neighbors and a compressed historical thumbnail. These conditions provide adjacent fine-scale structures and an overview of the scene generated so far. To integrate these complementary cues, we map both forms of history and the target to a shared canvas coordinate system to express their spatial relationships and scale differences. On Qwen-Image-Bench at 4K, Qwen-Image-HD achieves stronger overall evaluation performance than direct 4K generation with FLUX-3-Image-Klein. Compared with full-image 4K supervised fine-tuning of the same backbone, it achieves better generation quality with lower training compute and higher inference efficiency, while exhibiting fewer unnatural repetitive stripes in original-resolution comparisons. We further introduce a Wavefront-AutoRegressive inference schedule that generates tiles on the same anti-diagonal concurrently across GPUs to reduce single-image latency.

---


### 221. [Beyond Fixed-Context Likelihood: Zero-Shot AI-Generated Text Detection via Context Perturbation Discrepancy](https://arxiv.org/abs/2611.32778)

**<font color=#1a73e8>作者：</font>** Yifan Tang, Jingran Li, Yihao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The same increase in token log probability from earlier context can be typical at one position and unusually large at another. We introduce Context Perturbation Discrepancy (CPD), a zero-shot detector that measures this gain relative to what a single pretrained language model expects. Keeping the passage fixed, CPD scores each observed token under its full prefix and under a short window of recent tokens. Under the full-prefix distribution, the expected gain equals the KL divergence from that distribution to the restricted-prefix distribution. CPD subtracts this expectation from each observed gain and scales the sum of the signed deviations by its analytical reference standard deviation. On unedited human and AI texts from GEN, DetectRL-X, and HART, subtracting the expected gain raises AUROC by 32.78-35.81 percentage points at the same variance scale. CPD outperforms seven zero-shot baselines, averaging 94.80% AUROC and 79.60% recall at a 5% false-positive rate. On original and edited HART passages, the same scores separate texts more clearly by draft origin than by the benchmark's final-expression labels (89.15% versus 65.50% AUROC). Code is available at this https URL.

---


### 222. [C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems](https://arxiv.org/abs/2611.32780)

**<font color=#1a73e8>作者：</font>** Guowei Guan, Yurong Hao, Jiaming Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are transforming recommender systems into content-aware decision systems. In these systems, multimodal compression and cross-modal fusion are often viewed as robustness-enhancing mechanisms against content manipulation, as compression can filter noisy signals and cross-modal consensus can suppress inconsistent anomalies. We challenge this assumption by showing that the same process can expose a compression-to-consensus (C2C) bias in ranking decisions. Signals that remain salient after compression and receive consistent support across modalities can gain disproportionate influence in candidate comparison, offering an exploitable direction for content manipulation. In this paper, we introduce C3H, a novel inference-time attack that exploits this vulnerability. Rather than relying on noisy perturbations or training-time poisoning, C3H promotes a target item by tailoring its multimodal content to align with the decision criteria implicitly expressed by the recommender. Extensive experiments demonstrate that C3H substantially increases target-item exposure while maintaining overall recommendation utility. Code is available at this https URL.

---


### 223. [Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA](https://arxiv.org/abs/2611.32782)

**<font color=#1a73e8>作者：</font>** Daehee Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) keep the feed-forward network (FFN) intermediate width identical across every layer, a convention inherited from the original Transformer. Yet mechanistic work suggests layers at different depths do qualitatively different work, raising a natural question: are their capacity demands also non-uniform, and if so, can a fixed parameter budget be allocated more wisely than uniformly? To probe this, we apply principal component analysis (PCA) to the input of each FFN down-projection and measure, for every layer, its intrinsic dimensionality as the smallest number of principal components needed to reconstruct the activation up to a fixed cosine similarity. Scanning 58 open-weight LLMs spanning 14 families and 70M to 72B parameters, we find a recurring middle-heavy profile in which middle layers carry higher intrinsic dimensionality than edge layers; the profile is robust to the calibration corpus, even across English and Chinese, and is largely preserved through post-training fine-tuning. As a direct test that this signal is structurally meaningful, we use it to guide width pruning in a knowledge-distilled student under a matched parameter budget: the PCA-guided allocation outperforms the uniform-width convention by +2.3 points on Qwen3-8B and +2.5 on Qwen2.5-3B, while lower-dispersion teachers show smaller gaps (+0.9 on Gemma-3-4B, +0.5 on LLaMA-3-8B), and a budget-matched inverted control does worst on all four teachers. Across these four teachers, the size of the gap tracks how unevenly the teacher's intrinsic dimensionality is distributed across layers (a single-number summary we call $\sigma_{99}$), and the advantage persists through downstream supervised fine-tuning. Code is available at this https URL.

---


### 224. [Is Prosody Encoded in the Neural Audio Codec Mimi?](https://arxiv.org/abs/2611.32795)

**<font color=#1a73e8>作者：</font>** Nicolas Ballier, Artem Saloev, Erin Pacquetet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural audio codecs (NACs) have become a fundamental infrastructure for modern speech-language models, discretizing continuous speech signals into token sequences that enable large language models to process and generate audio. Most research evaluates codec quality at the decoding phase, assessing the naturalness of reconstructed speech. However, little research investigates what phonetic information is captured during encoding. In this paper, we investigated the potential correlates of prosody in the NAC Mimi, a codec used by conversational speech agents such as Moshi and Sesame and used in downstream tasks such as speech-to-speech translation (Hibiki).

---


### 225. [Scaling Laws of Ensemble Uncertainty in Language Models](https://arxiv.org/abs/2611.32801)

**<font color=#1a73e8>作者：</font>** Siamak Ravanbakhsh, David Nitchi, Khang Ngo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many use cases for large language models (LLMs)---from AI safety to exploration and human interaction---can benefit from epistemic uncertainty estimates. We argue that existing Bayesian Deep Learning solutions, which are often restricted to a fixed model family, fail to capture the full epistemic uncertainty at practical LLM scales. This is because the error due to the bounded capacity of the model family remains invisible to disagreement among models supported by the prior. We relate this error to the well-known power-law scaling of LLM loss with model size. We then show that a second power law quantifies the shrinking disagreement within ensembles as model size increases. Its slower decay relative to the capacity law above suggests that ensembles capture a growing share of epistemic uncertainty and become more competitive as an axis for scaling, compared to a single larger model. Finally, a third power law quantifies the loss of ensemble diversity as members share a larger fraction of training before branching, and therefore identifies a further limitation, beyond the capacity error, for LoRA ensembles and optimization-based or second-order methods that approximate uncertainty around a single training solution. At a high level, these findings suggest diverse ensembles can be a promising axis, both for scaling and uncertainty quantification at larger scales.

---


### 226. [Sample-Efficient In-Context Adaptation via Sleep](https://arxiv.org/abs/2611.32802)

**<font color=#1a73e8>作者：</font>** Sangyun Lee, Zhang Enyan, Michael Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to learn and generalize from limited experience, or sample efficiency, is a cornerstone of intelligence. How can we build language models that turn a few user interactions, a few snippets of unfamiliar code, or a handful of experimental results provided in context into knowledge that generalizes? Prior work has found that sleep, a process where the model performs $N$ recurrent forward passes to refine its representations of a chunk of context, can improve long-context reasoning (specifically, within SSM-attention hybrid models). We study whether this method also improves in-context adaptation on general, non-synthetic tasks for transformer language models. To this end, we pre-train language models up to 1.2B-parameters on up to 100B tokens with sleep mechanisms. Notably, longer sleep (i.e., using a larger number of recurrent forward passes $N$) enables the model to learn faster in-context on multiple few-shot algorithmic, question-answering tasks, while also achieving lower next-token prediction loss on out-of-distribution evaluations. On held-out code, models with $N=2$ and $N=4$ match the no-sleep baseline's loss using $2.10\times$ and $2.39\times$ fewer tokens in-context, respectively. More broadly, we view our work as a step toward building models that have better tradeoffs between in-context adaptation and decoding latency.

---


### 227. [From Grammar Deltas to Token Masks: Incremental Constrained Decoding under Runtime Grammar Evolution](https://arxiv.org/abs/2611.32807)

**<font color=#1a73e8>作者：</font>** Hantao Hua, Jiming Su, Yonggang Che 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammar-constrained decoding enables large language models to generate outputs that satisfy formal constraints, but in code and domain-specific language generation, the relevant constraints are not always fully available before decoding and may emerge progressively from new declarations, inferred type information, or runtime analysis feedback. Existing structured-decoding engines efficiently handle fixed, predeclared, or previously seen constraint structures; however, when a first-seen grammar update changes the parser state induced by an already committed prefix, the straightforward solution reconstructs the constraint state under the updated grammar, repeating parsing work already performed over the prefix. We introduce GramDelta, an incremental framework for constrained decoding with append-only runtime grammar updates. GramDelta maintains parse state over the committed prefix and propagates only changes induced by newly added grammar rules through historical dependencies, avoiding prefix replay. It then maps the updated parse state to exact next-token masks via compilation-free factorized projection over shared historical charts, avoiding per-update mask-cache recompilation. GramDelta therefore preserves the result of full reconstruction while making update cost sensitive to the actual impact of a grammar change. Experiments across four model configurations show that GramDelta adds negligible overhead without updates; under sustained runtime grammar evolution, it reduces median first-seen grammar-update latency by 10.7--11.5x and reduces the additional TPOT overhead over unconstrained decoding by 53.1--81.9% relative to the strongest reconstruction baseline. These results enable efficient constrained decoding when constraints progressively emerge and evolve with the generated prefix.

---


### 228. [EPRO: Robust Policy Optimization Through an Imperfect Execution-Policy Predictor](https://arxiv.org/abs/2611.32810)

**<font color=#1a73e8>作者：</font>** Yibo Wang, Changyi Yang, Yuanxin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL for LLMs often separates rollout generation from policy training. Although the two numerical engines share model parameters, they can induce different policies. This creates a challenge beyond correcting a known training-inference mismatch: during learner updates, the execution policy corresponding to the current parameters cannot be directly observed. We view this as optimizing an unobserved execution policy through an imperfect predictor of its evolution. This perspective raises two fundamental questions: how can we estimate the execution policy's response to learner updates, and how much should we trust that estimate when optimizing the actual execution policy? We introduce Execution-Policy Robust Optimization (EPRO) to address these challenges. Starting from the observed rollout-time execution policy, we use training-policy changes to construct a differentiable predictor of the current execution policy, whose score yields Transported Score Centering (TSC). Our robust-improvement analysis reveals how prediction error limits the magnitude of reliably justified updates. For practical implementation, we introduce Policy Shift as an observable proxy for prediction risk and use Shift-Aware Soft Clipping (SSC) to attenuate risky updates. Across four Qwen3 model settings, EPRO achieves the highest average held-out accuracy among the compared methods on seven mathematical reasoning benchmarks.

---


### 229. [Interactive Neural Computers](https://arxiv.org/abs/2611.32811)

**<font color=#1a73e8>作者：</font>** Ross Murphy, Marcel Hedman, Gabriel Brostow  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI agent, must adapt to whatever the operating system presents. This is limiting when someone needs a different workflow, or an interface suited to hands-free use or a disability. We explore an overlooked alternative. Rather than training an agent to operate an existing computer, we train a generative model to be the computer, predicting each next screen from past screens and the user's mouse and keyboard actions. Treating a desktop as an interactive world model raises problems that natural-video world models largely avoid. Without a camera pose to index memory, the model must remember content that has left the screen without any geometric cues. Arithmetic in a terminal has to be exactly right, not merely plausible. Small interface text must also stay legible at interactive frame rates. Our Interactive Neural Computer is structured like a Neural Turing Machine and starts to address these problems with three modules trained end to end from pixels and actions. A surprise-gated slot memory, supervised by latent next-frame prediction (MEMORY-JEPA), stores what is off screen. An exploratory query bridge brings in the reasoning of a pretrained VLM, and a residual renderer predicts only the latent changes between frames. In long closed-loop rollouts, our model recalls occluded files in 64.2% of trials (chance is 33.3%), compared with at most 56.0% for recurrent and sliding-window baselines. It also raises terminal-text OCR accuracy from 1.3% to 50.1%. Finally, because the memory is explicit, it can be transplanted at test time to causally change what the model renders.

---


### 230. [SpatialArena: Where Do Geometric Foundation Models Stand?](https://arxiv.org/abs/2611.32816)

**<font color=#1a73e8>作者：</font>** Yu Chen, Haosen Yang, Su Ee Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D perception is shifting from task-specific pipelines to geometric foundation models: monocular depth networks, feed-forward 3D/4D reconstruction models, and vision--language models that predict geometry. However, their progress cannot be measured reliably. Published numbers are not comparable, because every paper samples frames, sets resolutions, and selects test splits differently. They are not robust because the alignment required for every up-to-scale prediction can outweigh the gap between models: fitting depth in the wrong space nearly triples its error, and standard trajectory alignment understates the error of failing methods by up to $2.6\times$. And they rarely cover long recordings, dynamic scenes, or aerial views. We present SpatialArena, an open arena that scores geometric models with the same metrics and rules, with robust and deterministic alignment. SpatialArena spans five tasks, from monocular depth to SLAM. It covers 23 public datasets with 418,929 images across indoor, outdoor, aerial, object-centric, and dynamic scenes, together with Spatial Arena, our own captures with accurate poses and depth. Evaluating 52 models, we find that single-image depth is close to saturation on public benchmarks but not on large, uncontrolled scenes, and that progress now comes from consistency across frames and views, where feed-forward 3D/4D models match or surpass monocular specialists and overtake video depth models. The benchmark, toolbox, and leaderboard will be publicly released.

---


### 231. [Beyond Image-Text Pairs: Aligning Semantic Changes for Fine-Grained Visual Understanding](https://arxiv.org/abs/2611.32817)

**<font color=#1a73e8>作者：</font>** Yujie Sun, Zeqing Wang, Shuang Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-text alignment serves as a foundation for modern vision-language models (VLMs), yet prevailing training paradigms provide limited supervision for learning how semantic changes correspond across modalities. To address this limitation, we propose a post-training method that learns cross-modal semantic change correspondences through controlled visual and textual variations. Specifically, we introduce a Semantic Difference Alignment (SDA) loss which can align the directions of corresponding visual and textual representation changes. We combine our proposed SDA with pairwise sigmoid matching to jointly learn image-text correspondences and cross-modal semantic changes, encouraging more fine-grained and discriminative visual representations. To support this learning, we construct VarFamily-40K, a dataset of image-text pairs with controlled cross-modal semantic variations. Experiments demonstrate consistent improvements in compositional understanding and downstream classification performance, alongside further gains on multimodal tasks when the adapted visual encoder is integrated into VLMs.

---


### 232. [PhysMend: Verification-Guided Program Refinement for Physics-Aware Video Generation](https://arxiv.org/abs/2611.32821)

**<font color=#1a73e8>作者：</font>** Meilong Xu, Ziyi Zhao, Bhagyashree Puranik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generative models synthesize realistic scenes, yet their interactions often violate physics. A ball dropped onto sand should displace grains and settle into a crater, whereas a generated video may show it passing through the surface or leaving the sand flat. Post-hoc methods typically score generated videos with a vision-language model (VLM), but such scores offer limited guidance on which object or parameter to modify, and each correction costs another synthesis. Simulation-based pipelines instead run fixed stages before synthesis, so simulation errors reach the video. To address these limitations, we present PhysMend, a training-free framework for verification-guided program refinement. PhysMend describes the target event as an editable physical program of grounded objects, events, and required relations, paired with tunable execution parameters. Our key insight is to verify and repair the event on its simulated rollout and on the depth video that conditions the generator (depth control) rather than on generated videos, enabling quantitative violation measurement, targeted editing, and fast re-verification before synthesis. A hybrid verifier evaluates semantic event consistency, physical plausibility, solver stability, and visibility in the depth control. VLM judgments are confined to event semantics and cannot override failed physical measurements, which limits the impact of VLM hallucinations. Each failed check localizes the program fields eligible for repair, and its measured violation scales a bounded update of their parameters. Only accepted depth control reaches the generator, which runs once per input. Experiments on the commonly used benchmarks Physics-IQ, PhyGenBench, and VBench-2.0 demonstrate substantial gains across different generator backbones; for example, PhysMend raises the overall Physics-IQ score of Wan-VACE from 27.33 to 39.40.

---


### 233. [SAVERA: Bridging Frozen Vision and Language Models via Sparse Alignment and Visual Evidence Reuse](https://arxiv.org/abs/2611.32828)

**<font color=#1a73e8>作者：</font>** Jiajun Shen, Chuancheng Shi, Jiayi Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Independently pretrained vision and language models may learn shared structures of the same underlying world, providing a foundation for combining them to build multimodal capabilities. However, a key challenge remains in aligning cross-modal feature representations while preserving access to visual information before and after language adaptation. To this end, we propose sparse alignment with visual evidence-guided residual adaptation (SAVERA), a framework that combines frozen vision and language models through bidirectional alignment in a shared sparse space and prompt-guided residual fusion. Specifically, we first present shared-space projection, activation reconstruction and encoding (SPARE), which represents original visual, adapted visual, and textual features through shared soft-gated sparse encoding, with branch-specific reconstruction to preserve their respective information. Second, we devise bridge--text embedding and activation matching (BEAM), a bidirectional cross-modal alignment module that aligns adapted visual and textual features at both the sample and neuron levels, establishing fine-grained cross-modal correspondence. Finally, we introduce prompt-conditioned residual integration of vision and adapted features (PRIVA), a prompt-guided residual fusion module that models vision--language interactions through gating and attention and integrates complementary information from original and adapted representations through residual fusion. Extensive experiments show that SAVERA achieves competitive performance on image captioning and visual question answering while reducing object hallucination.

---


### 234. [Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models](https://arxiv.org/abs/2611.32848)

**<font color=#1a73e8>作者：</font>** Tanzeel Abbas, Tehseen Zia, David Windridge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluations of quantized language models attribute the change in a benchmark score to quantization. We write the measured change as the true change plus a term contributed by the instrument. Instrument error that is the same at every precision can shrink a paired comparison but cannot create or reverse an effect. Error that interacts with quantization can do both, and it is reported as an effect of quantization. We estimate this interaction for four measurement choices in 8 instruction-tuned models below two billion parameters, at float16, LLM.int8() and NF4, on identical items. Measured against labels from two human annotators, the 4-bit rise in harmful compliance is about half to two-thirds of the rise in non-refusal that a corrected key word detector records. Cloze and lettered multiple-choice scoring disagree about the effect of quantization far more than their noise allows: their estimates correlate at \r{ho} = 0.10, against a ceiling of about 0.77. LLM.int8() answers and generations depend on which items share a batch, and padding alone changes its answers. Rounding activations to 8 bits is enough to produce this dependence. NF4 is batch-invariant. The two largest reported calibration losses are response-bias shifts. We release item-level predictions, option scores and human annotations, and give recommendations for evaluating compressed small models.

---


### 235. [Fresh Keys, Stale Secrets: Numeric Leakage across Linked LLM Prompts](https://arxiv.org/abs/2611.32864)

**<font color=#1a73e8>作者：</font>** Jian Li, Qinglin Zhao, Shuoyao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Small businesses repeatedly ask cloud language models about the same confidential prices, unit costs and margins. Numeric prompt disguises for such numbers are evaluated one prompt at a time, but a provider sees a firm's history, in which each fresh secret gives a new, independent view of the same numbers. Since real costs are not public, we measure on synthetic firms with known values how much an honest-but-curious provider recovers when it knows the disguise algorithm, holds sector-level price and margin statistics, and links a firm's queries. In one prompt, per-field scaling, a fixed-axis instantiation of Zhang et al.'s order-preserving substitution and Pr$\varepsilon\varepsilon$mpt's released sanitizer keep the attacker's margin-hit advantage over a prior-only guess between -0.6 and +4.4 percentage points. After 16 linked queries with fresh secrets, every disguise we test (Pr$\varepsilon\varepsilon$mpt at $\varepsilon\geq 0.5$) has a target recovered significantly more often: under the order-preserving substitution, margin recovery rises from 25.0% to 59.4%. The same attacker recovers 29.4 percentage points more margins with fresh maps than with one reused map. Theory explains the contrast: one reused secret bounds all queries by a single full-precision view of the fields shown, whereas fresh scaling keys are identifiable. Except for Pr$\varepsilon\varepsilon$mpt at $\varepsilon=0.5$, the gains persist when the attacker's prior comes from another population model and when values drift by up to 5% between queries; on our firms, whose prose cues are weak, reading the prose with a language model adds at most 2.5 points. Code and data: this https URL

---


### 236. [Weight Scale Rebalancing: Transferable Training Recipes for Transformers](https://arxiv.org/abs/2611.32866)

**<font color=#1a73e8>作者：</font>** Yikun Hou, Naomi Graham, Alp Yurtsever  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training Transformers requires careful hyperparameter tuning, which becomes increasingly costly for large models. We introduce UDV-Rebalance (UDVR), a reparameterization that inserts an auxiliary diagonal matrix $D$ between naturally paired weight matrices $(U,V)$ appearing throughout Transformer architectures. UDVR periodically rebalances the factors to maintain unit-norm columns in $U$ and unit-norm rows in $V$, with $D$ absorbing the corresponding scales. With rebalancing, a single hyperparameter setting of UDVR remains effective across model scales, architectures, and data distributions. This yields a tuning-free rule that adapts to each weight matrix using only its dimensions. We fit this rule once on ViT models trained on CIFAR-10 and CIFAR-100, and it remains valid when the activation function or the optimizer is changed. The same rule transfers to new image domains in DomainNet, to ViT, Swin, and MaxViT on ImageNet, and to language-model pretraining with up to 1.3B parameters. UDVR consistently outperforms Weight Normalization and $\sigma$Reparam and matches a vanilla baseline whose hyperparameters are swept on each target model.

---


### 237. [MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques and Their Interactions](https://arxiv.org/abs/2611.32873)

**<font color=#1a73e8>作者：</font>** Natalia Frumkin, Alireza Khodamoradi, Kristof Denolf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in low-precision representation have introduced several microscaling numerical formats for LLM quantization. By sharing a scale factor across groups of 16 or 32 elements, these formats enable aggressive low-precision quantization with minimal accuracy degradation, particularly when combined with modern PTQ algorithms. Their accuracy depends on how the numerical format interacts with rotation, PTQ, and scale selection. We study the composability of PTQ configurations across six LLMs and three microscaling formats: MXFP6, MXFP4, and NVFP4, systematically varying Hadamard rotation granularity, PTQ algorithm, and scale-selection strategy. Our central finding is that effective quantization recipes are format dependent: both MXFP4 and NVFP4 support accurate 4-bit inference, but techniques that benefit one do not necessarily transfer to the other. MXFP4 benefits substantially from rotation and error-correcting PTQ, whereas NVFP4 gains less from rotation, consistent with its finer-grained scales capturing more within-block variation. Building on these findings, we introduce Midmax, a calibration-free scale-selection strategy that mitigates clipping error in power-of-two block scales and improves accuracy across a majority of the evaluated MXFP4 configurations. We show that pairing MXFP6 activations with MXFP4 weights recovers most of the accuracy lost at 4-bit and, on Llama-3.1-8B, matches or exceeds our in-house BF16 baseline. An additional study finds that augmenting MXFP4 with a per-tensor macroscale, a mechanism intrinsic to NVFP4, does not improve average accuracy, suggesting that global rescaling alone does not address the limitations of E8M0 block scales for MXFP4 quantization. Together, these results provide practical guidance for combining numerical formats, rotation, PTQ, and scale selection for accurate low-precision LLM inference.

---


### 238. [Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884)

**<font color=#1a73e8>作者：</font>** Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scores only the final answer, so it cannot teach the agent when to commit, because a lucky guess receives the same reward as an answer backed by evidence. During training, however, the simulator can compute the exact posterior over the answer at every step and tell whether the evidence is already enough. We propose Reinforcement Learning with Verifiable Beliefs (RLVB), which rewards the agent for taking further steps while this posterior still allows several answers and for committing once the evidence is sufficient. The reward needs no judge, critic or reward model, and it never reads the belief line the agent writes before each action. We also introduce Pro Worlds, a benchmark of visual puzzles where the agent views a large world through a small window. We evaluate three vision-language models on three benchmarks, two of which are never seen in training. RLVB improves the base model in all nine settings, by 17.1% on average. Under the outcome reward, GRPO and PPO fall below the base model on average. RLVB also outperforms PPO with a process reward from an LLM judge by 9.3% on average while using 1.6 times fewer GPU-hours. The trained agent answers with sufficient evidence in 51%, 12% and 74% of the episodes on the three benchmarks, against 8%, 0.4% and 36% for the base model. Its accuracy gain therefore comes from answering more often at high levels of evidence. The belief line shows how the agent reaches this evidence: it acts on its own belief. It commits at only 0.1 to 2.2% of the turns at which the evidence is insufficient and its line still names several answers, against 3 to 68% for the base model.

---


### 239. [Joint Detection of Constructive Speech, Hate Speech and Agreement in Online Conversations](https://arxiv.org/abs/2611.32889)

**<font color=#1a73e8>作者：</font>** Ida Dencker, Simon Karg, Kenneth Enevoldsen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online hate speech is an ever-growing issue with negative impacts on both groups and individuals, potentially causing users to withdraw from online conversations and debate. With some prominent social media platforms reducing their moderation efforts, constructive speech has emerged as an alternative strategy for countering hate. Automated detection of constructive and hateful speech can aid monitoring and improve understanding of their prevalence and online dynamics. In this work, we collect and annotate a large dataset of English and Danish social media comments for hateful tone, constructive tone, and agreement with parent comments. We fine-tune several multilingual LLMs to classify along these three dimensions and compare context-enriched and non-context-enriched model architectures. The E5-large LLM performs best on both the context-enriched (82% average F1) and non-context-enriched (81.6% average F1) classification tasks, demonstrating the potential of multilingual LLMs for scalable detection of hateful and constructive speech across languages.

---


### 240. [InstructReplay: Replaying Assistant Turns to Preserve General Behavior During Factual Fine-Tuning](https://arxiv.org/abs/2611.32918)

**<font color=#1a73e8>作者：</font>** Xiaofeng Shi, Qian Kou, Hua Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning an instruction-tuned language model on new facts often erodes its general abilities. We find that standard fine-tuning lowers instruction-following, reasoning and coding benchmarks by 35 points on average, and that these losses track a collapse in answer length: fine-tuned models at least halve their responses, and the further a response drifts from the initial model's length, the more often it fails. We propose InstructReplay: the initial model answers a set of general instructions once, and during fine-tuning the model is kept close to the initial model on these answers. Across three model families and two domains, InstructReplay reduces the average decline on five general benchmarks from 28.1 to 2.4 points and keeps answer length close to the initial model's, while learning the new facts as well as standard fine-tuning. It balances learning and retention better than seven adaptation methods in all six settings. Controlled comparisons attribute the gain to replaying the model's own answers to general instructions rather than to the form of the loss.

---


### 241. [Efficient Video Retrieval Augmented Generation via Token Allocation](https://arxiv.org/abs/2611.32938)

**<font color=#1a73e8>作者：</font>** Ayush Barik, Fan Lai, Francis Y. Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient long-video understanding requires identifying relevant evidence while minimizing the tokens processed by vision-language models (VLMs). Existing video retrieval-augmented generation (RAG) methods rely on frame selection and token compression, but overlook how much each additional token is worth. We introduce Lembas, a plug-and-play framework that formulates video RAG as a token allocation problem over frames and subtitles under a shared budget. Our key insight is that the value of a token diminishes within each item and decreases further as similar evidence receives more tokens. Lembas captures both effects in a single objective and solves it with an efficient iterative water-filling algorithm that has a provable convergence guarantee. For multi-turn conversations, Lembas reuses the tokens processed in earlier turns and refines relevance with the VLM's attention at no extra cost. Our evaluations show that Lembas improves accuracy by up to 7.2 percentage points over state-of-the-art baselines at comparable compute. On multi-turn video understanding, Lembas achieves up to 1.5 percentage points higher accuracy with 1.7-17.3x fewer TFLOPs.

---


### 242. [One Style Fits All? Cultural Values Embedded in Conversational AI via a People-Pleasing Lens](https://arxiv.org/abs/2611.32939)

**<font color=#1a73e8>作者：</font>** Yi-Jun Chen, I-Tsen Hsieh, Li-Wun Chang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems trained on large-scale web corpora inevitably encode the cultural values and interactional norms embedded in their training data, yet our understanding of how deployed LLMs reflect or reinforce culture-specific social expectations remains limited. This study examined how supportive versus challenging chatbot interaction styles shape user experience and continuance intention, and whether people-pleasing tendency (PPT) moderates these effects across cultures. Taiwanese (N = 49) and Korean (N = 52) participants completed a collaborative tourism-planning task. Results showed that: (1) supportive chatbots consistently led to higher continuance intention, satisfaction, and trust; (2) PPT did not moderate these effects; and (3) cultural variation emerged only in perceived threat, where higher PPT was associated with greater baseline threat in the Taiwanese but not the Korean sample. These findings reveal how a general-purpose LLM style may differentially activate culturally situated social scripts, raising implications for culturally inclusive conversational AI design.

---


### 243. [Do Vision-Language Models Know Their Own Visual Weaknesses? Probing Capability-Level Metacognition](https://arxiv.org/abs/2611.32940)

**<font color=#1a73e8>作者：</font>** Dohoon Kim, Taesup Moon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metacognition includes knowing one's own strengths and weaknesses across kinds of tasks, not only judging whether a single answer is correct. We test whether vision-language models (VLMs) know in advance which kinds of visual tasks and image conditions are hard for them, across a wide range of open and proprietary models. Because some tasks are hard for every model, we separate what a model knows about this shared difficulty from what it knows about itself. We find that VLMs know little in advance about their visual weaknesses. They misjudge their overall accuracy and do not even know which kinds of tasks are hard for every model, and most misjudge how degraded images affect them. We further train VLMs to predict their own accuracy, which teaches them their own level of accuracy on kinds unseen in training but not which kinds are hard for them. However, information about these weaknesses appears once a model starts solving. On a few unlabeled questions of a kind, the probability a model assigns to its own answers follows weaknesses particular to the model, across kinds of tasks and image conditions. VLMs thus hold information about their own weaknesses that their stated predictions do not yet reflect. By separating what is particular to a model from what holds for every model, our evaluation offers a test for methods that aim to teach VLMs their own weaknesses, and the answer probability offers them a signal to start from.

---


### 244. [ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks](https://arxiv.org/abs/2611.32946)

**<font color=#1a73e8>作者：</font>** Vincent Koc, Aditya Washikar, Rishab Naveen Venkataraman 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The use of AI agents among the general public has been increasing exponentially throughout 2026, though it is often hard for users to determine which configuration is most effective for their personal use. To help provide clarity here we introduce ShellBench, 100 day-to-day tasks based on more than 10 million user requests, each set in a realistic workspace with messy files and competing data sources, and graded for both correctness and safety. We evaluate 12 models across 5 agent harnesses at 3 reasoning levels for a total of 53,100 rollouts, 20% of which are on tasks designated for public release. We find that model choice impacts performance more than harness choice, but the three leading models differ by only 1.1 percentage points. GPT-6.1 Sol passed 61.4% of attempts at about one-sixth of GPT-6 Astra's estimated token cost per attempt, while GPT-6 Astra led at 62.5%. We also found that harness choice had little effect on either performance or safety with all harnesses scoring between 42.9 (Claude Code) and 45.2 (OpenClaw) for pass@1.

---


### 245. [OmniHarness-RSI: Modality-Aware Harness Evolution for Omnimodal Understanding](https://arxiv.org/abs/2611.32951)

**<font color=#1a73e8>作者：</font>** Shilin Ma, Xingming Shui, Jinglin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in harness-based recursive self-improvement (RSI) have improved video understanding by evolving executable agent workflows without updating foundation model parameters. However, extending this paradigm to omnimodal understanding remains challenging, as the heterogeneous and interdependent nature of multimodal perception and reasoning creates a complex evolution space, making targeted harness optimization difficult. To address these challenges, we propose OmniHarness-RSI, a modality-aware framework for evolving agent harnesses. Specifically, we factorize the evolution space into three capability dimensions: modality routing and collaboration, modality-aware evidence localization, and modality-specific perception. Based on this factorization, we construct a Factorized-Harness Agent integrating specialized perception experts and audio-video retrieval tools. We further introduce modality-guided harness evolution, which identifies deficiencies through structured modality-capability attribution and refines corresponding harness strategies through interactive code revisions and execution feedback. Validation-guided selection and held-out evaluation assess generalization within and across datasets. Experiments on WorldSense, Daily-Omni, and OmniVideoBench demonstrate test accuracy improvements of 8.86, 8.13, and 6.23 percentage points, respectively, consistently outperforming modality-agnostic RSI. The evolved harnesses also demonstrate cross-dataset transfer without adaptation, while reducing planner calls and viewed frames.

---


### 246. [LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving](https://arxiv.org/abs/2611.32954)

**<font color=#1a73e8>作者：</font>** Wentao Zhu, Ziao Sheng, Peng Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) serving engines offload the key/value (KV) cache from GPU memory to host DRAM and SSD so multi-turn and agent requests can reuse prompt prefixes. Capacity then limits service at two levels: external tiers govern prefix reuse before eviction, while the GPU KV pool bounds concurrent long requests, and lossy compression alters KV values and outputs. LoomKV brings lossless KV compression to both external tiers (tier mode) and the GPU pool (pool mode) on an unmodified engine. Using a calibrated per-head two-level 3-bit code over BF16 high bytes (sign and upper seven exponent bits), LoomKV stores BF16 KV at 0.71 of its raw size across nine models and FP8 KV at 0.85-0.87. In tier mode, TileStream writes exact-length records with length readback off the load path, leaving tier storage, eviction, and prefetch unchanged, and decompresses fetched records straight into scattered GPU pages. In pool mode, FragPack packs variable-length records into smaller shared-budget GPU pages read in place by a fused decode-attention kernel faster than FlashAttention-3 on BF16. Built with LMCache and vLLM, LoomKV makes compressed tiers act as 1.4x larger raw tiers on AgentX: across LMCache's LRU cliff, tier mode delivers 2.7-3.6x raw's goodput and 1.9-3.1x lower mean time-to-first-token (TTFT), shifts the cliff identically under other simulated replacement policies, and cuts repeated-prompt TTFT up to 1.7x via SSD-to-DRAM promotion. When tiers hold the working set, pool mode fits 1.31-1.34x as many GPU tokens, admitting 12 long requests with roughly raw's queue and goodput at 8. On an AI IDE trace where both tiers and the GPU pool are constrained, tier and pool modes raise goodput by 1.24x and 1.59x. Where raw capacity suffices, compression costs at most 2.2% throughput; tier mode is bit-exact with raw tiers, and pool mode matches FlashAttention-3's numerical accuracy.

---


### 247. [Attestation is All You Need: Toward a Zero-Trust Architecture for HPC AI Agents](https://arxiv.org/abs/2611.32958)

**<font color=#1a73e8>作者：</font>** Jie Li, Chenxu Niu, Tongyang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are beginning to automate data analysis, orchestration, and simulation steering in HPC environments, but they introduce a security problem that existing cluster defenses do not address: the hijacked authorized agent. An adversary can subvert an agent through prompt injection, poisoned shared data, compromised tools, or multi-agent coordination, then exfiltrate sensitive data through legitimate encrypted LLM API traffic. We propose behavioral attestation as a runtime defense for this setting. Our system, AEGIS, compiles task-derived behavioral constraints, monitors agent actions with ebpf-based syscall interception, verifies evidence against constraint profiles, correlates behavior across agents, and triggers slurm-level containment. On the real attestation path, AEGIS detects all four implemented attack classes with sub-second median latency at a 1-second interval and low measured verifier overhead. Controlled experiments show full attack-suite coverage, stronger detection than representative baselines, and no observed false positives on the evaluated benign workflows.

---


### 248. [Benchmarking Evidence Sufficiency in Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2611.32964)

**<font color=#1a73e8>作者：</font>** Nhat Ha Nguyen, Sudipta Chowdhury, Lokesh Das  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable driving VLMs must do more than answer correctly or localize relevant scene actors: they must determine whether the available visual evidence is sufficient to support an answer. Existing evaluations largely treat grounding and answerability as separate measurements, making it difficult to distinguish well-supported predictions from those localized to relevant but insufficient evidence. We introduce DriveAnswer, a benchmark of 20,151 questions across seven reasoning families, that operationalizes this distinction using matched strong- and weak-evidence configurations. Each pair preserves the underlying scene fact and semantic answer while changing whether the observations support answering, making abstention the appropriate response under weak evidence. On the six-family evaluation, the strongest zero-shot baseline reaches 67.31% strong-evidence accuracy, yet only 21.55% of matched questions satisfy both answer-abstain behavior and complete grounding. With controlled adaptation, Gemma-4-12B reaches 63.29% on this joint capability, nearly tripling its zero-shot performance. Qwen3-VL-8B exhibits the same broad improvement in evidence-sensitive answering and grounding. These results show that semantic correctness, evidence sufficiency, and grounding are distinct capabilities that should be evaluated jointly.

---


### 249. [Eliciting the Recall Capacity of Linear Attention](https://arxiv.org/abs/2611.32969)

**<font color=#1a73e8>作者：</font>** Johan Lindqvist, Antonio Orvieto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention models exhibit a disproportionate deficit relative to softmax attention in associative recall (AR) in language modeling. We investigate this gap through natural language evaluations, synthetic recall tasks, and targeted training interventions. Using a synthetic setting, we quantify the role of state-size in how many items can be recalled from memory and find a similar empirical scaling across the tested linear-attention architectures. Testing this relationship reveals that even a single layer at scale can learn to retrieve thousands of associations across long distances. Yet, standard language model training does not reliably teach a linear model to copy from context, whereas a comparable softmax model learns to do so. Considering this, we strengthen recall supervision during training through in-context sentence repetition and context-sensitive loss reweighting. Both methods improve recall-intensive benchmark performance and narrow the long-distance AR gap to the softmax baseline without changing the architecture, token budget, or number of optimization steps, at a slight cost to general language modeling. These targeted changes to training can thus elicit substantial but underutilized retrieval capacity in linear-attention models. These findings suggest that, although linear-attention architectures have substantial capacity for recall, their inductive biases and the demands of language model training make it difficult to develop this capability without dedicated incentives.

---


### 250. [Teaching Time Without Losing General Retrieval: Adapting Multimodal Embeddings for Time-Sensitive Video Retrieval](https://arxiv.org/abs/2611.32971)

**<font color=#1a73e8>作者：</font>** Toya Oyama, Rainer Lienhart, Shin'ichi Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In text-to-video retrieval, MLLM-based embedding models do well when the text describes the scene (general retrieval), but poorly when it describes actions and their direction (time-sensitive retrieval). TARA, a pioneering work, fine-tunes such a model on text triplets with temporal hard negatives; it improves time-sensitive retrieval but lowers general retrieval (mean R@1 over six benchmarks in our rerun on Qwen3-VL-Embedding-8B: 58.4->44.8), and its released model keeps general retrieval only when ensembled with Qwen3-VL-Embedding. Our goal is strong general and time-sensitive retrieval with one model and one vector per clip. Three findings lead to three simple components. Keep loss: general retrieval follows how far the output embeddings drift from the base model, not how far the weights move; we therefore keep them near the base model, which keeps most general retrieval even without general-domain data. Pair loss: the text embeddings of an action description and its reversed-direction version are well separated, but the video embeddings of a clip and its reversed copy are close; we therefore widen the gap between the video embeddings of each clip and its reversed copy, in the direction of the difference between their two text embeddings. Middle-layer LoRA: frames are combined in the middle layers, and temporal information peaks in or just after them; we therefore train LoRA only on these layers, which nearly matches training all weights on most time-sensitive benchmarks with 0.15% of the parameters and keeps general retrieval better. General R@1 stays at 58.4, while R@1 with each clip's reversed copy in the gallery rises from 55.5 to 63.2; the gains carry over to unseen benchmarks and InternVL2-8B-RA. The keep loss is also a remedy for the TARA recipe (general R@1: 44.8->57.8), and ensembling TARA with Ours gives the highest scores on RTime and unseen CiA among the compared models.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
