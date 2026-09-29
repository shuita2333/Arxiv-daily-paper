# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 301. [Relative Generalization Invariance of LLM Pretraining](https://arxiv.org/abs/2609.33016)

**<font color=#1a73e8>作者：</font>** Fengzhuo Zhang, Shuche Wang, Shenggui Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) pretraining performance is jointly shaped by three components of the training triplet: the optimizer, model architecture, and training data stream. However, how these components influence performance in distinct ways remains unclear. We take a first step toward isolating their effects by studying relative generalization. We introduce Relative Generalization Invariance (RGI), the invariance of the validation-loss difference between any two tokens across models. We show that RGI approximately holds across a wide range of optimizers and moderate architectural variations, suggesting that these choices induce an approximately uniform shift in token-wise losses. In contrast, changing the training data stream can substantially alter relative generalization. We further show that RGI cannot be explained by the neural tangent kernel or mean-field regimes alone and prove that it can emerge in an overparameterized quadratic model. Overall, our work identifies RGI as a new phenomenon in LLM pretraining that helps distinguish the effects of optimizers and architectures from those of training data.

---


### 302. [Improving the Diversity of LLM Outputs without a Trade-off](https://arxiv.org/abs/2609.33038)

**<font color=#1a73e8>作者：</font>** Ryoma Sato  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose DAST (Diversifying Arithmetic Sampling with TokenTour), a method that increases the diversity of LLM outputs without any change to the marginal distribution and with negligible generation-time overhead (a few microseconds). We observe that token IDs are often arranged in a meaningless order and reassign them so that tokens with similar meanings appear consecutively. This can be done in advance in a few hundred seconds per model, and the resulting order can be reused for all subsequent generations. By combining this order with arithmetic sampling (or quasi-Monte Carlo methods), we make similar tokens less likely to be generated across runs while preserving the distribution. Our method not only produces qualitatively good ideas but also significantly improves performance on the downstream task of ProtoQA.

---


### 303. [Agent Safety From Within: Detecting Harmful Trajectories from LLM Internal States](https://arxiv.org/abs/2609.33039)

**<font color=#1a73e8>作者：</font>** Difan Jiao, Ashton Anderson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents can now perform sophisticated sequences of actions via tools and harnesses, which has increased the scope of the damage they can cause. Guard models, however, are mainly built for content moderation and thus are not well-suited to detecting this agentic risk. To address this, we proceed by first conducting a representational analysis, then use the resulting insights to build a solution. In our analysis, we focus on two types of trajectory-level agentic harms: harmful content, which is expressed directly, and unsafe tool use, which depends on whether an action is consistent with the interaction that produced it. We investigate how open-source guard models represent these two types of harm and find that they are linearly readable inside the model, even though guard models predict no better than chance on pairs that differ only in the called tool's schema. The two harm types also follow nearly orthogonal internal directions, and neither reliably serves as a proxy for the other. These results motivate reading trajectory safety directly from internal states. We introduce TACIT, a readout of a frozen backbone's internal states that decodes no tokens. Trained on six trajectory-safety benchmarks, a linear probe raises mean macro-F1 from 62.3 for the strongest open guard to 80.7, and refined readouts reach 86.2. With each benchmark held out of training entirely, the refined readouts still lead the strongest guard (65.7 vs. 61.1). With the same backbone, training data and test split, the frozen readout is on par with full safety fine-tuning, and it improves the fine-tuned model further when applied on top. The probe trains about one millionth as many parameters as full fine-tuning in about a sixth of the time, and TACIT has the lowest latency of the guards we evaluate.

---


### 304. [Medical Knowledge Is Not All You Need: When Medical Q&A Becomes Situated Patient Assistance](https://arxiv.org/abs/2609.33040)

**<font color=#1a73e8>作者：</font>** Shreya Bali, Riku Arakawa, Jill Fain Lehman 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reliability in medical Q&A is often pursued by grounding responses in authoritative medical information. We show that when Q&A is embedded within ongoing care, reliability depends on more than what the system knows medically. In a study with 73 skin cancer patients practicing postoperative wound care, 41.9% of response-requiring questions depended on information beyond the procedure, including visual or physical state, environmental context, or prior actions. These demands varied across patients, consistent with patients recruiting the assistant into different informational roles. We then replayed the questions to seven LLMs while adding procedural and postoperative guidance. Errors remained substantial, including treating unknown states as known, even under explicit guardrails; with full procedural context, six of seven models more often introduced later steps prematurely. Based on these findings, we propose a design space for situated medical assistance that connects what the assistant and patient can each reliably establish to the form of assistance provided.

---


### 305. [Balancing Early Performance Sacrifices with Long-Term Gains: Scaling Learning-Rate Warmup Duration Across Training Horizons](https://arxiv.org/abs/2609.33041)

**<font color=#1a73e8>作者：</font>** Kristi Topollai, Anna Choromanska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-rate warmup is a standard technique in language-model training, yet its duration remains largely heuristic. Common approaches use either a fixed number of updates or a fixed fraction of the training horizon, two choices that imply very different scaling as training gets longer. When should warmup stay fixed, and when should it grow with the horizon? We address this question with a quadratic model whose modes respond differently to the peak learning rate. Warmup slows progress in directions that already contract well at the peak rate, but can remove persistent error in directions near the stability edge, with higher peak rates shifting the balance toward longer warmup durations. This yields a compact horizon scaling law that captures regimes ranging from essentially no warmup, through fixed-duration warmup, to durations that grow with the training horizon, and explains how the preferred regime changes with peak learning rate. Because the law captures the tradeoff between giving up early progress and improving the trajectory that follows, it can be fit using shorter runs and used to predict warmup at substantially longer horizons. Together, our results explain several familiar properties of warmup through a single tradeoff and suggest treating warmup duration as a horizon-dependent hyperparameter rather than a fixed training heuristic.

---


### 306. [Pinned and Still Unstable: Within-Judge Verdict Variance and the Noise Floor of LLM-as-Judge Leaderboards](https://arxiv.org/abs/2609.33044)

**<font color=#1a73e8>作者：</font>** Krishna Chytanya Ayyagari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern LLM evaluation assumes that pinning a judge to a fixed model snapshot and decoding at temperature zero yields reproducible verdicts. We show this assumption fails as a property of how LLM-as-Judge is operationalized on cloud serving infrastructure, not of any particular model family. Across four frontier judges all served via a single major enterprise cloud platform and three standard benchmarks (Arena-Hard, AlpacaEval 2, MT-Bench), identical inputs to the same pinned, temperature-zero judge produce different verdicts across re-runs: per-item flip rates of roughly 5% on average and about 40% on the close-call items that decide leaderboard margins, with a per-judge magnitude spanning a 40x range (from 0.13% to nearly 10%). We introduce metrics tailored to this instability: per-item flip rate, a two-part stability profile (waver fraction and conditional intensity), and adjacency separability - and report what the variance does and does not do to rankings. For a single judge the aggregate ranking is stable (0% top-K instability, 0% pooled winner flip); what degrades is precision: under a paired hierarchical bootstrap, roughly one-fifth to three-quarters of adjacent leaderboard positions are statistically indistinguishable, a noise floor we attribute primarily to finite prompt sampling rather than to the judge. Across judges, leaderboards agree on the coarse ordering but diverge in the middle (Kendall's tau as low as 0.42-0.64 between families on Arena-Hard), and of 13 published head-to-head ranking claims we re-judge, 5 fail under a defensible judge swap or re-run. We argue that leaderboards report unhedged point estimates that misrepresent the noise floor of the instrument, and we propose a minimal, low-cost reporting protocol: several judge re-runs, published stability profiles and adjacency intervals, and results under at least two judges from different families.

---


### 307. [Cost-free Spectral Estimation for Adaptive Newton--Schulz in Matrix Optimizers](https://arxiv.org/abs/2609.33047)

**<font color=#1a73e8>作者：</font>** Kristi Topollai, Anna Choromanska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix optimizers such as Muon transform each momentum matrix through an approximate orthogonalization, typically implemented by a small number of Newton-Schulz matrix multiplications. The quality and cost of this approximation depend strongly on the singular-value spectrum of its input, yet existing implementations use the same fixed polynomial routine for every layer and throughout training. We show that this uniform treatment is unnecessary: the computations in the Newton-Schulz method already reveal enough information to make the method adaptive. The Gram matrices formed inside Newton-Schulz iterations yield spectral moments through inexpensive scalar reductions, requiring no additional matrix multiplications. From these moments, we recover an estimate of the empirical singular-value distribution and use it to select a polynomial routine specialized to the current matrix. This turns Newton--Schulz orthogonalization into a spectrum-adaptive procedure that responds to differences across both layers and training time. On saved momentum matrices, spectral estimation substantially reduces orthogonalization error at a fixed iteration budget or reaches the same accuracy with fewer iterations, and in GPT pretraining up to 1B parameters it lowers the validation loss of two matrix optimizers. Our results suggest that matrix-function operations inside optimizers need not be designed for a conservative worst-case spectrum: they can cheaply measure the spectrum they are already processing and specialize computations accordingly.

