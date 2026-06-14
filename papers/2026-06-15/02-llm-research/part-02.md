# 🧠 大模型相关研究 | 2026年06月15日

> 本类共 **128** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-128](./part-03.md)

---

### 51. [X-MADAM-RAG: Diagnosing and Handling Chinese-English Evidence Conflict in Retrieval-Augmented Generation](https://arxiv.org/abs/2606.12903)

**<font color=#1a73e8>作者：</font>** Yongqi Kang, Yu Fu, Yong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems may receive evidence that is not merely noisy but mutually contradictory. This issue becomes particularly salient in multilingual settings, where retrieved Chinese and English evidence may support incompatible answer candidates. We study this problem through X-RAMDocs-ZHEN, a controlled Chinese-English benchmark derived from RAMDocs for diagnosing evidence conflict in RAG. The benchmark contains 300 examples across six balanced conditions, including monolingual support, bilingual agreement, reversed conflict directions, and conflict with optional noise. We further examine X-MADAM-RAG, an interpretable pipeline that decomposes evidence handling into per-document candidate extraction, visible-evidence repair, deterministic candidate grouping, and conflict-aware aggregation. On the original controlled benchmark with Qwen2.5-7B-Instruct, X-MADAM-RAG achieves 0.9667 strict accuracy and 0.9767 conflict-aware success, outperforming an evidence-normalized single-call baseline. However, a zero-call rule-only extractor reaches 1.0000 on the same benchmark, revealing strong template regularity. To probe this limitation, we construct a deterministic naturalized stress test that removes explicit answer templates while preserving candidate strings. On its 100-sample subset, rule-only extraction falls to 0.0000, but X-MADAM-RAG also drops to 0.3000 strict accuracy, below both naive and evidence-normalized baselines. A privileged oracle remains perfect, indicating that document-level extraction is the main bottleneck. These findings position X-RAMDocs-ZHEN and X-MADAM-RAG as diagnostic tools for controlled evidence conflict rather than as evidence of general hallucination detection or robustness to natural retrieval.

---


### 52. [SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/abs/2606.12908)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Yuxuan Lu, Yimeng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model agents are increasingly effective in solving realistic tasks through multi-turn tool use. However, training reliable tool-using agents remains challenging in practice. While reinforcement learning provides an on-policy paradigm for improving agents from their own environment interactions, its effectiveness depends heavily on the training task distribution. When tasks are fixed before training, the task distribution can become increasingly mismatched with the policy's evolving capabilities, causing many rollouts to be spent on uninformative tasks. We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks. SENTINEL follows a Controller--Proposer--Solver loop: the Controller analyzes failed trajectories and summarizes recurring error patterns, the Proposer generates executable tasks that stress these weaknesses, and the Solver is trained on the targeted tasks. On Tau2-Bench Retail with Qwen3-4B-Thinking-2507, SENTINEL improves Pass\^{}1 from 66.4 to 74.9 and outperforms RL on general synthetic tasks across Pass\^{}k metrics. These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents.

---


### 53. [MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback](https://arxiv.org/abs/2606.12916)

**<font color=#1a73e8>作者：</font>** Zehong Wang, Yijun Ma, Connor R. Schmidt 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular dynamics (MD) is the canonical in-silico method for atomistic molecular science, simulating molecular behavior from first-principle physics. Designing an MD pipeline for a new system requires substantial expert knowledge: running it on even one molecule is expensive, ruling out trial-and-error. We automate this expert pipeline-design process with an LLM agent. Unlike existing MD agents that orchestrate a predefined tool set, we treat pipeline design as open-ended code generation in which the agent's behavior is reshaped online by verbal reward. Specifically, we build MDForge, an LLM agent whose in-context update rule densifies the sparse reward via a multi-agent debate among physics experts. On three SAMPL host-guest binding free-energy benchmarks, MDForge automatically designs MD pipelines competitive with human experts. Deployed on a library of unseen candidate guests, its CB[7] pipeline discovers a novel binder that wet-lab competition NMR confirms is a high-affinity, picomolar CB[7] binder. Our data and code are available at this https URL.

---


### 54. [Polar: A Benchmark for Evaluating Political Bias in LLMs](https://arxiv.org/abs/2606.12922)

**<font color=#1a73e8>作者：</font>** Sangho Kim, Heejin Kim, Yoonhee Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political bias in large language models (LLMs) is increasingly significant, but difficult to measure reproducibly across political and linguistic contexts. We introduce Polar, a 4,026-instance multiple-choice benchmark that measures political bias through option-level likelihoods rather than prompt-based generation. Polar covers two ideological axes and eight issue categories derived from the Manifesto Project, and evaluates models in parallel across U.S. and South Korean political contexts. Across 38 LLMs, measured bias varies systematically with political context, issue category, model group, and presentation language. All models lean left-progressive on U.S. political content, but show more centered and mixed patterns on South Korean content. Translation experiments further show that presentation language alone can shift measured bias. These findings highlight the need for multilingual and cross-contextual evaluation of political bias in LLMs.

---


### 55. [Iterating Toward Better Search: A Two-Agent Simulation Framework for Evaluating Agentic Search Architectures in E-Commerce](https://arxiv.org/abs/2606.12924)

**<font color=#1a73e8>作者：</font>** Jetlir Duraj, Jayanth Yetukuri, Shuang Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a modular two-agent simulation framework for evaluating conversational shopping assistant architectures. An independent buyer agent, configured with personas, missions, and patience levels, is paired with an interchangeable responder that integrates with a real e-commerce search API. Holding the buyer constant across experiments enables controlled comparison of responder designs on identical scenarios. Using 2011 conversations across 14 persona buckets, we establish four empirical findings. First, rolling-window memory outperforms intent-extraction memory on all quality metrics while being 35% faster per query. Second, illustrating rapid evidence-driven iteration, a systematic failure analysis of a responder version enables targeted fixes that reduce failure and near-failure rates by 62% across the full dataset. Third, swapping the responder LLM backbone from Gemini~2.5 to Llama~3.3~70B costs 0.16--0.45 points despite identical architecture. Finally, we document systematic philosophical disagreement between frontier LLM judges: Gemini rewards process correctness while Claude demands concrete outcomes, despite using the same evaluation prompt.

---


### 56. [MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling](https://arxiv.org/abs/2606.12935)

**<font color=#1a73e8>作者：</font>** Wenbo Chen, Puheng Li, Mengyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallel test-time scaling samples many reasoning traces and majority-votes their answers, improving LLM accuracy but requiring traces to run to completion, incurring substantial computational overhead. We observe that probing partial traces at intermediate checkpoints can extract current answers without disrupting generation, revealing an evolving aggregate vote. Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement. The rule separates two sources of uncertainty. It learns the trace-level switch probabilities that determine how much of the current margin is likely to be retained, while handling the harder question of where switching traces land through an adversarial bound calibrated from warmup traces. With true switch probabilities, MARS guarantees with high probability that the early-stopped answer matches the full-budget vote. In practice, a five-feature logistic model closely matches oracle switching behavior. Across three reasoning models and three competition-math benchmarks, MARS saves 25-47% of self-consistency tokens and 14-29% on top of DeepConf Online, a strong confidence-weighted baseline that already filters and truncates weak traces, while matching the accuracy of the corresponding full-budget baselines.

---


### 57. [PRISMR: Overcoming Parse Collapse in Multimodal Listwise Ranking via Parameterized Representation Internalization](https://arxiv.org/abs/2606.12942)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Xin Li, Annan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative listwise ranking with Large Multimodal Models (LMMs) aims to capture global list context in a single forward pass, but
its effectiveness degrades in long-context multimodal scenarios. We identify a recurring failure mode, parse collapse, where the
autoregressive decoder produces fluent yet incomplete rankings by silently omitting candidates and terminating early. This
failure stems from limited context utilization rather than simple formatting mistakes, making prompt engineering and constrained
decoding insufficient. We propose PRISMR (Parameterized Representation Internalization for Semantic Multimodal Ranking), a
framework that replaces transient in-context list processing with parametric structural conditioning. PRISMR uses a lightweight
hypernetwork to encode multimodal candidates in parallel and generate item-specific LoRA weights, which are synthesized into an
instance-specific adapter for a LMM. This paradigm enables more robust internalization of list structure while preserving the
base model. We further introduce a large-scale multimodal review-ranking benchmark for evaluation. Experiments demonstrate that
PRISMR substantially reduces parse collapse, improves listwise ranking performance, and transfers effectively across domains and
instruction-tuned backbones.

