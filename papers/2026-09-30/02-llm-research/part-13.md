# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**601-650**（第 13/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 601. [One Sequence, Many Decodings: CAGenMol-2 Recasts Drug Design as Masked Molecular Inference](https://arxiv.org/abs/2609.34301)

**<font color=#1a73e8>作者：</font>** Yanting Li, Enyan Dai, Lei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug design couples property evaluation, conditional generation, structure-based design, and local optimization, yet machine learning systems typically address these capabilities with separate task-specific models. We introduce CAGenMol-2, a masked diffusion molecular language model that represents molecules, continuous scalar properties, and 3D protein pockets within a single wrapped sequence. Within this pretrained interface, downstream operations are selected by which sequence regions are observed or masked at inference, allowing one checkpoint to perform property prediction, property- and pocket-conditioned generation, and partial-constraint design without task-specific architectures or backbone fine-tuning. We further propose Adaptive Fragment Optimization (AdaFO), a gradient-free mask-and-refill search that turns the masked decoder into an iterative local molecular optimizer. On CrossDocked2020, AdaFO increases Success Rate from 30.2\% to 70.8\%, the best reported under this protocol, while largely preserving drug-likeness and diversity. Finally, scaffold-preserving directional editing and CRBN/VHL case studies demonstrate its use in compound design workflows spanning local molecular editing, structure-based prioritization, and downstream simulation-based screening.

---


### 602. [MaLiang-Harness: A Programmable Path to Image and Video Generation](https://arxiv.org/abs/2609.34309)

**<font color=#1a73e8>作者：</font>** Haoyu Zhao, Zihao Zhang, Xudong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Executable programs offer explicit control over how images and videos are constructed, but generating runnable code is only the beginning of visual creation. A program can execute correctly while violating the requested composition, appearance, or motion. We define this discrepancy as the Program-to-Visual (P2V) gap and introduce MaLiang-Harness, a unified framework for organizing MLLM-driven visual generation into a persistent process of construction, inspection, and revision. Its central design is to make the evolving visual program, its construction history, and its verification share a common revision reference. We define the Persistent Executable Generation (PEG) state as preserving programs and task context. Traceable Generation Process (TGP) connects edits to rendered evidence, and Revision-aware Editing and Verification (REV) supports restoration and checks the current revision before completion. Together, these mechanisms coordinate planning, execution, and visual feedback across rendering backends. We evaluate 11 powerful closed-source MLLMs on MaLiang-IBench and four on MaLiang-VBench, measuring generation success, visual quality, and computational cost. GPT-6-Astra achieves 100% generation success on both benchmarks, with 96.0% of image tasks and 76.9% of video tasks meeting all quality thresholds. The comparison also reveals a mismatch between general capability scores and visual generation performance, with similarly scored models differing substantially in their ability to satisfy visual requirements. MaLiang-Harness provides a systematic basis for studying how MLLMs translate executable code into visual outcomes, exposing both the potential of programmable generation and the limitations of general benchmarks as predictors of this ability. The project is available at this https URL.

---


### 603. [ControlScope: Workflow Revision and Reliability in LLM Agents](https://arxiv.org/abs/2609.34313)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Xueqi Li, Yibo Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How much of a running workflow should a language model agent revise? ControlScope compares continuing generated code, editing the next tool call's data arguments, and replacing the unfinished workflow from the same public execution state. The nested permissions separate available repairs from the actions an agent selects. We evaluate one-time and repeated reviews across filesystem tasks, ALFWorld, and AppWorld. Across two source programs per task and three reasoning-reviewer draws on 20 filesystem tasks, FULL completes 15-16 tasks versus 13 for KEEP; across four fast draws it completes 10-13 versus 13. Fresh student-record confirmation reproduces a batch-read repair. ALFWorld fast panels yield KEEP/ARG/FULL scores of 85/86/87 on 87 tasks across 52 scenes and 134/134/127 on 134 tasks across four scenes; reasoning on the 87-task cohort also yields 85/86/87 with substantial review cost. An AppWorld V1 official-test panel of 585 task instances from 195 scenario templates shows small net differences. Frozen replays expose viable agent-written replacements interrupted by later revision in two failed file-organization runs. An offline source-trajectory midpoint comparison shows later reviews completing an insufficient repair. Five-call protection saves 19.4% of logged model output and loses one success across 20 fresh source runs. An argument-only shortcut shows that the broader sampled policy can overlook a cheaper successful edit available in both operation sets. These outcomes tie repair access to actual choices and subsequent execution.

---


### 604. [PlaylistEval: Can Video-Language Judges Be Trusted at Day Scale and Beyond?](https://arxiv.org/abs/2609.34314)

**<font color=#1a73e8>作者：</font>** Shayekh Bin Islam, Hwanjun Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models are increasingly used as judges of video understanding, both for evaluating model outputs and for training reward models. Whether their judgments remain reliable when the evidence is buried in day-long videos has yet to be established. Existing benchmarks cannot answer this. Their videos are typically only a few minutes long, many answer pairs can be separated from the transcript alone, and collecting human judgments does not scale to ultra-long videos. We introduce PlaylistEval, an agentic framework that builds video-language judge benchmarks over 100-hour playlist collection without human annotation. It automatically generates questions with paired answers whose differences are controlled by causal degradation, so that every pair demands retrieval across the collection. The resulting benchmark contains 630 pairs across seven domains spanning both static and dynamic knowledge, and on a stratified subset of 152 pairs it agrees with human judgments 93.0% of the time (IAA 0.781). Evaluating 17 omnimodal and multimodal models from eight families reveals that frontier judges reach only 75.4% pairwise accuracy, while open-source judge models perform far behind. We further show that both retrieval and final judgment depend on using multiple modalities, and that judge accuracy degrades as the playlist set grows. We release our pipeline, benchmark, and evaluation code at this https URL.

---


### 605. [Text-Vision Synergistic Token Caching: A Training-Free Framework for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2609.34319)

**<font color=#1a73e8>作者：</font>** Qianer Li, Chengjie Zhang, Jingwen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models enable generalizable robotic control but remain computationally expensive. Token caching provides a training-free, plug-and-play acceleration alternative. However, existing VLA caching does not fully exploit a key inductive bias of VLA models: text-vision synergy, wherein textual semantics guide the precise visual grounding of task-relevant regions. In particular, existing designs insufficiently account for head-wise reliability in attention aggregation and layer-wise stability in cache reuse. To address this, we propose Text-Vision Synergistic Token Caching (TVCache), a training-free framework for efficient VLA inference. TVCache filters attention heads based on text-vision information focus to improve task-relevant and physically consistent visual grounding. Concurrently, we introduce a reuse-layer selection mechanism guided by text-vision entropy differences to avoid caching unstable representations and improve cache resource allocation. Extensive experiments across four representative VLA models, two simulation benchmarks, and real-world robotic tasks demonstrate the effectiveness and generality of TVCache. At matched token-retention ratios, TVCache consistently improves task success over existing VLA caching with comparable computational cost. On OpenVLA-OFT, it improves average success by up to 14.5 percentage points over VLA-Cache at 12.5% retention while reducing FLOPs by 2.45x relative to full-token inference.

---


### 606. [Certified Selective Automation of LLM Agent Evaluation](https://arxiv.org/abs/2609.34320)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Yunhao Liang, Qinghao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM agents still ends with a human reading trajectories, because automatic judges carry no guarantee on how often they are wrong. We ask the operational question: what fraction of agent evaluation can a judge take over, with a certificate that the error rate among auto-decided trajectories stays below a budget alpha? Agent corpora resist the standard answer: many agents attempt the same tasks, so trajectories arrive in correlated clusters, and the i.i.d. certificates of existing selective-judging methods can overstate what is safe: a naive certificate can claim 98% automation while its realized error exceeds the budget in 17.5% of task resamples. We introduce a task-level bootstrap certificate that is valid in every regime we test while matching the naive certificate's coverage; finite-sample cluster-valid alternatives certify nothing at realistic task counts. Under this certificate, a 4B logprob judge trained with SFT and reject-weighted GRPO certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1, the only judge, among strongly elicited frontier models, certifying on both headline corpora. Certified coverage is predictable before training from base rate and discrimination alone (leave-one-corpus-out R^2=0.96). Finally, the certificate doubles as a self-training filter: pseudo-labels harvested inside certified regions have contamination bounded by alpha by construction (realized 0.000-0.041 across six harvests), letting a judge enter an unseen domain at in-domain strength with zero target training labels.

---


### 607. [One Rollout Is All You Get: Fully Test-Time Adaptation for GUI Agents](https://arxiv.org/abs/2609.34321)