---


### 308. [SketchSSM: Write to the Full State, Read from a Compact Sketch](https://arxiv.org/abs/2609.33051)

**<font color=#1a73e8>作者：</font>** Omin Kwon, JoongWon Shin, Minseo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid-attention models replace most softmax attention layers with linear attention, reducing KV-cache growth and enabling larger decode batches where recurrent state access becomes a major bottleneck. ReplaySSM amortizes state updates by buffering keys and values, but each new query still requires a full-state read even though the state remains unchanged between state updates. We observe that low-rank state-weighted query approximation accurately preserves state-read outputs. Although future queries are unknown, the basis vectors used to approximate them can be fixed offline. Based on this observation, we introduce SketchSSM, which preserves full-state updates while approximating reads. At each state update, SketchSSM reads the full state once to precompute outputs for these basis vectors, storing them in a compact sketch. Each subsequent decode step combines the sketch vectors with query-dependent coefficients to reconstruct the output without a full-state read. Across four Mamba-2-, GDN-, and KDA-based models, SketchSSM reduces state-access traffic by approximately 10x while largely preserving average accuracy across four decode benchmarks and recall on four RULER retrieval tasks. On one NVIDIA B300, linear-attention kernel speedups over the standard vLLM baseline reach 7.78x, 5.22x, and 5.20x for Mamba-2, GDN, and KDA, respectively, with up to 2.64x higher decode throughput on Nemotron 3 Super.

---


### 309. [Large Language Models Substantially Compress Well-Being Inequality but Largely Preserve Its Socioeconomic Structure](https://arxiv.org/abs/2609.33055)

**<font color=#1a73e8>作者：</font>** Nattavudh Powdthavee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research using large language models (LLMs) to generate synthetic populations has repeatedly shown that model outputs compress the diversity of human experience. This has raised doubts about whether LLM-generated data can capture meaningful differences within populations. We show that such compression does not necessarily erase the social structure of human heterogeneity. Using 93,901 respondents from 66 countries and territories in Wave 7 of the World Values Survey, we ask six LLMs to predict respondents' life satisfaction from demographic, socioeconomic, and attitudinal profiles. All six models substantially understate the overall dispersion of life satisfaction. Yet after normalizing for these differences in scale, they largely reproduce the human income gradient in well-being inequality: lower-income groups remain relatively more heterogeneous than higher-income groups. The pattern is robust to country fixed effects, equal-country weighting, WVS survey weights, and observed demographic composition, and it extends directionally to employment, education, and perceived control. Fidelity is weaker for extreme outcomes and country-specific gradients. These results show that the amount of heterogeneity preserved by an LLM and the way that heterogeneity is distributed across social groups are distinct properties. LLM-generated populations can therefore substantially compress human variation while retaining meaningful information about where that variation is concentrated.

---


### 310. [LLM sequential decision making under uncertainty in biochemical domains](https://arxiv.org/abs/2609.33061)

**<font color=#1a73e8>作者：</font>** Mattias Akke, Soojung Yang, Jurgis Ruža 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to drive scientific discovery. Understanding how LLMs make decisions from new data and memory of the literature is vital before trusting them to design experiments under tight experimental budgets. However, their decision strategies are invisible in the current performance scores used to evaluate research agents. Here, we benchmark five frontier LLMs in a Bayesian Optimization setting against published statistical baselines on seven combinatorial datasets spanning protein engineering, reaction optimization, molecular design, peptide self-assembly, and catalysis. Performance is paired with direct measurements of model beliefs and actions, enabling highly resolved behavior analysis. A prompt ablation that progressively strips context separates memorization from chemical reasoning and from bare categorical optimization. Prior chemical knowledge helps in expectation, but with high variance and occasionally even harms performance. No configuration tested decisively beats a mean statistical baseline across domains. Belief-movement and Martingale diagnostics, corrected here for a measurement-noise bias that mislabels rational agents as irrational, show that models overreact to incoming data rather than entrenching on their priors in the contexts studied here. Interestingly, while LLM actions are exploitative, models sincerely intend to explore and consistently act on that intent. This failure is a competence gap arising from context-stickiness. Removing in-context history restores exploration, indicating that priors and data must be decoupled to achieve effective LLM-driven discovery.

---


### 311. [Reading Too Much into Context: Passive Exposure Can Steer LLM Decisions](https://arxiv.org/abs/2609.33065)

**<font color=#1a73e8>作者：</font>** Yuxiang Zheng, Lin Tian, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants can now search the web and consult external sources while completing user requests. These sources can provide useful evidence, but they can also introduce additional content into the model's context. Can such passive exposure steer a decision even when the added content provides no reason to change it? We examine the stability of model decisions on the same tasks with and without such external content. Across all open-weight and closed-weight models we test, exposure systematically shifts decisions, with effects reaching nearly 50 percentage points in closed-weight models. The same pattern appears with real-world online opinions. The influence also extends beyond subjective preferences. Such exposure can steer models toward choices that violate explicit user requirements and increase their acceptance of false claims. In short, what enters an LLM's context can influence its decision even when it should not determine it.

---


### 312. [KernelZero: Co-Evolving Proposer and Coder for Continuously Improved GPU Kernel Generation](https://arxiv.org/abs/2609.33074)

**<font color=#1a73e8>作者：</font>** Changxin Ke, Rui Zhang, Zixiang Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-performance GPU kernels are essential to modern machine learning systems, yet automatically generating kernels that are both correct and efficient remains challenging. Existing LLM-based approaches face two major limitations: the scarcity of high-quality training data aligned with the model's current capabilities, and the inherent trade-off between kernel correctness and performance. To address these challenges, we propose KernelZero, a co-evolution framework that continuously improves GPU kernel generation through two specialized models: a Proposer that generates Torch modules from API sets and a Coder that translates them into CUDA or Triton kernels. KernelZero uses a frontier-driven module generation mechanism to continuously produce capability-aligned training modules based on the Coder's current weaknesses. It further introduces Correctness-Aware Group Relative Policy Optimization (CA-GRPO), which optimizes performance only after correctness becomes sufficiently reliable. By alternating the optimization of the Proposer and Coder, KernelZero forms an automatic curriculum that enables targeted and training-efficient capability improvement. Empirically, KernelZero-7B surpasses Claude-4.5-Sonnet on CUDA and DeepSeek-V4-Pro on Triton. On KernelBench Level 1 and 2, it achieves CUDA pass@1 scores of 75.8% and 69.6%, respectively, with pass@10 reaching 100% and 97%. On Triton, it achieves pass@1 scores of 77.2% and 72.5%, respectively.

---


### 313. [SemReward-VL: Semantic Reward-Guided Video-Language Adaptation for Developmental Behavior Assessment](https://arxiv.org/abs/2609.33082)

**<font color=#1a73e8>作者：</font>** De Jiang, Shuo Zhang, Kehong Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developmental screening videos show how children perform specific behaviors, but clinical records usually contain outcomes rather than descriptions of what happened. We present SemReward-VL, which learns to describe item-specific behavior from these outcomes. A vision-language model generates a description, and a frozen language model scores its agreement with the clinical outcome, relevance to the item, abstention on unrelated video-item pairs, and clarity. Group relative policy optimization (GRPO) updates LoRA adapters using this semantic reward. On 13,379 videos covering 41 items, the method improves aggregate accuracy and the number of items with recall above 0.5. Errors remain in temporal direction, duration, and age-specific interpretations of behavior.

---


### 314. [dKFD: Phase-Structured Evidence Allocation for Fixed-Budget Localized Event Understanding](https://arxiv.org/abs/2609.33083)