---


### 58. [Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory](https://arxiv.org/abs/2606.12945)

**<font color=#1a73e8>作者：</font>** Zhibao Chen, Qian Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget. Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known. We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank. We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting. In the realistic blind regime, a learned multi-factor value retains 0.770 \pm 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model. The learned weights are interpretable -- reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is correctly down-weighted for the forgetting decision. A controlled synthetic task with planted confounds confirms the learner recovers a separating weighting (1.00 retention) where uniform weighting fails (0.62). The substrate is open-source; all experiments run on a single CPU with no API calls.

---


### 59. [OpenMedQ: Broad Open Pretraining for Medical Vision-Language Models](https://arxiv.org/abs/2606.12953)

**<font color=#1a73e8>作者：</font>** Ibrahim Gulluk, Max Van Puyvelde, Olivier Gevaert  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present OpenMedQ, a medical vision-language model pretrained on the broadest fully-open medical mix to date: 14 datasets totaling ~3.35M pretraining samples spanning pathology, radiology, microscopy, and text-only clinical QA. OpenMedQ reaches state-of-the-art BLEU-1 on PathVQA (75.9), beating Med-PaLM M variants up to 562B parameters (~80x larger), and matches the best reported VQA-MED BLEU-1 (64.5). Its vision encoder, transferred to 8 unseen medical classification benchmarks under an identical downstream recipe, obtains the highest average macro-F1 (0.757) among BiomedCLIP (0.745), PMC-CLIP (0.745), PubMedCLIP (0.746), and a from-scratch baseline (0.616). We release our code and an interactive demo is publicly available as a reproducible baseline for the community.

---


### 60. [Multi-Modal Agents for Power Distribution Defect Detection: An Evaluation of Foundation Models](https://arxiv.org/abs/2606.12969)

**<font color=#1a73e8>作者：</font>** Quan Quan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The power distribution network is critical to reliable electricity delivery, yet traditional inspection methods face limitations in semantic understanding, generalization, and closed-loop automation. To address these challenges, this paper proposes a Multi-Modal Agent framework specifically for power distribution defect detection. Central to this study is the systematic evaluation of multimodal foundation models as unified cognitive engines. We rigorously assess their integrated performance across three critical capabilities: (1) Perception, where the model must accurately identify equipment and generate expert-level descriptions of defects; (2) Reasoning, where the model interprets visual findings to diagnose causes, assess severity, and plan maintenance strategies based on domain knowledge; and (3) Tool Usage, where the model acts as an autonomous operator to execute actions -- such as querying knowledge bases or generating work orders -- to achieve closed-loop maintenance. To support this evaluation, a domain-specific evaluation dataset and a comprehensive benchmark are developed. Experimental results demonstrate the strengths and limitations of current foundation models in these three dimensions, providing empirical evidence for deploying autonomous agents in high-stakes industrial environments.

---


### 61. [EPM-JEPA: Operator-Side Experience Modulation in JEPA-Family World Models](https://arxiv.org/abs/2606.12979)

**<font color=#1a73e8>作者：</font>** Vedant Pandya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> JEPA-family world models use a static predictor whose weights do not adapt when test-time dynamics diverge from training. We compare two mechanisms for incorporating accumulated experience into a JEPA predictor under distribution shift: operand-side injection, where a compressed experience representation is added as a residual to the predictor's hidden state (EI-JEPA), and operator-side modulation, where the same representation generates low-rank weight deltas via LoRA applied to the predictor's weights (EPM-JEPA). On a pre-registered comparison (Moving MNIST, gravity shift), EPM-JEPA (D_shift^{n=50} = 0.7848 +/- 0.0078, three seeds) differs from EI-JEPA (0.8238) by delta = 4.74% - Outcome C: a null result - by our stated criterion, a valid outcome. As a secondary, non-pre-registered observation, EPM-JEPA improves 1.90% over a no-memory baseline (0.8000), consistently across seeds, while EI-JEPA underperforms the baseline, indicating the benefit is specific to weight-level modulation. Our primary contribution is a mechanism analysis: the D_shift^{n=50} trajectory reflects three independent dynamical processes - buffer cycling, EMA target drift, and an intrinsic LoRA settling transient of +0.021 - rather than convergence to equilibrium. These findings motivate PEM-JEPA, a physics-grounded successor addressing this dynamical-peak limitation.

---


### 62. [Structured Testbench Generation for LLM-Driven HDL Design and Verification-Oriented Data Curation](https://arxiv.org/abs/2606.12983)

**<font color=#1a73e8>作者：</font>** En-Ming Huang, Yu-Hung Kao, Ren-Hao Deng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated testbench generation has become a critical bottleneck in large language model (LLM)-driven Register Transfer Level (RTL) workflows, where large numbers of candidate designs must be verified rapidly and reliably. Existing prompt-based approaches treat testbench generation as unconstrained code synthesis, yielding stochastic outputs with high token cost, low reproducibility, and insufficient coverage. To address this gap, we present STG, a Structured Testbench Generation framework that exploits the inherent structure of hardware designs to generate deterministic testbenches. As a direct verification tool, STG runs 720x faster than an iterative LLM-based testbench generation flow and higher rate of successful compilation, achieves higher coverage, and reduces false-pass verdicts on incorrect DUTs. STG also helps identify errors in RTL generation benchmarks by exposing faulty benchmark testbenches. As a data curation engine, it is 11x faster than LLM-based filtering on a single CPU core with 127x less energy, and the resulting distilled models provide state-of-the-art performance in our multi-benchmark evaluation. As a test-time scaling oracle, it reduces node count by 14-47\%. Our models are available at this https URL.

---


### 63. [DeepJEB++: Foundation Model-Driven Large-Scale 3D Engineering Dataset via 2D Latent Space Augmentation](https://arxiv.org/abs/2606.12994)

**<font color=#1a73e8>作者：</font>** Soyoung Yoo, Leekyo Jeong, Jinsu Ra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven engineering design is constrained by the lack of large-scale 3D datasets that pair geometry with physics-based performance labels. In particular, existing 3D data augmentation techniques have limitations in preserving subtle and diverse geometric variations, and it remains difficult to automate the subsequent simulation-labeling process, where boundary conditions vary depending on the generated geometry. We present DeepJEB++, a foundation-model-driven data-augmentation framework that expands a small seed set of jet engine brackets into a large, simulation-labeled 3D dataset under constrained resources. Our key idea is to augment in the data-rich 2D latent space, then transfer to 3D. In Stage 1, we fine-tune a pretrained 2D latent diffusion model on multi-view renders and synthesize novel views by latent interpolation, retaining manufacturable designs through a vision-language-model (VLM) quality filter. In Stage 2, the validated images are lifted to 3D meshes by a domain-adapted generative foundation model. In Stage 3, an automated pipeline recognizes the load and bolt interfaces on each mesh and assigns finite-element labels -- mass, stress, and displacement -- without manual intervention. We assess augmentation quality along three intrinsic axes: manufacturability, label fidelity against the SimJEB ground truth, and distributional consistency. Starting from fewer than 400 seed designs, DeepJEB++ yields 15,360 simulation-labeled 3D brackets -- a 40x expansion -- using a single GPU per stage. The dataset will be made publicly available to support reproducible engineering-AI research.

---


### 64. [scLLM-DSC: LLM-Knowledge Enhanced Cross-Modal Deep Structural Clustering for Single-Cell RNA Sequencing](https://arxiv.org/abs/2606.13007)