**<font color=#1a73e8>作者：</font>** Ziqiang Wang, Li Gu, Zhixiang Chi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GUI agents are deployed with frozen weights and discard everything they experience on the job. Existing ways to update an agent's weights assume something deployment withholds: ground truth, rollouts beyond the single attempt (retries, samples, practice runs), or a learning phase other than deployment. Because GUI actions can be irreversible, a deployed agent gets one attempt per task occurrence, in arrival order, and every attempt counts. No ground truth is available at any point. We define fully test-time adaptation for GUI agents by these constraints and pair it with a minimal weight-space method, SOLO. Auxiliary models read each episode: a judge selects the episodes it deems successful, and a proposer-verifier pair relabels a failed episode's prefix with the subtask that prefix completed. Admitted episodes enter a short sliding window, and each admission updates a small adapter by top-K self-distillation on the agent's own predictions, provided the window holds a judged success. On recurring task streams built from WebArena, VisualWebArena and MobileWorld, SOLO improves on the frozen agent with both UI-TARS-7B and Qwen3-VL-8B, by three to six points of success rate, and exceeds two in-setting memory methods on the web streams.

---


### 608. [Test-Time Scaling via Budgeted Multi-Attribute Verification](https://arxiv.org/abs/2609.34322)

**<font color=#1a73e8>作者：</font>** Bo Xue, Ji Cheng, Shen-Huan Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifying LLM-generated answers under a shared computational budget requires jointly deciding which candidates to inspect and which verification attributes to evaluate. We formulate this problem as multi-attribute good-arm identification under a global budget: each candidate is an arm evaluated along several costly attributes, and the goal is to certify as many candidates as possible whose mean scores exceed the prescribed thresholds on all attributes. We propose \textsc{BMA-GAI}, an algorithm that combines cost-aware arm selection with adaptive sampling of attributes. Every observation serves both to guide adaptive allocation and to support anytime-valid certification, which removes the need for a separate confirmation stage. We establish an asymptotic coverage guarantee for \textsc{BMA-GAI} and derive a matching information-theoretic converse that characterizes the intrinsic complexity of the problem, thereby proving that \textsc{BMA-GAI} is first-order optimal away from critical budget levels. Experiments on synthetic benchmarks and an LLM answer-verification task show that \textsc{BMA-GAI} allocates the verification budget more efficiently and certifies more high-quality candidates than competing methods.

---


### 609. [Routing Without Embeddings: Fast And Interpretable Routing With Regular Expressions](https://arxiv.org/abs/2609.34326)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Qiyue Zhang, Haotian Shan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) routers commonly rely on neural query embeddings, with larger encoders expected to better capture query intent and difficulty. Yet scaling Qwen2.5 encoders from 0.5B to 72B parameters brings little improvement in routing accuracy (Figure 1b), suggesting that small encoders may already capture the query properties needed for routing. We therefore investigate which properties matter and whether they can be extracted directly from text without a neural encoder. We introduce REGEXROUTE, a pipeline that uses sparse autoencoders (SAEs) to discover interpretable regular-expression (regex) features. Using unlabeled text, an LLM turns descriptions of grouped SAE latents into regex extractors and refines them to match latent activation patterns. These extractors supply numerical features to a lightweight routing head, eliminating neural encoding at inference (Figure 1a). Across four benchmarks, one fixed set of 128 features achieves 76.43% average routing accuracy, comparable to 76.41% for the strongest neural text encoder baseline, with much smaller latency and strong robustness. These findings establish explicit, interpretable text features as a practical basis for designing and understanding LLM routers.

---


### 610. [Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge](https://arxiv.org/abs/2609.34327)

**<font color=#1a73e8>作者：</font>** Chanuk Lee, Minki Kang, Sangwoo Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling test-time computation is a powerful way to improve language-model reasoning, and is particularly appealing for small reasoning models (sRMs) that are cheap to serve. However, is additional thinking always the right operation? By intervening at intermediate reasoning states across two model families and multiple scales, we find that self-refinement largely consolidates probability mass onto solutions already reachable from the current state, rather than making new ones reachable. These interventions reveal two failure regimes: execution bottlenecks, where the correct path is reachable and reflection can recover it, and knowledge bottlenecks, where relevant external information makes it reachable. Motivated by this distinction, we introduce FlyBy, a selective querying framework, and train 4B and 8B variants to reason first, diagnose what remains unresolved, and, at a knowledge bottleneck, query stronger models whose parametric knowledge extends beyond its own. Supervised fine-tuning bootstraps a multi-depth query action, and cost-aware reinforcement learning calibrates whether to query, what to ask, and how much to spend. On 1,158 hard problems across six benchmarks, FlyBy-4B achieves 45.96% pass@8, surpassing Qwen3-14B (41.64%) at 2.7 times lower serving cost, while also exceeding Qwen3-8B in pass@1 (16.85% vs. 15.31%). Scaling to FlyBy-8B further improves pass@8 to 51.81%.

---


### 611. [MiCo: Mutual Information Coverage Optimization through Semantic Erasure Modeling for Efficient MLLM Inference](https://arxiv.org/abs/2609.34330)

**<font color=#1a73e8>作者：</font>** Tinghao Wang, Yichen Guo, Qizhe Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated impressive performance in multimodal understanding, but processing large numbers of visual tokens results in high computational costs. While many methods have been proposed to reduce the number of visual tokens, most of them rely on heuristics and are prone to discarding substantial visual information during pruning, leading to degradation in model performance. In this work, by using a semantic erasure model, we derive a general mutual information coverage objective from task log-loss and propose MiCo, a training-free two-stage pruning method. MiCo first uses visual signals to select a representative candidate pool before visual tokens enter the language model, then performs task-aware subset selection within it. At each stage, suitable observable proxies instantiate the derived objective as a monotone submodular coverage function, which MiCo greedily optimizes under the token budget. MiCo is evaluated on diverse MLLMs ranging from 7B to 13B parameters across a broad range of image and video benchmarks spanning general visual reasoning, fine-grained OCR and grounding, hallucination detection, and long-video understanding. MiCo consistently achieves the best performance across nearly all evaluated models under all pruning ratios. On LLaVA-NEXT-13B, MiCo uses only 5.6% visual tokens, retains 97.5% of baseline performance, and achieves a 3.8-fold inference speedup. Our experiments demonstrate the effectiveness of MiCo and our mutual information coverage objective for visual token pruning.

---


### 612. [SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing](https://arxiv.org/abs/2609.34342)

**<font color=#1a73e8>作者：</font>** Zhiwei Chen, Tianchun Wang, Zhongtao Rao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A strong LLM strategic agent should reason prospectively over uncertain futures, adapt its strategy to opponents' behavioral tendencies, and continuously recalibrate its decision process from interaction experience. However, incorporating these sources in free-form reasoning could lead to unsupported strategic assumptions, inconsistent opponent estimates, and harmful interference from irrelevant historical interactions. To address these issues, we propose SAGE, a training-free inference-time framework that structures LLM strategic reasoning around three coordinated operations: anchor, adapt, and recalibrate. SAGE first anchors reasoning to an equilibrium policy that provides a strategically valid prior. It then conditions deviations from this anchor on a soft belief over opponent behavioral tendencies, enabling opponent-specific exploitation. Finally, SAGE distills strategically related interactions into counterfactual hypotheses about previously missing considerations, allowing past experience to recalibrate the model's reasoning. We evaluate SAGE on three repeated imperfect-information games: Leduc Hold'em, Liar's Dice, and Goofspiel, against various opponent types in each game. Compared with reasoning-intensive LLM agents, including Suspicion-Agent, ReTA, Agent-Pro, EMO, and Hypothetical Minds, SAGE achieves up to a 127.6% payoff improvement in Liar's Dice while reducing input and output token usage by up to 80% and 90%, respectively. In direct match-up play, it attains non-negative mean payoff against 5/10, 8/10, and 8/10 evaluated opponents in Leduc Hold'em, Liar's Dice, and Goofspiel, respectively, while using relatively fewer tokens. Code is available at this https URL.

---


### 613. [Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large Language Models via Trainable Vectors](https://arxiv.org/abs/2609.34344)

