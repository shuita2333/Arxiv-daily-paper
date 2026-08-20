# 🧠 大模型相关研究 | 2026年08月21日

> 本类共 **166** 篇论文：已确认 **153** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-166**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-166**

---

### 151. [Learned, Then Lost: A Measured Single-Example Counterfactual in Pre-training](https://arxiv.org/abs/2608.19168)

**<font color=#1a73e8>作者：</font>** Zachary Speck, Asa Shepard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A single training example's contribution to a finished model is normally estimated rather than measured, because measuring it takes two expensive full pre-training runs that differ in one row of one batch. We ran that counterfactual 24 times at a small scale. We trained 32 GPT-2 models at 124M parameters from scratch on OpenWebText, over four conditions and eight seeds. At step 200 of 9,536, at peak learning rate, we replaced one row of a 256-row batch with a fixed context injection carrying a 194-token passage. The three injected conditions are: 1. fluent prose with a corpus-attested subject, 2. fluent prose with a fabricated subject matched to it within 0.14% on full-batch gradient delta, and 3. random keyboard characters. The fourth condition is an uninjected twin. The passage is learned from one exposure and then decays. Fifty steps after injection, the arm that saw a passage predicts it better than the arm that did not by 0.039 and 0.044 nats of cross-entropy on the passage, at eight of eight seeds with p < $10^{-4}$. At the final step we do not detect that difference for either passage, at p = 0.25 and p = 0.71, against minimum detectable effects of 0.025 and 0.079 nats, nor between the two passages, at p=0.54. Every geometric measure we report is taken after that decay. Our pre-registered contrast on interpolation loss barrier is +0.0068 with p = 0.509, against a minimum detectable effect of 0.032 barrier units. Held-out cross-entropy is $-0.00044$ with p = 0.310. Per-layer centered kernel alignment does not detectably separate any condition at any layer. Weight displacement reaches 44.1% of the seed-to-seed Euclidean distance and is 92% settled by the midpoint of training, while the barrier reaches 3.0% of the seed-to-seed barrier. Those two figures sit roughly 15 times apart, and that is a lower bound. The injection relocates the model within its basin without moving it out.

---


### 152. [Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning](https://arxiv.org/abs/2608.19181)

**<font color=#1a73e8>作者：</font>** Zhu Zhang, Jixun Wang, Xiaoang Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own responses using dense token-level guidance from a stronger teacher. In long-context tasks, however, token-level teacher support can favor locally plausible responses that omit evidence distributed across the input or violate global task constraints. Task-specific verifiers, in contrast, evaluate task completion at the response level and may return graded rewards that reflect partial success. We diagnose this mismatch on fixed responses from two representative long-context evidence-aggregation tasks. Across longer input ranges, trajectory-level OPD scores become progressively less aligned with verifier rewards, indicating teacher-verifier disagreement. Motivated by this observation, we introduce Group-Calibrated On-Policy Distillation (GC-OPD). GC-OPD separately normalizes verifier rewards and trajectory-level OPD scores within each rollout group and uses their difference as a signed teacher-verifier disagreement residual. Relative-advantage-based credit assignment (RACA) distributes this trajectory-level residual across tokens according to their relative OPD advantages while preserving the original OPD signal. Across five long-context benchmarks, post-training with GC-OPD raises the five-benchmark averages of the official Qwen3-4B and Qwen3-8B checkpoints from 29.08 to 40.47 and from 35.12 to 44.65, respectively. Vanilla OPD reaches 39.31 and 43.56 under the same setup. Controlled ablations show that the signed residual is more effective than either an additional OPD-derived term or direct group-normalized verifier reward addition, while RACA further improves over uniform token allocation. Together, these results demonstrate that group-relative residual calibration can incorporate verifier outcomes without discarding dense token-level guidance. Code is available at this https URL.

---


### 153. [SPADE: Self-Play in Adaptive Synthetic Executable Environments](https://arxiv.org/abs/2608.19197)