**<font color=#1a73e8>作者：</font>** Aditya Bagri, Ashutosh Kumar, Chaitanya Lakhchaura 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse video understanding often requires selecting a small set of visual evidence under a fixed frame budget. Most sparse selectors allocate this budget globally, allowing all frames to compete with one another. For temporally localized events, this can be a poor inductive bias: useful evidence is often distributed across pre-event context, the event itself, and post-event consequences. We study fixed-budget evidence allocation for localized event videos and show that globally competitive Top-$K$ selectors can preserve recognition and grounding while producing unstable event evidence. On DoTA Video Anomaly Recognition, Global Top-$K$ obtains competitive recognition and temporal grounding, but low selector-event alignment at $K=12$ (Frame AUC $51.5 \pm 10.8$). We propose dKFD, a phase-structured differentiable selector that reserves evidence capacity across pre-event, event, and post-event phases after full-sequence temporal encoding. Under matched-budget multi-seed evaluation, dKFD improves Frame AUC by $+30.97$ over a matched Global Top-$K$ selector at $K=12$ ($p<0.01$), while yielding modest but statistically significant recognition gains and comparable temporal grounding. Mechanism ablations show that phase supervision is load-bearing: removing it reduces Frame AUC to $41.1 \pm 12.0$ even when phase-partitioned budgets are retained. Downstream diagnostics on VRU-Accident show consistent gains over learned Global Top-$K$ across VLM families, while dense captioning reveals a boundary condition where uniform sampling remains competitive. These results support phase-structured allocation as a controlled fixed-budget approach for event-centric sparse evidence selection, not as a universal video summarization strategy.

---


### 315. [The Model Knows Another Way: Strategy Switching for Effective RLVR Exploration](https://arxiv.org/abs/2609.33085)

**<font color=#1a73e8>作者：</font>** Jin Cui, Xinyue Long, Boran Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is often limited by insufficient exploration: difficult problems can yield uniformly incorrect rollout groups and therefore little learning signal. We show that such failures need not reflect missing capability. Instead, finite sampling often concentrates on a problem-specific dominant reasoning strategy while leaving alternative strategies already supported by the model unexplored. Moreover, the accessibility of these strategies evolves during RL: some are internalized into autonomous behavior, while others become difficult to elicit before being absorbed. Motivated by these observations, we introduce Problem--Strategy Rollout Allocation (PSRA), which treats unguided and strategy-conditioned prompts as competing exploration arms and uses Bayesian sequential allocation to direct a fixed rollout budget toward arms most likely to yield informative, non-saturated groups. A preservation objective keeps useful strategy-conditioned routes accessible while successful guided behaviors are transferred to the unguided policy. Across Qwen2.5 models from 1.5B to 7B and two RL training corpora, PSRA consistently improves reasoning performance, reduces dead saturation, strengthens out-of-distribution transfer, and maintains larger gains under increased inference budgets.

---


### 316. [From Constitutions to Control: Interpretable Rewards for Aligning Language Models](https://arxiv.org/abs/2609.33086)

**<font color=#1a73e8>作者：</font>** Johann D. Gaebler, Calvin Isley, Max Lamparth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current approaches to aligning language models often make it hard to know what behavior is being rewarded or to change that reward in a targeted way. In particular, standard preference-based methods collapse multiple considerations into aggregate human judgments, obscuring what drives the resulting reward, while principle-based methods specify high-level values without fully operationalizing them. To address this gap, we develop a rubric-based framework to transform a general-purpose constitution into an interpretable and tunable reward model, using constitution-guided AI feedback to estimate initial weights for the constituent rubric items. We then reweight those dimensions to construct modified rewards for training. Across experiments on political alignment and safety-helpfulness tradeoffs, reweighting individual dimensions predictably changes targeted behaviors largely independently while navigating tradeoffs between conflicting alignment objectives. We show that the same framework can mitigate label bias encoded in preference judgments -- including sycophancy and demographic bias -- by reducing their influence on the training reward. Our results demonstrate that constitution-derived, interpretable rewards can translate high-level alignment principles into more transparent and controllable model behavior.

---


### 317. [OneSign: Unifying Sign Language Understanding Tasks with One Model](https://arxiv.org/abs/2609.33090)

**<font color=#1a73e8>作者：</font>** Shiwei Gan, Yafeng Yin, Xiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SLU encompasses a diverse set of tasks, including ISLR, CSLR, and SLT. Although these tasks share basic semantic and linguistic foundations, they are typically addressed with task-specific architectures and training pipelines, which hinders knowledge sharing and requires costly pretraining and finetuning for each task. In this paper, we focus on two aspects of SLU tasks: (1) training and inference pipelines are highly fragmented: most methods rely on pretraining on large-scale SL datasets followed by task- or dataset-specific finetuning, which leads to multiple specialized models rather than a single checkpoint. (2) current LLM-based methods may overlook the inherent modality discrepancy between sign and text tokens, simply concatenating them and processing both modalities with the same decoder layers. In this paper, we present OneSign, a unified framework that addresses multiple SLU tasks within a single model and a single checkpoint. OneSign reformulates ISLR, CSLR, and SLT under a single training paradigm. To accommodate the heterogeneous characteristics of sign and text representations, we introduce a Modality-Adaptive Mixture-of-Experts (MA-MoE) architecture, consisting of a shared expert and modality-specific experts for sign and text tokens. A modality router dynamically activates the corresponding experts, and their outputs are aggregated to form the final token representations. By enabling modality-dependent expert specialization while preserving a shared expert path, MA-MoE can effectively model the modality differences between continuous sign representations and discrete text tokens. Extensive experiments on multiple benchmarks demonstrate that OneSign achieves competitive or state-of-the-art performance on several benchmarks, highlighting its effectiveness as a unified SLU model. Datasets are available at : this https URL.

---


### 318. [ORBIT: A Framework for Multi-Agent Safety and Security Evaluations](https://arxiv.org/abs/2609.33102)

**<font color=#1a73e8>作者：</font>** Ben Hagag, William L. Anderson, Srija Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are increasingly deployed for complex, long-horizon tasks or emerge as a natural consequence of agents interacting in the wild. Yet they give rise to significant safety and security risks: the flexible protocols that enable task generalization also expose novel threats, from cascading prompt injection to inter-agent collusion. Progress in defending against these threats has been slowed by a lack of shared empirical infrastructure, which forces bespoke environment development for every new defense and makes standardized comparison impossible. Existing evaluations address isolated threat models or single-agent settings, but none jointly vary attack, defense, and architecture across realistic multi-agent environments. To address this gap, we introduce ORBIT, a configurable evaluation framework for empirical multi-agent safety and security research, built on UK AISI's Inspect. ORBIT lets researchers configure communication topologies, memory, scheduling, and agent roles. It supports four threat types and four defense strategies, as well as non-adversarial failures, with a benchmark suite spanning five scenario families covering browser use, computer use, agentic coding, customer service, and cooperative allocation. Our central finding is a gap in defense transferability across threats: per-action defenses that cut a compromised agent's attack success by 60 points on multi-issue coding give no measurable protection against colluding agents, and none of the defenses we tested generalized over all attacks tested. We further demonstrate security-performance tradeoffs and interactions between architecture and defense effectiveness. We make ORBIT available open-source at this https URL.

---


### 319. [Toward Comprehensive 3D Grounding: Orientation Grounding through Vision-Language Models](https://arxiv.org/abs/2609.33109)

**<font color=#1a73e8>作者：</font>** Tuo Liang, Disheng Liu, Nengbo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding is a core capability of spatial vision-language models, yet most existing work focuses only on where a referred object is. Many 3D tasks also require knowing how it is oriented. Although existing 3D VLMs may predict oriented boxes, box pose does not explicitly capture object-centric orientation or symmetry-induced ambiguities. We introduce orientation grounding, a referring grounding task that predicts an object's 6D orientation and axial symmetry from a language or box query in single-view or multi-view scenes. To support this task, we construct ReferOri, with 331K multi-view and 387K single-view orientation-grounding queries obtained through scalable reconstruction, consistency checking, and human verification. We further present OG-VLM, which adapts a 3D VLM with structured box/orientation outputs, sign and symmetry tokens, and geometry-aware auxiliary losses. Across single-view and multi-view benchmarks, OG-VLM substantially outperforms orientation-aware VLM baselines and surpasses object-level orientation foundation models on scene-level referring benchmarks, showing that explicit orientation grounding is a distinct and learnable capability beyond localization. Downstream results validate its benefit for orientation-related spatial reasoning.

---


### 320. [Modular Discovery of General Game-Playing Algorithms with Large Language Models](https://arxiv.org/abs/2609.33115)