**<font color=#1a73e8>作者：</font>** Yuchen Cai, Ding Cao, Qixiang Yin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a key paradigm for enhancing the reasoning of large language models, yet the high dimensionality of parameter updates makes its training dynamics hard to analyze. We study reinforcement learning with verifiable rewards (RLVR) and use vector steering to identify a low-dimensional effective manifold in activation space associated with RL-induced gains. We uncover two geometric properties. (1) Effective Manifold Capacity: the capacity needed to reproduce RL gains can be very small but is not infinitely compressible; at extremely low capacity, intervention dimensionality and input-dependent expressiveness become key constraints, and this requirement varies with injection depth. (2) Control Manifold Separation: effective control directions lie mainly in the low-variance complement of the activation principal subspace. Within a task and base model, the learned geometry stays largely consistent across training configurations, and across tasks geometric alignment correlates with capability transfer. Experiments on 5 LLMs and 6 verifiable-reward tasks support these findings. We then propose Alpha-Stabler, a plug-and-play framework with a Predictor that monitors principal-subspace intrusion for early collapse warnings, and a Controller that removes the principal-subspace component of activation gradients during backpropagation while preserving the orthogonal complement. Alpha-Stabler stabilizes training for 2,000 steps and consistently improves RL gains, offering practical insights for robust post-training. Code: this https URL

---


### 614. [CRISP: Cultural Reward Modeling for Implicit Situated Propriety](https://arxiv.org/abs/2609.34345)

**<font color=#1a73e8>作者：</font>** Zekun Yuan, Yangfan Ye, Baohang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed across countries and regions, the ability to recognize and respond appropriately to diverse cultural contexts becomes increasingly important. However, existing research has largely focused on cultural knowledge or tasks with predefined response spaces, while open-ended culturally situated behavior remains comparatively underexplored. In this work, we introduce CRISP-RM, a culturally situated reward model that assigns rewards according to cultural appropriateness in open-ended social scenarios. During policy optimization, we further introduce Norm Grounding Supervision (NGS), providing guidance that enhances the policy's sensitivity to relevant cultural norms. To construct culturally situated data, we employ a collaborative multi-agent framework that instantiates implicit cultural norms into diverse social scenarios and further curate NormCompass as a dedicated testbed. We conduct comprehensive experiments to evaluate the effectiveness of CRISP-RM in both reward modeling and policy optimization. Best-of-\(N\) experiments show that CRISP-RM consistently outperforms strong general reward models. During GRPO policy optimization, CRISP-RM generally improves culturally situated behavior, while incorporating NGS yields further gains. Further analyses demonstrate the advantages of CRISP-RM in distinguishing culturally appropriate behavior beyond superficial fluency and politeness, while NGS provides complementary gains during policy optimization by improving norm grounding.

---


### 615. [Commutator Memory: Sparse, Path-Local Reading and Steering in Language Models](https://arxiv.org/abs/2609.34348)

**<font color=#1a73e8>作者：</font>** John Sweeney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient updates on different data generally do not commute: training a language model on two data sources in opposite orders gives different weights, even with the same data and total exposure. Loss or benchmark deltas show that the models differ, not where. We ask whether this path dependence leaves a parametric training-history memory: a weight component that flips sign when the two sources are swapped, is localized in output space, changes the held-out loss gap between the two orders under targeted interventions, and reveals which trained model came from which order. For one small SGD step of size $\eta$ on each of sources $A$ and $B$, the weight difference $\theta_{AB}-\theta_{BA}$ is, to leading order, $\eta^2 b_{AB}$, where $b_{AB}=H_Bg_A-H_Ag_B$ is the Lie bracket of the two gradient fields at the base model. We define commutator memory by projecting the bracket through the logits into one score per vocabulary token; the scores sum to the bracket's prediction of the gap. The scores are localized: on three models, the same readout of the measured $\theta_{AB}-\theta_{BA}$, or of a bracket from disjoint batches, shares 82-99% of the original top-20 tokens, versus 35-49% for norm-matched random directions. They are causally actionable: in Qwen-3-4B SFT, downweighting the ten tokens with the largest predicted share of the gap closes a median 32% of the measured gap, while frequency-matched tokens with near-zero scores have almost no effect. The weights themselves carry the component: projecting the difference between the two trained models onto $b_{AB}$ identifies which came from which order in 92% of cases across four LLMs (chance 50%). Controlled tests also cover matched-batch DPO, a frozen-rollout GRPO-style objective, and an AdamW endpoint check. The memory is defined per source pair, not per example, and its projection on $b_{AB}$ decays with further training.

---


### 616. [FORGE: Form-Optimal Routing of Grounded Evidence for Frozen LLM Agents](https://arxiv.org/abs/2609.34358)

**<font color=#1a73e8>作者：</font>** Xi Xiao, Yunbei Zhang, Chen Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In agentic AI systems, frozen foundation models are increasingly deployed as closed-weight API endpoints, making downstream adaptation possible only through the inputs and inference procedures surrounding the model. As a result, for each input query, two coupled decisions largely determine both answer quality and token cost: what evidence to provide and how much reasoning budget to allocate. Fixed defaults along these axes are often suboptimal, misallocating support form or reasoning depth on roughly 80% of queries in our analysis. To address this challenge, we propose FORGE, a unified framework for adapting frozen models through per-query routing over a joint action space that spans both support form and thinking depth. Under an entropy-regularized, cost-aware utility objective, we derive a closed-form Boltzmann routing target and instantiate the policy as a lightweight 269K-parameter factorized router. The routing policy is trained around the frozen host, without any weight access, through a three-stage pipeline: offline arm enumeration, supervised Kullback-Leibler (KL) distillation from the Boltzmann target, and Group Relative Policy Optimization (GRPO) refinement with host feedback. Across 5 knowledge-intensive benchmarks and 8 frozen backbones ranging from 7B to 671B parameters, FORGE improves accuracy at 42-45% lower token cost on both main hosts, transfers zero-shot across hosts at lower token cost, and composes with intrinsic thinking budgets where available.

---


### 617. [Improving Large Language Models for Code through Runtime Program-State Reasoning](https://arxiv.org/abs/2609.34359)

**<font color=#1a73e8>作者：</font>** Hongwei Li, Spandan Garg, Yufan Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models receive limited explicit training in reasoning about runtime program states. We study whether training models to reason about runtime program states improves downstream software-engineering capabilities. We introduce two complementary program-state reasoning tasks. Buggy input-output reasoning requires a model to generate a concrete input that exposes a behavioral difference between a buggy program and a hidden correct implementation and to predict the resulting execution behavior. Precondition-postcondition reasoning requires an agent to symbolically characterize a bug-triggering precondition, predict the expected postcondition, explain their causal connection, and instantiate this reasoning as an executable regression test. By incorporating these two tasks into a staged post-training pipeline, we develop Comet-9B, a 9B language model based on Qwen3.5-9B Base. We evaluate the resulting checkpoints on repository-level patch generation, regression-test generation, and security PoC generation. Adding both program-state reasoning tasks to supervised fine-tuning (SFT) on issue resolution improves success rates by 7.25 percentage points on SWE-bench Pro and 9.70 points on SWT-Bench Verified. Sequential reinforcement learning on the two tasks yields further gains of 7.25, 26.79, and 4.67 percentage points on SWE-bench Pro, SWT-Bench Verified, and CyberGym, respectively. Despite having only 9B parameters, Comet-9B achieves a score comparable to the reported GPT-5.2 result on SWE-bench Pro and matches the reported success rate of a GPT-4o-based agent on SWT-Bench Verified.

---


### 618. [Spexis: Speculative Lookahead Scheduling for LLM Inference](https://arxiv.org/abs/2609.34370)

**<font color=#1a73e8>作者：</font>** Hyungyu Jung, Jaehyeok Yu, Hoonseo Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism. Rather than using speculative decoding only to accelerate token generation, Spexis runs speculation in parallel with normal execution, introducing a new parallelism axis without increasing KV-cache memory usage. This improves memory efficiency and helps mitigate the bottlenecks of multi-GPU inference.
Spexis further uses lookahead scheduling to predict speculation quality and future memory pressure, allowing it to reduce wasted speculation, KV-cache eviction, and recomputation. Built on top of vLLM, Spexis largely improves serving performance across a range of GPU configurations, achieving speedups of up to 34% over a baseline that uses the optimal combination of pipeline and tensor parallelism. Spexis's source code is publicly available at this https URL.

---


### 619. [From Static to Dynamic: On-Policy Distillation from Image to Video Diffusion Models](https://arxiv.org/abs/2609.34371)