**<font color=#1a73e8>作者：</font>** Ping Xu, Pengjiang Li, Tian Du 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is fundamental to scRNA-seq analysis, serving as a cornerstone for identifying cell populations and resolving tissue heterogeneity. However, existing methods focus on mining numerical statistical patterns, suffering from semantic agnosticism by neglecting the intrinsic biological functions encoded by genes. While Large Language Models (LLMs) offer promising semantic capabilities, their direct adaptation to cell clustering is hindered by the structural mismatch between generative pre-training objectives and discriminative downstream tasks. To bridge this gap, we propose scLLM-DSC, a novel LLM-Knowledge Enhanced Cross-Modal Deep Structural Clustering framework. Diverging from data-driven paradigms, scLLM-DSC establishes a semantically-grounded representation by synergizing two views: a Knowledge-Driven Semantic View derived from NCBI gene priors and contextualized Cell2Sentence embeddings, and a Structure-Aware Topological View extracted via a graph-guided encoder. Crucially, we introduce a cross-modal contrastive alignment mechanism to enforce consistency between biological semantics and transcriptomic features within a unified latent space. Extensive benchmarks demonstrate that scLLM-DSC significantly outperforms eleven state-of-the-art baselines in clustering accuracy.

---


### 65. [SciR: A Controllable Benchmark for Scientific Reasoning in LLMs](https://arxiv.org/abs/2606.13020)

**<font color=#1a73e8>作者：</font>** Pierre Beckmann, Marco Valentino, Andre Freitas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Three paradigmatic forms of inference recur across scientific reasoning: deduction, induction, and causal abduction. Reliably evaluating LLMs on these in scientific settings is currently out of reach: scientific benchmarks built on human annotations are costly and lack mechanistic ground truth, while synthetic logical-reasoning benchmarks do not resemble real scientific documents. We introduce SciR, a benchmark that combines multi-paradigm reasoning with controllable scientific rendering, anchored on three paradigmatic scientific problems. Tasks are generated from formal objects (deduction tree, inductive rule hypothesis, causal graph) to guarantee verifiable answers, then rendered into multi-document scientific discourse via per-track domain-tuned genres. The construction lets us independently vary two difficulty axes: how hard it is to extract the key information needed for inference, and how hard the principled inference itself is. We test six models. Both axes hurt every model, and their effects compound. The rendering even hurts neurosymbolic pipelines, which hand inference to a verified solver. The two axes yield a per-model extraction-vs-inference profile: for instance, reasoning models like deepseek-r1 mostly surpass non-reasoning instruct models on the inference axis. To our knowledge, SciR is the first multi-paradigm scientific-reasoning benchmark with parametric control on both extraction and inference difficulty.

---


### 66. [CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery with Pattern-Routed Heterogeneous Experts](https://arxiv.org/abs/2606.13024)

**<font color=#1a73e8>作者：</font>** Bo Liu, Di Dai, Jingwei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Granger Causal Discovery (GCD) is fundamental for analyzing temporal dependencies in complex systems. However, existing neural GCD methods predominantly rely on a "one-size-fits-all" paradigm, struggling to capture distribution shifts and dynamic regime changes inherent in real-world time series. This often leads to entangled representations and spurious causal graphs. In this paper, we propose CausalMoE, a billion-scale multimodal Granger causal foundation model that explicitly models patch-level heterogeneity. CausalMoE introduces a Pattern-Routed Mixture of Heterogeneous Experts, which dynamically identifies latent temporal patterns and routes patches to specialized domain experts, effectively decoupling regime-specific mechanisms from shared dynamics. To ensure interpretable graph recovery, we design a Causality-Aware Self-Attention mechanism operating across variables, yielding sparse Granger causal graphs via proximal optimization. Furthermore, CausalMoE is the first to integrate LLMs and VLMs to align numerical signals with textual and visual priors, regularizing causal estimation in complex scenarios. Extensive experiments demonstrate that CausalMoE establishes a new state-of-the-art on fully supervised benchmarks, while effectively generalizing to few-shot settings where traditional methods fail.

---


### 67. [TetherCache: Stabilizing Autoregressive Long-Form Video Generation with Gated Recall and Trusted Alignment](https://arxiv.org/abs/2606.13035)

**<font color=#1a73e8>作者：</font>** Yu Meng, Xiangyang Luo, Letian Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models provide a natural formulation for streaming and variable-length video generation by conditioning newly generated frames on previously generated content. However, extending these models to minute-level generation remains challenging: the limited KV-cache budget prevents the model from retaining the full history, while repeatedly conditioning on self-generated frames induces a context distribution shift that accumulates over time, leading to visual artifacts, quality degradation, and temporal drift. In this paper, we propose TetherCache, a training-free and plug-and-play cache management strategy for drift-resistant long video generation. TetherCache organizes the cache into sink, memory, and recent regions, and introduces two complementary mechanisms. First, GRAB (Gated Recall with Attention-Diversity Balancing) selects long-range memory frames using a gated score that combines attention-based relevance with temporal diversity, preserving informative yet diverse historical context under a fixed cache budget. Second, TAME (Trusted Alignment via Memory Editing) lightly edits newly recalled memory tokens by aligning their statistics to a trusted context distribution, reducing the pollution caused by drifted historical features. Built on Self-Forcing, TetherCache consistently improves long-video generation quality on VBench-Long across 30s, 60s, and 240s settings. In particular, for 240s generation, it substantially improves overall and semantic scores while reducing quality drift from 7.84 to 1.33, demonstrating its effectiveness for stable long-horizon autoregressive video diffusion.

---


### 68. [Nous: An Attempt to Extract and Inject the Cognition Behind Prediction-Market Behavior](https://arxiv.org/abs/2606.13038)

**<font color=#1a73e8>作者：</font>** Haowei Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents proliferate in prediction markets and collective decision-making, they risk a cognitive monoculture: agents built on shared foundation models produce correlated forecasts, and recent measurement finds frontier-model errors correlated at r ~ 0.77. We ask whether human cognitive diversity can be recovered from behavior and transferred to LLM agents. Nous extracts a structured eight-dimension behavioral profile from real Polymarket trading activity and injects it into agents through prompts. Our central finding is a dissociation between the two halves of that pipeline. Extraction works, partially: across 100 wallets, 8 of 14 parameters are temporally stable (split-half ICC >= 0.5, bootstrap CI lower bound > 0.3; contrarian score reaches ICC ~ 0.9); wallets are identifiable from their profiles well above chance (top-1 retrieval 17-22% vs. 1% chance); and two of four pre-specified dimensions rank-correlate with future realized profit out-of-sample, though the correlations do not survive behavioral-confound controls. Prompt-level injection does not measurably transmit it: on a semantic embedding metric, structured injection shows no significant advantage over a length-matched control on any model, and the diversity it induces neither reduces ensemble error correlation nor improves Brier score -- a null that persists across exploratory checks on sampling temperature, profile diversity, and question difficulty. Measuring the prompts themselves locates the compression before the model: the structure-to-narrative translator emits near-uniform prompts whose spread does not track profile spread. We position Nous as measuring the cognitive-monoculture problem and the limits of a prompt-level remedy, motivating deeper, below-the-prompt injection (fine-tuning, activation steering). Code, frozen profiles, prompts, and model outputs: this https URL

---


### 69. [TWLA: Achieving Ternary Weights and Low-Bit Activations for LLMs via Post-Training Quantization](https://arxiv.org/abs/2606.13054)

**<font color=#1a73e8>作者：</font>** Zhixiong Zhao, Zukang Xu, Zhixuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit exceptional general language processing capabilities, but their memory and compute costs hinder deployment. Ternarization has emerged as a promising compression technique, offering significant reductions in model size and inference complexity. However, existing methods struggle with heavy-tailed activation distributions and therefore keep activations in high precision, fundamentally limiting end-to-end inference acceleration. To overcome this limitation, we propose TWLA, a post-training quantization (PTQ) framework that achieves 1.58-bit weight compression and 4-bit activation quantization while maintaining high accuracy. TWLA comprises three components: (1) Euclidean-to-Manifold Asymmetric Ternary Quantizer (E2M-ATQ) minimizes layer-output error under weight ternarization via a two-stage optimization from Euclidean initialization to manifold relocation; (2) Kronecker Orthogonal Tri-Modal Shaping (KOTMS) applies a Kronecker-structured orthogonal rotation to reshape weights into ternary-friendly tri-modal distributions, while the shared rotation statistically suppresses activation outliers; and (3) Inter-Layer Aware Activation Mixed Precision (ILA-AMP) explicitly introduces adjacent-layer second-order interaction costs in bit allocation and jointly optimizes for the layer-wise disparity of activation quantization gains induced by the shared orthogonal transform, preventing cascades triggered by a few weak layers. Extensive experiments demonstrate that TWLA maintains high accuracy under W1.58A4, while delivering significant inference acceleration. The code is available at <this https URL.