**<font color=#1a73e8>作者：</font>** Bo Liu, Simon Yu, Yiding Jiang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environment pools (hand-curated, statically synthesized, or frozen-verifier) keep the goal distribution fixed as the learner scales. We introduce SPADE (Self-Play in Adaptive Synthetic Executable Environments), a self-play RL framework in which a single LLM plays two roles: an Environment Designer that writes complete, long-horizon training environments as executable code with an OpenAI Gym-style reset()/step() interface, and a Reasoning Agent that learns to act in them. Each is a stateful, multi-turn environment (state transitions, reward functions, and verification code), so one interface spans reasoning problems and multi-step agentic tool use. The Reasoning Agent's regret is estimated using the gap between its reward with and without privileged hints; in optimizing this regret signal the Environment Designer learns to target environments at the edge of the agent's capabilities while keeping them feasible. Through extensive experimentation, we find several components critical to success: grounding the Environment Designer on documents sampled from a large pretraining corpus, and giving it an accumulated environment memory. Scaling to 30B-parameter models, SPADE improves over the strongest fixed-environment baseline by +5.3 on average across eight held-out math, science, code, and reasoning benchmarks, and lifts the tool-use setting by +5.7 on BFCL-v4 multi-turn and +13.9 on ACEBench-Agent; on the games setting, the margin over the strongest baseline grows with model scale. By making environment design itself a learnable component, SPADE takes a concrete step toward open-ended self-improvement.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 154. [Position: Current Model Cards Are Insufficient for Downstream Governance of Open-Weight Foundation Models](https://arxiv.org/abs/2608.18086)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sungwon Chae, Keonwoo Kim, Hoki Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growth of open-weight foundation models (OWFMs) has prompted the AI community to re-evaluate strategies for effective downstream governance. Although model cards have been widely adopted as transparency artifacts in model repositories, existing frameworks often fail to adequately inform downstream developers and users about the distinct safety challenges posed by OWFMs. This position paper analyzes 500 model cards hosted on Hugging Face and argues that effective governance of OWFMs requires a multi-layered approach integrating three complementary components: (i) model cards, (ii) acceptable use policies (AUPs), and (iii) licenses. To motivate this claim, we identify a safety gap left by existing regulatory approaches, including model heritage, alignment provenance, and empirically observed behaviors, through an analysis of model cards with safety-critical information. We further argue that standard open-source licenses (OSLs) are not well suited for OWFMs and may weaken the enforceability of AUPs. Building on these observations, we outline directions for evolving model cards, AUPs, and licenses into integrated safety artifacts to enable a more comprehensive governance framework that coherently integrates informational, normative, and legal dimensions.

---


### 155. [FraudBench: Stress-Testing Policy-Grounded Banking Agents Against Adaptive Fraud](https://arxiv.org/abs/2608.18136)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dheeraj Mohandas Pai, Lu Xian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational agents now act for end users through tools while holding access to customer databases and internal policy documents that a caller can reach through dialogue alone. Banking is the clearest case: the same agent that answers a question can also change contact details, reset a PIN, or move money, so ordinary customer service is inseparable from authorization, fraud detection, and policy compliance. Existing financial-fraud benchmarks classify static transactions or messages, and general agent-safety benchmarks target prompt injection or generic harmful use; none test whether a policy-grounded banking agent safely acts when a caller manipulates identity, authorization, and trust over a conversation. We introduce FraudBench, an executable benchmark built on the $\tau^2$-bench dual-control framework and the $\tau$-Knowledge banking environment. Both the agent and the simulated caller act through tools over shared, mutable account state, and the agent may grant the caller access to selected tools; the environment exposes a 698-document internal policy corpus that the agent must retrieve from. FraudBench contains 150 authored adversarial scenarios; a frozen public set of 107 (90 across ten fraud mechanisms plus 17 chained adaptive attacks) is used for all reported runs, with 43 further chained attacks held out. Safety is history-dependent: single-control tasks satisfy every precondition but one, and adaptive attacks make a later, locally valid request unsafe because of an earlier probe, admission, or failed attempt. Each scenario is annotated with observable evidence, prohibited actions, safe dispositions, and intervention points. A preliminary single-trial evaluation of four agents on the 107 graded tasks yields attack-security between 49\% and 65\%, with money-mule and first-party fraud the most common cross-model weaknesses.