**<font color=#1a73e8>作者：</font>** Bingqing Jiang, Li Luo, Zichao Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) specializes pretrained video diffusion models through teacher supervision along the student's own generation trajectory. Although large video models are natural teachers, developing specialized video experts can require costly video data and training, while querying them incurs substantially higher latency than querying image experts. More readily available and cheaper to query, image experts offer a cost-effective alternative, particularly for largely temporal-agnostic capabilities such as aesthetics and OCR that admit frame-level supervision. However, heterogeneous image and video latent spaces prevent direct supervision of intermediate student states, while image experts lack cross-frame motion supervision, making temporal consistency vulnerable to frame-level improvements. In this paper, we propose MILD, a Motion-Preserving Image-to-Video Latent Distillation framework that transfers specialized image expertise while preserving pretrained video dynamics. MILD uses a learnable linear connector that aligns student latent states and predicted updates with those of image experts, enabling supervision transfer across heterogeneous latent spaces. We further constrain image-guided corrections around the pretrained student's predictions to preserve video dynamics and incorporate an optical-flow-based motion reward to improve motion quality and temporal consistency. Across specialized image experts and multiple video-student backbones, our method consistently outperforms video-teacher OPD baselines, with further studies demonstrating effective transfer across connector designs and heterogeneous architectures. These results establish image-to-video distillation as an effective route to improving video generation by drawing on the diverse and evolving capabilities of the image-generation ecosystem.

---


### 620. [PersMem: Internalizing Personality into Dual-Pathway Memory for LLM Agents](https://arxiv.org/abs/2609.34372)

**<font color=#1a73e8>作者：</font>** Hanzhong Zhang, Ziwei Xiang, Weicheng Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The profile of a role-playing agent usually depends on the pre-defined personality in a system prompt, whereas its memory processing pipeline, including prioritisation of stored memories and subsequent retrieval, remains independent of this personality. This separation causes the agent's memory processing to be inconsistent with the pre-defined personality, and makes it difficult to validate whether agent behaviours follow this personality. In this paper, we propose Personality-Integrated Memory (PersMem), which integrates personality into the agent's memory processing pipeline, making it consistently personality-dependent. PersMem processes memory using four steps, where the personality is mapped to operation-specific parameters controlling: (i) affective appraisal annotating emotion states of the user input; (ii) retention of previously stored memories along with the current input; (iii) passive affect-driven memory retrieval exploring memories similar to user input in semantics and personality-guided emotions; and (iv) active goal-driven memory retrieval that refines and selects passively retrieved memories for the reply. Consequently, consistency with the pre-defined personality can be examined by inspecting memory-processing traces during human-agent interactions. We evaluate these personality-dependent differences in attachment and Big Five settings. PersMem exceeds the chance baseline for four-way attachment classification by 23.1 percentage points. In Big Five dialogue comparisons, PersMem achieves 67.5% accuracy, 6.7 percentage points above a baseline using uniformly sampled memories. On CoSER, PersMem achieves an average score of 66.13, with scores of 69.33 for Character Fidelity and 84.33 for Storyline Quality. Together, these results show that PersMem produces distinguishable personality-related memory-processing patterns.

---


### 621. [ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control](https://arxiv.org/abs/2609.34374)

**<font color=#1a73e8>作者：</font>** Eric Frankel, Banghua Zhu, Sewoong Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model post-training is often bottlenecked by the need for human-collected preference data, which is expensive and difficult to scale. Reinforcement learning from AI feedback (RLAIF) style approaches that leverage pseudo labels offer an abundant alternative but introduce systematic biases that degrade downstream alignment. Recent general-purpose semi-supervised methods correct for teacher bias using a small set of human-labeled examples, but suffer from high variance especially when human annotations are scarce. To this end, we propose ABC-Align, leveraging abundant pseudo label signal to minimize variance and applying a lightweight, adaptive correction grounded in the human-labeled subset. The correction strength is tuned automatically during training using plug-in estimates of the relevant bias--variance quantities. On LLM alignment with RLHF, DPO, and GRPO where human feedback is scarce, we empirically demonstrate that ABC-Align achieves superior performance over prior semi-supervised baselines in a series of experiments on an increasing scale. Our code is available at this https URL .

---


### 622. [Just-In-Time Agent Memory with Runtime Agentic Research](https://arxiv.org/abs/2609.34385)

**<font color=#1a73e8>作者：</font>** Bingyu Yan, Chaofan Li, Hongjin Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is critical for AI agents. Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives. While this reduces online serving cost, such request-agnostic memory construction can discard fine-grained information that later becomes important. To address this limitation, we propose Just-In-Time Agent Memory (JAM), a trainable framework for query-conditioned context construction at runtime. A Memorizer preserves complete raw histories in a hierarchical page-store with compact navigational summaries, while a Researcher iteratively retrieves, inspects, and integrates evidence for each request. To train these memory-use behaviors, we introduce Memory-Gym, an evidence-grounded data synthesis pipeline covering nine task types across six domains, and optimize the Researcher through verified-trajectory supervised fine-tuning followed by Hint-guided Group Relative Policy Optimization. We demonstrate the effectiveness of JAM across a variety of benchmarks on agent memory and long-context processing, where it achieves stronger task performance than AOT-style memory systems while remaining substantially more efficient than prior trained agentic memory approaches. To support reproducibility and future research, we release our anonymized source code at this https URL.

---


### 623. [Look Before You Select: Rethinking Vocabulary Sparsification in On-Policy Distillation](https://arxiv.org/abs/2609.34386)

**<font color=#1a73e8>作者：</font>** Yongliang Miao, Shuang Liu, Yanguang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) uses teacher correction on student-generated responses. Full-vocabulary correction can provide important corrections even for tokens that the student assigns low probability, but backpropagating through all token logits becomes memory-intensive for long sequences. Existing memory-saving approaches estimate corrections from sampled tokens or restrict supervision to the student's TopK tokens, introducing sampling noise or changing the full-vocabulary correction. We introduce \textbf{SparseOPD}, which uses full-vocabulary teacher correction to determine which corrections matter before selecting the token logits to differentiate. SparseOPD first constructs the full-vocabulary correction without retaining its backward graph, then selects tokens by correction magnitude rather than student probability. Signed residual compensation preserves the total promoting and suppressing correction mass, while correction-aware budget allocation distributes the sparse support across positions. Finally, the update backpropagates only through the selected token logits. Across six task--scale settings spanning mathematics, chemistry QA, and multimodal reasoning, SparseOPD outperforms Sampled Token and TopK in task-average accuracy and matches or exceeds Full Vocabulary. Gradient cosine similarity reaches 99\% on 4B mathematics, while 8K full-parameter profiling shows 70.5\% lower backward memory.

---


### 624. [CAR-VLA: Complexity-Aware and Risk-Adaptive Reasoning for Autonomous Driving](https://arxiv.org/abs/2609.34387)

**<font color=#1a73e8>作者：</font>** Xiaolei Chen, Zhuolin He, Yuxuan Liang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing adaptive reasoning methods for driving Vision-Language-Action (VLA) models primarily focus on whether to reason, overlooking how reasoning should differ across driving situations. Our key insight is that while scene complexity informs reasoning depth, dynamic risk is equally critical for deciding how to reason in time-critical situations. We therefore propose CAR-VLA, a unified driving VLA model that jointly considers scene complexity and dynamic risk to guide reasoning depth, urgency, and focus. CAR-VLA maps four complexity--risk categories to three reasoning modes: \textit{Fast Intuition} for direct trajectory generation in simple low-risk scenes, \textit{Slow Thinking} for deliberate reasoning in complex low-risk scenes, and \textit{Reflex Response} for compact, hazard-focused reasoning in high-risk scenes regardless of complexity. Rather than merely shortening deliberation, Reflex Response centers reasoning on the most critical hazard and the immediate safe response. We train CAR-VLA through progressive supervised learning that links scene assessment, reasoning-mode selection, and trajectory generation, followed by reasoning-augmented reinforcement learning to improve driving quality and reasoning behavior. Experiments on NAVSIM v1(91.1 PDMS), NAVSIM v2(90.3 EPDMS), and Navhard(35.0 EPDMS) demonstrate competitive driving performance. Qualitative comparisons on navtest and in-house high-risk scenarios further illustrate risk-aware reasoning and hazard-responsive trajectory generation. The code for this paper will be released publicly at: this https URL

---


### 625. [Reciprocal Guidance: Orchestrating Draft and Verify Budgets for Advancing the Diffusion-AR Self-Speculation Frontier](https://arxiv.org/abs/2609.34388)