---


### 70. [LaME: Learning to Think in Latent Space for Multimodal Embedding via Information Bottleneck](https://arxiv.org/abs/2606.13061)

**<font color=#1a73e8>作者：</font>** Peixi Wu, Biao Yang, Feipeng Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning-driven universal multimodal embedding has advanced rapidly by introducing Chain-of-Thought (CoT) reasoning into the embedding pipeline. Despite the strong performance across both general and complex tasks, this paradigm suffers from two core limitations: (i) autoregressive CoT reasoning incurs high computational cost, making it impractical for low-latency retrieval; and (ii) embedding performance is heavily coupled with CoT annotation quality, making large-scale training unreliable. These raise fundamental questions: Is textual CoT the optimal form of reasoning for embedding, and can effective embedding reasoning be accomplished in latent space? To this end, we propose LaME (Latent Reasoning Multimodal Embedding), which formulates embedding-oriented latent reasoning as a weakly supervised information bottleneck. LaME employs K learnable reason tokens as a fixed-capacity bottleneck, completing all reasoning within a single forward pass. The two weak supervision signals structurally decouple contrastive from autoregressive objectives and eliminate dependence on CoT annotations, while a two-stage training pipeline ensures stable convergence. Experiments on MMEB-v2 and MRMR show that LaME achieves competitive performance, surpassing some explicit CoT-based models, while delivering 60x faster inference than explicit CoT methods and 2x faster than latent baselines with throughput comparable to discriminative embedding models. Code will be released.

---


### 71. [sebis at CRF Filling 2026: A Two-Stage Local LLM Pipeline for Medical CRF Filling](https://arxiv.org/abs/2606.13082)

**<font color=#1a73e8>作者：</font>** Katharina Sommer, Tristan Till, Florian Matthes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The extraction of structured clinical information from unstructured EHR notes is a persistent bottleneck in healthcare informatics. While large language models (LLMs) offer high performance, their deployment in clinical settings is hindered by privacy risks, inference costs, and the tendency to hallucinate beyond textual evidence. We address these challenges for the CL4Health 2026 Case Report Form (CRF) filling task by proposing a fully local, domain-adapted pipeline using the MedGemma-27B model. Our two-stage architecture, which separates binary presence classification from value extraction, enforces strict adherence to textual evidence and ensures deterministic outputs for negated, uncertain, or unknown states. By leveraging item-specific, few-shot in-context learning without external API calls or fine-tuning, our approach achieves a macro-F1 score of 0.55 on the official English test track. This result secures second place among all locally-hosted, open-source submissions. Our work demonstrates that privacy-preserving, on-premise LLM pipelines can achieve near-competitive performance with proprietary frontier models, providing a practical, data-sovereign framework for clinical NLP.

---


### 72. [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](https://arxiv.org/abs/2606.13092)

**<font color=#1a73e8>作者：</font>** Hongbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scale buys interpolation; structure buys a certified horizon. A world model's average error says nothing about whether a particular prediction can be trusted, or for how long. For equivariant latent world models we give a computable, multi-step certificate of the predictable horizon: $T$-step rollout error is provably constant over each symmetry orbit (Theorem A) and stratified channel-by-channel by the predictor's Lyapunov spectrum, $T_j(\epsilon)\sim\log(1/\epsilon)/\lambda_j$. The horizon is two-sided -- a matching lower bound makes approximate equivariance provably horizon-limited -- and the certificate is exclusive to structure: orbit-constant error characterizes equivariance, so no non-equivariant model has it at any scale. Empirically, on 40-D Lorenz-96 only a $\mathbb{Z}_N$-equivariant network recovers the full Lyapunov spectrum ($R^2{=}0.98$); dense and recurrent baselines fail.
Because the spectrum is faithful, the certificate acts, a priori: under a fixed sensing budget a $c\times$-inflated certificate provably needs $c\times$ the budget, and the equivariant certificate meets a budget its inflated dense counterpart cannot -- with zero calibration data. The same read-out, unchanged, audits public pretrained world models training-free: TD-MPC2 checkpoints land on the certificate's own scope taxonomy -- calibrated where strongly expansive (ratio 0.94-1.02), optimistic where weakly expansive, correctly abstaining where contracting -- a map a deployed monitor replicates cell-by-cell, out-of-sample. Across the official 1M-317M multitask ladder, calibration does not improve with parameters. On V-JEPA 2-AC (1B, real robot data) the measured cross-check correctly overrides an over-promising tangent spectrum -- the cross-validated audit, not the raw number, is the deployable object. Scale buys interpolation, not a calibrated horizon.

---


### 73. [Authority, Truth, and Citation Bias: A Large-Scale Multi-Domain Benchmark for Studying Epistemic Susceptibility in Large Language Models](https://arxiv.org/abs/2606.13104)

**<font color=#1a73e8>作者：</font>** Aryan Khurana, Aravind Ramana RN, Dhruv Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in citation-augmented settings, yet the effect of citation presence on model behavior independent of factual content remains poorly understood. We introduce AuthorityBench, a 220,564-prompt multi-domain benchmark that isolates how citation-based authority signals influence epistemic behavior in LLMs. The benchmark uses a fully balanced 2x2 factorial design crossing claim veracity with citation veracity, the first to do so, across four domains (general knowledge, science, law, and medicine), with controlled variation over 40 prompt templates, four venue prestige tiers, and a country-coded author name dataset. Evaluating seven models on 12 structured research questions, we find that citation presence, whether real or fabricated, consistently increases hallucination rates relative to a no-citation baseline. The effect is strongest when fabricated citations accompany true claims, raising hallucination rates by 3 to 22 percentage points and reaching 35 to 77% in the general knowledge domain, while legal claims are comparatively robust and venue prestige and author demographics show negligible impact. All datasets and evaluation code are available at: this https URL

---


### 74. [PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks](https://arxiv.org/abs/2606.13108)

**<font color=#1a73e8>作者：</font>** Yubo Zhang, Xueqing Wang, Manhui Lin 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved impressive results on general vision-language tasks, yet they suffer from hallucination, imprecise localization, and prohibitive computational cost when applied to dedicated OCR scenarios. This paper presents PP-OCRv6, a lightweight OCR system that combines architectural innovation with data-centric optimization. PP-OCRv6 redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization, decoupling spatial token mixing from channel mixing and supporting both tasks through task-specific stride configurations. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge. On our in-house benchmarks, PP-OCRv6_medium achieves 83.2% recognition accuracy and 86.2% detection Hmean, outperforming PP-OCRv5_server by +5.1% and +4.6% respectively while surpassing Qwen3-VL-235B, GPT-5.5, and Gemini-3.1-Pro with orders of magnitude fewer parameters. The tiny tier achieves 3.9$\times$ faster inference than PP-OCRv5_mobile on Intel Xeon CPU while maintaining comparable accuracy.

---


### 75. [MÖVE: A Holistic LLM Benchmark for the German Public Sector](https://arxiv.org/abs/2606.13111)

