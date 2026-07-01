# 🧠 大模型相关研究 | 2026年07月02日

> 本类共 **121** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-121](./part-03.md)

---

### 51. [LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment](https://arxiv.org/abs/2606.31310)

**<font color=#1a73e8>作者：</font>** Hong-Yun Lin, Fu-An Chao, Bi-Cheng Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fueled by increasing model scale and multimodal inputs, Multimodal Large Language Models (MLLMs) have emerged as a promising paradigm for Spoken Language Assessment (SLA). While effective, this paradigm often overlooks the intrinsic ordinal structure of language acquisition. This paper works around the necessity of large-scale MLLMs by introducing Latent Ordinal Prototype Alignment (LOPA) for SLA, a prototype-based regularizer that enforces an ordinal geometric prior directly on the latent space. Coupled with Semantic-Anchored Layer Routing (SALR), which adaptively harvests multi-depth representations from a frozen Whisper encoder, our framework achieves an RMSE of 0.361. This performance rivals billion-parameter systems without the need for LLM-based fine-tuning. Further analysis reveals that SALR's synergy with LOPA offers interpretable, criterion-aligned preferences, thereby supporting an efficient and ordinal-aware modeling alternative to current scaling-centric models for SLA.

---


### 52. [Optimization Algorithms for Joint OFDM Waveform Design and RIS Configuration in 6G Networks: From Convex Relaxation to Foundation Models](https://arxiv.org/abs/2606.31334)

**<font color=#1a73e8>作者：</font>** Ahmet Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Joint OFDM-RIS optimization for 6G is a mixed-integer nonlinear programming (MINLP) problem covering sum-rate maximization, energy efficiency, max-min fairness, and peak-to-average power ratio (PAPR)-constrained objectives. Seventy-eight joint OFDM-RIS optimization works published between 2021 and 2026 are surveyed. No standardized benchmark exists, and cross-paper comparisons remain infeasible. This survey classifies these works into four paradigms: (I) model-based convex relaxation, (II) heuristic and metaheuristic search, (III) deep reinforcement and unsupervised learning, and (IV) emerging methods including foundation models (FM), diffusion-based generative AI, and quantum optimization. A literature synthesis of self-reported benchmarks shows that ML-based methods (Paradigm~III) report 95-99\% of model-based spectral efficiency at 10^2-10^4 x faster per-inference runtime (method-pair dependent; literature values are self-reported and exclude ML pre-training cost). A companion tutorial benchmark at N=16, N=64, and N=128 reveals a critical scaling property: GPU-based neural network inference (DDQN, PPO, graph neural network (GNN), unsupervised DL) is N-invariant, with identical runtime at N=16 and N=128, while iterative solvers (AO+SCA, PSO) scale polynomially. Energy efficiency (P2) and PAPR-constrained (P4) benchmarks are deferred to future work with standardized power models and waveform generators. Six open challenges emerge from the synthesis: the cross-paradigm benchmark deficit, real-world hardware-constrained deployment, joint waveform-RIS optimization for doubly-dispersive channels, multi-objective PAPR trade-offs, LLM safety in live network control, and diminishing returns of standalone heuristics. We specify requirements for a standardized benchmark. This study serves as a roadmap for researchers and practitioners working on joint OFDM-RIS optimization in 6G networks.

---


### 53. [Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?](https://arxiv.org/abs/2606.31371)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When large language model (LLM) agents adapt their behavior through evaluator feedback, systematic evaluator biases propagate into the agent's learned strategy distribution - a phenomenon termed evaluator preference coupling. Prior work has documented this coupling and established a diagnostic framework (EPC) to measure it, but has not investigated whether calibration techniques can mitigate the effect. We present the first study of evaluator calibration as mitigation: applying probability calibration to the evaluator's pairwise judgments to reduce spurious preference propagation. In a controlled within-subjects experiment (N=5) comparing standard binary TTRL (win/loss) with confidence-calibrated TTRL (probability-weighted updates) using DeepSeek-V4-Pro as executor and GLM5.2 as evaluator, we find that calibration reduces the coupling coefficient gamma by 20-49% and Jensen-Shannon divergence by 45-67%. A symmetric-LR control confirms the effect is not due to reduced update asymmetry. We release the calibrated TTRL protocol and recommend it as a lightweight mitigation for LLM-as-judge deployment pipelines.

---


### 54. [MS-Resampler: Multi-Scope Visual Resampling for Efficient Multimodal LLMs](https://arxiv.org/abs/2606.31383)

**<font color=#1a73e8>作者：</font>** Zhongyang Li, Yaqian Li, Faming Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) typically employ resampling-based projectors to transform dense visual features into a compact token sequence for language modeling. Most existing resamplers adopt a single, fixed aggregation scope via global cross-attention, which can blur fine-grained local evidence and limit the ability to capture both local details and global context within a fixed token budget. In this work, we propose MS-Resampler, a multi-scope visual resampling framework for MLLMs. MS-Resampler instantiates multiple scope-specific resamplers by injecting explicit spatial scope priors into the resampling attention, enabling each branch to aggregate visual information at a particular granularity from local to global. The outputs of these scope-specific resamplers are then adaptively fused to produce the final visual representations for language modeling. Extensive experiments on ten public multimodal benchmarks show that MS-Resampler consistently improves visual understanding and multimodal reasoning over conventional single-scope resamplers, while introducing only minimal computational overhead.

---


### 55. [ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents](https://arxiv.org/abs/2606.31392)

**<font color=#1a73e8>作者：</font>** Binjie Zhang, Mike Zheng Shou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented vision-language models (VLMs) can solve multimodal, multi-step tasks by calling external tools, yet they remain fragile in practice. Existing works have two common gaps. Supervised fine-tuning (SFT) is built mostly on successful trajectories and offers little signal for recovery after tool failures, while sparse trajectory-level RL rewards provide limited guidance on which step failed and how to repair it. We introduce ReGRPO (Reflection-augmented Group Relative Policy Optimization), a framework that learns reflection-guided correction in tool-using agents. ReGRPO starts with a structured reflective data engine: we execute near-miss actions to collect grounded failure observations, then build Reflection-of-Thought triplets (ErrorType, Evidence, FixPlan) paired with corrected actions for warm-start SFT. We then optimize reflection tokens and corrective actions jointly within local trajectories using group-relative advantages, and include a reflection-cost term to reduce unnecessary reflection. Experiments on GTA and GAIA show that, under the same backbone and tool suite, ReGRPO consistently outperforms strong open-source baselines and achieves the best results among the compared open-source controllers. Code and RoT data are available at this https URL.

---


### 56. [Mixture-of-Control: State-Aware Fine-Tuning for Transformer-based Models](https://arxiv.org/abs/2606.31397)

**<font color=#1a73e8>作者：</font>** Duc Anh Nguyen, Tien Ngoc Luu, Tung Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-based fine-tuning has emerged as a compelling alternative to weight-based adaptation for transformers, updating lightweight controls into states rather than model weights, offering substantial memory savings while retaining parameter efficiency. However, most existing state-based methods typically apply only per-block control updates, which limits inter-block information exchange and restricts representational adaptation. Meanwhile, prior mechanisms that enable cross-block communication often introduce considerable computational overhead, reducing their practicality for efficient fine-tuning. We introduce Mixture-of-Control (MoC), a lightweight fine-tuning framework that adaptively integrates local and global control signals to enhance representation learning. MoC treats block-wise control states as experts in a sparse mixture-of-experts process, enabling efficient communication across transformer blocks. Empirical results across diverse transformer-based benchmarks demonstrate that MoC outperforms state-based methods while maintaining a comparable memory and computational efficiency.

---


### 57. [Wisdom Of The (AI) Crowd: Investigating Artificial Swarm Intelligence In Large Language Models](https://arxiv.org/abs/2606.31404)