**<font color=#1a73e8>作者：</font>** Linye Wei, Shutian Zheng, Haoyu Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion drafting with autoregressive (AR) verification has emerged as a promising paradigm for efficient speculative decoding. Recent self-speculation models, represented by Nemotron-Labs-Diffusion, further simplify the speculative pipeline by unifying drafting and verification within a shared backbone, while enabling longer acceptance lengths. However, the Pareto frontier between aggregate and per-request throughput remains underexplored. At low concurrency, sequential draft-verify execution requires two model forward passes per round, limiting the effective tokens per forward (TPF). By contrast, at high concurrency, longer drafts incur increasingly expensive computation, forcing individual requests to operate under constrained speculation budgets and preventing full exploitation of the full-backbone drafter. Our key observation indicates that drafting and verification exhibit reciprocal predictability. Draft logits can anticipate likely verification mismatches, while recent verification outcomes predict future drafting utility and suitable block sizes. Building on this observation, we introduce Reciprocal Guidance (RecGuide), a runtime draft-verify orchestration framework that adapts speculative decoding to varying serving loads. RecGuide exploits spare compute capacity through verification-overlapped drafting at low concurrency, while dynamically allocating request-specific draft block sizes as the workload becomes increasingly compute-intensive. Experiments across a wide range of concurrency levels demonstrate consistent throughput improvements over vanilla self-speculation, achieving up to $1.8\times$ speedup.

---


### 626. [Org-Agent: Beyond Personal Assistants Towards Organizational Agents](https://arxiv.org/abs/2609.34392)

**<font color=#1a73e8>作者：</font>** Luyao Zhuang, Yujing Zhang, Zijin Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents serving organizations must coordinate requests from multiple users while using knowledge distributed across their interactions. We identify two complementary capabilities for this setting, namely cross-user interaction and decision-making, as well as cross-user memory and knowledge use. Both capabilities are governed by organizational constraints across three aspects: user identity, authority, and access permissions; the attribution and temporal validity of information; and rules for resolving conflicting requirements across users and completion requirements for joint decisions. These constraints shape what information or decisions must be obtained before an action can proceed and what conditions must be satisfied during its execution. Motivated by this, we introduce Org-Agent, a unified constraint-centric reasoning framework that organizes task execution in three stages. Specifically, Org-Agent decomposes a task into atomic subtasks and constructs a task dependency graph whose edges encode the dependencies among them. Building on this graph, it schedules the subtasks in dependency order through topological sorting. It then executes each subtask while accounting for the task's constraints, supported by evidence-acquisition and memory-management tools. Experiments on MUSES-Bench and GroupMemBench demonstrate the effectiveness of Org-Agent on both capabilities, and ablations further support the contributions of dependency modeling and tool use.

---


### 627. [SkillFocus: Evolving Agent Skills via Capability Decomposition](https://arxiv.org/abs/2609.34397)

**<font color=#1a73e8>作者：</font>** Ning Wang, Zhiren Gong, Bingdong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skill evolution seeks to improve reusable procedural guidance for large language model (LLM) agents through iterative revision. Existing methods base each revision mainly on execution trajectories or feedback, leaving recurring behavioral requirements across tasks implicit and tying revision to the behavior of the current skill. We introduce SkillFocus, which decomposes recurring task requirements into a capability space that remains fixed as the skill evolves, separating what tasks require from how the current skill behaves. SkillFocus maps current task outcomes to this space to identify the capability that leaves the most tasks unresolved, then uses that capability to determine what to revise and which evidence to use. Across four benchmarks spanning heterogeneous tasks, SkillFocus achieves the best held-out accuracy on all four, outperforming the strongest competing result by 5.7 points on average while using 24\% fewer evolution tokens on average than the closest iterative baseline. Controlled studies further show that capabilities derived from recurring task requirements outperform task-semantic and execution-derived alternatives, while randomizing task--capability assignments reduces final accuracy by up to 20.2 points. Matching evidence to the selected capability increases candidate gain by 4.4 points under prioritized revision.

---


### 628. [Distilling Visual Reasoning into Text Space](https://arxiv.org/abs/2609.34408)

**<font color=#1a73e8>作者：</font>** Wenhan Yang, Nilay Naharas, Ali Payani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have shown strong promise for multimodal reasoning, yet often struggle with tasks requiring concepts beyond what is directly observable in the input image. Existing methods generate intermediate images or latent visual tokens to guide reasoning, but these representations can introduce errors and increasingly interfere with textual reasoning as reasoning progresses. We propose Visual-to-Text Chain-of-Thought Distillation (V2T), a framework that enables LVLMs to internalize visual reasoning without generating intermediate visual representations at inference time. V2T first trains a teacher LVLM using interleaved visual and textual chains of thought, and then uses knowledge distillation to train a student LVLM using the teacher's logits and cross-entropy supervision from ground-truth textual reasoning. When reasoning images can be mapped to the original image, V2T can additionally distill the teacher's attention to corresponding regions, while ground-truth bounding boxes can further guide a subsequent reinforcement learning stage. Experiments across multiple multimodal reasoning benchmarks show that V2T consistently outperforms the teacher and existing baselines, improving average accuracy by 14.3% on a held-out set and 2.7% on the broader visual evaluation suite. Moreover, lightweight SFT and substantially reduced RL make V2T up to 42x faster to train than state-of-the-art baselines.

---


### 629. [PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety](https://arxiv.org/abs/2609.34415)

**<font color=#1a73e8>作者：</font>** Ding Jia, Wei Liu, Xianglong Du 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The transition from Large Language Models (LLMs) to agents shifts safety stakes from toxic text to irreversible environmental harm. While current defenses remain largely retrospective, proactive runtime intervention is bottlenecked by the lack of large-scale, causally-consistent data. We propose PROACT-Agent, a framework for synthesizing high-fidelity trajectories to enable real-time guardrails. We identify a critical "safety drift" in prior benchmarks, where lenient annotation paradigms fail to enforce temporal consistency. PROACT-Agent addresses this through: (1) Progressive Trajectory Unrolling to reveal risks hidden in long-context interactions; (2) Reasoning-Augmented Causal Rectification to enforce monotonic causal consistency; and (3) Culturally-Aware Data Localization for cross-border robustness. We introduce PROACT-Bench, a bilingual safety benchmark with 155,780 states labeled through multi-model adjudication. Evaluating updated context before the next LLM inference, the trained guard achieves 91.46% unsafe-class F1 and 90.63% exact-boundary detection under complete source holdout. In AgentDojo, it reduces non-DoS targeted attack success from 20.82% to 0.40%.

---


### 630. [OSPD: On-Policy Self-Distillation for Persona-Consistent Dialogue](https://arxiv.org/abs/2609.34418)

**<font color=#1a73e8>作者：</font>** Rui Xu, Yikai Zhang, Aili Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maintaining persona consistency across multi-turn dialogues remains a core challenge for role-playing language models. Off-policy distillation from external teachers incurs distribution mismatch that compounds across dialogue turns, while reinforcement learning struggles with reward ambiguity inherent in subjective persona fidelity. We propose OSPD, an on-policy self-distillation framework where the same model serves as both teacher and student under asymmetric information: the teacher receives a complete character profile while the student sees only a brief summary, and the student generates trajectories from its own policy. We find that teacher confidence in role-playing dialogue exhibits a bimodal structure---sharply peaked at character-critical tokens yet diffuse at generic utterances---and introduce role-aware divergence switching to match this structure. A progressive trait masking curriculum further forces staged internalization of character knowledge along semantic dimensions. Experiments on CharacterBench, CharacterEval, and SocialBench show that OSPD substantially improves persona consistency over supervised fine-tuning and multi-turn RL baselines, without requiring any external teacher or reward model.

---


### 631. [Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning](https://arxiv.org/abs/2609.34422)

**<font color=#1a73e8>作者：</font>** Lirui Luo, Kelong Mao, Heming Xia 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. Recent work has begun to use reinforcement learning to make memory control part of the policy, often relying on predefined memory tools within domain-specific training environments of relatively short horizons. This setup ties learned memory behavior to environment-specific interfaces that lie outside the base model's pre-training and must be learned from scratch, so even after post-training, agents struggle to use memory in long-horizon tasks. To address these limitations, we introduce Coding Agent Memory Gym (CAMG), a suite of long-horizon agentic-RL environments spanning Shop, Coding, DeepResearch, and AutoResearch. Alongside each environment's native task interface, CAMG provides executable shell access and an episode-persistent workspace, enabling agents to create, revise, search, and reuse files as memory throughout an episode. We also introduce CAMG-RL, which trains a single policy jointly across all four environments with fully asynchronous PPO, learning this file-based memory behavior directly from downstream task reward, and we train CAMG-RL-4B and CAMG-RL-9B from Qwen3.5 models of matching size. On SWE-bench Verified and MLE-bench Lite, CAMG-RL-4B and CAMG-RL-9B are competitive with Qwen3.5-35B-A3B and Qwen3.5-122B-A10B, respectively.

---


### 632. [Zero-Shot Cue-Grounded Topic Segmentation of Spoken Documents](https://arxiv.org/abs/2609.34425)