**<font color=#1a73e8>作者：</font>** Camilla Dalerci, Thilo Michael, Robin Schaefer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present MÖVE (Modelle für die Öffentliche Verwaltung Evaluieren), a holistic benchmark for evaluating large language models (LLMs) in the context of the German public sector. While LLMs are increasingly adopted in public administration, model selection remains largely ad hoc, and existing benchmarks offer limited guidance: they are predominantly English-centric, US-centric in content, and focus exclusively on task performance. MÖVE addresses these gaps by evaluating 39 models across two complementary dimensions. Performance criteria cover summarization, question answering, and topic extraction. Governance criteria assess hallucination tendencies, energy consumption, provider transparency, and alignment with German constitutional values and knowledge about positions by German political parties. In total, we utilize ten German-language datasets, including gold- and silverstandard datasets that we constructed to reflect public-administration domains. We employ a multi-metric evaluation strategy combining classical NLP metrics, embedding-based methods, and LLM-as-a-judge approaches. Our results show that no single model dominates across all criteria: top performers differ between tasks, and model size alone is a poor predictor of quality. We further evaluate the benchmark itself, analyzing its statistical precision, LLM judge reliability, the impact of our private datasets on model rankings, the sensitivity of our results to prompt formulation, and the validity of our energy consumption estimates. MÖVE is designed as a living benchmark under active development; results are publicly available at this https URL.

---


### 76. [G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents](https://arxiv.org/abs/2606.13115)

**<font color=#1a73e8>作者：</font>** Minjun Choi, Yoonjin Jang, Sangwon Youn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of processing extensive raw text. Existing approaches typically rely on either unstructured memory storage, which is prone to information loss, or computationally expensive LLMs that incur high latency. To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs. Furthermore, we introduce the novel attention-aware importance scoring mechanism that leverages the intrinsic cross-attention signals of a T5 summarizer to identify salient memories. Extensive experiments across diverse benchmarks demonstrate that G-Long achieves state-of-the-art performance in both response generation and memory retrieval, yielding performance gains of up to 9.8% in response quality on MSC and 40.8% in retrieval recall on LME, while significantly minimizing computational overhead.

---


### 77. [MP3: Multi-Period Pattern Pre-training forSpatio-Temporal Forecasting](https://arxiv.org/abs/2606.13119)

**<font color=#1a73e8>作者：</font>** Lilan Peng, Yandi Liu, Qingren Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal forecasting is crucial in diverse fields, such as transportation, climate, and energy. Urban spatio-temporal data exhibits temporal mirage: similar short-window inputs have divergent future trends, and vice versa. Existing spatio-temporal graph neural networks (STGNNs) cannot effectively identify such mirages. We argue that the core reason lies in the short-window inputs that have incomplete period observation, heterogeneous global spatial correlation, and cross-period superposition causality. To bridge this gap, we develop a novel Multi- Period Pattern Pre-training (MP3), a plug-and-play pre-training plugin for distinguishing temporal mirages. MP3 presents two core innovations: (1) The multi-period pattern learning is designed to learn multi-period patterns from long time series. Specifically, multi-period temporal modeling leverages edge convolution to identify different multi-period patterns. Multi-period spatial modeling uses a bottleneck project and a global memory bank to capture heterogeneous global spatial relations efficiently. Cross-period pattern interaction employs a causality-enhanced Transformer to capture dependencies across different period patterns. (2) This plugin can seamlessly integrate into existing STGNN backbones to strengthen their forecasting performance. The experiment on five STGNN baselines across five real-world datasets (including a large-scale dataset CA) verify the effectiveness, superior scalability and strong adaptability of MP3, which brings consistent and robust performance improvements across all evaluated baselines. On average, MP3 reduces the MAE 4.7% and the RMSE 5.0%. The code can be available at this https URL.

---


### 78. [Select and Improve: Understanding the Mechanics of Post-Training for Reasoning](https://arxiv.org/abs/2606.13125)

**<font color=#1a73e8>作者：</font>** Akshay Krishnamurthy, Audrey Huang, Nived Rajaraman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has rapidly emerged as a key component in the training of reasoning and coding models, yet it remains poorly understood from a mechanistic perspective. We study how and through what underlying processes capabilities are acquired or enhanced via reinforcement learning post-training. Our analysis, based on controlled math reasoning experiments with Qwen-2.5-1.5B, reveals two core mechanisms: strategy selection and strategy improvement. Our results highlight the role of SFT data and reinforcement learning data in activating these mechanisms, in particular showing how supervising the model on diverse reasoning strategies can enable strategy selection and how increasing difficulty in reinforcement learning data can enable strategy improvement. Taken together, our results provide mechanistic insight into RL training and suggest practical interventions to continue scaling reasoning capabilities.

---


### 79. [Rethinking RAG in Long Videos: What to Retrieve and How to Use It?](https://arxiv.org/abs/2606.13141)

**<font color=#1a73e8>作者：</font>** Yuho Lee, Jisu Shin, Nicole Hee-Yeon Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation is moving beyond text into long, egocentric video, where systems must select query-relevant chunks across multiple modalities and temporal granularities. Yet progress in VideoRAG is limited by two gaps: existing benchmarks allow queries to be answered without the video, obscuring retrieval errors, and prior methods apply a single modality-granularity configuration per query, ignoring chunk-level variability. We address both by introducing V-RAGBench, a benchmark of $\langle$query, evidence chunk, answer$\rangle$ triplets that enables faithful, decoupled evaluation of retrieval and generation, and CARVE, a simple method that runs parallel retrievers across configurations and employs chunk-adaptive reranking to identify the winning configuration for each chunk. Each chunk then enters the generator under its winning configuration selected during retrieval, yielding an interleaved evidence form where the chunk-level decision propagates across both stages. CARVE outperforms eight recent VideoRAG baselines, with the chunks supplied to the generator interleaving multiple configurations rather than sharing a single one, a behavior unattainable by query-level methods.

---


### 80. [TerraBench: Can Agents Reason Over Heterogeneous Earth-System Data?](https://arxiv.org/abs/2606.13148)

**<font color=#1a73e8>作者：</font>** Dat Tien Nguyen, Thao Nguyen, Fadillah Adamsyah Maani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Climate and environmental decision-making increasingly requires reasoning across heterogeneous inputs, including gridded physical data, satellite imagery, geospatial context, and simulator outputs. Weather and climate foundation models can forecast well, but do not reason interactively in language, while large language models (LLMs) reason in language but cannot operate directly on high-dimensional Earth-system data. As a result, real scientific workflows in Earth-science remain underserved. We introduce TerraBench, a benchmark for grounded Earth-science reasoning, built on TerraAgent, a ReAct-style executable framework that interleaves reasoning, tool calls, and observations to couple LLM planning with scientific tools for environmental retrieval, geospatial processing, simulation, and artifact-backed computation. TerraBench unifies analysis of Earth observation imagery, gridded data, GIS reasoning and simulation in a single executable interface, whereas prior benchmarks isolate these capabilities into narrow individual tasks. It is also the first in this space to pair process-level tool-use metrics with tolerance-aware numeric scoring. The benchmark comprises 403 extensive agentic tasks across three tracks (Fundamentals, Simulator-Grounded, and Document-Grounded Verification) and eight application domains with 24,500 verified execution steps. These results indicate that reliable Earth-science agents must go beyond tool access to coordinate heterogeneous workflows, parameterize tools precisely, and preserve artifact provenance.

---


### 81. [Iterative Visual Thinking: Teaching Vision-Language Models Spatial Self-Correction through Visual Feedback](https://arxiv.org/abs/2606.13156)

**<font color=#1a73e8>作者：</font>** Animesh Tripathy, Aswanth Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong singleshot spatial grounding, yet lack any mechanism to observe and correct their own predictions. We find that naively prompting a VLM to iterate over rendered visualizations of its predictions causes catastrophic failure: Acc@0.5 on referring expression comprehension collapses from 79.6% to 48.7% (a 31 percentage point drop), revealing a fundamental gap between grounding capability and self-correction ability. We propose Iterative Visual Thinking (IVT), a closed-loop framework in which the model predicts a bounding box, observes the prediction rendered on the image, and iteratively refines through visual feedback. A two-phase training recipe closes the self-correction gap: first, we exploit the base model's own predictions as realistic errors and prompt a teacher VLM to generate corrective reasoning traces, yielding supervised data without human annotation; second, we apply Group Relative Policy Optimization (GRPO) with a simple IoU reward to stabilize multi-step refinement. On a mixed benchmark spanning RefCOCOg, Ref-Adv, and Ref-L4 (505 test samples), SFT warm-up with IVT surpasses the single-shot base model on every metric: Acc@0.5 rises to 82.0% (+2.4pp), Acc@0.7 to 74.1% (+3.2pp), and Acc@0.9 to 48.3% (+2.8pp). GRPO further reduces per-step IoU degradation by 5x, stabilizing the refinement trajectory. All training uses only 2,400 samples on a single GPU, demonstrating that spatial self-correction is a learnable capability that can be instilled at modest scale.