**<font color=#1a73e8>作者：</font>** Zun Li, John Schultz, Marc Lanctot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General Game Playing across arbitrary games from rules alone remains challenging due to differing algorithmic requirements across game classes and strict decision-time constraints. Rather than hand-designing search heuristics for specific domains, can we leverage Large Language Models (LLMs) to discover general game-playing algorithms? Because language models can propose and refactor structured code, they provide an expressive proposal engine for exploring the space of algorithmic designs. We introduce a multi-agent LLM meta-learning system to co-evolve game-agnostic procedural search mechanisms in C++ alongside domain heuristics synthesized directly from game rules. Controlling the compute budget, we benchmark the discovered mechanisms across more than 400 diverse environments, including OpenSpiel training and held-out games, procedural simulation engines, and games with deep neural policy-value representations trained via PPO. Evaluated via AlphaRank stationary distributions and Soft Condorcet Optimization (SCO) against 15 established MCTS baselines, the discovered search mechanisms consistently achieve top-tier ratings and pairwise ballot majorities over most baselines across independent evolutionary runs, generalizing to unseen human-designed and procedurally synthesized games and remaining competitive with baselines on frozen neural network representations.

---


### 321. [ECG-Scroll: A Long-Horizon, Streaming Benchmark and Agent Environment for Interpretation of Ambulatory Electrocardiograms](https://arxiv.org/abs/2609.33117)

**<font color=#1a73e8>作者：</font>** Haitao Li, Chenglin Li, Zhengyao Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can now interpret a standard ten-second, twelve-lead electrocardiogram (ECG) with clinically grounded, reward-verified reasoning. Real cardiac monitoring is different. Ambulatory (Holter) and telemetry recordings span hours to days and are read as they stream in, and their clinically decisive findings are paroxysmal, brief episodes buried in an otherwise unremarkable trace. Such a recording cannot be held in one context at diagnostic resolution, and its future has not yet happened, so a reader must work online, deciding what to measure now, committing evidence to memory as it passes, and reporting events as they occur. We recast long-duration ECG interpretation as a long-horizon, online (streaming, causal) sequential decision process and introduce ECG-Scroll. As a benchmark, long ambulatory recordings are streamed to an agent chunk by chunk, and it must localize, quantify, and promptly flag paroxysmal events without access to future signal; because the underlying signal is retained, every answer is checkable against objective ground truth, giving rule-based rather than judge-based rewards, and the streaming formulation adds a metric batch evaluation cannot express, the detection latency between an event's onset and the moment the agent records it. As an agent environment, it is a fixed, gym-style interaction layer that exercises three competencies single-glance ECG models never touch: Memory, Tool use through signal-grounded measurement rather than reading pixels, and Planning of what to measure now and when to commit. We release 390 whole-recording instances spanning 2,536 hours of two-lead ambulatory ECG and evaluate a signal-threshold rule agent alongside off-the-shelf LLM agents online, characterizing how they use memory, tools, and planning and where the benchmark's head-room lies.

---


### 322. [MedRouter: Demystifying Knowledge Differences Across Medical LLMs for Routing-Based Reasoning](https://arxiv.org/abs/2609.33119)

**<font color=#1a73e8>作者：</font>** Lang Cao, Binghang Lu, Yuhao Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical question answering spans diverse specialties and modalities, and individual medical large language models (LLMs) exhibit distinct strengths across tasks and domains. This heterogeneity suggests that combining specialists may enable broader coverage of medical questions than relying on any single model. However, existing LLM routing methods primarily seek to balance answer quality and inference cost, leaving open how to exploit differences in specialist competence to improve medical reasoning. In this paper, we introduce MedRouter, an agentic system that uses an embedding-based multi-label router to select and query specialist LLMs, then passes their responses to a generator to produce the final answer. We further propose SCALE (Specialist Competence-Aware Learning), a two-stage training framework that first trains the Router with specialist correctness supervision and then optimizes its selections through reinforcement learning. The second stage uses a Performance Gain Reward (PGR) that measures how specialist information affects the generator's answer correctness relative to answering without that information. Experiments on eight text-based and multimodal medical QA benchmarks show that MedRouter outperforms the strongest routing baseline by 8% in average accuracy. Our analysis of specialist outputs further reveals distinct strengths and complementary question-level coverage, motivating learned routing to combine these capabilities for more comprehensive medical reasoning.

---


### 323. [Classifying Dominant Temporal Orientation without Pretrained Text Embeddings: A Novel Morphosyntactic Inventory Vector Approach](https://arxiv.org/abs/2609.33121)

**<font color=#1a73e8>作者：</font>** Jonathan Cleveland, Peter S. Bearman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational methods have consistently struggled to determine the dominant temporal orientation of a sentence. This difficulty is especially pronounced when a sentence contains multiple embedded clauses with competing tense and aspectual information. To address this difficulty, we propose an alternative approach for identifying a sentence's past, present, or future global reference interval. Our method does not use any form of pretrained embeddings. We rather encode sentences using fixed-length inventory vectors that are comprised of part-of-speech counts, dependency relation counts, and explicit futurate pattern counts. We term this inventory vector of a sentence a "Morphosyntacton". The method does not use any padding, sequence models, or large language models. Evaluation on 1,799 syntactically complex English sentences, annotated as past, present or future, shows balanced and high accuracy multiclass classification, achieving an overall multi-class accuracy of 92%.

---


### 324. [Compositional Safety Failures in Harness Evolution: Identification and Runtime Monitoring](https://arxiv.org/abs/2609.33123)

**<font color=#1a73e8>作者：</font>** Zhixiang Zhang, Zesen Liu, Wai Ip Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agent harnesses continually update persistent components such as memory, prompts, skills, and tools. We call this process harness evolution. However, such evolution could introduce unexpected safety risks. Existing work studies harness misevolution and validates candidate harnesses or attributed individual component updates, leaving safety analysis of cross-component update interactions largely unexamined. To address this gap, we study compositional safety failures in harness evolution, where interactions among individually safe and utility-preserving component updates can produce undesirable or unsafe agent behavior, revealing a safety risk intrinsic to harness evolution. Across three safety-related benchmarks, we identify 43 pairwise and 18 irreducible 3-way compositional safety failures. Conventional solution incurs combinatorial complexity in validating cross-component interactions, leaving the safety checking impractical as the harness evolves. To solve this, we introduced a typed hypergraph that represents component states as nodes and safety-relevant higher-order interactions as hyperedges. When the harness changes, the hypergraph updates only the interaction neighborhood of the changed states rather than reconstructing the global composition space. Building on that, we develop a hypergraph-guided runtime monitoring mechanism. Experiments show that our method effectively mitigates compositional safety risks while preserving task utility and reducing interaction-checking costs, and further reveal an empirical safety-utility-cost trade-off across different safety mechanisms.

---


### 325. [Train Together or Merge Later? Unifying VLA Experts via a Shared Action Interface](https://arxiv.org/abs/2609.33125)

**<font color=#1a73e8>作者：</font>** Zhizhen Zhang, Yuxia Fu, Zijian Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-training offers a straightforward way to build a multi-task vision-language-action (VLA) policy, but can fall short of the performance achieved by training each task independently. The challenge is to retain these task-specific gains in a multi-task policy without joint post-training. Combining independently trained experts through model merging is a natural approach, yet strong individual experts do not necessarily yield a strong merged policy. We identify one source of this incompatibility: task-specific changes to the action interface, comprising action normalization and the action encoder and decoder. We propose PolicyWeave, combining merge-compatible post-training with context-guided sparse merging. During post-training, all experts retain the common base policy's action interface, while task adaptation is restricted to LoRA updates in the hidden layers of the action model. This makes the experts more compatible with existing model merging methods. However, merging all experts can still introduce interference from unrelated tasks at deployment. PolicyWeave scores each expert's LoRA updates using the initial visual-language context, determines the expert set through leave-one-layer-out ranking stability, and forms a sparse weighted merge of the selected updates that remains fixed for current task. We evaluate PolicyWeave with GR00T N1.5 on 18 RoboCasa365 tasks, using only 10% of the target-task demonstrations for supervised fine-tuning (SFT). Preserving the shared action interface raises the average success rate across four static merging methods from 17.0% to 52.8%. PolicyWeave achieves 64.7% success with these SFT experts and 74.1% after task-specific reinforcement learning (RL), compared with 60.7% for joint RL. Further evaluations on LIBERO-10 and an AgileX Piper arm support the deployment of independently learned skills in long-horizon and real-world manipulation.

---


### 326. [Save Your Saturated Data: Learning Beyond Reward Saturation in Group-Based RL](https://arxiv.org/abs/2609.33126)