**<font color=#1a73e8>作者：</font>** Justin Brenne, Christian Meske  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human swarm intelligence demonstrates remarkable collective accuracy but faces scalability constraints in cost, coordination, and time. We investigate whether large language models (LLMs) can approximate swarm intelligence effects through artificial swarms, addressing a critical gap in understanding AI-based aggregation mechanisms. We conducted a controlled experiment with 960 manually executed prompts across three proprietary models (GPT-5, Gemini 2.5 Pro, Claude Sonnet 4.5), testing intra-model sampling and inter-model aggregation on eight estimation tasks. Results reveal consistent error reduction through intra- and inter-model aggregation, with significant error reductions up to 37 percentage points in MAPE across different aggregation strategies. We observed small to large effect sizes for positive correlations (Spearman's $\rho=0.242-0.568$, all $p<0.001$) between relative confidence interval widths and relative estimation errors, suggesting LLMs possess metacognitive awareness when assessing uncertainty. We discuss implications for research and practice, providing actionable insights for deploying LLM swarms in organizational decision-making.

---


### 58. [Visual Semantic Entropy: Do Vision Language Models Recognize Visual Ambiguity?](https://arxiv.org/abs/2606.31407)

**<font color=#1a73e8>作者：</font>** Ta Duc Huy, Trang Nguyen, Townim Chowdhury 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can produce confident answers on visually ambiguous inputs, resulting in biased predictions. Common entropy-based methods, such as Semantic Entropy (SE), rely on output diversity. Yet our analysis shows that overconfident visual embeddings suppress output diversity under stochastic decoding, causing SE to underestimate uncertainty in such cases. Recent methods instead probe output diversity through input perturbations, including textual paraphrasing or joint text-image perturbations, and show improved performance. We study these approaches and reveals that the resulting variability is often dominated by textual changes rather than visual evidence, causing uncertainty estimates to reflect prompt sensitivity rather than visual ambiguity. We therefore propose Visual Semantic Entropy (VSE), which perturbs only the image to probe nearby visual variations while keeping the text query fixed. VSE measures uncertainty by clustering generated answers into semantic prototypes and computing the mass-weighted dispersion among them. Extensive evaluation across five modern vision-language models and five diverse VQA benchmarks demonstrates that VSE effectively captures visual ambiguity, establishing a new state-of-the-art for VLM uncertainty estimation.

---


### 59. [Xiaomi-GUI-0 Technical Report](https://arxiv.org/abs/2606.31410)

**<font color=#1a73e8>作者：</font>** Wanxia Cao, Chengzhen Duan, Pei Fu 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents build on vision-language models to complete user tasks end-to-end in real applications through interface actions such as tapping, swiping, text entry, and navigation. However, existing GUI agents are trained and evaluated largely on offline trajectories, simulated environments, and standardized benchmarks. These differ substantially from real applications in interface layout, interaction logic, and abnormal-state distribution, and cannot faithfully characterize execution stability in real-world use, where account states, permission dialogs, payment authentication, and risk control continually reshape the state distribution and open a persistent gap between benchmark scores and real usability. To close this gap, we propose Xiaomi-GUI-0, a native multimodal GUI agent for real mobile environments, trained and evaluated within a real-device closed loop. At its core is a real-device-dominant hybrid infrastructure, where physical devices are the primary execution environment and sandboxes provide auxiliary support, so that data collection, training, rollout, and evaluation share an execution distribution close to real deployment. We construct multi-source training data spanning high-frequency head tasks, high-generalization data for long-tail intents, and capability-enhancement data for reflection and memory, and introduce an error-driven data flywheel that turns failure trajectories into corrected actions, reflective explanations, and recovery demonstrations. The model is trained through a progressive three-stage pipeline of supervised fine-tuning, step-level reinforcement learning, and agentic reinforcement learning. Evaluated on public benchmarks and our in-house RealMobile, Xiaomi-GUI-0 achieves 72.0% success on RealMobile and 78.9% on AndroidWorld, while substantially improving execution stability and abnormal-state recognition in real-world tasks.

---


### 60. [Team MKC at CLPsych 2026: Capturing and Characterizing Mental Health Changes through Social Media Timeline Dynamics](https://arxiv.org/abs/2606.31464)

**<font color=#1a73e8>作者：</font>** Kyomin Hwang, Hyeonjin Kim, Hyunho Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have motivated their adoption across a wide range of domains, including Artificial Intelligence (AI) for mental health. Given the growing prevalence of mental health disorders worldwide and the limited accessibility of professional care, there is an increasing demand for scalable computational approaches that can assist in early detection and continuous monitoring of psychological well-being. In this area, ongoing efforts have focused on curating domain-specific datasets and leveraging them to develop LLMs capable of supporting holistic mental health analysis. In line with this direction, we propose an LLM-based pipeline for comprehensive mental health analysis over sequentially ordered user posts, as part of the CLPsych shared task. Our pipeline offers a unified framework that jointly enables post-level assessment and user-level temporal modeling.

---


### 61. [AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience](https://arxiv.org/abs/2606.31467)

**<font color=#1a73e8>作者：</font>** Wenyi Zhang, Fanglong Yao, Youzhi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of aerospace embodied intelligence, enabling Unmanned Aerial Vehicles (UAVs) to autonomously understand and reason about complex environments has become increasingly important. However, existing UAV-based spatial reasoning approaches face critical limitations: single-view perception renders them vulnerable to occlusions and perspective distortions, while most VLMs lack explicit geometric modeling, relying on semantic cues and yielding inconsistent reasoning under viewpoint and scale variations. To address these challenges, we propose SatAgent, a UAV-Satellite collaborative spatial reasoning model inspired by the dual-pathway mechanism of the human visual system. By jointly leveraging satellite and UAV perspectives, SatAgent enables robust, accurate reasoning in complex urban environments. We first introduce a Geometric-Aware 3D Reconstruction Encoder that elevates 2D UAV features into explicit 3D spatial representations. Next, we design a multi-view topology-semantic alignment module integrating cross-view features within a unified BEV coordinate system. We further introduce a multi-view consistency loss encouraging viewpoint-invariant representations. Finally, we construct SatAgent-SR130K, the first large-scale UAV-Satellite collaborative multi-view spatial reasoning dataset. Experiments show SatAgent outperforms state-of-the-art general-purpose foundation models and specialized spatial reasoning models by 25.91\% and 11.69\%, respectively, across diverse tasks, achieving particularly high accuracy in complex geometric relationship reasoning.

---


### 62. [CLOUDADV: Decision-Aligned Instance Sizing with Zero-Shot Foundation Models under Drift](https://arxiv.org/abs/2606.31470)

**<font color=#1a73e8>作者：</font>** Jack Bell, Giacomo Carfi, Gerlando Gramaglia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cloud virtual machines are often overprovisioned, creating avoidable cost and operational inefficiency. We present CLOUDADV, an interactive engineer-facing advisory system for cloud instance sizing under workload drift. The system combines zero-shot time-series forecasting with bounded recommendation generation across day-, week-, and month-scale planning horizons. For each query, CLOUDADV constructs a structured decision context from historical utilization, forecast summaries, current VM metadata, candidate instance options, pricing, and explicit sizing heuristics. A higher-capacity LLM is used offline to generate reference recommendations, while a smaller production model is evaluated on the same prompts to assess deployment-time alignment under latency and cost constraints. Evaluation prioritizes downstream recommendation quality using simulated Azure cost savings and ex-post exceedance, with rolling-origin forecast accuracy reported as a secondary diagnostic against classical and supervised baselines. In a case study of seven production VMs, the reference recommendations reduce simulated monthly cost from about \$1,503 to \$708, yielding \$795/month in savings (52.9%) under conservative heuristic constraints, while the highest observed exceedance rate among downgraded cases is 1.5%. Although Chronos-2 does not minimize every forecasting metric, it often induces recommendation patterns similar to those of a supervised per-VM baseline. These results suggest that zero-shot foundation models can support decision-aligned provisioning in non-stationary cloud environments while reducing the operational burden of repeated per-tenant retraining, revalidation, and redeployment.

---


### 63. [TabPATE: Differentially Private Tabular In-Context Learning Without Public Data](https://arxiv.org/abs/2606.31474)

**<font color=#1a73e8>作者：</font>** Dariush Wahdany, Matthew Jagielski, Jesse C. Cresswell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models enable accurate in-context learning (ICL) from small labeled datasets, but the private records placed in context can leak through model predictions. We first show that even basic membership inference attacks succeed against tabular ICL, motivating formal privacy protection. We then introduce TabPATE, a differentially private PATE-style defense for tabular ICL that does not require public in-distribution data. TabPATE partitions the private context across teacher models, privately aggregates their labels on synthetic tabular queries, and releases the resulting labeled queries as a student context. Because tabular features are bounded and relatively low-dimensional, useful queries can be generated from feature ranges alone or from lightly privatized marginals. Across tabular benchmarks, TabPATE preserves competitive utility while reducing membership inference to near-random success, providing a practical path to private tabular ICL without public data.