---


### 156. [Entropy-Constrained Adaptive Stochastic Quantization](https://arxiv.org/abs/2608.18147)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ran Ben Basat, Yaniv Ben-Itzhak, Michael Mitzenmacher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive stochastic quantization (ASQ) is a recently introduced quantization approach that optimizes the Mean Squared Error (MSE) for a given input while preserving unbiasedness. It is designed to alleviate the communication and memory bottlenecks of modern data and machine learning workloads, including model, gradient, and KV-cache compression and nearest-neighbor search. Further, practical systems can then compress quantized data with a lossless entropy encoder. However, existing unbiased methods, including ASQ, choose their quantization values without considering this later encoding stage, leaving accuracy on the table.
We formulate the Entropy Constrained Adaptive Stochastic Quantization (ECASQ) problem, which jointly selects adaptive quantization values to minimize MSE under an entropy budget and an unbiasedness constraint. We give an optimal dynamic program with $O(sd^2)$ time and $O(d^2)$ space for a length-d vector and at most s quantization values, and a GPU-friendly approximate dynamic program with $O(sd^2)$ time and $O(d)$ space. The approximation guarantees that the solution has an MSE no larger than the optimal solution that uses one fewer bit of entropy per entry. We also provide an iterative refinement procedure for the approximation solution that, in our experiments, yields near-optimal results while retaining a substantial speed advantage over our solver for the optimal solution.

---


### 157. [Human-Centric Intelligence in the Era of Foundation Models: A Survey](https://arxiv.org/abs/2608.18184)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Chen, Tianqi Wang, Xiaorui Jiang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-centric intelligence is evolving in the foundation-model era, with growing emphasis on scale, transferability, and general-purpose modeling. Yet it has not fully integrated with foundation models to achieve the comparable progress seen in them. More importantly, recent advances across this broad landscape remain fragmented across tasks, modalities, and research communities, leaving their intrinsic conceptual and methodological connections unclear. To bridge these divides and rethink human-centric intelligence in the foundation-model era, we introduce a full-spectrum human context taxonomy that integrates six interconnected levels by viewing humans as observable subjects through visual appearance and spatial geometry, as dynamic actors through kinematic dynamics and interaction modeling, and as situated agents through world simulation and embodied agency. We next present the methodological foundations of the field, covering human-centric data families, computational architecture paradigms, and representative training and inference optimization strategies. We then systematically review representative methods across these levels and organize the associated datasets, benchmarks, and evaluation metrics. We further discuss open challenges and promising research directions toward human-centric intelligence that is scalable, trustworthy, physically grounded, and deployable, aiming to provide a coherent framework and practical reference for advancing the field. Finally, we provide a systematically organized and continuously updated collection of human-centric AI literature and resources on our project page.

---


### 158. [WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing](https://arxiv.org/abs/2608.18486)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenbo Zhang, Xiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In a Transformer, each layer attends to past tokens only through KV produced at its own depth, despite the presence of deeper representations during autoregressive decoding. Feedback architectures allow shallow consumer layers to attend to KV produced by deeper past-token representations, but give all consumer layers the same fixed connection patterns to source layers. We propose WhiteMatter, which connects every attention layer to the representations from all layers of each past token, with connection weights that can vary across consumer layers and adapt to the source token. For each token, a router implements these connections by mixing its $L$ layer states into $k$ KV channels that are cached for subsequent tokens; each consumer layer attends to one of the channels. The number of channels $k$ controls the KV-cache size. Setting $k<L$ reduces the cache's memory footprint. In our pretraining experiments, WhiteMatter outperforms a vanilla Transformer with 50% more layers and retains most of this gain with a 50% KV-cache compression.