**<font color=#1a73e8>作者：</font>** Ziyuan Yang, Yike Wang, Shangbin Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-relative reinforcement learning (RL) relies on reward variation among sampled responses to estimate informative relative advantages. As language models become increasingly capable, existing training data can become reward-saturated: all sampled responses to the same problem might receive equally high rewards, where the group-relative learning signals vanish and leave previously useful data obsolete. In this work, we investigate whether useful learning signals can be recovered from such saturated data. We study interventions at four levels of group-policy RL pipelines---data, rollout, reward, and advantage---and conduct extensive RL training on saturated reasoning data only. While standard GRPO on saturated data would almost always yield near-0 advantages and near-noise signals, diverse interventions successfully recycle and repurpose such data: among the proposed strategies, interventions at rollout generation are consistently most effective: nudging the policy to generate ``high-quality'', incorrect solutions introduces rollouts with poor rewards into saturated groups as negative samples, which turns out to improve GRPO by 6.4% to 9.0% across Qwen3-1.7B and 4B. Other interventions such as increasing rollout temperature or adding auxiliary rewards can also restore non-zero advantages, but yield less consistent gains. Further analyses show that effective negative rollouts require informative negative trajectories, that the method remains effective alongside unsaturated data, and that it supports iterative recycling of newly saturated examples. While increasingly stronger LLMs would render more data as saturated, our results demonstrate that don't waste your saturated data: with the right strategies they can be recycled into useful RL training signals in an increasingly data-scarce world.

---


### 327. [Ceiling of a Task: When Can a Transformer Succeed Without Its Chain of Thought?](https://arxiv.org/abs/2609.33134)

**<font color=#1a73e8>作者：</font>** Jiashu He, Jinxuan Fan, Xiao Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models generate long chains of thought before they answer, yet it is debated whether the content of these chains does real computational work or is largely decorative. We study this question by viewing a transformer as a shallow circuit. One forward pass through a fixed number of layers has constant depth, so any procedure that runs the model a constant number of times is a shallow circuit. We call the best accuracy that a shallow circuit can reach on a task the ceiling of the task, and a task is serial if its ceiling lies below one. We prove three results on serial tasks that hold for every transformer, no matter how it was trained. Necessity: replacing the chain by anything that does not depend on its content, such as filler tokens or a restatement of the question, drives the accuracy down to the ceiling, and on a maximally serial task down to chance. Depth: no shallow computation can write the chain of a model whose accuracy exceeds the ceiling, not even approximately. Locality: the answer is one shallow pass away from the finished chain, so all of the serial reasoning happens in the chain. On word problems of finite groups, whose ceilings are known, small transformers trained from scratch, with or without reinforcement learning, attain the predicted numbers: chain-trained models solve every input length and fall to chance when the chain is erased, chainless models collapse to the ceiling as the input length grows, and open-weight reasoning models given the same problem in words return to the baseline without their chain. On MATH-500 and AIME, erasing the chain costs open reasoning models 0.52 to 0.82 accuracy, a sentence shuffle is harmless, and a token shuffle is as harmful as erasing; the same holds for checkpoints trained by GRPO with a correct or a random reward. The ceiling of a task therefore answers when a transformer can succeed without its chain of thought.

---


### 328. [On Device Agentic Operation Caches -- Classifier-Centric NL-to-Action Generation](https://arxiv.org/abs/2609.33141)

**<font color=#1a73e8>作者：</font>** Moghis Fereidouni, Anthony Arnold, Sumit Gulwani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is increasingly being embedded in software applications to provide natural language interfaces to features and functionality. In most cases these agents are powered by enterprise (100+ billion parameter) or frontier class large language models that require substantial computational resources run and depend on cloud hosted inference to handle the task of transforming natural language inputs into actionable software operations. This reliance on cloud-hosted inference introduces substantial network latency on top of LLM inference times, creates data privacy concerns, and, given the costs of running these models, can rapidly escalate expenses associated with supporting agentic features.
This paper introduces a novel means of converting the NL-to-Action problem from a generative one into a classification-centric formulation via on-device operation caches. These caches allow an agentic system to handle frequently occurring classes of actions completely on-device -- reducing latency, enhancing privacy, and lowering operational costs. We show that for a classic NL-to-Formula task, generating Excel Formula in response to user requests, this approach reduces total inference cost by 56% when compared to cloud-only model-routing based inference and, on cache hits, reduces the latency to response latency by 5x.

---


### 329. [Knowing Is Not Choosing: What Explicit Verification Adds Beyond Generative Preference](https://arxiv.org/abs/2609.33142)

**<font color=#1a73e8>作者：</font>** Yilong Li, Chengpo Yan, Aayan Arish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating a correct answer does not mean that a language model will select it. We separate factual recall into three steps: generating a correct candidate, ranking the available candidates, and selecting the final answer. Pre-generation readouts predict factual recall and which questions sampling will cover across three model families, but say little about whether an available correct answer will ultimately be selected. Explicit verification with $P(\mathrm{True})$ improves within-question ranking over mean log-likelihood in Gemma, Qwen3, and Llama, with AUROC gains of $0.08$--$0.12$. In a prospectively defined Gemma cohort, verification raises plurality accuracy by about $5$ points, and still gains about $2$ points over chat-template likelihood, a stronger generative baseline. The advantage is strongest for relations with common-answer priors and depends on access to the entity; masking the entity removes the ranking advantage in larger Qwen models. Finally, the measured benefit depends on how correctness is defined: recall-oriented reference matching can credit option lists favored by likelihood and substantially understate the improvement seen under human semantic judgments.

---


### 330. [CAME: Company-Aware Evidence-Memory Experts for Interpretable Quarter-Ahead Revenue Forecasting](https://arxiv.org/abs/2609.33143)

**<font color=#1a73e8>作者：</font>** Ya-Wen Wu, Meng-Fen Chiang, Kuang-Da Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quarter-ahead revenue forecasting requires company-scale numerical accuracy, strict temporal validity, and company-specific interpretation of narrative disclosures. LLMs can distill textual evidence but can produce scale-misaligned forecasts, whereas history-based anchors are stable but miss forecast-time signals such as product transitions, supply constraints, and management guidance. We introduce CAME (Company-Aware Evidence-Memory Experts), a residual-forecasting framework that refines a no-leakage statistical anchor when current semantic evidence and prior error patterns justify an adjustment. On a development-inclusive rolling backtest of 336 company-quarters from 12 large public technology and platform firms, CAME achieves the lowest aggregate point-estimate error among the reported methods, with statistically supported macro-sMAPE gains over the matched Statistical Anchor, and outperforms History + Guidance on all six aggregate metrics. CAME also links adjustments to source-linked evidence cards and guarded memory traces, supporting forecast inspection, provenance, and failure localization.

---


### 331. [LiteEvo: Automated, Cost-Efficient Harness Evolution for Generalization to Unseen Tasks](https://arxiv.org/abs/2609.33146)

**<font color=#1a73e8>作者：</font>** Euntae Choi, Sumin Song, Sungjoo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM agent is defined by two things: the weights inside its model and the harness of components assembled around it. Harnesses are still handcrafted, and HarnessX, which evolves them automatically, starts each benchmark from a handcrafted harness, reports gains on the tasks it evolved on, and budgets 100 to 175 million meta-agent tokens per benchmark. We propose LiteEvo, a lightweight harness-evolution algorithm whose tool-free meta-agents mine agent trajectories for reusable components, curate them into a versioned library, and compose each round's harness from it, starting every benchmark from the same neutral harness and never naming the benchmark. Evolving on the graded tasks of five agentic benchmarks with a frozen Qwen3.5-9B, LiteEvo lifts pass@2 by 10.5 to 67.7pp and reaches comparable or higher pass@2 than a reproduction of HarnessX (71.0 against 67.3 on average) at 13.0 lower mean API cost. Harnesses evolved on train tasks keep their gains on unseen test tasks of four benchmarks, and LiteEvo also lifts Claude Code with Sonnet 4.6 by 1.2 to 71.4pp.

---


### 332. [CFLoRA: Federated Fine-tuning of LLMs with Complementary Factors for Error-free Aggregation](https://arxiv.org/abs/2609.33147)

**<font color=#1a73e8>作者：</font>** Yanan Ma, Qiyuan Chen, Zihan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated low-rank adaptation (LoRA) enables collaborative fine-tuning of large language models without centralizing private client data. Its factorized update, however, creates a structural mismatch in federated averaging: averaging the two LoRA factors separately does not equal averaging their products. Existing exact methods resolve this issue mainly by freezing an entire factor or alternating factors across rounds, but none can update factors simultaneously without aggregation errors or expanding communication ranks. To address this fundamental problem, we present \texttt{CFLoRA}, a federated LoRA scheme that partitions latent LoRA channels into two complementary sets in every communication round. By ensuring that columns and rows are complementary across factors, we eliminate bilinear terms in matrix multiplications, making federated aggregation exact. Crucially, our framework also supports clients with heterogeneous rank budgets. Convergence analysis validates \texttt{CFLoRA} achieves $\mathcal{O}(1/\sqrt{T})$ convergence rate of the \textit{original} LoRA objective in homogeneous-rank cases. Extensive experiments with RoBERTa on the GLUE benchmark and with LLaMA-3.2-3B-Instruct on commonsense reasoning tasks demonstrate that \texttt{CFLoRA} achieves superior performance and training efficiency compared to state-of-the-art federated LoRA baselines.