---


### 64. [SimpleSearch-VL: A Simple Recipe for Multimodal Agentic Deep Search](https://arxiv.org/abs/2606.31504)

**<font color=#1a73e8>作者：</font>** Ming Dai, Zhihong Lu, Jinjie Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SimpleSearch-VL, an efficient, reliable, and practical framework for multimodal agentic search. Its core idea is to improve the agent's own search-and-verification process rather than scaling data, tools, or auxiliary model components. For efficiency, Factorized Adaptive Rollout (FAR) improves sampling efficiency by forming more informative training groups while using redundant samples to mitigate long-tail latency and expose hard samples. For reliability, SimpleSearch-VL performs evidence-verified reasoning, explicitly using chain-of-thought verification to assess the relevance of retrieved visual and textual cues to the original context. For practicality, SimpleSearch-VL keeps a lightweight tool interface and performs webpage self-summary within the agent, requiring no additional external dependencies. With only 5K supervised tool-interleaved trajectories and 2K RL data, SimpleSearch-VL improves Qwen3-VL agentic baselines by 15.8 and 16.0 average points for the 8B and 30B-A3B variants, respectively. The SimpleSearch-VL-30B-A3B model further achieves performance competitive with agentic Gemini-3-Pro.

---


### 65. [Design and Implementation of Agentic Orchestrations and Orchestration of Agents](https://arxiv.org/abs/2606.31518)

**<font color=#1a73e8>作者：</font>** Stefanie Rinderle-Ma, Juergen Mangler, Johannes Loebbecke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic Business Process Management has gained momentum recently. The prospect is that the autonomy of AI agents, i.e., predominantly LLM-based agents, can be balanced with a certain level of robustness, tractability, and traceability through a combination with process technology. In this paper, we provide a classification framework for agentic orchestration options along properties such as task specificity, traceability and tractability, autonomy and reactivity, and correctness assurance and present qualitative decision criteria for realizations of different scenarios. We also provide metrics for the quantitative assessment of realization properties and show them through different agentic implementations of a predictive light sensing scenario. Altogether, this work aims at providing properties, criteria, and metrics for the design and implementation of agentic orchestrations and orchestration of agents.

---


### 66. [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](https://arxiv.org/abs/2606.31519)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Jinhao Dong, Hailin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context Large Language Model inference is severely bottlenecked by the massive Key-Value (KV) cache, yet existing sparse attention methods often suffer from static fixed-budget (Top-k) retrieval or rely on proxy scores that are computationally expensive and biased. To address these limitations, we propose RaBitQCache, a novel sparse attention framework that utilizes randomized rotated binary quantization and high-throughput binary-INT4 arithmetic to efficiently estimate attention weights. Our proxy score serves as an unbiased estimator with a proven error bound, enabling adaptive Top-p retrieval that dynamically adjusts the token budget based on actual attention sparsity. We further implement a hardware-aware system with asynchronous pipelining and lazy updates to mask overhead. Evaluations demonstrate that RaBitQCache significantly accelerates inference and reduces memory I/O while preserving generation quality compared to state-of-the-art baselines. Code is available at this https URL.

---


### 67. [On the Convergence of Self-Improving Online LLM Alignment](https://arxiv.org/abs/2606.31524)

**<font color=#1a73e8>作者：</font>** Xudong Wu, Pangpang Liu, Vaneet Aggarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Self-Improving Alignment (SAIL) algorithm addresses distribution shift by reducing a bilevel formulation of the problem to an efficient, single-level method. Empirically, SAIL has demonstrated strong performance on this task. However, a formal analysis of its convergence properties has been lacking. We identify a key theoretical challenge: the standard SAIL objective function is not guaranteed to be strongly concave due to unfavorable properties of its Hessian. To address this limitation, we propose a regularized objective, SAIL-RevKL, which incorporates a reverse Kullback-Leibler (KL) divergence penalty to improve the optimization landscape. Our central theoretical contribution is to prove that this regularized objective satisfies the Polyak-Lojasiewicz (PL) condition within a bounded parameter space. We establish global convergence guarantees, achieving a near-linear sample complexity. We further validate the effectiveness and stability of SAIL-RevKL through empirical evaluations, demonstrating that it outperforms the vanilla SAIL on both MuJoCo benchmarks and LLM alignment tasks.

---


### 68. [Modality-Driven Search with Holistic Trace Judging for ARC-AGI-2](https://arxiv.org/abs/2606.31543)

**<font color=#1a73e8>作者：</font>** Johan Land  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can produce fluent, internally coherent reasoning traces for abstract reasoning tasks while still being confidently wrong - making selection among candidates, not just generation, the central challenge. I present a solver for ARC-AGI-2, a few-shot visual reasoning benchmark, built around two principles: (i) treating reasoning modalities as search operators, generating diverse candidates independently across text, image, and code channels, and (ii) context-preserving holistic judging, in which a judge model jointly compares all candidate reasoning traces within a single long-context prompt. Unlike self-consistency or majority voting, this approach reliably recovers correct minority hypotheses on tasks where the modal answer is wrong.
On the ARC Prize semi-private evaluation set, the solver achieves 72.9 percent at USD 38.99 per task - the highest score on the verified leaderboard at the time of writing, exceeding the best standalone frontier models, GPT-5.2 Pro at 54.2 percent and Gemini 3 Pro at 54.0 percent, by +18.7 percentage points. On the public evaluation set, it achieves 76.1 percent at USD 19.69 per task. I release the full source code and document extensive negative results, including the finding that prescriptive prompting templates and iterative refinement systematically reduce hypothesis diversity and degrade performance.

---


### 69. [AutoTrainess: Teaching Language Models to Improve Language Models Autonomously](https://arxiv.org/abs/2606.31551)

**<font color=#1a73e8>作者：</font>** Zhaojian Yu, Penghao Yin, Shuzheng Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training language models (LMs) remains a highly human-intensive process, even as frontier language model agents become increasingly capable at software engineering and other long-horizon tasks. A central challenge is that autonomous post-training is not just a coding problem: it requires the agent to repeatedly plan iterations, construct benchmark-aligned data, run stable training jobs, evaluate checkpoints, and preserve experiment state across many hours of interaction. We present AutoTrainess, a LM agent that exposes these operations as a repository of agent-computer interfaces for planning, data preparation, training, evaluation, and logging. Rather than leaving the agent to operate in a raw CLI environment with an underspecified action space, AutoTrainess externalizes prior human experience as explicit workflows, rules, and execution constraints that guide the agent toward effective and reliable training behavior. On PostTrainBench, AutoTrainess consistently outperforms CLI-only baselines, achieving 26.94 average score with GPT-5.4 (Codex) versus 23.21 for CLI-only. It also generalizes across models and harnesses, improving DeepSeek-V4-Flash (OpenCode) from 12.13 to 19.58.

---


### 70. [ACE: Pluggable Adaptive Context Elasticizer across Agents](https://arxiv.org/abs/2606.31564)

**<font color=#1a73e8>作者：</font>** Ning Liao, Zihao Long, Xiaoxing Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing complexity of agentic tasks has led to rapidly growing trajectory lengths, which poses significant challenges for large language model (LLM) based agents with fixed context windows. Existing context management techniques, such as truncation and summarization, suffer from inherent inflexibility and irreversibility: once information is discarded or compressed, it cannot be recovered even when it becomes critically relevant in later decision steps. To address these limitations, we propose the Adaptive Context Elasticizer (ACE), a plug-and-play module that elastically orchestrates historical step information into the agent's context at each decision step. ACE maintains a lossless message maintenance layer that stores both raw messages and compressed abstractions for each historical step, while a context orchestration layer adaptively assigns each step an elastic type as raw, abstract, or drop, at every decision step based on the current task state. This reversible design ensures that the main LLM always receives a compact yet information-rich context. We adapt ACE to four diverse agent frameworks, including ReAct, DeepAgent, WebThinker, and MiroFlow, without training or architectural modifications. Experiments show that ACE consistently outperforms truncation and summarization baselines, and brings consistent performance gains across all four agent frameworks.