---


### 159. [Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR](https://arxiv.org/abs/2608.18574)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lirui Luo, Guoxi Zhang, Hongming Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) commonly post-trains reasoning models on multiple tasks, while rerunning multitask RLVR (MTRL) as new tasks are added makes capability expansion costly. We therefore study continual RLVR, which updates the existing model as each task arrives. The central question is whether a model updated this way can perform as well as a jointly trained model. To answer this question, we introduce Continual Reasoning Gym, a continual-RLVR environment that organizes text and visual reasoning tasks into five task sequences. In this setting, we identify two key observations: Sequential RLVR exhibits modest forgetting, yet its final performance remains below that of MTRL. To understand the latter, we decompose final performance and show that forgetting accounts for only part of the gap. To explain the former, we identify shared reasoning: transferable reasoning structure allows training on one task to support others on average. We therefore introduce Continual Prompt Replay (CPR), which harnesses shared reasoning to improve learning on the arriving and future tasks by replaying previous-task prompts and regenerating their responses with the current policy. On average, only CPR reaches MTRL-level performance.

---


### 160. [FACET: Preserving Source Intent and Executable State in Terminal Task Synthesis](https://arxiv.org/abs/2608.18580)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kou Shi, Zun Wang, Qisheng Su 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training terminal agents requires scalable executable supervision, yet synthesizing high-quality terminal tasks remains challenging. Each task couples an instruction, an initialized environment, a reference solution, and an executable verifier; if these artifacts are generated from inconsistent assumptions, the resulting task may be unsolvable or incorrectly evaluated. Meanwhile, multi-stage synthesis can discard the goals, dependencies, state transitions, and procedural constraints encoded in the original sources. We present FACET (Fine-grained Agentic Construction of Executable Tasks), a framework that addresses both information preservation and cross-artifact consistency. FACET reconstructs related agent skills into coherent, information-rich scenarios, then realizes and repairs the execution environment before generating the final task artifacts. The resulting container state serves as shared grounding for the instruction, solution, and verifier, while execution-based validation and targeted repair correct artifact-specific failures without unnecessarily regenerating valid components. FACET produces complex terminal tasks with dense executable checks, and successful trajectories collected from these tasks provide effective, data-efficient supervision. Fine-tuning models across multiple scales consistently improves performance on Terminal-Bench 2.1, while analyses of alternative generation schemes support the importance of environment-grounded construction for task validity and solution-verifier alignment. These results establish source-intent preservation and shared executable-state grounding as key principles for scalable terminal-task synthesis.

---


### 161. [VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio Generation](https://arxiv.org/abs/2608.18607)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yinming Huang, Shuyuan Tu, Xi Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using reinforcement learning to post-train joint video-audio generation models requires a reward signal. Existing methods construct this reward by combining metrics for individual quality dimensions, including audio quality, visual fidelity, and synchronization. However, these metrics evaluate perceptual dimensions separately and fail to capture the overall semantic and temporal coherence among the text prompt, video, and audio that shapes human preferences. Optimizing models against these metrics encourages reward hacking, generating video-audio content that achieves high scores on these metrics yet appears incoherent or unfaithful to human viewers. To address this problem, we first construct a large-scale human-preference dataset VAPref-10K for joint video-audio generation, comprising 9K prompts and 10.3K fine-grained paired comparisons from open-source generation models. We also introduce the VA-Judger-Bench benchmark with both in-domain and out-of-domain model comparisons to evaluate whether reward models truly align with human preferences. We further propose VA-Judger, a chain-of-thought omni-reward model for joint video-audio generation. In particular, VA-Judger first learns from pairs with clear quality gaps to establish structured output and coarse preference discrimination, then distills reliable preference explanations for harder near-quality comparisons via rejection sampling verified against human annotations, and finally performs dimension-wise reinforcement learning that decomposes human feedback into individual quality dimensions for denser reward signals than a single binary preference label. Experiments show that VA-Judger outperforms metric baselines in predicting human preferences on both in-domain and out-of-domain evaluations. Using its human-aligned rewards for post-training audio-video generation model also yields significant improvements in generation quality.