---


### 333. [Not Too Hard, Not Too Easy: Learning from Intermediate States for LLM Structured Reasoning](https://arxiv.org/abs/2609.33149)

**<font color=#1a73e8>作者：</font>** Hongbo Chen, Guohua Lu, Ting Dang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common principle of effective learning is to practice material that is neither already mastered nor too difficult to permit progress. We ask how to apply this principle to structured reasoning tasks such as Sudoku and maze solving. In these tasks, a model can repeatedly revise an incomplete or incorrect candidate solution until it satisfies the problem's constraints. The intermediate candidate solutions along this trajectory provide natural training examples: some are already solved, some cannot yet be repaired by the model, and others lie at its current frontier of achievable progress. We therefore investigate whether pretrained language models can learn to revise such states and whether training on states at this frontier improves reasoning more broadly. To achieve this, we couple a pretrained language-model backbone with a recurrent updater that repeatedly revises an explicit solution state, using the same parameters at every update step. We further introduce Frontier-Oriented Curation Using Self-trajectories (FOCUS), which selects training states from trajectories generated by the current model. FOCUS measures how much the model improves each state within a fixed number of recurrent updates and prioritizes states from which it can make substantial progress. With Qwen3-1.7B, FOCUS achieves 64.4% exact solve accuracy on Sudoku-Extreme and 91.1% on Maze-Hard, with similar gains observed across five Qwen and Llama backbones spanning 1.7B to 8B parameters. We further observe zero-shot transfer in the adapted LLM to mathematical reasoning and code execution, even when the recurrent updater is disabled and no downstream fine-tuning is performed.

---


### 334. [Where Do Test-Time Scaling and Training Fall Short in Individual Stance Prediction?](https://arxiv.org/abs/2609.33155)

**<font color=#1a73e8>作者：</font>** Yuyang Zhao, Xuan Liu, HaoYang Shangm Haojian Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling and post-training have improved LLM performance in coding and mathematical reasoning, but their effectiveness for individual stance prediction remains unclear. We study this question by predicting a person's stance in a new discussion from their history. We evaluate widely used test-time scaling strategies and post-training methods, such as supervised fine-tuning and reinforcement learning, and identify four failure modes across generation, selection, and learning: (1) incorrect consensus, where repeated samples agree on the wrong stance; (2) selection failure, where generation covers the observed stance but selection misses it; (3) response overfitting, where supervised fine-tuning improves imitation but harms prediction; and (4) early plateau, where reinforcement learning shows modest initial gains followed by limited further improvement. We expose these failures using STANCE-BENCH, which contains 2499 prediction tasks from 500 Hacker News users. Guided by this analysis, we explore a simple approach that combines direct scores for all candidate stances with explicit assessments of support from the individual's history. On the 781-task test set, this approach achieves 21.83 discussion-specific Macro F1 with Qwen3-8B, compared with 19.27 for direct scoring. Our results motivate evaluating candidate generation, final selection, and person-specific evidence use separately.

---


### 335. [FOCUS: Benchmarking Retinal Model Generalization from Foundation Vision Encoders to Multimodal LLMs](https://arxiv.org/abs/2609.33158)

**<font color=#1a73e8>作者：</font>** David Restrepo, Chenwei Wu, Luis Filipe Nakayama 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in AI-based retinal image analysis has advanced with foundation models, yet evaluating their reliability remains challenging. Performance reported on a single dataset does not capture how models behave under dataset shift, across clinical definitions, or for different patient subgroups. This limitation is particularly critical in medical imaging analysis, where robustness, calibration, and fairness are essential for safe deployment. We introduce FOCUS (Foundation Ophthalmic Cross-Dataset Understanding under Shift), a cross-dataset benchmark for evaluating retinal fundus models that considers vision-only encoder models (VM), vision-language dual-encoder models (VLM), and multimodal large language models (MLLM). FOCUS harmonizes binary diabetic retinopathy, referable diabetic retinopathy, and glaucomatous optic neuropathy tasks across ten public datasets spanning diverse geographies, acquisition conditions, and label protocols. The benchmark evaluates models through a unified analysis layer that measures ranking performance, calibration, subgroup disparities, and image-quality robustness. We present a large-scale evaluation covering 532 base configurations and 228 MLLM configurations adapted through supervised fine-tuning with low-rank adaptation (LoRA). Results show that no model family consistently dominates across tasks and datasets: general VM encoders achieve the strongest average ranking performance, medical MLLMs are competitive but variable, and dual encoder VLMs benefit substantially from lightweight adaptation. Fine-tuning improves in-domain performance but exhibits heterogeneous transfer to external datasets, particularly in calibration. These findings demonstrate that retinal model evaluation is inherently multidimensional. FOCUS provides a practical framework and public benchmark to assess generalization, reliability, and robustness beyond single-dataset leaderboards

---


### 336. [Downstream-Aware Context Selection for Online In-Context Reinforcement Learning](https://arxiv.org/abs/2609.33166)

**<font color=#1a73e8>作者：</font>** Ruihan A. Li, Shangtong Zhang, Rohan Chandra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context reinforcement learning (ICRL) enables large language model agents to adapt to new environments using their interaction history without updating model parameters. However, repeatedly conditioning on growing histories can lead to substantial token cost. We propose a bounded-history context-management framework that predicts the task-dependent downstream effect of removing historical interactions to guide history selection and determine a decision-dependent context budget. Formally, our framework uses the full rolling history as a reference. The predictor evaluates removal effects, defines a deletion ordering, and applies a shared selection criterion to determine how much history to retain at each decision. We evaluate the method in closed-loop SUMO driving under held-out in-distribution, unseen-domain, and unseen-route settings, and in ScienceWorld under a continual ICRL protocol. Relative to a baseline using the full context, our method reduces total token usage by 25.7%, 25.8%, and 23.2% across the three driving settings while maintaining comparable closed-loop driving performance. In ScienceWorld, it reduces total token usage by 52.1% compared to full context and uses 30.2% and 37.8% fewer tokens than the Recent and Similarity baselines, respectively, while maintaining performance.

---


### 337. [Scoring the Wrong Question: Readout Failures in Constrained-Option Evaluation](https://arxiv.org/abs/2609.33179)

**<font color=#1a73e8>作者：</font>** Jiaxuan Guo, Kejia Zhang, Shuo Xin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constrained-option scoring reads a model's probabilities for a fixed set of permitted answers, so it returns a score even when the model is about to write something else. We study a prompt that quotes a multiple-choice item, ending in the item's own answer instruction, and asks for a forecast of whether a reader model given only a short note will answer it correctly. The model can begin answering the quoted item: on three Qwen3 checkpoints an answer letter is the most probable token on nearly every passage, and the forecast ranks the reader's correctness indistinguishably from chance. Beyond prior work's argmax check and prefill repair, we contribute a label-free diagnostic of the declared options' support, their first-token mass in context; a deletion test tracing the Qwen3 answer-letter start to the quoted instruction; and rendering and tokenisation checks for dropped separators and coinciding first tokens. Prefilling an answer stem lifts the median option mass from below to above one half on all nine checkpoints scored with this prompt and, with options and renormalisation unchanged, raises the Qwen3-averaged AUC from 0.4929 to 0.6152. lm-polygraph's default P(True) estimator shows a related failure: it reads True where Qwen3 without thinking favours an answer letter (MMLU) or the prompt's (A)/(B) label (TriviaQA), and its Qwen3-averaged AUROC is indistinguishable from chance on MMLU and below chance on TriviaQA. Scoring and renormalising the (A)/(B) labels after an answer stem raises it to 0.632 and 0.868, renormalising True against False in place reaches 0.660 and 0.860, and on TriviaQA both exceed all fourteen default single-answer library estimators. The original forecast is renormalised too, yet stays indistinguishable from chance: option mass flags low support in both settings without labels, and only checking the intended target shows which score still ranks.

---


### 338. [SeOPD: Self-Evolving LLMs via Online Policy Distillation from Self-Generated Chain-of-Thought](https://arxiv.org/abs/2609.33181)