---


### 71. [Which Tokens Matter? Adaptive Token Selection for RLVR with the Relative Surprisal Index](https://arxiv.org/abs/2606.31575)

**<font color=#1a73e8>作者：</font>** Outongyi Lv, Yanzhao Zheng, Yuanwei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a powerful tool for propelling Large Language Models (LLMs) beyond imitation-based training towards more robust reasoning capabilities. Among existing approaches, RL with Verifiable Rewards (RLVR) has emerged as a pivotal paradigm for advancing LLM reasoning. Despite its empirical success, recent studies have offered different insights. One line of inquiry advocates prioritizing high-entropy token positions during training, while another perspective cautions against allowing low-probability tokens to dominate gradient updates. Notably, although high-entropy tokens are usually correlated with low probability, both paradigms empirically yield substantial performance gains. In this work, we argue that evaluating sampled-token probability or entropy in isolation is insufficient to capture the policy optimization dynamics. To resolve this tension, we introduce the Relative Surprisal Index (RSI), a principled, information-theoretic metric that naturally couples the token's entropy with the probability of the selected token. We show that, under mild conditions, RSI is related to the local ratio between the first-order variations of the logit-gradient norm and predictive entropy under a selected-logit perturbation. Building on RSI, we propose RSI Selection (RSI-S), an entropy-adaptive token filtering method that retains tokens within a stable RSI interval. RSI-S successfully reconciles previous contradictory paradigms and filters out both redundant low-surprisal tokens and unstable high-surprisal tail tokens. Empirical evaluations show that RSI-S achieves higher avg@32 accuracy across different model scales (Qwen2.5-1.5B, 3B, and 7B) on AIME and AMC benchmarks: RSI-S improves avg@32 accuracy by 2--3 percentage points over GRPO. Overall, RSI offers a promising perspective for RLVR improvement.

---


### 72. [Localized Conformal Prediction for Image Classification with Vision-Language Models](https://arxiv.org/abs/2606.31577)

**<font color=#1a73e8>作者：</font>** Clément Fuchs, Tim Bary, Benoît Macq  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conformal predictions have attracted significant attention in the field of uncertainty quantification, mainly because of their strong marginal coverage guarantees. Full conditional guarantee is not an attainable goal, a well known fact in conformal predictions literature. As a result, several approaches have tried to approximate this behavior by adapting the conformal sets of test-time samples according to their similarity to calibration examples. Although the latter has gained traction and shown impressive performances for regression problems, its application to image classification remains under-explored. We conduct an extensive benchmarking on natural image classification tasks with vision-language models (VLMs), using our open source implementation of a recent localized conformal prediction algorithm. We show that straightforward usage of the cosine similarity between test-time and calibration visual features, an intuitive choice for VLMs, is not sufficient to improve over the non-local baselines. In response, we propose a simple non-linear transformation of the cosine similarities, which conserves marginal coverage guarantees and achieves statistically significant mean set sizes reduction. Code is available at this https URL.

---


### 73. [Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment](https://arxiv.org/abs/2606.31591)

**<font color=#1a73e8>作者：</font>** Jason R. Brown, Patrick Leask, Lev McKinney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM) is a recently discovered phenomenon in LLMs where fine-tuning on a narrow misaligned task, such as writing insecure code, leads to broadly misaligned behaviour on unrelated prompts. Previous work has noted that the severity of EM is highly sensitive to training choices; however, we still lack a systematic characterisation of this sensitivity. We perform a sweep over several Qwen3 models, optimisers, datasets, and batch sizes, and find that the choice of optimiser has the largest effect, producing a 7x spread in misalignment rate. Surprisingly, model size has a negligible effect within the Qwen3 family. An additional sweep over 12 models from three families using Adam confirms that model scale (1B-235B) and family have negligible effects for that optimiser. Analysing the loss-alignment relationship on Qwen3-8B, we find that final log training loss is a strong predictor of alignment, and that stratifying by optimiser captures nearly all the residual variance. Training dynamics reveal that each optimiser follows a different trajectory through loss-alignment space, and that after significant training, the optimiser becomes more important than training loss as a predictor of alignment. Muon, the adaptive optimiser that preserves alignment the best, implicitly regularises for a more uniform distribution of singular values of the LoRA adapter. We evaluate this insight by training with an additional loss term that incentivises a flatter singular value spectrum, and find that this substantially recovers alignment for the more EM-prone adaptive optimisers (Adam and Lion), with negligible cost to training loss. These results identify optimiser choice as a key factor in EM severity, but show that spectral regularisation can substantially mitigate the effects of EM-prone optimisers.

---


### 74. [Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning](https://arxiv.org/abs/2606.31599)

**<font color=#1a73e8>作者：</font>** Kaitao Chen, Weiqian Zhao, Jiamin Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) combining reinforcement learning (RL) ignite remarkable progress in multimodal reasoning, yet still struggle with medical images, which typically exhibit extremely sparse visual evidence to inform clinical decision-making. We recognize that pruning visual tokens outside the grounding region greatly enhances medical reasoning. However, a united RL framework for active visual token pruning (VTP) and medical multimodal reasoning remains unestablished. Here, we propose a dual-stream RL framework, ViToS, to fulfill token pruning and question answering. ViToS trains one policy model with two task branches, where one focuses on grounding while the other conducts token-sparse reasoning after VTP. Furthermore, we solve the coupled policy learning problem by introducing the cross-feedback sequential optimization, avoiding gradient conflict and facilitating convergence of the shared policy model. Evaluated on seven medical benchmarks, our method reduces visual tokens to 77% of the original sequence length while achieving a 108.27% relative performance on Lingshu-7B and 104.16% relative performance on HuatuoGPT-Vision-7B. Overall, ViToS delivers superior performance and inference speedup, establishing an efficient paradigm for medical multimodal reasoning.

---


### 75. [Robust Text Watermarking for Large Language Models via Dual Semantic Embeddings](https://arxiv.org/abs/2606.31602)

**<font color=#1a73e8>作者：</font>** Jonas Schäfer, Cezary Pilaszewicz, Gerhard Wunder  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work presents Dual-Embedding Watermarking (DEW), a semantic watermarking scheme for large language models (LLMs) that leverages contextual and token-level embeddings to enhance robustness against paraphrasing and translation. DEW utilizes a signal-processing methodology, applying algebraic vector-space operations to \mbox{token and context embeddings to derive a watermark signal that degrades gracefully under semantic shifts. The method obfuscates the watermark by projecting embedding vectors through pseudo-random matrices seeded with a secret key. Relevant distributions derived from the underlying algebra are evaluated and employed for statistical testing and benchmarking of DEW. Experimental results across multiple LLMs indicate that DEW improves post-paraphrase detection while maintaining competitive text quality, and remains detectable after translation, even when prior semantic watermarks degrade significantly. These findings position DEW as a practical and robust solution for safeguarding LLM-generated text and addressing critical issues in responsible AI deployment.

---


### 76. [CLExEval: A Human-in-the-Loop Framework for Qualitative Evaluation of LLM Clinical Reasoning](https://arxiv.org/abs/2606.31608)

**<font color=#1a73e8>作者：</font>** Ajmal M., Abin Roy, Afthab Salam Kanniyan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong results on many medical benchmarks, but their clinical reasoning remains difficult to evaluate reliably. A central risk is an evaluation illusion: fluent and well-structured explanations can appear clinically convincing even when the final diagnosis is incorrect. We introduce CLExEval, a human-in-the-loop framework for evaluating LLM clinical reasoning under progressive information masking. CLExEval combines 5,600 expert-physician annotations with 200 clinical reasoning traces derived from 40 rare diagnostic cases. Our analysis identifies three recurring failure patterns: (i) verbosity bias, where GPT-4o-mini's diagnostic accuracy drops from 95.0% to 32.5% under information scarcity; (ii) a hidden knowledge paradox, where a specialist model reaches 92.5% maximum diagnostic potential but fails to retrieve that knowledge reliably in verbose contexts; and (iii) a 68.6% reasoning-to-output mismatch, where correct diagnoses appear in reasoning traces but are not reflected in final answers. We further evaluate the LLM-as-a-Judge paradigm on a human-verified failure set (n = 142). GPT-4o-mini approved 47.9% of clinically incorrect outputs, while HuatuoGPT-o1 approved all validly scored failures and showed a positive self-preference bias. These results suggest that standalone automated clinical evaluations can substantially overestimate clinical reliability without expert-grounded validation.