---


### 82. [NTS-CoT: Mitigating Hallucinations in LLM-based News Timeline Summarization with Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.13171)

**<font color=#1a73e8>作者：</font>** Feng Lyu, Huiqin Yan, Sijing Duan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid updates of online news make tracking event developments challenging, highlighting the need for timeline summarization (TLS). Hallucinations, where LLM-generated content deviates from source news, still remain a critical issue in LLM-based TLS and are not well studied in existing works. To bridge this gap, we identify two primary types of hallucinations: unfaithful content during news summarization and information omission in date-event summarization. Then, we propose NTS-CoT, a novel framework that leverages Chain-of-Thought (CoT) reasoning to mitigate hallucinations in TLS. The framework consists of three key modules: i) Element-CoT to capture essential news elements for faithful summarization, ii) Date Selection to combine temporal saliency and event prominence for timestamp selection, and iii) Causal-CoT to infer causal relationships and reduce omissions in date-event summarization. Extensive experiments, including quantitative analysis on three TLS benchmarks and human evaluation, demonstrate that NTS-CoT outperforms state-of-the-art baselines, effectively mitigating hallucinations and improving LLM-based TLS performance. Our source code is available at this https URL .

---


### 83. [Mental-R1: Aligning LLM Reasoning for Mental Health Assessment](https://arxiv.org/abs/2606.13176)

**<font color=#1a73e8>作者：</font>** Xin Wang, Boyan Gao, Yibo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health problems such as anxiety, depression, and suicide remain urgent global challenges, where timely and accurate assessment is critical for effective intervention. Recently, large language models have been explored for mental health assessment. However, existing general-purpose post-training methods do not align with the cognitive processes of human assessment, which may lead to unreliable reasoning outcomes. To bridge this gap, we propose Cognitive Relative Policy Optimization (CRPO), a reinforcement learning framework tailored for the mental health domain. CRPO extends group relative policy optimization by integrating stage-dependent uncertainty modeling into the policy optimization process. Specifically, we introduce a stage-wise entropy regularization mechanism that encourages broad exploration in early reasoning phases and progressively enforces confident decision-making in later stages, mimicking the human cognitive shift from uncertainty to certainty. In addition, inspired by cognitive appraisal theory, we formalize cognitive reasoning stages, thereby guiding theory-grounded interpretable inference. Experiments on 8 mental health datasets show that CRPO achieves an average improvement of 10.4 percentage points in weighted F1-score over the best reinforcement learning baseline. Furthermore, the CRPO-trained model Mental-R1 demonstrates clear advantages compared with existing large language models on reasoning-intensive cases, suggesting that CRPO enhances reasoning capabilities for mental health assessment.

---


### 84. [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](https://arxiv.org/abs/2606.13177)

**<font color=#1a73e8>作者：</font>** Minjae Kim, Jinheon Baek, Soyeong Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to support future tasks. However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence. Furthermore, this is especially limiting on resource-constrained platforms with hard memory budgets, motivating us to formulate storage-budgeted memory management, the task of keeping an already constructed memory store within a fixed budget while preserving information useful for future interactions. To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.

---


### 85. [SICI: A Semantic-Pragmatic Complexity Index Reveals Regime Shifts in LLM Stance Detection](https://arxiv.org/abs/2606.13189)

**<font color=#1a73e8>作者：</font>** Fuqiang Niu, Bowen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt-based LLMs are increasingly used for stance detection, but harder examples are not always repaired by clearer instructions, reasoning prompts, retrieval, or debate. We introduce SICI (Stance Inference Complexity Index), a seven-dimensional diagnostic measure of the semantic-pragmatic burden imposed by a target--text pair. Across SemEval-2016 and VAST, SICI predicts LLM accuracy better than surface proxies and shows substantial cross-scorer reliability ($\alpha=0.771$). More importantly, LLM errors change regime as SICI increases: low-complexity examples invite over-attribution, especially Against predictions; intermediate examples form an unstable boundary; and high-complexity examples rapidly concentrate on None. This phase-transition-like structure persists across GPT-3.5, GPT-4o-mini, DeepSeek-V3, and GPT-4o, although stronger models move the boundaries. A 15-method intervention study further shows that prompting, retrieval, and debate often shift models along the attribution--abstention axis rather than removing the high-complexity bottleneck.

---


### 86. [Reasoning for Mobile User Experience with Multimodal LLMs: Task, Benchmark, and Approach](https://arxiv.org/abs/2606.13192)

**<font color=#1a73e8>作者：</font>** Ruichao Mao, Zhou Fang, Teng Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User experience (UX) centered on usability, perceived consistency, and functional clarity is fundamental to real-world user interfaces (UI). The application of
multimodal large language models (MLLMs) in the field of user interfaces is evolving rapidly, such as visual element grounding, graphical user interface (GUI)
agents, and design-to-code generation. However, research efforts on evaluating UX based on UI screenshots are still immature. To address this, we propose UXBench,
a novel multimodal benchmark consisting of 2,000 VQA data samples designed to assess MLLMs' ability to perform UI-based reasoning. UXBench includes 8 tasks based
on real-world UI screenshots that require fine-grained diagnosis of UX issues across layout relationships, visual hierarchy, and content consistency. Our
extensive evaluation of mainstream MLLMs shows that they remain fundamentally limited in their capacity for UI-based reasoning. The results underscore the need
for further advancements in this area. To bridge this gap, we propose UI-UX, an MLLM based on Qwen3-VL-4B-Thinking foundation model and enhanced via reinforcement
learning with two key innovations: a reward routing mechanism that dynamically balances perceptual understanding and logical reasoning during inference, and an
asymmetric transition reward that suppresses redundant or insufficient reasoning steps. Experiments demonstrate that UI-UX achieves state-of-the-art (SOTA)
performance on UXBench, attaining an accuracy of 0.7963 -- surpassing Claude-4.5-Sonnet's 0.6550 -- while exhibiting strong generalization across diverse UI tasks
and maintaining low inference latency.

---


### 87. [ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning](https://arxiv.org/abs/2606.13197)

**<font color=#1a73e8>作者：</font>** Fuqiang Niu, Bowen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) can improve large language model reasoning, but fixed debate pipelines often waste computation and can amplify correlated errors among similar agents. We propose ARMOR-MAD, a training-free heterogeneous MAD framework that treats debate as conditional computation. ARMOR-MAD combines three components: Pre-debate Agreement Routing (PAR) decides whether independently generated Round-0 answers require debate; Early Agreement Stopping Evaluator (EASE) stops debate after convergence; and Semantic Outlier Detection (SOD) down-weights abnormal final answers during aggregation. Across MATH Level 5, GSM8K, MMLU, and MMLU-Pro, ARMOR-MAD consistently improves over fixed-round heterogeneous debate with the same model pool, reaching 65.5\%, 96.5\%, 90.0\%, and 81.5\% accuracy, respectively. The results suggest that genuine model heterogeneity and agreement-based control are both important for making MAD more accurate and efficient.

---


### 88. [When Similar Means Different: Evaluating LLMs on Arabic--Hebrew Cognates](https://arxiv.org/abs/2606.13218)