**<font color=#1a73e8>作者：</font>** Suhwan Choi, Myeongho Jeon, Myungjoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic segmentation structures spoken documents into coherent sections, facilitating navigation and downstream understanding. The appropriate granularity can vary substantially, ranging from broad thematic shifts to fine-grained subtopics. Existing LLM-based segmenters, however, often struggle to adapt to this variation, causing them to either merge distinct subtopics or over-segment coherent themes. To address this, we introduce Cue-Grounded Segmentation (CGS), a training-free framework that operates without any task-specific supervision. CGS first identifies phrases that explicitly signal the start of a new topic and uses their sentence positions as segment boundaries. When such cues are insufficient, it falls back to semantic segmentation, guided by the document structure inferred during cue extraction. Across six benchmarks and six LLM backbones, CGS consistently outperforms existing baselines, remains robust to noisy ASR transcripts, and achieves these gains with low API cost on proprietary models.

---


### 633. [LLMs as Adaptive Meta-Solvers: Strategy-Diverse RL for Industrial-Scale Optimization](https://arxiv.org/abs/2609.34427)

**<font color=#1a73e8>作者：</font>** Shihao Zhang, Weiting Liu, Siyu Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling LLM-based optimization from textbook-scale instances to real-world, industrial tasks remains a critical open challenge. Existing approaches are predominantly evaluated on small, self-contained textual problems and often commit to a solver-integrated paradigm, limiting their ability to handle the scale and structural diversity of practical optimization workloads. In this work, we propose a practical framework for training open-source LLMs to tackle real-world, industrial-scale optimization. We first show empirically that solver-integrated reasoning, exact combinatorial algorithm, and heuristic search exhibit complementary strengths across different problem structures and scales. Motivated by this, we introduce Strategy-Diverse Reinforcement Learning (SDRL), which trains LLMs as adaptive optimization meta-solvers. SDRL leverages this complementarity through a correctness-gated hierarchical diversity reward that promotes robust exploration across varying strategies and within each strategy, effectively preventing premature strategy collapse. We further introduce a mixed-format training scheme that jointly supports both self-contained textual problems and file-grounded instances. Across comprehensive evaluations, our framework outperforms existing fine-tuned methods and frontier models including DeepSeek-V4-Pro and GPT-5.5, both on average across benchmarks and on industrial-scale optimization tasks.

---


### 634. [AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering](https://arxiv.org/abs/2609.34428)

**<font color=#1a73e8>作者：</font>** Chanhee Park, Jeongho Yoon, Sungbin Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic tasks require a large language model to interact with the world, navigating information and gathering evidence across multiple steps with restricted resources. Due to this complexity, agentic task failures arise from various sources, and pinpointing these failure causes is essential to diagnose and improve agentic systems. Existing benchmarks, however, tend to focus on a single leaderboard score, leaving the underlying failure modes opaque. To fill this gap, we introduce AgentHop, a diagnostic benchmark of 1,011 multiple-choice questions paired with a controlled seven-tool sandbox under fixed token, turn, and tool-call constraints. AgentHop reveals model vulnerabilities by dissecting a single accuracy score along four axes of agent operation: retrieval, synthesis, tool-call, and resource management. Across 19 models, we find that behavior clusters by model family, with tool-call signatures revealing distinct family fingerprints: GPT models commit early, Anthropic and GLM checkpoints verify before committing, DeepSeek and Kimi over-search, and Gemini-3 Pro stays balanced. Decomposed axes further expose within-family structure: Claude Opus 4.6 and Sonnet 4.6 land within one accuracy point yet diverge on retrieval-versus-synthesis emphasis, with Opus retrieving more and Sonnet synthesizing better. We release the full benchmark set and the harness to support diagnostic agent benchmarking.

---


### 635. [Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents](https://arxiv.org/abs/2609.34438)

**<font color=#1a73e8>作者：</font>** Wanqi Zhou, Jiawei Lu, Yang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for language agents to maintain coherent and effective behavior over extended, multi-session interactions. Existing memory systems mainly use retrieval at read time, while write-time memory formation still relies on direct extraction or compression. However, when future information needs are unknown, compressing an entire interaction in one pass can overlook locally important details that may matter later. To this end, we introduce RIME, a retrieval-induced memory framework that shifts memory construction from monolithic compression toward evidence-centered integration. RIME uses generic self-questions to retrieve focused dialogue evidence and grounds memory formation in both the retrieved evidence and relevant historical memories, which are jointly reconciled into an evolving memory bank with temporal and provenance information. At inference time, compressed memory serves as the primary rather than the sole source of evidence: when it cannot support an answer, RIME retrieves relevant source dialogue together with its local context to recover information omitted during memory formation, without resorting to full-history processing. Extensive experiments on LoCoMo with Qwen3-235B-A22B and GPT-5.6 Sol show that RIME consistently achieves the best performance across all three quality metrics among the compared methods, while requiring substantially fewer query-time LLM tokens.

---


### 636. [Clinical Trajectory Alignment for Medical Vision-Language Pre-training](https://arxiv.org/abs/2609.34439)

**<font color=#1a73e8>作者：</font>** Huimin Yan, Xian Yang, Zhi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language pre-training largely follows a visit-level image-report matching paradigm, aligning paired images and reports at individual visits. While effective for static cross-modal correspondence, this paradigm provides limited supervision for longitudinal clinical change, such as whether abnormalities improve, remain stable, or worsen over time. Learning such change is challenging because temporal semantics are implicit in free-text reports, and different abnormalities within the same patient may evolve asynchronously or even in opposite directions. We propose MedCTA, which reframes medical vision-language pre-training from visit-level cross-modal matching to learning clinical change. Rather than compressing a patient history into a single temporal representation, MedCTA models clinical change at two complementary scopes. At the abnormality scope, clinically grounded queries construct abnormality-conditioned visual and textual trajectories to capture heterogeneous abnormality evolution. At the patient-course scope, global image and report sequences are modeled to capture overall clinical progression beyond any individual abnormality. Structured trend supervision is extracted from longitudinal reports by an offline LLM parser, removing the need for manual temporal annotations. Combined with static image-report alignment, MedCTA learns representations that preserve visit-level cross-modal correspondence while encoding longitudinal change semantics. Experiments on temporal image classification, image-text retrieval, and zero-shot classification show consistent gains over strong medical vision-language baselines.

---


### 637. [Making LLMs Truly Forget: Deep Unlearning by Searching, Selecting, and Severing Knowledge Paths](https://arxiv.org/abs/2609.34442)

**<font color=#1a73e8>作者：</font>** Jialu Wang, Peizhi Niu, Haoteng Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While an unlearned language model may no longer recall a fact directly, the fact often remains recoverable through multi-hop reasoning over related knowledge. Most existing unlearning techniques overlook this vulnerability, targeting facts in isolation while leaving their supporting knowledge intact. To achieve true forgetting, we propose a general deep unlearning framework compatible with existing unlearning algorithms. Our approach adaptively explores both explicit responses and latent internal representations to discover valid reasoning paths, compiles them into a confidence-aware supporting subgraph, and we apply a graph minimum cut to sever all recovery paths while preserving unrelated knowledge. To rigorously evaluate deep unlearning, we introduce a model-specific pipeline that extracts and completes knowledge graphs from raw text, filtering them by calibrated model confidence to reflect what the model genuinely retains. Comprehensive experiments demonstrate that selectively unlearning supporting knowledge yields substantially deeper forgetting than superficial methods while preserving model utility, highlighting that genuine unlearning requires breaking the relational structures that enable factual reconstruction.

---


### 638. [Social Circuits behind Multi-agent Echo Chambers](https://arxiv.org/abs/2609.34444)

**<font color=#1a73e8>作者：</font>** Chuiyang Meng, Wenlu Yu, Ming Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents exchange messages to combine evidence, but their communication can also create echo chambers that reinforce shared errors. However, overall task performance does not explain how a message changes the receiving agent's internal activations and affects its decision. In this work, we introduce Social Circuits, a framework for tracing message effects through receiver activations. We compare the receiver's answers before and after changing a message. Then, we restore selected activations recorded under the original message to determine how much of the message effect these activations reproduce. Based on Social Circuits, we propose Circuit-Guided Deliberation (CGD), which learns to select useful messages using receiver activation changes. We establish when activation replacement preserves receiver decisions and bound the gap between CGD's task performance and the best achievable through message selection. Experiments show that receiver activation changes explain the message effects and guide message selection that improves the task performance. Across three models and four datasets, CGD achieves the highest or joint-highest average accuracy in our main comparisons while generating fewer tokens than multi-agent baselines.

---