---


### 162. [A Critical Synthesis of Uncertainty Quantification and Foundation Models for Semantic Segmentation](https://arxiv.org/abs/2608.18709)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Steven Landgraf, Joceline Hinz, Markus Ulrich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly breaking what seemed to be impossible not long ago by enabling unprecedented accuracy and cross-domain generalization. Yet their lack of interpretability, tendency to be overconfident, and sensitivity to real-world domain shifts pose critical challenges for safety- and mission-critical applications. Uncertainty quantification (UQ) offers a principled way to address these issues, but its integration into segmentation foundation models has yet to be explored. In this paper we present the first systematic evaluation of UQ methods applied to a foundation model for semantic segmentation. We fine-tune a lightweight DPT decoder on top of the pretrained SAM2 encoder to establish a simple yet competitive baseline and benchmark four representative UQ approaches - Monte Carlo Dropout, Deep Sub-Ensemble, Test-Time Augmentation, and Evidential Deep Learning - across Cityscapes, NYUv2, and two challenging out-of-domain settings. Our analysis compares segmentation accuracy, calibration, uncertainty quality, and inference time, revealing clear trade-offs between predictive performance, reliability, and computational cost. These results highlight both the promise and the current limitations of uncertainty-aware foundation models, pointing to the need for future work that jointly optimizes accuracy, robustness, and efficiency for real-world deployment.

---


### 163. [GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models](https://arxiv.org/abs/2608.18849)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qi Qin, Jiajie Zhu, Dali Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and memory costs, hindering large-scale deployment. We propose GEAR (\emph{Generative Expansion and Real Anchoring}), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs. Stage 1 uses synthetic covariates solely as teacher-query locations and trains the student on soft TFM targets, expanding coverage beyond observed rows. Stage 2 re-anchors the student to the target distribution using real labels and out-of-fold teacher predictions, whitch avoids self-labeling leakage. We further derive a risk certificate characterizing the trade-off between generated-query volume and generator fidelity. Experiments on TALENT and TabArena demonstrate the broad applicability of GEAR. Two-stage MLPs outperform supervised MLPs by 1.81--2.00 AUC points on binary tasks and 1.19--1.35 points on multiclass tasks, with additional gains over real-data-only distillation of 1.76--2.19 and 2.09--2.40 points, respectively. On binary tasks, the gains also transfer to LightGBM and XGBoost, and all three student families outperform CatBoost, the strongest non-TFM baseline, in mean AUC. Ablations show gains beyond longer training or alternative warm starts, greater stability from staged than mixed optimization, and generator-dependent diminishing returns as query volume increases. Finally, GEAR reduces median inference time by 57--2866 times and peak prediction memory by 1.9--3.3 times, while retaining higher AUC than matched supervised baselines.

---