---


### 77. [Robust Autonomous UAV Landing on Maritime Platforms via Multimodal Agentic AI and Active Wave Compensation](https://arxiv.org/abs/2606.31613)

**<font color=#1a73e8>作者：</font>** Francisco S. Neves, Pedro N. Pereira, Raul D.S.G. Campilho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous aerial inspection of marine infrastructure is frequently compromised by stochastic sea states, introducing risks of high-kinetic impacts, post-landing toppling, and sensory occlusion. This paper proposes a decoupled, multi-vehicle landing framework synchronizing an Unmanned Surface Vehicle (USV) equipped with a 3-RPU stabilized platform with a robust Unmanned Aerial Vehicle (UAV). The architecture utilizes two independent Deep Reinforcement Learning (DRL) agents: a Soft Actor-Critic (SAC) agent providing high-frequency wave-motion compensation for the landing deck, and a multimodal RL agent for the UAVs final approach. Evaluated in high-fidelity maritime simulations, the system achieved a 100% landing success rate across 15 trials in wave states varying from calm to rough. Results show a mean stabilization efficacy of 87.8%, maintaining the landing surface within 1 degree of the horizontal plane for 96% of the mission duration in rough conditions, effectively contributing to safer landings.

---


### 78. [Calibration, Not Compilation: Detecting and Repairing Misspecified Probabilistic Programs Written by Language Models](https://arxiv.org/abs/2606.31630)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models increasingly write probabilistic programs (in NumPyro, Stan, or Pyro), but a program that compiles, runs, and passes every unit test can still be \emph{statistically} wrong -- a Gaussian likelihood for heavy-tailed data, a Poisson for over-dispersed counts, an invalid prior support, or a pathological parameterization. The right verifier is therefore not a test suite but the Bayesian workflow itself: posterior predictive checks, simulation-based calibration, sampler diagnostics ($\hat R$, divergences, ESS), and held-out predictive density. We study this calibration oracle along three axes. \textbf{Detection:} on a benchmark of $14$ misspecification types across $10$ model families ($200$ instances), it flags the bug with AUC $0.97$ ($88\%$ at $2\%$ FPR \emph{when handed the correct reference program, an upper bound}) -- and a fully \emph{reference-free} version that uses no correct program reaches $62$--$78\%$ (the upper figure from a small automated model search), versus $0\%$ for a unit-test oracle. \textbf{Repair:} used as feedback in an LLM repair loop across fifteen models, calibration significantly outperforms unit-test feedback -- which is itself \emph{significantly worse than no feedback at all}, a passing test inducing false confidence that suppresses repair -- and improves over no feedback on strong-but-unsaturated models (GPT-5.1 $33{\to}92\%$, Claude $75{\to}100\%$; paired McNemar, $n{=}228$). \textbf{Reality:} on programs LLMs write from scratch for neutral briefs, $15$--$47\%$ of runnable ones are statistically misspecified (unit tests catch none), and calibration-guided repair significantly beats LLM-as-judge review, a Bayesian-workflow checklist, and data-summary self-debug. Across all three, the lesson is the same: for probabilistic programs, correctness is calibration, not compilation.

---


### 79. [Moral Safety in LLMs: Exposing Performative Compliance with Puzzled Cues](https://arxiv.org/abs/2606.31644)

**<font color=#1a73e8>作者：</font>** Mohammadamin Shafiei, Shuyue Stella Li, Yulia Tsvetkov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models take on morally consequential roles in healthcare, legal, and hiring contexts, we need to examine whether their ethical behaviors are genuine or superficial. We show that current fairness evaluations substantially overestimate moral safety. Models appear fair when demographic identity is stated as an explicit label, yet become measurably less fair when the same identity must be inferred. We term this failure \emph{performative compliance}, where a model is fair when the presentation resembles a fairness evaluation and less fair as that cue weakens. We introduce a cue-variation methodology that holds the moral dilemma and the demographic identity fixed and varies only how that identity is conveyed. Hiding the explicit label raises harmful decisions by $+4.4$~pp and changes model safety rankings, and the shift persists when models correctly infer the demographic, ruling out attribution error. We propose the \textbf{Cue Visibility Gap}, a model-agnostic robustness metric that can be added to any existing fairness benchmark to separate genuine from performative moral safety. Fairness evaluations that omit cue variation measure surface compliance, not moral robustness, and should not ground deployment decisions in high-stakes settings.

---


### 80. [Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents](https://arxiv.org/abs/2606.31648)

**<font color=#1a73e8>作者：</font>** Utsav Garg, Sungjin Hong, Jason Jung 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and uses preamble conditioning to switch between concise non-reasoning behavior and longer tool-oriented reasoning. We study four choices for scaling tool-using agents efficiently: multilingual supervised fine-tuning, reinforcement learning with verifiable rewards for multi-step tool-use tasks, language-consistency rewards for Korean user-facing responses, and 4-bit quantization for single-GPU serving. The adapted model improves mathematical reasoning, function calling, and agentic natural-language-to-SQL (NL2SQL) performance while preserving general Korean and English instruction-following quality. These results provide a practical recipe and failure-mode analysis for adapting post-trained multilingual models to verifiable agentic workflows under memory-constrained deployment.

---


### 81. [ECHO: Prune to act, trace to learn with selective turn memory in agentic RL](https://arxiv.org/abs/2606.31650)

**<font color=#1a73e8>作者：</font>** Zijun Xie, Binbin Zheng, Enlei Gong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents must repeatedly interact with tools, accumulate evidence, and make decisions under bounded context windows. Existing context-management methods make such rollouts feasible by truncating distant history, folding past turns into summaries, or selecting compact memory states. However, these breakthroughs introduce two coupled limitations. First, as the number of turns grows, historical observations are progressively removed or collapsed into compressed states, making it harder for the policy to reuse fine-grained evidence. Second, once the original turns are no longer source-addressable, outcome-based RL loses an explicit path for aligning policy updates with the evidence that supported a successful final answer. To this end, we propose ECHO, a selective turn-memory framework that jointly addresses history collapse and traceable learning through source-indexed reconstruction. Specifically, ECHO compresses each completed environment turn into a compact memory record, reconstructs bounded policy contexts by selecting from these records, and reuses the selected source indices to route positive outcome credit to the evidence and selection actions that support successful answers. On BrowseComp-Plus, ECHO reaches 43.4% held-out accuracy, outperforming GRPO (28.9%) and the rolling-summary baseline SUPO (36.1%), while using fewer turns and lower trajectory volume than SUPO (Figure 1). Additionally, the trained policy improves zero-shot generalization across multi-objective QA, code generation, and deep information-seeking benchmarks on both dense and MoE backbones.

---


### 82. [SAMBA: A Scatter-Guided Masked Bidirectional Mamba Foundation Model for SAR Target Recognition](https://arxiv.org/abs/2606.31668)

**<font color=#1a73e8>作者：</font>** Ke Wang, Xiaoyi Pan, Zhaoyu Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar automatic target recognition (SAR ATR) is critical for Earth observation and defense, but its practical deployment is constrained by scarce annotated training data. Self-supervised pre-training alleviates this label bottleneck, yet prevailing Transformer architectures incur prohibitive quadratic computational complexity, and conventional universal masking neglects the unique electromagnetic scattering properties intrinsic to SAR imagery. To address these limitations, we propose SAMBA (Scattering-Guided Bidirectional Mamba), an efficient self-supervised pre-training foundation model for SAR target interpretation. Our framework features three core innovations: (i) a linear-complexity Mamba encoder with a mid-sequence class token to mitigate computational bottlenecks; (ii) a three-level hierarchical Scattering-Guided Masked Autoencoder (SG-MAE) masking strategy guided by SAR physical priors, aligning the pretext task with SAR's intrinsic imaging mechanism; (iii) a lightweight SpatialMix feature interaction module to enhance cross-region feature fusion. We also design a two-stage cross-domain pre-training pipeline to optimize the overall pre-training process. Extensive evaluations demonstrate that SAMBA consistently delivers superior performance across all pre-training configurations, with substantially fewer parameters than both CNN and Transformer baselines. Compared with the default masking strategy in standard MAE, the proposed SG-MAE strategy further boosts the model's few-shot transfer capability. Benchmarking on seven downstream datasets covering classification and detection tasks shows SAMBA achieves state-of-the-art (SOTA) performance on most metrics, fully validating its robust generalizability across diverse SAR interpretation tasks. Source code and pre-trained weights are publicly available at this https URL.