### 639. [Unbiased Top-$k$ Estimation for On-Policy Distillation](https://arxiv.org/abs/2609.34447)

**<font color=#1a73e8>作者：</font>** Linjian Meng, Siyuan Gan, YuHan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is becoming an important component of large language model (LLM) post-training for transferring the reasoning capability of a strong teacher LLM to a weaker student LLM. OPD trains the student by minimizing the reverse KL divergence between the teacher and the student via rollouts generated by the student's policy. However, estimating the gradient of the reverse KL divergence in OPD remains a challenge. Using only the sampled token from the student-generated rollout is computationally cheap but provides limited distributional supervision, which will degrade accuracy. In addition, using the full vocabulary provides complete distributional supervision but is computationally expensive. Therefore, recent works propose Top-$k$ OPD (TK-OPD) that use selected top-$k$ tokens, which provides richer distributional supervision than sampled-token estimation at substantially lower computational cost than full-vocabulary estimation. Unfortunately, using only the selected top-$k$ tokens induces bias, leading to accuracy degradation, as the probability mass outside the selected top-$k$ tokens is discarded. To address the bias of TK-OPD, we propose Tail-Corrected Top-$k$ On-Policy Distillation (TT-OPD). It preserves the advantages of TK-OPD, including rich distributional supervision and low computational cost, while providing an unbiased estimator of the gradient of the reverse KL divergence. The key insight of TT-OPD is to use not only the selected top-$k$ tokens, but also the sampled token from the student-generated rollout, thereby recovering the discarded probability mass in expectation, avoiding the bias. Experimental results demonstrate that TT-OPD significantly outperforms other tested OPD variants.

---


### 640. [CORTEX: Learning to Share and Specialize in Dense Language Models](https://arxiv.org/abs/2609.34449)

**<font color=#1a73e8>作者：</font>** Chuiyang Meng, Ming Tang, Vincent W.S. Wong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are trained on heterogeneous data mixtures, where different knowledge domains require both shared knowledge and specialization. Existing modular approaches typically impose explicit components or discover modules through interpretability analysis after training. In this work, we propose CORTEX, a learning dynamics-inspired framework that learns internal modularization within dense language models. CORTEX partitions trainable matrices into parameter groups and learns module assignments from domain-conditioned gradient and cross-domain gradient similarity. We introduce the selective lesion score and module-domain mutual information to characterize the target-domain lesion effects and alignment, and analyze how module assignment affects the trade-off between assignment bias and update magnitude. Experiments with 160M, Qwen3-8B, and Qwen3-32B backbone models show that CORTEX achieves the highest synthetic-domain exact match and largest average perplexity reduction, while remaining competitive on real-domain evaluations and forming identifiable modules.

---


### 641. [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](https://arxiv.org/abs/2609.34450)

**<font color=#1a73e8>作者：</font>** Liang He, Sheng Wu, Haomiao Hao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly evaluated on cybersecurity tasks such as vulnerability reproduction, exploitation, and patching. However, existing cybersecurity benchmarks predominantly operate under a post-environment evaluation paradigm, i.e., handing the agent source code, a container, or an executable binary. This setup bypasses the critical environment reconstruction step, leaving a fundamental question for real-world vulnerability analysis: can an agent autonomously reconstruct the required execution environment and reproduce a vulnerability entirely from scratch?
To address this gap, we present ReproBench, an evidence-grounded benchmark designed to evaluate agent capabilities in end-to-end vulnerability reproduction starting from solely a CVE identifier. ReproBench decomposes the full reproduction workflow into six distinct phases, and assesses performance on each phase independently using verifiable experimental artifacts: downloaded firmware images, unpacked binaries, granular analysis logs, and validated crash samples, among others. We instantiate ReproBench with 30 real-world IoT firmware vulnerabilities, which serve as ideal test cases for our from-scratch evaluation setting.
Our evaluation demonstrates that 45.3% of test runs resort to vulnerability simulation - a prevalent remediation workaround adopted across all evaluated LLM agents - while only 5.3% of CVE-model pairs achieve successful reproduction of real-world vulnerabilities. Despite the low overall success rate, these non-trivial successful cases confirm that state-of-the-art LLM agents already possess the capacity for fully autonomous end-to-end vulnerability reproduction. Concurrently, our in-depth analysis of failed cases identifies core bottlenecks impeding LLM agents throughout the reproduction pipeline, offering actionable insights for subsequent research.

---


### 642. [When Words Fall Short: Iterative Synergy Between Verbalized Reasoning and Hidden Features for LLM Confidence Estimation](https://arxiv.org/abs/2609.34454)

**<font color=#1a73e8>作者：</font>** Yekun Xu, Ante Wang, Jingyi Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Confidence estimation is crucial for developing trustworthy large language models (LLMs), with most methods following estimator-based or verbalization-based paradigms. While recent research increasingly focuses on improving verbalized self-reports of confidence, we challenge the prevailing view that this approach surpasses independent confidence estimators. Our empirical study shows that a dedicated confidence estimator can substantially outperform verbalized confidence, indicating that LLMs' internal representations contain richer confidence signals. Building on this finding, we propose Iterative Policy-Estimator Training (IPoET), a framework that synergizes the complementary strengths of verbalized reasoning traces and informative representations. IPoET alternates policy optimization with estimator updating, integrating estimator-derived confidence feedback into policy learning and refreshing the estimator on new policy rollouts. Experiments across diverse datasets and Qwen and Llama backbones demonstrate that, by iteratively exploiting richer hidden features and adapting to the evolving policy distribution, IPoET consistently outperforms both estimator- and verbalization-based baselines in-domain and achieves superior or comparable results across all out-of-domain metrics. For more details, refer to this https URL.

---


### 643. [RGDT-Bench: Benchmarking LLM Reasoning for Rule-Governed Decisions and Their Justifications](https://arxiv.org/abs/2609.34455)

**<font color=#1a73e8>作者：</font>** Jianpeng Zhao, Haihua Xu, Haoyang Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study reasoning in Rule-Governed Decision Tasks (RGDTs), where models apply external rules to case facts and justify decisions, as required in policy, contract, and compliance settings. Beyond the deductive capability emphasized by standard mathematical and logical reasoning tasks, RGDTs require interpreting rules and their applicability, assessing conditions from evidence, combining judgments under rules and exceptions, and providing checkable justifications. These demands motivate a benchmark assessing both decisions and their stated grounds. We introduce RGDT-Bench, providing 202.1K condition-level supervision slots across four task tracks and eight supported task-probe combinations that vary access to supporting information. Label-blind extraction and deterministic checks produce labels for warrant completeness: source-referenced coverage and consistency of stated decision grounds. The benchmark attributes failures to four process layers: rule use, condition, evidence, and aggregation, and checks the final outcome. Among evaluable correct responses, warrant incompleteness averages 40.2% across six evaluated LLMs and supported task-probe combinations. Such warrant incompleteness poses potential safety risks and remains difficult to detect: the best of seventeen existing evaluators reaches only 57.69% (random: 50%) task-averaged area under the receiver operating characteristic curve (AUROC). To address this difficulty, we train a simple reward model with warrant supervision. It achieves 69.24% task-averaged AUROC among correct answers, exceeding the matched outcome-supervised baseline by 10.37 pp (percentage points) and the best existing evaluator by 11.55 pp. Beyond completeness assessment, the model outperforms both outcome-supervised baselines across nearly all response-selection comparisons, supporting RGDT-Bench's warrant supervision for RGDT reasoning.

---


### 644. [ZonoGPT: Towards An Abstract Domain for Verifying Large GPT Models](https://arxiv.org/abs/2609.34457)

**<font color=#1a73e8>作者：</font>** Hai Duong, Thanh Le, ThanhVu Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models are widely used for reasoning, coding, and multimodal agentic tasks. To provide formal assurance of desirable behaviors, such as robustness, safety, and fairness, neural network verification techniques prove required properties and provide auditable guarantees before deployment. However, prior work remains limited to small or restricted Transformers, and maintaining precision across deep models remains challenging. In this work, we introduce ZonoGPT, an abstract domain for verifying large transformers that maintains a space complexity independent of network depth. ZonoGPT uses a structured zonotope and a generator reduction mechanism to efficiently preserve correlations. To maintain precision, it introduces block-specific fused transformations for Attention and LayerNorm that retain feature relations, along with an affine transform for GELU that preserves generator relations. These mechanisms enable \tool{} to be the first approach to verify standard architectures, scaling to official HuggingFace models up to GPT-2 Medium (24 blocks, 300M+ parameters) and successfully verifying 1,339 instances across text and vision tasks.

---