**<font color=#1a73e8>作者：</font>** Xiaoshu Chen, Xiangyu Wong, Sihang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in online policy self-distillation (OPSD) have demonstrated that large language models (LLMs) can improve their capabilities by leveraging external privileged information (PI), such as manual annotations or feedback from external environments. However, obtaining accurate annotations and constructing sophisticated environments often require substantial human effort and computation, limiting the scalability of OPSD. While a few recent studies have explored self-improvement without external PI, the resulting gains remain limited. In this work, we explore whether LLMs can achieve comparable self-improvement without external PI. Our key observation is that a single LLM can support multiple reasoning modes, such as deep-thinking and non-thinking modes, with deep thinking generating additional information during reasoning. Based on this observation, we propose Self-Evolving Online Policy Distillation (SeOPD), which enables LLMs to distill and internalize information generated by their own chain of thought (CoT). Specifically, it (1) generates CoT with the deep-thinking mode, (2) produces responses with the non-thinking mode, and (3) uses the generated CoT as PI to provide token-level supervision for the non-thinking response, allowing new information inferred during reasoning to guide the non-thinking mode and be internalized into the shared model parameters, thereby improving both non-thinking and deep-thinking capabilities. Extensive experiments across LLMs and tasks demonstrate the effectiveness of SeOPD.

---


### 339. [Unlocking Latent Personalization in LLMs](https://arxiv.org/abs/2609.33182)

**<font color=#1a73e8>作者：</font>** Wei Chen, Guanghui Zhu, Zhongliang Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly expected to adapt to individual users, yet effective personalization remains challenging when only limited user-specific samples are available. In this work, we take an alternative perspective: pretrained LLMs may already possess latent capacity for personalization, and a few user samples may therefore suffice to guide the model toward user-aligned behavior with minimal user-specific adaptation. From this perspective, we propose LatentPersonal, a framework that formulates personalization as navigation in a shared latent adaptation space. LatentPersonal infers a compact latent representation from a few user samples to guide user-specific model adaptation, regularized with a variational information bottleneck to encourage compact preference representations. We instantiate LatentPersonal with LoRA, leveraging its low-rank parameterization as a natural low-dimensional adaptation space for personalization. By simply inserting a user-specific guidance vector between the shared low-rank factors, the model can navigate toward personalized adaptations through lightweight inference of this compact representation, without updating the shared LoRA parameters. Experiments across multiple personalization datasets demonstrate that LatentPersonal substantially reduces user-specific adaptation overhead while achieving effective personalization from only a few user-specific interactions, with particularly strong performance in the one-shot regime.

---


### 340. [Identifying Temporal Features within Transcoders for Time Sensitive Factual Recall](https://arxiv.org/abs/2609.33183)

**<font color=#1a73e8>作者：</font>** Sanjay Govindan, Yang Song, Maurice Pagnucco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) suffer from temporal misalignment, often due to the contradictory nature of their training corpora. While current mitigation strategies rely on computationally expensive fine-tuning or context-heavy retrieval augmented generation (RAG), the internal mechanisms governing time-sensitive recall remain under-explored. Unlike prior studies that identify temporal components such as attention heads and MLP layers, we provide the first feature-level map of temporal recall by isolating individual MLP features via transcoder circuit tracing. We identify three node categories (common temporal, common to the year, and chrono-semantic) which interact to generate a temporal filter during factual recall. By analysing Gemma 2 2B, LLaMA 3.2 1B, and Qwen3-4B, we show that these features do not follow a simple linear pipeline but represent time through a parallel and mixed syntactic-semantic interplay across layers. We additionally discover a class of higher-layer temporal components invisible to existing EAP-IG methods, establishing transcoders as a more complete lens for temporal interpretability in time-sensitive factual recall. These findings present MLP components for potential targeted interventions in time-sensitive factual recall

---


### 341. [AG-CoT: Verified Algorithmic Traces for LLM Program Synthesis on Clifford Circuits](https://arxiv.org/abs/2609.33192)

**<font color=#1a73e8>作者：</font>** Lu Wei, Yufeng Wang, Chenfeng Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific code generation can produce executable programs that fail to compute the intended scientific object. We study this problem in language-model synthesis of Clifford circuits, which prepare the stabilizer states used in quantum error correction and admit exact classical verification. In our target-conditioned framework, each target is given as compact signed stabilizer generators, and an exact verifier checks the generated OpenQASM circuits. We supervise models with Aaronson-Gottesman chain-of-thought (AG-CoT) traces checked by the verifier, and continue training on model generations that the verifier accepts. Across two independently trained model families (3B and 7B), AG-CoT supervision multiplies greedy-decode state-equivalence accuracy by four to six times over circuit-only baselines, and verifier-filtered continuation training adds a further consistent gain atop both. A complementary 32B study shows that supervised models achieve near-perfect syntax and Clifford validity while the strongest direct model reaches 6.14% state equivalence per target, rising to over 10% under verifier-guided selection with multiple candidates. These results show that algorithmic trace supervision gives a large, statistically significant gain in both model families and that verifier-filtered continuation adds a further repeated gain. The persistent gap between Clifford validity and state equivalence confirms that exact verification is necessary: a circuit can be syntactically and physically valid yet prepare the wrong quantum state.

---


### 342. [Orthogonal Witness Control for Muon Optimization via Sigmoid Spectral Reshaping](https://arxiv.org/abs/2609.33194)

**<font color=#1a73e8>作者：</font>** Dat Phi Van, Ngo Vu Minh, Tuc Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-valued optimizers such as Muon exploit the spectral structure of neural network updates through Newton--Schulz orthogonalization, but their near-flattening of the singular spectrum discards relative magnitude information across gradient modes. We introduce \emph{Soren} (\textbf{S}pectral \textbf{O}rthogonal \textbf{Re}shapi\textbf{n}g), a matrix-valued optimizer that preserves the singular subspaces of the gradient while applying a bounded, monotone sigmoid transformation to its singular values. This smoothly compresses dominant modes without fully flattening the spectrum. We interpret Soren as a positive-definite preconditioned gradient method and establish convergence guarantees under relative smoothness and metric Polyak--Łojasiewicz geometry. To avoid explicit singular value decomposition, we further develop a finite-depth Soft Newton--Schulz (SNS) polynomial realization of the sigmoid spectral map and characterize how its spectral approximation affects the induced convergence geometry. Experiments across LLM pre-training, supervised fine-tuning, and direct preference optimization demonstrate the effectiveness and robustness of Soren against established optimizers.

---


### 343. [Are Benchmarks Reliable? Toward Structural Diagnosis via Sample-Level Capability Boundaries](https://arxiv.org/abs/2609.33196)

**<font color=#1a73e8>作者：</font>** Haiquan Hu, Yuzhu Liang, Weicheng Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) relies heavily on benchmark scores, yet aggregate metrics can obscure whether benchmark samples reliably support model comparison. We introduce \textbf{BSDProbe}, a sample-level framework for \emph{benchmark structural diagnosis} that estimates capability boundaries from repeated-response trajectories along ordered model axes. BSDProbe summarizes samples by boundary position, boundary width, boundary-signal validity, and order consistency, then aggregates them into benchmark-level structural profiles. Experiments on six benchmarks show that benchmark reliability is axis-conditioned and heterogeneous: GSM8K and MATH exhibit the most stable measurement structures, MMLU and TriviaQA are relatively stable but heterogeneous, while GPQA and PopQA show stronger axis-conditioned risks. These profiles remain consistent across Qwen3, Qwen2.5, and cross-model axes. BSDProbe further selects compact high-value subsets whose model discriminability reaches up to $8.58\times$ that of the full benchmark. These results suggest that reliable benchmark use requires examining sample-level capability boundaries beyond leaderboard scores.

---


### 344. [Turning Speech Language Models into Multilingual Listeners](https://arxiv.org/abs/2609.33204)

**<font color=#1a73e8>作者：</font>** Tolúlopé Ògúnrèmí, Dan Jurafsky, Chris Manning 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Language Models (SLMs) that understand spoken language questions support only a few high-resource languages, limiting access to millions of people worldwide. This gap stems from the scarcity of multilingual speech instruction-tuning datasets. We present MULTISPEECHQA, a large-scale, synthetically generated and human-verified dataset comprising 9200 hours of 10.8 million spoken question-answer pairs in 23 typologically diverse languages. Using MULTISPEECHQA, we also introduce MULTISPEECH-BENCH, a multi-task benchmark for evaluating SLM performance on 23 languages. We compare the performance of a cascading system to open-weight and closed SLMs on MULTISPEECH-BENCH and find that the cascading system outperforms open-weight SLMs but not all closed SLMs. We use MULTISPEECHQA to finetune Qwen 2.5-Omni, which improves its performance on our benchmark. Our findings show that high-quality synthetic datasets offer a cheap solution to improving the multilingual capabilities of SLMs.