**<font color=#1a73e8>作者：</font>** Junhong Liang, Noor Abo Mokh, Bashar Alhafni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic and Hebrew, as closely related Semitic languages, share a substantial lexicon of true cognates, misleading false friends, and modern loanwords. This overlap poses a challenge for cross-lingual semantic understanding in large language models (LLMs). To evaluate this capability, we introduce SemCog Bench, a curated benchmark of 1,858 Arabic--Hebrew word pairs with sentence-level annotations for cognate identification and semantic disambiguation. We evaluate open-source and commercial LLMs across multiple input representations (raw, diacritized, Romanized, and phonetic) and reveal a critical gap in cross-lingual reasoning. While models achieve high accuracy on true cognates, performance drops sharply on false friends and loanwords, reflecting a strong reliance on surface-form similarity. Furthermore, sentence-level context yields only modest improvements, suggesting that contextual cues alone are insufficient to overcome misleading form-based signals. These findings reveal a fundamental limitation of current LLMs in resolving cross-lingual form--meaning conflicts and establish SemCog Bench as a rigorous benchmark for multilingual semantic reasoning. Our code and data are publicly available.

---


### 89. [LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis](https://arxiv.org/abs/2606.13220)

**<font color=#1a73e8>作者：</font>** Fabrizio Marozzo, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as interactive assistants for technical problem solving. However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence. We refer to this behavior as user-driven sycophancy: the tendency of an LLM to reinforce a user-provided hypothesis instead of testing alternative explanations. This paper introduces LLM-as-an-Investigator, an evidence-first agentic AI methodology for robust problem diagnosis. The approach is implemented through a Solution Investigator Agent, which estimates the ambiguity of an initial problem description, generates candidate hypotheses, asks targeted clarification questions, and updates hypothesis probabilities after each answer. Rather than producing an immediate response, the agent continues the investigation until the evidence makes one candidate explanation stronger than the alternatives. To evaluate the approach, we build a benchmark from solved technical forum threads in mechanical, electrical, and hydraulic domains. We use a three-agent evaluation pipeline in which a Problem-Solution Extractor Agent converts solved threads into structured cases, a Ground-Truth Evaluator Agent simulates the user while hiding the known solution, and the tested assistant attempts to recover the solution through dialogue. The experiments compare standard assistants, reasoning-oriented LLMs, and the proposed investigator-based model across LLM backbones. In addition to diagnostic accuracy, we analyze how standard assistants follow misleading user hypotheses in diagnostic cases. The results show that the proposed approach identifies the problem more accurately than direct prompting and reasoning-only baselines, while its evidence-first protocol helps reduce user-induced conversational bias.

---


### 90. [From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation](https://arxiv.org/abs/2606.13221)

**<font color=#1a73e8>作者：</font>** Bora Kargi, David Salinas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating new large language models typically requires costly human annotation campaigns at scale. LLM-as-a-judge offers a cheaper alternative, but judge scores carry systematic errors - such as position bias, self-preference, or intransitivity - that can strongly miscalibrate the resulting rankings. We quantify the resulting judge-human disagreement at two complementary levels. At the local level, we estimate per-battle uncertainty from the judge's own score differences by propagating calibrated win probabilities rather than hard labels into the Bradley-Terry procedure. This alone provides a drastic improvement to Elo estimation accuracy, bringing LLM-derived ratings within 17.9 Elo MAE of human-derived ones when averaged over 55 held-out models on LMArena. At the global level, we apply split conformal prediction to the residual gap between LLM-derived and human-derived Elo ratings across held-out models, producing prediction intervals with distribution-free marginal coverage guarantees that account for irreducible LLM-human disagreement. Together, these two layers yield a low-cost evaluation tool that provides developers with calibrated Elo estimates and honest uncertainty bounds, without access to large-scale human this http URL facilitate reproducibility, we release our code at this https URL .

---


### 91. [PolyAlign: Conditional Human-Distribution Alignment](https://arxiv.org/abs/2606.13227)

**<font color=#1a73e8>作者：</font>** L. D. M. S. Sai Teja, Ufaq Khan, Sathira Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training methods such as supervised fine-tuning (SFT) and preference optimization typically align language models toward a single global assistant behavior. While effective for improving average helpfulness, this can suppress the natural variation of human responses across languages, tasks, and dialogue settings. We study this problem as conditional human-distribution alignment: models should match the human response distribution appropriate to the current interaction context, rather than a universal response style. We introduce PolyAlign, a distribution-aware alignment framework that organizes bilingual interaction data into bucket-specific human reference distributions defined by language, interaction track, response family, and length. PolyAlign combines Bucket-Aware SFT, which balances optimization across heterogeneous buckets, with Human-Distribution Preference Optimization (HDPO), which regularizes preference learning using critic-estimated distance to bucket-specific human support. Across a bilingual evaluation suite covering English and Chinese single- and multi-turn settings, PolyAlign improves conditional naturalness and distributional faithfulness while preserving competitive task utility. The results suggest that post-training should move beyond global alignment objectives toward interaction-aware alignment with human response distributions.

---


### 92. [Multi-Field Hybrid Retrieval-Augmented Generation for Maritime Accident Root Cause Analysis](https://arxiv.org/abs/2606.13249)

**<font color=#1a73e8>作者：</font>** Seongjin Kim, Sungil Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maritime accident adjudication reports contain critical tribunal findings for root cause analysis (RCA), yet retrieving relevant precedents and drafting consistent reports from decades of records remains labor-intensive. This paper proposes a multi-field hybrid retrieval-augmented generation (RAG) framework for automated maritime RCA, utilizing a comprehensive dataset of 13,329 Korea Maritime Safety Tribunal (KMST) reports (1971-2025). We transform raw adjudications into a structured knowledge base of "incident cards", indexing three distinct fields-Summary, Causes, and Disposition-alongside a hierarchical L1/L2 cause taxonomy. Our retrieval strategy employs a field-aware hybrid approach, fusing sparse and dense rankings via Reciprocal Rank Fusion (RRF). Given the lack of large-scale expert relevance labels, we evaluate retrieval performance using ceiling-normalized recall and nDCG based on a metadata-derived proxy relevance score. Experimental results demonstrate that our proposed retrieval significantly outperforms baseline methods, improving NormRecall@100 from 0.18 to 0.55. Furthermore, grounding the generator on the retrieved precedents enhances RCA generation quality over an LLM-only baseline, increasing the LLM-as-a-judge score from 3.34 to 3.72. These findings suggest that field-aware RAG can substantially streamline maritime safety investigation workflows by enabling faster precedent search and more consistent, evidence-based RCA drafting.

---


### 93. [Evaluating Pluralism in LLMs through Latent Perspectives](https://arxiv.org/abs/2606.13254)

**<font color=#1a73e8>作者：</font>** Laura Majer, Jan Šnajder, Martin Tutek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing need to represent diverse perspectives has increased interest in pluralistic LLM generation. Although difficult to operationalize, identifying perspectives expressed in text would provide clear guidance on pluralistic alignment and more clearly articulate the pluralistic gap in LLM generation. While models have been shown to reduce the diversity of training data and generate homogeneously, this has been demonstrated primarily on multiple-choice questionnaires or using high-level characteristics of free-form text. In this paper, we introduce and implement a domain-agnostic multi-layered framework for unsupervised extraction of perspectives suitable for identifying the pluralistic gap in LLM-generated text. We evaluate our framework on book reviews, a highly opinionated dataset representing diverse perspectives, and compare various prompts and models. Our results show that while some models and prompting techniques come close to covering a broad spectrum of perspectives, rarer perspectives remain disproportionately underrepresented, resulting in distributions that diverge from human text.

---


### 94. [From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification](https://arxiv.org/abs/2606.13262)

**<font color=#1a73e8>作者：</font>** Rongxin Yang, Shenghong He, Siyuan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent approaches combining Large Language Models (LLMs) with retrieval-augmented reasoning have shown promise for automated fact verification. To process complex claims, these verification pipelines typically execute multi-stage workflows that coordinate tightly coupled modules, including claim decomposition, evidence gathering, and verdict prediction. However, existing methods optimize individual stages in isolation or rely on fixed heuristics, which limits adaptive coordination among stages and can lead to suboptimal outcomes. In this work, we propose ProFact, an agentic reinforcement learning framework for end-to-end optimization of multi-stage fact verification trajectories. ProFact trains a unified policy to coordinate claim decomposition, evidence seeking, answer generation, and verdict prediction. To address the sparse and delayed supervision provided by final veracity labels, ProFact introduces process-aware rewards that provide stage-level learning signals throughout the verification process. Empirical evaluation shows that ProFact consistently outperforms strong baselines in both verification performance and inference efficiency. These results highlight the effectiveness of process-aware trajectory optimization for multi-stage fact verification.