---


### 83. [WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models](https://arxiv.org/abs/2606.31672)

**<font color=#1a73e8>作者：</font>** Ting-Bing Xu, Jiacheng Sui, Zhe Gao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in interactive world models (IWMs), existing benchmarks evaluate action following only at trajectory level and ignore memory and interaction physics. We introduce WorldRoamBench, an open-world benchmark for long-horizon stability across four dimensions, each with tailored innovations: (i) Action: per-frame action metric bypassing cross-model semantic scale disparity and exposing failures hidden by trajectory; (ii) Vision: segment-based drift metric capturing non-monotonic mid-sequence collapse missed by start-vs-end comparisons; (iii) Physics: controllability-gated evaluation over mechanics, optics, and 3D consistency, scoring plausibility under faithful action execution; (iv) Memory: action-decoupled protocol evaluating scene memory via transition-localized 3D point-cloud reconstruction and subject memory via tracking-plus-VLM reasoning. The benchmark comprises 600+ test cases across Nature, Urban, and Indoor scenes in first/third-person views with WASD 10-60s continuous interaction. Evaluating 10+ open/closed-source models reveals none reliably satisfies all dimensions; even the best achieves only moderate scores. Advances on WorldRoamBench are steps toward IWMs that are stable, physically grounded, memory-faithful, and deployable in real-world applications.

---


### 84. [ShellMaker: Language-Guided Exterior Completion under Structural Constraints](https://arxiv.org/abs/2606.31680)

**<font color=#1a73e8>作者：</font>** Ruiqi Xu, Daniel Aliaga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in indoor scene generation, synthesizing coherent building exteriors consistent with generated interiors remains largely unexplored. Existing methods can generate floor plans and wall layouts but typically stop at a structural shell, lacking stylistically consistent facades and roofs. Completing these exteriors is challenging because the footprint, wall geometry, and opening semantics must remain fixed-constraints that unconstrained generative models often violate. We introduce ShellMaker, a language-guided exterior completion framework that operates under these structural constraints. Given a building scaffold and a text style prompt, ShellMaker generates a complete exterior mesh with PBR materials by combining parametric roof generation, LLM-based part-aware prompt refinement, joint wall-roof material retrieval, and geometry-aware assembly. Operating on a format agnostic scaffold representation, ShellMaker generalizes to indoor generators, CityGML, and CAD inputs, while maintaining structural consistency and improving architectural coherence over retrieval and unconstrained generative baselines. The project page is available at this https URL

---


### 85. [Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot, and Fine-Tuned Evaluation on Romanian](https://arxiv.org/abs/2606.31718)

**<font color=#1a73e8>作者：</font>** Dragos-Mitrut Vasile, Elena-Simona Apostol, Stefan-Adrian Toma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relation extraction (RE) for low-resource languages is typically constrained by the lack of annotated corpora. We investigate the feasibility of cross-lingual RE for Romanian by combining automatic dataset translation with large language model (LLM) inference. We translate the SemEval-2010 Task 8 benchmark from English to Romanian using an LLM-based translation pipeline and evaluate Gemma 4 31B under zero-shot, few-shot, and QLoRA fine-tuned configurations, against four encoder baselines spanning 125M to 560M parameters: XLM- RoBERTa (base and large), Romanian BERT, and RoBERT- large. We assess two task formulations: relation classification with marked entities and end-to-end extraction. Our results show that Romanian incurs a 3 to 5 percentage point (pp) drop relative to English in prompt-only settings, that few-shot prompting provides marginal gains over zero-shot, and that QLoRA fine-tuning improves macro F1-Score by more than 22 percentage points in both languages while reducing the cross-lingual gap from 3.3 to 1.4pp. The encoder baselines come within 1-4pp of QLoRA Gemma on Romanian despite being 50-250 times smaller, with monolingual Romanian BERT at 125M parameters matching multilingual XLM-R at 278M. The case for using a 31B model for single-task RE on Romanian is therefore weak in deployment scenarios where compute matters. We release the translated dataset, evaluation code, and trained models.

---


### 86. [Seeing Is Not Sharing: Some Vision-Language Models Overestimate Common Ground in Asymmetric Dialogue](https://arxiv.org/abs/2606.31719)

**<font color=#1a73e8>作者：</font>** Nan Li, Albert Gatt, Massimo Poesio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In collaborative dialogue, shared perception does not guarantee shared interpretation. Mutual understanding must be established through interaction. We investigate whether vision-language models (VLMs) can distinguish what could be shared from what has been shared between dialogue participants through grounding. We formulate this as an interpretation-matching task on 13,077 annotated reference expressions from HCRC MapTask dialogues, and evaluate VLMs under systematically controlled manipulations of dialogue context and map-information access. Our results show that providing authentic map images improves overall performance but shifts models toward over-predicting alignment. Textual descriptions of the same map content reproduce this bias, while non-informative images suppress alignment predictions entirely, indicating that the bias is driven by task-relevant map content, not the visual channel. This improvement comes at the cost of degraded accuracy on non-aligned cases. Calibration analysis and reference-chain tracking further suggest that models rely on static referential cues on the maps rather than tracking how grounding unfolds through dialogue history. We observe these patterns most clearly in Qwen3-VL-8B-Instruct and, to varying degrees, in four additional models from two architecture families. In models that exhibit the bias, map content, whether presented visually or textually, is treated as evidence of mutual understanding, conflating potential with established common ground.

---


### 87. [UniCoder: Unified Visual-to-Code Generation via Symbolic Rewards and Reference-Guided Code Optimization](https://arxiv.org/abs/2606.31732)

**<font color=#1a73e8>作者：</font>** Yaozhi Zheng, Yilei Jiang, Manyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-to-Code generation, which transforms scientific plots, vector graphics, and webpages into executable scripts, demands a level of pixel-precise alignment that standard Multimodal Large Language Models (MLLMs) fail to achieve through Supervised Fine-Tuning (SFT) alone. While Reinforcement Learning (RL) offers a theoretical pathway to bridge this gap, its application is hindered by two fundamental obstacles: (1) \textit{Reward Coarseness}, where semantic metrics like CLIP scores fail to penalize fine-grained element deviations, and (2) \textit{Exploration Stagnation}, where the sparse, heterogeneous code search space prevents the policy from bootstrapping valid trajectories. To overcome these limitations, we introduce UniCoder, a unified RL framework that integrates two novel mechanisms. First, we propose \textbf{Symbolic Attribute Alignment}, which employs a lightweight auxiliary LLM to parse generated code into discrete visual attributes (e.g., hex colors, coordinate limits), enabling dense, element-wise reward computation. Second, to escape local optima, we devise \textbf{Reference-Guided Code Optimization}, a strategy that dynamically injects ground-truth trajectories into low-performing rollout groups, transforming blind exploration into guided policy improvement. Extensive experiments on ChartMimic, UniSVG, Design2Code and ScreenBench benchmarks demonstrate that our 8B-parameter model not only surpasses all open-source baselines but also achieves state-of-the-art performance comparable to proprietary models, establishing a new paradigm for generalized visual-to-code synthesis.

---


### 88. [MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734)

**<font color=#1a73e8>作者：</font>** Jiwen Yu, Jianxiong Gao, Jianhong Bai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video World Models are interactive video generation models that predict future world states based on user actions and history video frames. A critical challenge in video world models is the lack of memory, causing inconsistent generated scenes over extended durations. Previous methods explored rule-based context frame retrieval as memory, but they fail to generalize in scenarios with scene occlusions and dynamic objects. We propose MemLearner, a learning-based adaptive context query method using query tokens to bridge context and predicted tokens. By leveraging the video generation model itself for context querying, MemLearner exploits pre-trained visual priors without training additional modules from scratch, and incorporates efficient strategies for training and inference. We collect a dataset of long videos with scene occlusions and dynamic objects, paired with camera pose annotations, and propose a multi-dataset training strategy leveraging both annotated rendered and unannotated real-world videos. Extensive experiments demonstrate that MemLearner significantly outperforms prior video world models in terms of scene consistency and memory, particularly under challenging occlusion and dynamic scenarios.