### 164. [Falcon Perception-HD: High Density Perception via Reinforcement Learning](https://arxiv.org/abs/2608.18881)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sofian Chaybouti, Yasser Dahou, Ngoc Dung Huynh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive perception models trained to localize visual entities under the open-vocabulary setting are mostly trained using Supervised fine-tuning (SFT) with maximum likelihood, yet it optimizes a proxy objective (per-token cross-entropy) that is fundamentally misaligned with perception metrics such as precision and recall. In this paper, we explore post-training reinforcement learning (RL), specifically GRPO, to directly align these models with their evaluation metrics. Building up on the recently introduced Falcon Perception, we design an RL framework that addresses perception-specific challenges: reward design for set-structured outputs and multi-head sampling control. We discover multiple benefits from RL for perception: first, RL unlocks state-of-the-art performance in very dense scenes (up to 500 objects per scene), a regime where most existing systems degrade sharply or collapse; furthermore it fixes common issues in autoregressive perception models like mask repetitions and removes almost entirely the need for NMS and coordinate deduplication, which improve both performance and efficiency and remove the need for hyperparameters tuning; overall, we notice improvements on all levels of difficulties in referring expression segmentation (on PBench and SACO-Gold), and we find an elegant way to preserve the knowledge of whether an object exists or not (as evaluated by MCC) without training on negative samples. We show that a simple reward that penalizes false negatives and positives is sufficient. We develop two hybrid self-annotation pipelines, respectively tailored for difficult referring expressions and very dense scenes, and show their benefits on RL-training. Model weights are released as a Falcon Perception revision~\footnote{this https URL}. Datasets will be published.

---


### 165. [Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference](https://arxiv.org/abs/2608.18982)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Blazej Banaszewski, Andrew W. Fitzgibbon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bioassay activity prediction is often data-limited because drug-discovery datasets rely on time-consuming and expensive wet-lab experiments for data generation and evaluation. This challenge has inspired recent research into molecular foundation models (MFMs), which aim to encode general-purpose chemical knowledge into molecular representations that generalize well in data-constrained scenarios. This paper presents Monroe, a new MFM with several innovations over the existing state of the art: increased scale allowing pre-training on over 81 million molecules from the PM6 quantum chemistry dataset; improved graph representation of stereochemistry; improved training losses including conformer denoising and embedding decorrelation; improved multi-task learning; and the use of a prior-data-fitted model (TabPFN) for downstream in-context prediction. Our evaluations use a principled pairwise comparison framework that measures statistically significant performance differences. Across established Polaris benchmarks, Monroe matches or exceeds existing MFMs, while on activity cliff benchmarks, designed to assess utility for molecular discovery, it achieves significant improvements over prior methods. Finally, ablation and transfer experiments show that PFN-based downstream predictors also substantially improve two leading existing models, MiniMol and CheMeleon, yielding new state-of-the-art variants we call MiniMol_PFN and CheMeleon_PFN, suggesting that our downstream adaptation strategy generalizes beyond Monroe. Source code is at this http URL.

---


### 166. [Subgroup performance analysis of adaptation strategies for chest X-ray foundation models](https://arxiv.org/abs/2608.19078)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dhruv Gupta, Emma A.M. Stanley, Fabio De Sousa Ribeiro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly adapted for downstream medical imaging tasks, yet the influence of the chosen adaptation strategy on subgroup fairness remains poorly understood. We investigate how three parameter-efficient adaptation techniques, including linear heads on the raw CLS token, an MLP, and an attention-pooling module over multi-layer patch features, affect both pathology classification performance and subgroup disparities when applied to the frozen Rad-DINO chest X-ray encoder. Using MIMIC-CXR, we evaluate eight pathologies across race, sex, and imaging-view subgroups on a prevalence-preserving, demographically balanced test set, and additionally probe how strongly each adapter encodes protected attributes. We find that attention pooling achieves the strongest overall discriminative performance and encodes attributes, particularly race, most strongly, but that improved overall performance does not consistently reduce subgroup disparities. Notably, stronger attribute encoding did not correspond to larger disparities: early network layers encoded race most weakly yet produced the largest subgroup performance gaps. Exploring different attention-pooling layer combinations further revealed no consistent relationship between the layers pooled, attribute encoding strength, and subgroup fairness. Our results indicate that richer, more expressive representations can improve accuracy while leaving fairness implications task-dependent and unpredictable, which must be assessed directly and per-task rather than inferred from encoding strength or overall performance alone.

---


> [!TIP]
> 当前位于：**151-166**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-166**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