---


### 95. [Clipping Makes Distributed and Federated Asynchronous SGD Robust to Stragglers](https://arxiv.org/abs/2606.13287)

**<font color=#1a73e8>作者：</font>** Samuel Erickson, Mikael Johansson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In modern machine learning, parallelization of training is an important strategy for increasing scale. Asynchronous stochastic gradient descent (ASGD), which maximizes the utilization of available hardware by avoiding waiting for slow workers. However, with constant step sizes, the convergence of ASGD is nonetheless affected negatively by slow workers due to large delays in updates. At the same time, it has been empirically observed in asynchronous training of deep learning models that gradient clipping "stabilizes" training. In this work, we provide a theoretical justification for this behavior, as we show that clipping removes the dependence of the maximum delay in the oracle complexity. We employ a sub-Weibull model of gradient noise which generalizes sub-Gaussian and sub-exponential distributions to more heavy-tailed distributions, motivated by empirical observations in deep learning. We show convergence in expectation, and the first time in asynchronous optimization, convergence with high probability.

---


### 96. [Cross-Modal Masked Compositional Concept Modeling for Enhancing Visio-Linguistic Compositionality](https://arxiv.org/abs/2606.13288)

**<font color=#1a73e8>作者：</font>** Wei Li, Zhen Huang, Xinmei Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastively trained vision-language models like CLIP, have made remarkable progress in learning joint image-text representations, but still face challenges in compositional understanding. They often exhibit a "bag-of-words" behavior--struggling to capture the object relations, attribute-object bindings, and word order dependencies. This limitation arises not only from the reliance on global, single-vector representations for optimization, but also from the insufficient exploitation and modeling of the rich compositional information inherently present in paired image text data. In this work, we propose MACCO (MAsked Compositional Concept MOdeling), a framework that masks compositional concepts in one modality and reconstructs them conditioned on the full contextual information from the other, enabling the model to capture and align cross-modal compositional structures more effectively. To facilitate this process, we introduce two auxiliary objectives that jointly align and regularize masked features both inter-modally and intra-modally. Extensive experiments on five compositional benchmarks, along with in-depth analyses, demonstrate that our approach not only significantly enhances compositionality in VLMs but also improves their ability to capture syntactic structure and linguistic information. Additionally, the improved compositionality also benefits text-to-image generation and multimodal large language model. Code is available at this https URL.

---


### 97. [HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers](https://arxiv.org/abs/2606.13289)

**<font color=#1a73e8>作者：</font>** Guozhen Zhang, Xuerui Qiu, Yutao Cui 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Holistic visual tokenizers are fundamental to unified multimodal models (UMMs) as they map diverse visual inputs into a unified representation space. In this paper, we present HYDRA-X, the first UMM that unifies image and video tokenization within a single Vision Transformer (ViT). Our design is driven by two core challenges: efficiently injecting spatiotemporal reconstruction capability into a native ViT, and embedding image- and video-level semantic awareness into the latent space. To address the first, comprehensive ablations reveal two key findings: (1) frame-level causal temporal attention suffices for visual reconstruction, whereas full spatiotemporal attention degrades it; and (2) hierarchical temporal compression substantially outperforms single-step alternatives. To tackle the second, we propose a lightweight decompressor that upsamples temporally compressed features under joint image-video teacher supervision, thereby enforcing complementary semantic structures within the compact latent space. Building on this holistic tokenizer, we further propose a principled improvement of the editing pipeline: source-target interaction should occur at the latent level inside the tokenizer rather than at the semantic level inside the LLM, substantially improving editing consistency and accelerating convergence. Instantiated at the 7B dense model, HYDRA-X achieves strong performance across image and video understanding and generation tasks, paving the way for future unified-tokenizer UMMs.

---


### 98. [Masked and Predictive Self-Supervised Foundation Models for 3D Brain MRI](https://arxiv.org/abs/2606.13315)

**<font color=#1a73e8>作者：</font>** Esra Ergün, Hersh Chandarana, Dan Sodickson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised foundation models have shown strong promise in medical imaging. However, existing MRI foundation-model studies have primarily emphasized segmentation and dense prediction tasks, while systematic investigation of self-supervised foundation models for MRI-based disease detection remains limited. In this work, we investigate two major self-supervised pretraining paradigms for MRI-based disease detection: reconstruction-based learning via Masked Autoencoders (MAE) and predictive representation learning via Joint Embedding Predictive Architectures (JEPA). We study the role of auxiliary objectives by introducing a novel spectral-domain reconstruction loss for MAE to enhance sensitivity to fine-grained anatomical structure, and by integrating variance--covariance regularization (VCR) within our JEPA framework to encourage decorrelated latent representations. Our models are pretrained on heterogeneous single-contrast MRI volumes in a contrast-agnostic setting, without modality concatenation. Across five downstream disease detection tasks, our results highlight the importance of self-supervised objective design for medical foundation model pretraining, demonstrating that the downstream benefit of each objective is determined by its relevance to the task's structure. Specifically, spectral regularization yields the largest improvements when the downstream discriminative signal is characterized by strong high-frequency anatomical structures, while covariance regularization is most beneficial when discriminative information spans multiple decorrelated feature dimensions. MAE with spectral-domain supervision consistently achieves superior downstream performance for MRI-based disease detection. These findings suggest that self-supervised objectives in medical imaging encode specific biases, and their downstream benefit is fundamentally conditioned on the task's structure.

---


### 99. [ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning](https://arxiv.org/abs/2606.13316)

**<font color=#1a73e8>作者：</font>** Xucong Wang, Ziyu Ma, Yong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is a central technique for improving long-horizon reasoning in Large Language Models (LLMs). However, existing RLVR methods often encourage unnecessarily long reasoning rollouts, which can degrade reasoning coherence and exhaust the available context budget. Existing approaches to long-context organization often depend on external mechanisms to organize rollouts, rather than enabling the model to manage its own reasoning trajectory. To address this limitation, we propose ReSum, a novel RLVR framework that enables LLMs to compress and organize their reasoning trajectories through self-summarization. Our pilot studies show that self-summarization stabilizes generation by lowering token-level entropy, and that introducing a ``summarization'' phrase can substantially mitigate errors propagated from an incorrect rollout prefix. Motivated by these findings, ReSum adopts a summarization-aware adaptive rollout mechanism that contrastively evaluates whether self-summarization benefits the ongoing reasoning process. Specifically, when the model spontaneously triggers self-summarization, ReSum masks the summarization phrase to create a contrastive branch; for non-summarization positions, it instead randomly injects the phrase to create a matched branch. We further design a summarization-aware advantage to enable finer-grained comparison between contrastive rollout trajectories. Extensive experiments show that ReSum improves performance at an average of 4\% while reducing rollout length by 18.6\%.

---


### 100. [SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents](https://arxiv.org/abs/2606.13317)

**<font color=#1a73e8>作者：</font>** Kunfeng Chen, Qihuang Zhong, Juhua Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill self-evolution methods for LLM agents aim to turn execution trajectories into reusable skill documents, but current pipelines typically learn from one trajectory per task, merge candidate skill patches before checking them, and load the full skill corpus before inference. We propose SkillCAT, a training-free framework that separates this process into three stages. Contrastive Causal Extraction (CCE) samples multiple trajectories for each task and compares same-task success/failure pairs to identify evidence that explains outcome differences. Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones and keeps only patches that improve or preserve task outcomes before hierarchical skill patch merging. Topology-Aware Task Execution (TTE) compiles the evolved skills into a routable sub-skill topology, so inference loads only the capability nodes relevant to the task. We evaluate SkillCAT on common agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further test cross-model and out-of-distribution generalization. Across these settings, SkillCAT raises the average score over baselines by up to 40.40%, demonstrating reliable skill evolution without model training.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-128](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