---


### 89. [Addressing Over-Refusal in LLMs with Competing Rewards](https://arxiv.org/abs/2606.31748)

**<font color=#1a73e8>作者：</font>** Taeyoun Kim, Aviral Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety training on language models often induces over-refusal: improved safety on harmful prompts at the cost of increased refusal on harmless ones. Though this trade-off can be mitigated by training models with reinforcement learning (RL) to reason before answering, it does not remove the underlying problem that reasoning can often be a "rubber stamp" for a predetermined response. In this paper, we address the safety-refusal trade-off by rethinking how models are trained to reason about safety. Our key insight is that unsafe reasoning can itself serve as a useful exploratory signal. Rather than preemptively blocking harmful thoughts, we encourage the model to sufficiently explore unsafe reasoning but produce a safe response. The harmful exploration improves the model's ability to distinguish harmful from harmless prompts by resolving ambiguity, allowing it to remain safe while complying only when appropriate. We cast this as an adversarial optimization problem in which a reasoning player explores strategies for producing an unsafe response and an answer player ensures that the final output is safe. We train a single model with dense rewards to play both roles within one chain-of-thought, across different segments. To achieve this, we find that process rewards are crucial for stable optimization of competing objectives. Our resulting model SEAR deliberately engages in harmful reasoning as exploration while reliably flipping back to a safe answer. We demonstrate that this behavior helps mitigate over-refusal and defend against attacks that directly manipulate the reasoning to be harmful.

---


### 90. [Investigating LLM-Powered Dissenting Minority Support in Power-Imbalanced Group Decision-Making: Counterargument and Mediation as Intervention Strategies](https://arxiv.org/abs/2606.31762)

**<font color=#1a73e8>作者：</font>** Soohwan Lee, Seoyeong Hwang, Mingyu Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Minority viewpoints are often suppressed in power-imbalanced group decision-making due to social pressure to comply with the majority. To address this problem, we developed an LLM-powered dissenting minority support system that aimed to foster attention to minority views through either AI-generated counterarguments or AI-mediated messages. We conducted a mixed-method experiment with 96 participants in 24 groups, comparing minority members' experiences across baseline, AI-counterargument, and AI-mediated message conditions. Our findings revealed a nuanced trade-off: AI-generated counterarguments fostered a more flexible atmosphere and enhanced satisfaction, while AI-mediated messaging increased minority participation but unexpectedly reduced their psychological safety. This research contributes empirical evidence on how different AI implementations affect group dynamics, identifies a critical support paradox between participation and psychological safety, provides design implications for future systems, and highlights ethical challenges in implementing AI-mediated communication in hierarchical settings. These insights advance understanding of designing more equitable AI support for power-imbalanced group decision-making.

---


### 91. [A Self-Evolving Agentic System for Automated Generation and Execution of Biological Protocols](https://arxiv.org/abs/2606.31763)

**<font color=#1a73e8>作者：</font>** Yankai Jiang, Weiting Tang, Haoran Sun 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous wet-lab experimentation requires more than plausible protocol text: biological intent, quantitative procedures, device constraints and experimental feedback must remain aligned from protocol and SOP design to code and physical execution. We developed ProtoPilot, a self-evolving multi-agent system, together with an expert-grounded benchmark and evaluation framework for testing this conversion as an experimental automation problem. The framework spans 294 synthetic-biology and molecular-biology tasks derived from 98 gold-standard protocols, wet-lab expert rubrics, device-level validity gates and real experimental tests. ProtoPilot incorporates layer-wise verifiability, multi-agent orchestration and a runtime-updated skill library to generate protocols, expand SOPs, synthesize SDK-compliant code and revise workflows from wet-lab feedback. It achieved a Top@3 expert-preference rate of 90.2%, an overall protocol-to-code gate pass rate of 89.5% and an Opentrons pass rate of 88.24%, compared with 32.35% for OpenTrons-AI. Wet-lab validation produced interpretable readouts, Sanger-confirmed products and feedback-corrected PCA-assembled DNA targets, establishing a verifiable route to autonomous experimentation. Together, these results show that the evaluation framework captures execution-relevant requirements for autonomous wet-lab automation, and that ProtoPilot can meet them by converting protocol and code generation into validated execution and feedback-guided revision.

---


### 92. [CHERRY: Compressed Hierarchical Experts with Recurrent Representational Yield](https://arxiv.org/abs/2606.31796)

**<font color=#1a73e8>作者：</font>** Dohyeon Kwon, Youngjin Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study three complementary techniques for training compute-efficient language models.
(1) Selective supervision and per-token efficiency. Selective Ground Truth Token Training (SGT) concentrates supervision on the ~15% of output tokens that carry semantic payload. Through positive gradient coupling in position-shared transformer weights -- a token-level instance of auxiliary-task transfer -- the remaining 85% of unsupervised tokens still improve substantially, giving a 4.5x per-supervised-token efficiency (at the step-100 eval optimum, ~67% of the full-sequence loss reduction is recovered from 15% of the supervision). We prove that this improvement on unsupervised tokens is guaranteed whenever the gradient coupling coefficient gamma-bar = 0.72 is positive (Theorem 1), and show the effect is a property of natural-language structure: it collapses on shuffled text.
(2) Depth compression with recurrent recovery. A 48-layer, 1B-parameter transformer is compressed to 6 layers (227M) by averaging adjacent layers and restored through learned recurrent unrolling. With 34 effective recurrent layers it reaches a held-out loss of 2.934, within measurement noise of a 566M dense model at 2.926 -- a 2.5x reduction in parameters.
(3) Fusion of compressed experts. Assembling several compressed models as a Mixture of Efficient Experts (MoEE) with multi-token prediction improves over each single expert at comparable active parameters: a 2-expert MoEE reaches loss 2.789 versus 2.926 for the best single compressed model.
We validate these techniques on CHERRY-1.8B, a Korean foundation model whose every trainable parameter derives from our own training runs. We are explicit throughout about the scope of the evidence (one model family, Korean data, loss-based metrics) and about which claims are established versus prospective.

---


### 93. [Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision](https://arxiv.org/abs/2606.31800)

**<font color=#1a73e8>作者：</font>** Xianda Zheng, Huan Gao, Meng-Fen Chiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent progress, the reasoning capabilities of large multimodal language models (MLLMs) remain fundamentally constrained by static supervision, where fixed prompts, rules, or reward models provide non-adaptive guidance throughout training. Such static signals are often sufficient to enforce output formats, but fail to shape the underlying reasoning process, leading to brittle generalization and performance saturation in complex decision-making tasks. We propose Evo-PI, a principle-centric learning framework that treats reasoning principles as explicit, language-based supervision signals that can be generated, evaluated, and iteratively evolved. Instead of relying on fixed rewards, Evo-PI enables a co-evolutionary loop in which principles guide model reasoning, while model behaviors in turn refine the principles that supervise them. This dynamic alignment mechanism allows supervision to progressively adapt to the model's reasoning deficiencies. We instantiate Evo-PI in medical visual question answering as a high-stakes testbed requiring structured visual-textual reasoning. Across eight benchmarks and multiple model backbones, Evo-PI consistently improves reasoning accuracy, achieving gains of up to 24.6%. Our results suggest that evolving principle-guided supervision offers a scalable and general paradigm for training expert-aligned reasoning in MLLMs. Code is available at this https URL.

---


### 94. [RAISE: LLM-based Automated Heuristic Design with Robust Adversary Instance Search](https://arxiv.org/abs/2606.31801)