### 645. [When Does Structured Knowledge Help Neural Theorem Proving?](https://arxiv.org/abs/2609.34460)

**<font color=#1a73e8>作者：</font>** Sareh Nabi, Roland Vogl, Marzieh Nabi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does structured mathematical knowledge help LLMs prove theorems in Lean 4? If so, for which models, and does the answer vary by problem? Formal libraries such as Mathlib encode 285,000+ verified theorems with syntactic dependencies, but the semantic layer mathematicians rely on for discovery (analogies, generalizations, cross-domain bridges) remains implicit. We introduce MathAgent, which builds this layer as a knowledge graph, MathKG, and uses it to augment LLM theorem provers. MathKG connects 364 Mathlib theorems and definitions by 9,434 typed semantic edges inferred via LLM-based relation extraction anchored to verified Mathlib declarations. We run a controlled ablation across four augmentation modes (no context, knowledge-graph context, Mathlib retrieval, both) and five models: Qwen3-8B/32B, their Lean-specialized derivatives Goedel-Prover-V2-8B/32B, and Claude Sonnet 4.6, on miniF2F, plus PutnamBench and MathOlympiadBench for Sonnet. Three findings emerge. (i) Specialization dominates augmentation: Lean fine-tuning adds 33-38 percentage points of solve rate in every mode, and a specialized 8B model beats a $4\times$ larger general one by 29-35 points, while no augmentation mode improves solve rate by more than 3 points. (ii) Augmentation is capability-conditioned: knowledge-graph context helps small models but hurts large ones, with the specialized model gaining more relative to its general base at every scale. (iii) Yet the augmentation modes solve different problems: an oracle selecting the best mode per problem solves 6% to 58% more than the unaugmented prover, a complementarity effect that strengthens on harder problems (32% more on PutnamBench). These results motivate adaptive strategies that select augmentation by model capability and problem. Code, data, and artifacts are available at this https URL

---


### 646. [Alignment-Guided Flow Transformer for Efficient Vision-Language-Action Policy Learning](https://arxiv.org/abs/2609.34467)

**<font color=#1a73e8>作者：</font>** Shengchao Hu, Peng Wang, Qiyang Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language-Action (VLA) models point toward general-purpose robotic intelligence by unifying perception, instruction, and control. Despite impressive progress, existing VLA models often adapt poorly due to \emph{tri-modal misalignment} among vision, language, and action, which weakens action grounding and hurts generalization and fine-tuning efficiency. In this work, we present Alignment-Guided Flow Transformer (AGFT), a novel framework that explicitly enforces tri-modal alignment through a dedicated alignment loss, bridging the representational gap across modalities and enhancing task adaptation. While prior research has predominantly emphasized bi-modal vision--language alignment, we systematically formalize and study tri-modal alignment in VLA models, and provide both ablations and analysis to isolate its role in improving adaptation and robustness. To further accelerate deployment, we adopt a flow-matching objective, enabling substantially fewer inference steps than diffusion-based policies while maintaining accuracy. Theoretically, we establish a quantitative connection between the tri-modal alignment gap and the optimization tightness of flow matching; empirically, experiments on the extensive benchmark show that AGFT achieves superior success rates and lower inference latency compared to SOTA baselines, underscoring tri-modal alignment as a key ingredient for scaling robust VLA manipulation.

---


### 647. [Causal Routing for Unlearning](https://arxiv.org/abs/2609.34475)

**<font color=#1a73e8>作者：</font>** Bardh Prenkaj, Andrea D'Angelo, Davide Mottin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs cannot forget the way we delete a file. Strangely, we are asked to remove something that was never put anywhere in particular. What the model took from a piece of text is now smeared across billions of weights. Existing methods rewrite all of them to change one thing, and none of them say which part produced that change. To address this, we introduce Causal Routing for Unlearning (CRU) by asking where the concept is expressed in the model and suppressing only that part. One untrained forward pass over the forget set ranks neurons by how their activations vary. Then, small routing modules on those neurons gate and suppress only the concepts that need to be forgotten. In CRU, the base model is frozen, and any change in behavior is caused only by the gated neurons; hence, why the routing is causal. Due to our parameter efficiency (only ~0.01% as many parameters as the base model), unlearning a concept costs 14 GiB, whereas the baselines require 71 GiB. On TOFU, CRU is indistinguishable from the retained model (p > 0.05, KS test) and is never Pareto-dominated, whereas every compared baseline matches its forgetting on the larger-forget batches only by collapsing utility. On RWKU, it achieves an adversarial-probe recall of 0.052, compared to 0.250 for the strongest baseline, meaning the knowledge is gone, not merely harder to reach. Thus, deciding on the intervention at query time, rather than fixing it beforehand, is the axis along which we argue that unlearning should proceed.

---


### 648. [Learn Here, Move Less Elsewhere: Input-Conditioned Plasticity from Retained-Domain Activation Atlases](https://arxiv.org/abs/2609.34478)

**<font color=#1a73e8>作者：</font>** Jiangtao Lin, Bangyang Wei, Yihang Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task-specific fine-tuning can rewrite a language model's answers beyond the training task, complicating updates that must preserve existing behavior. We introduce ATLAS, which turns retained-domain representations into an input-dependent rule for task adaptation. An activation atlas supplies local reference centers and directional filters to a shared low-rank residual. Target supervision learns the residual, while retained geometry shapes its action throughout training and inference. On Qwen3-8B, ATLAS achieves lower mean retained-output Kullback-Leibler (KL) divergence than all seven published baselines at shared coding-performance requirements, with consistent advantages across multiple training seeds. Structural comparisons identify the contributions of retained reference states and directional conditioning, and answer-level analyses show fewer rewritten mathematical answers and more stable commonsense choices. Experiments spanning five backbones and two retained domains further demonstrate coding gains with reduced retained-output movement. With compact storage and modest decoding overhead, ATLAS provides a practical mechanism for acquiring specialized skills while maintaining continuity in existing responses.

---


### 649. [SentZero: An Enhanced Sentence-Centric Vision-Language Pretraining for Multi-Task Zero-Shot Chest X-Ray Analysis](https://arxiv.org/abs/2609.34479)

**<font color=#1a73e8>作者：</font>** Hangyul Yoon, Hyungyung Lee, Edward Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language (VL) pretraining using paired chest X-ray (CXR) images and radiology reports has shown strong potential for medical image understanding. However, existing methods often remain dependent on task-specific finetuning because radiology reports are lengthy, clinically dense, and difficult to align with simple zero-shot prompts. Recent sentence-level approaches partially address this limitation using clinical phrases extracted by large language models (LLMs), but they largely overlook the intrinsic characteristics of radiology discourse. In particular, limited positive-pair diversity constrains further gains, while clinically equivalent sentences frequently recur across patients, creating false negatives in contrastive learning. To address these issues, we propose SentZero, an enhanced sentence-centric VL pretraining framework for zero-shot, multi-task CXR analysis. SentZero introduces LLM-based abstract-level sentence structuring and mapping to expand positive-pair diversity, together with an additional loss term to mitigate false negatives. We further introduce sentence-conditioned residual modulation of visual embeddings, enabling visual features to adapt to the semantic characteristics of each input sentence. Across diverse downstream tasks and datasets, SentZero improves zero-shot generalization and outperforms prior multi-task zero-shot methods.

---


### 650. [PACER: Progressive Availability-Conditioned Evidence Routing for Radiology Report Generation under Incomplete Clinical Context](https://arxiv.org/abs/2609.34487)

**<font color=#1a73e8>作者：</font>** Yulong Chen, Yadong Liu, Haoyu Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation (RRG) increasingly incorporates heterogeneous clinical evidence, such as multi-view radiographs and previous reports, whose availability varies across examinations. However, accommodating different input combinations does not ensure effective evidence use: generated reports may still omit or inaccurately describe clinically relevant findings. To address this problem, we propose PACER, a Progressive Availability-Conditioned Evidence Routing framework for structured incomplete-context RRG that follows a Refine-Calibrate-Commit pipeline. It first refines observed visual representations through endpoint-preserving patchwise routing across frozen encoder depths, incorporating complementary cues while retaining the pretrained terminal representation. It then calibrates the language-model prefix according to the observed evidence and availability state, adapting the shared generator's conditioning as the available source set changes. Finally, it generates polarity-structured clinical commitments before the report in the same autoregressive trajectory, providing structured clinical context for subsequent generation. Experiments demonstrate state-of-the-art clinical efficacy across all four MIMIC-RG4 settings and strong MIMIC-CXR performance, while maintaining competitive language-generation quality.

---


> [!TIP]
> 当前位于：**601-650**（第 13/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