---


### 345. [Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?](https://arxiv.org/abs/2609.33209)

**<font color=#1a73e8>作者：</font>** Keyi Li, Yihao He, Quanyi Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed-decision models such as TypeSafe's Jev answer a declared yes/no or multiple-choice question about a state with a probability instead of text, and their evaluations report accuracy and calibration. Neither requires that the probabilities a model gives to logically related questions fit together item by item, which is what a system that acts on those probabilities needs. We test this property, coherence, with a battery of logically linked questions that needs no labels. For 160 items from ChaosNLI and PubMedQA, each with three mutually exclusive labels, we ask whether the label is X, whether it is not X, whether it is one of the other two labels, and which label applies. On 480 negation pairs, Jev's probabilities for "the label is X" and "the label is not X" miss summing to one by 0.064 on average (95% CI 0.055 to 0.072). Qwen3.8-27B, run from its official BF16 weights, misses by 0.293 with first-token probabilities and by 0.122 with verbalized probabilities. The gap to the first-token readout persists on pairs where both systems give similar probabilities, without double-negation labels, and after averaging Jev's repeated calls. Jev is not coherent either: its violations are about five times its repeat noise, and it over-endorses statements about single labels, so that its three single-label probabilities sum to 1.14 on average. The two systems also fail differently. Qwen3.8-27B's first-token readout under-endorses the complement of a label whether or not the question contains "not", rejecting both a statement and its negation in 196 of 480 pairs, and it does not become more coherent where it is more confident, whereas Jev's violations concentrate where its answer is uncertain. Because the checks need no labels, they expose biases that appear only when question forms are compared, and inconsistencies within items.

---


### 346. [CoLMbo-SV: A Grounded Language Model for Explainable Speaker Verification](https://arxiv.org/abs/2609.33212)

**<font color=#1a73e8>作者：</font>** Massa Baali, Sarthak Bisht, Ziyue Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speaker verification systems achieve high accuracy but provide little account of the acoustic evidence behind their judgments. Making these systems inspectable requires exposing interpretable evidence while retaining the richer information on which their decisions depend. We present \textbf{CoLMbo-SV}, a speaker language model that combines strong speaker discrimination with structured, acoustically grounded comparison reports. By connecting a pretrained speaker encoder to a language model and supplying explicit acoustic measurements, CoLMbo-SV makes voice comparisons inspectable without restricting verification to the evidence verbalized in its reports. We additionally introduce \textbf{VoxReason}, paired recordings with measured acoustic properties and comparison reports filtered through numerical and qualitative checks, providing supervision for this combined capability. We also develop an evaluation framework that separates what acoustic information a speaker representation encodes, what influences the verification score, and what the generated report discusses. On VoxCeleb1-O, CoLMbo-SV achieves 0.99\% EER, reducing verification error by approximately 80\% relative to the strongest audio-language baseline fine-tuned on VoxReason, while attaining a numerical-grounding score of 0.82. Our analysis further demonstrates that acoustic correctness and decision relevance are distinct properties of an explanation, exposing a gap that numerical-grounding metrics miss. Together, these contributions substantially advance audio-language speaker verification, bring its accuracy toward that of dedicated speaker encoders while adding checkable acoustic reporting, and establish an empirical framework for connecting natural-language explanations to the decisions they explain.

---


### 347. [RMB: Reward Model Boosting Mitigates Reward Hacking](https://arxiv.org/abs/2609.33221)

**<font color=#1a73e8>作者：</font>** Jiabin Fan, Dezhi Ye, Yongchang Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) is a powerful technique for aligning large language models (LLMs) with human preference. However, it often suffers from the reward hacking issue, where policy optimization improves the proxy reward model while actually degrading performance with respect to the true human preference, due to the imperfection of the proxy. To address this, we propose Reward Model Boosting (RMB), a novel approach that enhances the robustness and reliability of the reward signal for RLHF. RMB first trains a set of reward models with a diversity-promoting regularizer. This encourages each model to learn complementary aspects of the reward landscape. Then, RMB learns a lightweight aggregator in the principle of boosting to aggregate the outputs of the diverse reward models into a more accurate and robust reward signal. Our extensive experiments demonstrate that RMB significantly improves reward accuracy on both in-distribution and out-of-distribution datasets, substantially mitigating the reward hacking issue and ultimately improving RLHF performance.

---


### 348. [Beyond Memory Construction: Rethinking Memory Access for LLM-based Conversational Agents](https://arxiv.org/abs/2609.33226)

**<font color=#1a73e8>作者：</font>** Donghua Cai, Yongheng Deng, Yifei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is a core component of conversational agents, enabling coherent and context-aware behavior over long interactions. Recent approaches commonly rely on LLM-based memory construction, where raw interactions are rewritten into structured memory units and later retrieved via a RAG pipeline. While effective in controlled settings, we show that this paradigm breaks down in long-horizon, high-entropy conversations: memory construction becomes increasingly lossy and unstable as context length and information complexity grow, and incurs prohibitive cost due to repeated LLM invocation. To address these limitations, we propose Threader, a memory system that shifts the focus from memory construction to efficient, structure-aware access over raw interactions. Instead of rewriting interactions, Threader preserves them as first-class memory, organizes them into topic-coherent segments via lightweight incremental segmentation, and enables accurate retrieval through multi-view representation. At query time, it performs multi-signal retrieval that combines segment-level access with localized evidence matching, ensuring both completeness and coherence. Extensive experiments demonstrate that Threader consistently improves answer accuracy and evidence recall, while significantly reducing the memory construction overhead.

---


### 349. [PARSEE-VAD: Efficient Training-Free Online Video Anomaly Detection via Proposition-Aware Reasoning and Streaming Evidence Escalation](https://arxiv.org/abs/2609.33236)

**<font color=#1a73e8>作者：</font>** Ji Wang, Shuangqing Zhang, Guo-Sen Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free online video anomaly detection (VAD) with frozen multimodal language models faces two coupled challenges: extracting reliable current-window semantics under causal and computational constraints, and maintaining temporal continuity without repeatedly transmitting high-dimensional history. Encoding history through text can compress visual evidence and introduce semantic bias, whereas retaining visual history expands multimodal context. We introduce PARSEE-VAD, a two-module framework that separates semantic evidence acquisition from score-state evolution. Proposition-Aware Reasoning (PAR) extracts structured propositional evidence from the current causal window and conditionally activates more specific queries when coarse evidence warrants further refinement. By sharing a reusable causal visual prefix across queries, PAR reduces redundant computation through selective execution. Streaming Evidence Escalation (SEE) maps the acquired proposition evidence into a compact score-domain event state through current evidence escalation, then propagates only the resulting bounded state across decisions to support temporal continuity. Experiments on four benchmarks demonstrate strong training-free online performance while selective routing reduces specialist computation and score-state propagation remains sparse. These results support a current-first principle for streaming multimodal inference: resolve present semantics first, then use compact historical state only to repair residual continuity gaps.

---


### 350. [CodeSkill: Latent Skill Abstraction for Long-Horizon Code Agents](https://arxiv.org/abs/2609.33243)

**<font color=#1a73e8>作者：</font>** Song-Li Wu, Jingyi Wang, Zhaocheng Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code agents require long-horizon decision-making over complex interaction trajectories. However, existing reinforcement learning (RL) approaches typically optimize behavior at the token level, creating a mismatch between low-level generation and high-level behavioral reasoning. This limitation leads to inefficient exploration and weak credit assignment under sparse rewards. Moreover, while large-scale agent trajectories often contain recurring multi-step behavioral patterns, their noisy token-level representations hinder effective experience reuse. To address these challenges, we propose CodeSkill, a framework that adapts hierarchical latent skill modeling to the code agent domain. CodeSkill first leverages a teacher model to distill both successful and failed trajectories into multi-level textual abstractions. It then integrates temporal variational inference with reinforcement learning to map these discrete semantics into continuous latent variables, while an adaptive boundary mechanism dynamically gates skill transitions based on execution feedback. The learned skills are injected into a frozen LLM policy as latent semantic prefixes, enabling optimization in a compact semantic space rather than over raw token sequences. By shifting RL from token-level exploration to experience-level reasoning, CodeSkill improves optimization efficiency and long-horizon behavioral coherence. Extensive experiments demonstrate that CodeSkill achieves highly competitive performance against strong open-weight baselines across diverse general and industrial coding benchmarks. Furthermore, the learned skills exhibit strong transferability and robust cross-domain generalization, highlighting the effectiveness of explicit behavioral abstraction for scalable agentic code generation.

---


> [!TIP]
> 当前位于：**301-350**（第 7/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