**<font color=#1a73e8>作者：</font>** Fei Liu, Alessio Figalli, Patrick Owen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated Heuristic Design (AHD) with Large Language Models (LLMs) has shown remarkable progress in discovering high-quality heuristics. However, existing LLM-based AHD methods optimize heuristics for a fixed training instance set and may fail catastrophically when deployed under real-world distributional shifts. We propose Robust Adversary Instance Search (RAISE), a framework that integrates constrained worst-case instance search within a principled neighborhood of the training distribution into the LLM-based evolutionary search loop. RAISE treats robust AHD as a constrained adversarial instance search problem: the outer loop evolves heuristics via LLM operators, while an LLM-free inner loop efficiently identifies hard instances within an epsilon-ball around the training instance set using a basis distribution parameterization with boundary projection. Comprehensive experiments on Online Bin Packing (OBP), Online Job Shop Scheduling (OJSP), and Online Vehicle Routing (OVRP) across five distribution families demonstrate that existing LLM-based AHD methods degrade by up to 19 times under distribution shift, while RAISE consistently maintains strong performance across all tested distributions and problem scales

---


### 95. [Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models](https://arxiv.org/abs/2606.31804)

**<font color=#1a73e8>作者：</font>** Keivan Faghih Niresi, Alice Cicirello, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependencies across interconnected energy nodes. However, in real-world energy systems, accurate point forecasts alone are insufficient, as operators also require reliable uncertainty estimates to support risk-aware decision-making, grid stability, and operational planning under uncertainty. Conformal prediction provides a principled and model-agnostic framework for uncertainty quantification with statistical coverage guarantees, making it particularly attractive for safety-critical energy applications. However, existing conformal prediction approaches often fail to fully capture the complex spatial-temporal structure of energy systems. To address these limitations, we propose STOIC (Spatial-Temporal Graph Conformal Prediction with In-Context Learning), a novel framework that integrates graph-based forecasting with the zero-shot calibration capabilities of tabular foundation models. STOIC first generates point forecasts using an STGNN and subsequently reformulates spatial-temporal residuals into a tabular representation suitable for in-context learning. Leveraging a tabular foundation model, STOIC calibrates prediction intervals without task-specific retraining, effectively capturing both sequential and relational dependencies. We evaluate STOIC on five diverse benchmarks, including synthetic simulations as well as real-world electricity and district heating networks. Across all datasets, STOIC consistently outperforms existing conformal prediction baselines, delivering more reliable and robust uncertainty estimates for complex graph-structured energy time series.

---


### 96. [Large Databases Need Small, Open-Weight Language Models](https://arxiv.org/abs/2606.31808)

**<font color=#1a73e8>作者：</font>** Parker Glenn, Alfy Samuel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model systems built around proprietary APIs often operate on a token-based cost model. This becomes prohibitively expensive in the context of large databases, where LM-enhanced relational operators can incur costs exceeding $10,000 for a single set of experiments, hindering thorough research and practical deployment. In this paper, we demonstrate that quantized, open-weight models running locally on just 16GB of VRAM can match or exceed the accuracy of closed-source counterparts at lower latency and a fraction of the price, challenging the prevailing assumption that closed-source LM APIs are necessary for effective LM-database integration. We present and analyze the key system optimizations required to efficiently deploy these open-weight models within an LM-DB system. By integrating these local models into the BlendSQL v0.1.0 framework, we demonstrate a 390x reduction in overall costs and 3.8x reduction in latency compared to a proprietary LM API. We make our code available at this https URL.

---


### 97. [Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR](https://arxiv.org/abs/2606.31813)

**<font color=#1a73e8>作者：</font>** Ruijia Zhang, Jiacheng Zhu, Hanqing Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) and its variants enable parameter-efficient fine-tuning of large language models under the supervised fine-tuning (SFT) paradigm. However, their efficacy and behavior under Reinforcement learning with verifiable rewards (RLVR) are less well understood. In particular, two structurally initialized LoRA variants, PiSSA and MiLoRA, which outperform standard LoRA under SFT, can underperform standard LoRA under RLVR and may even exhibit training instability. These observations suggest that how to initialize the low-rank matrices in RLVR remains unclear. In this work, we develop a theoretical analysis of LoRA in RLVR, showing that orthonormal initialization achieves the minimal gap between LoRA outcome and that of full fine-tuning. Guided by this insight, we propose geometry-preserving orthonormal initialization for low-rank adaptation in RLVR, leading to two new variants, RLPO and RLMO. Experiments on mathematical reasoning benchmarks show that the proposed orthonormal initialization stabilizes RLVR training and outperforms standard LoRA, contrasting with PiSSA and MiLoRA. Finally, our unified analysis for LoRA initialization also explains why PiSSA and MiLoRA can underperform in RLVR, which may be of independent interest. Code and checkpoints are publicly available at this https URL.

---


### 98. [Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning](https://arxiv.org/abs/2606.31825)

**<font color=#1a73e8>作者：</font>** Junha Jung, Minbyul Jeong, Suhyeon Lim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models have shown great promise in clinical image reasoning, but existing post-training pipelines remain predominantly outcome-centric, relying on final answer correctness or sequence-level preferences. This suffers from sparse credit assignment, making it difficult to optimize the reasoning process essential for clinical applications. Our analysis reveals that cascading errors from early-stage reasoning failures are a leading cause of incorrect predictions in medical visual question answering (VQA) benchmarks. Motivated by this, we propose Medical Reasoning-aware Policy Optimization (MRPO), an RL algorithm that incorporates step-wise process rewards. When the final answer is incorrect, MRPO assigns exponentially larger penalties to tokens in earlier invalid reasoning steps, breaking failure cascades without compromising successful paths. Across three multimodal LLM backbones, MRPO consistently outperforms standard GRPO and a recent RL baseline, and on Qwen3-VL-8B-Instruct even surpasses substantially larger medical MLLMs such as HuatuoGPT-Vision-34B by 2.79 points. Moreover, MRPO reduces early-stage reasoning failures from 64.0% to 13.0%, showing that targeted mitigation of cascading failures improves both reasoning quality and final answer accuracy. Our code is available at this https URL

---


### 99. [An Agentic AI Framework to Accelerate Scientific Discovery in Plant Phenotyping](https://arxiv.org/abs/2606.31831)

**<font color=#1a73e8>作者：</font>** Renan Souza, Daniel Rosendo, Kelsey Carter 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-throughput plant phenotyping now generates image derived datasets far faster than scientists can analyze them. At Oak Ridge National Laboratory's Advanced Plant Phenotyping Laboratory (APPL), automated stations image hundreds of plants daily across multiple remote sensing modalities; yet, trait extraction and interpretation remain manual, expert-bound, and strictly post-hoc, making analysis, not acquisition, the binding constraint on discovery. We present an end-to-end agentic AI framework that turns the facility from a data factory into an interactive autonomous, discovery platform, where scientists partner with AI agents to accelerate time to insight. A conversational Co-Scientist Agent translates a scientist's natural-language question into a structured analysis plan, and a headless Compute Agent dispatches Vision Transformer segmentation and trait extraction on the Frontier exascale supercomputer. The two agents run in separate security and resource domains and communicate over a secure, token-authenticated streaming channel, a design that accounts for the federation, data-movement, and provenance realities cloud-native agentic frameworks ignore, ensuring end-to-end provenance is captured for every interaction. The framework turns a days- to weeks-long analysis process into an interactive loop where agents reason over results, recommend next analyses, and respond to follow-up questions in seconds.

---


### 100. [Harnessing Textual Refusal Directions for Multimodal Safety](https://arxiv.org/abs/2606.31876)

**<font color=#1a73e8>作者：</font>** Moreno D'Incà, Massimiliano Mancini, Nicu Sebe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary findings confirm this ability, though effectiveness is conditioned by layer selection, steering strength, and cross-modal alignment, with the latter causing safe multimodal inputs to be spuriously steered toward refusal. Building on this, we introduce Modality-Agnostic Refusal Steering (MARS), a light-weight training-free approach that injects multimodal safety without the need for multimodal safety data. MARS corrects modality misalignment via activation re-centering, adaptively scales steering strength within a geometrically defined trust region, and selects the optimal intervention layer, operating at the first generated token. Evaluated on five SOTA MLLMs across safety, utility, and video jailbreak benchmarks, MARS achieves consistent safety gains while preserving utility. These results reveal that safety-relevant structure is shared across modalities and that textual refusal directions are a powerful and underexplored foundation for multimodal alignment.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-121](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
