# 🧠 大模型相关研究 | 2026年09月21日

> 本类共 **176** 篇论文：已确认 **162** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-176**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-176**

---

### 151. [What Parents Can See: Divergent Accounts of Youth AI Companion Use in Parenting and Teenager Subreddits](https://arxiv.org/abs/2609.20720)

**<font color=#1a73e8>作者：</font>** Thomas Berkane, Anne Bischops, Anika Mellacheruvu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Youth increasingly use AI companions, and parents are the primary mediators of that use. How effective that mediation can be depends on whether parents are aware of how adolescents actually use these systems and what risks and benefits such use carries; nevertheless, prior work has only studied these demographic groups in isolation, and existing taxonomies attend almost entirely to risk. We analyze 1,628 Reddit posts about youth AI companion use from parenting and teenager communities (2023--2026); develop a codebook covering modes of use, risks, benefits, and parental mediation; and apply it at corpus scale with an LLM. The two communities yield divergent accounts. Teenagers most often discuss receipt of emotional support from AI companions (31% of teenager posts vs. 19% of parenting posts), whereas parents most often discuss teenage use of AI companions for romantic and sexual interaction (36% vs. 25%). Teenagers are not unaware of other risks, however; indeed, attachment and dependence is the risk they raise most (19%), close to the parental rate (16%). Teenagers also describe benefits that risk-centered taxonomies do not capture and parents rarely mention, most notably emotional support (27% vs. 5%). We argue these differences track what a given kind of use makes visible to someone outside the conversation. Chatting with a companion for hours every night leaves a trace beyond the chat itself; sexting with a character stands out when a parent reads the log; venting about a fight with a friend does neither, since it looks like any other conversation. The first surfaces as dependence, the second as sexual content, and the third as emotional support, which is the one parents most often miss. Parental guidance and system design should attend to use cases that reach parents by neither route, emotional support foremost among them.

---


### 152. [Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models](https://arxiv.org/abs/2609.20722)

**<font color=#1a73e8>作者：</font>** Frank E. Bobe III, Gregory D. Vetaw, Darshan W. Bryner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and causal head-level attribution to autonomously discover optimal steering parameters. Across three scales (1B x 3, 2-3B x 2, and 7-9B x 4), our engine achieves 16.7 percentage-point improvement on spam at 1B (standard deviation 4.7; 39 runs), with gains increasing to 21 to 42 percentage points at 7-9B across four architectures. On SST-2 sentiment, it achieves a 13.1 percentage-point improvement with zero code changes. Mechanistic grounding enables automated discovery of intervention points that generalize across tasks and architectures. On sentiment, RepE without head masking fails to improve over baseline, while Deep Noir improves all models (p less than 0.01). We further show that steering creates a predictable prompt-injection attack surface whose vulnerability increases monotonically with steering magnitude. This finding is relevant to agent systems deploying steered classifiers.

---


### 153. [Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure](https://arxiv.org/abs/2609.20732)

**<font color=#1a73e8>作者：</font>** Zofia Smoleń  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic cell annotation improves chunking interpretability for spreadsheets in LLM-driven RAG systems, aiding answer generation through enriched context rather than improved retrieval accuracy. We propose a novel framework of splitting any spreadsheet into interpretable chunks using cell role annotation. Our framework beats the state of the art, yet it faces a hard ceiling. Spreadsheets are fundamentally two-dimensional unstructured data with continuous relationships and infinite potential cell roles. Because classification models are restricted to finite, pre-defined classes, they cannot perfectly capture this structural nuance, even with human-level annotation. We show that addressing the spreadsheet-to-LLM bottleneck requires moving beyond discrete cell classification. Instead, the field must develop dimensionality-reduction techniques to directly flatten 2D unstructured spreadsheets into 1D unstructured text. Text chunks would be easier for downstream RAG to interpret and generate from.

---


### 154. [On-Demand Attention: Language Models Know When to Recall](https://arxiv.org/abs/2609.20734)

**<font color=#1a73e8>作者：</font>** Haibo Feng, Ruiqi Liang, Hanyang Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning and agentic workloads increasingly demand efficient long-context inference. Yet full-attention decoding reads the growing history at every step, regardless of its benefit to the next prediction. We show that a pretrained model's decoding states already contain information predictive of this benefit, before the global read. Building on this finding, we introduce On-Demand Attention (ODA), a local-first decoding method that uses a lightweight recall head to selectively invoke global attention as its predicted benefit changes during generation. ODA trains only the recall head, leaving pretrained weights unchanged and the complete historical KV cache available for future recall. We further implement GPU-side conditional execution in vLLM, translating reduced global reads into practical decoding speedups over full attention at long context lengths. Experiments across Qwen and Gemma models, including hybrid-attention backbones, show that selective recall recovers most of the performance lost under local attention while substantially reducing global reads. These findings support long-context inference in which pretrained models guide their own access to the information they retain.

---


### 155. [Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation](https://arxiv.org/abs/2609.20744)

**<font color=#1a73e8>作者：</font>** Haocheng Xi, Yiming Xie, Hexu Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck. Linear attention offers an appealing alternative and has been widely adopted in recent large language models, but directly applying it to video models often fails to preserve the fine-grained interactions required for high-quality generation. We present Video DeltaNet (VDN), which combines local Softmax attention with bidirectional linear memory for long-range video context. Its linear branch introduces Video Delta Attention (VDA), which updates memory once per frame by jointly incorporating its spatial tokens. Separate output projections and learnable gates calibrate the two branches, while a staged teacher-alignment recipe progressively introduces the new pathway into pretrained models. We instantiate VDN on MiniMax H3, applying the hybrid to video-to-video interactions while retaining Softmax for interactions involving text or audio. With eight-step distillation and an optimized SGLang serving stack, VDN-H3 completes DiT denoising for a 14.3-second, 768p video in 6.70 seconds on eight NVIDIA B200 GPUs, corresponding to a 14.5x speedup over the 50-step dense H3 baseline on the same GPU count.

---


### 156. [dQwen3.5: Hybrid-Attention Diffusion Language Models](https://arxiv.org/abs/2609.20751)

**<font color=#1a73e8>作者：</font>** Anton Xue, Litu Rout, Aditya Akella 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting a pretrained autoregressive (AR) model is a cost-efficient route to a diffusion language model (DLM). While nearly all such adaptations start from a full-attention transformer, AR modeling has shifted toward hybrid architectures that interleave attention and RNN layers. This creates an obstacle for adaptation: unlike attention, RNNs are structurally causal and nontrivial to bidirectionalize. Despite this mismatch, we investigate whether such backbones can become effective DLMs by adapting Qwen3.5 at 0.8B, 2B, 4B, and 9B scales, yielding the dQwen3.5 family. We find that hybrid backbones can be efficient starting points for adaptation: against a full-attention control, the hybrid reaches a given training loss in about half the tokens. Across scales, dQwen3.5 resembles full-attention DLMs in any-order decoding behavior and performs strongly under parallel decoding.

---


### 157. [RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents](https://arxiv.org/abs/2609.20754)

**<font color=#1a73e8>作者：</font>** Mingxuan Zhang, Xiaowen Wang, Anupma Sharan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective troubleshooting agents in enterprise customer support depend on retrieving actionable guidance from similar historical cases, yet existing retrieval-augmented generation (RAG) systems treat support cases as static documents and overlook their multi-stage, stateful nature. We introduce RAFT (Retrieval-Augmented Framework for Troubleshooting Agents), a stateful RAG framework that abstracts each closed historical case into a directed chain of timeline entries and retrieves at the entry level, surfacing cases whose intermediate states match the active case and returning the parent-case trajectory anchored at the matched state; an optional case-level graph links cases through a configurable similarity representation. We evaluate this retrieval layer directly, which, unlike evaluating a full agent system, requires no production deployment. Because public multi-stage troubleshooting data is extremely rare, we pair a synthetic benchmark built from Microsoft Learn Windows Server documentation with real Apache Jira issues carrying human-created duplicate labels. RAFT improves Case Hit over vanilla RAG and GraphRAG baselines at every stage of case progress, with statistically significant gains over the strongest baseline; the Jira results provide directional evidence that the advantage transfers to real case histories. We release our benchmark, implementation, and the Apache Jira evaluation set.

---


### 158. [Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations](https://arxiv.org/abs/2609.20779)

**<font color=#1a73e8>作者：</font>** Sarah Wyer, Sue Black, Noura Al Moubayed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters prevalent in GPT-2 women-directed output disappear by GPT-4, while men-directed completions gain positive representational territory (caregiving, emotional range, ally identity) that women-directed completions do not. The pattern is most visible at GPT-5: Topic~5 (1,997~documents) frames breast cancer as a men's rights debate, while zero equivalent clusters appear in women-directed output. Three independent classifiers score this content as non-toxic. Sentiment scores invert at GPT-4: early models demean women; later models over-correct. Topic diversity in women-directed completions falls 36\% relative to men at the GPT-4 alignment boundary (W/M~$= 0.58$, from $0.91$ at GPT-2). REGARD representational harm disparity correlates with release date ($\rho = +0.55$, $p = .034$) while Detoxify does not ($\rho = -0.23$, $p = .42$): toxicity scores fall as representational harm grows. We formalise harm laundering as a three-criteria test and provide a three-stage detection protocol applicable to any generative model. Within the OpenAI GPT lineage, toxicity score reduction is not a sufficient proxy for harm reduction.

---


### 159. [RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2609.20784)

**<font color=#1a73e8>作者：</font>** Yan Yu, Zhengxi Lu, Yizhou Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn agents trained with reinforcement learning (RL) receive a single scalar reward per trajectory, which motivates self on-policy distillation (OPD) to supply dense token-level supervision from a self-teacher with privileged task skills, letting a skill-free student internalize them. This recipe, however, is undermined by two findings in agentic tasks: privileged information alone does not always make a teacher reliable, and the benefit of teacher supervision is stage-dependent. We therefore propose RetireOPD (Self-Retiring On-Policy Distillation), which first optimizes a decoupled, skill-conditioned teacher with environment rewards and then trains a skill-free student jointly with RL and OPD. Rather than following a predefined distillation schedule, RetireOPD adopts Adaptive Retirement: the student drops the teacher on its own once their discrepancy stops shrinking and it reaches a target fraction of the teacher's success rate, after which training proceeds with RL alone. Across Qwen2.5 models from 1.5B to 7B, RetireOPD improves ALFWorld success rate over RL baseline by 14.1% to 18.8% and WebShop accuracy by 11.8% to 19.0%, and surpasses its own skill-conditioned teacher in every setting.

---


### 160. [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804)

**<font color=#1a73e8>作者：</font>** Run-Ze Fan, Zihao Zhang, Simin Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluated on SWE-Bench Verified and Terminal-Bench 2.1, we evaluate 176 matched settings spanning five context-management strategies, four context-window budgets, and targeted ablations of planning and action space. We find that: (1) Context management becomes increasingly valuable as the context-window budget tightens, with most of its benefit coming from preventing context-overflow failures. (2) Staging rule-based elision before LLM-based summarization provides the strongest overall efficiency among the context-management strategies, whereas making elided content recoverable adds machinery that models rarely use and yields no accuracy gain. (3) Planning shifts from an accuracy scaffold for weaker models to a cost saver for stronger models, with little change in accuracy. (4) Predefined tools improve performance for models with weaker bash proficiency, whereas bash-capable models can operate effectively with a bash-only interface and achieve substantially lower cost, especially on command-line-centric tasks. Trajectory-level analysis explains these effects: context management extends execution trajectories without substantially altering agent behavior, planning changes where trajectories stop, and the action space changes the granularity at which code is written. These findings inform model- and budget-aware harness design and provide a modular framework for evaluating future harness components.

---


### 161. [Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807)

**<font color=#1a73e8>作者：</font>** Martin Marek, Max Ryabinin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) of large language models is notoriously sensitive to small differences between training and inference engines, often referred to as the training-inference mismatch (TIM). However, completely eliminating TIM is impractical, as it would come at a major cost to rollout efficiency. In this paper, we show that the instability of RL under TIM is primarily caused by drift: a persistent bias between training and inference engines that accumulates with every training step. We derive an additive "score centering" correction term that stabilizes RL under TIM by canceling drift. When training models from 0.6B to 30B parameters, score centering alone matches or outperforms methods based on importance sampling under quantization, with the gap growing as the mismatch becomes more severe. Because the correction is additive, score centering also composes with importance sampling -- their composition outperforms pure importance-sampling baselines in our staleness experiments.

---


### 162. [Paint-Anything: Unified Any-Color Control for Image Generation and Editing](https://arxiv.org/abs/2609.20816)

**<font color=#1a73e8>作者：</font>** Ji Xie, Dewei Zhou, Xinyu Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-prompt interface for generation and editing through object-level color supervision. We develop a data pipeline that constructs Paint-500K from real images through object grounding, perceptual color labeling, and editing-pair synthesis. Since shadows make real-image labels only approximate colors, we complement this supervision with pure-color anchors whose pixels exactly match their paired hex values. These anchors are used only at high-noise timesteps, leaving low-noise training to natural images. We further introduce Any Color Benchmark (ACBench), comprising ACBench-T2I and ACBench-Edit, to measure object-level hex color fidelity across both tasks. On FLUX.2-4B, Paint-Anything improves ACBench-T2I and ACBench-Edit scores by 85.3% and 28.3%, respectively, relative to the base model, with ablations supporting the training recipe. It also achieves the highest average CompColor score among the compared methods.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 163. [Advantage Scale Calibration Imbalance in Group-Relative Optimization under Low-Variance Rewards: Diagnosis and Bounded Recovery](https://arxiv.org/abs/2609.19164)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fei Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In verifier-style RLVR, group-relative optimization often treats advantage scale as an implementation detail. This paper separates two low-variance cases: sub-resolution jitter that should not become a preference signal, and credible but small cardinal gaps that should be learned without distorting KL calibration. We propose an advantage-scale three-way calibration interface: the same within-group scale denominator simultaneously determines the reward-branch strength, prompt-level batch weight, and the effective KL calibration induced when the reward branch is re-expressed on the original cardinal scale. This interface explains why RLOO / this http URL can let credible small gaps become KL dominated, whereas GRPO's standard-deviation denominator can amplify tiny gaps without bound. Based on this interface, we further introduce the Reward-Resolution Protocol and MaxNorm-AC, respectively filtering sub-resolution gaps and providing bounded cardinal recovery on credible nonzero gaps. Across dense / MoE architectures and math / code reasoning, MaxNorm-AC improves over the strongest robust-scale baseline while truncating the low-variance inverse-scale tail.

---


### 164. [Position: It is Time to Virtualize Foundation Models with a Self-evolving Operating System Layer](https://arxiv.org/abs/2609.19203)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Suparna Bhattacharya, Tarun Kumar, Cong Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI applications have shifted from single, monolithic foundation models (FM) to compound agentic systems. Yet today's stacks remain fragmented: even as protocols (e.g., MCP, A2A) ease tool/agent connectivity, each framework embeds an implicit runtime for state, memory, budgets, and guardrails, making behavior non-portable and governance brittle. It mirrors computing before operating systems, when every program re-implemented basic services. This position paper argues that the field now needs a Foundation Model Operating System (FMOS) -- a system layer that virtualizes FM interactions analogous to how virtual machines abstract physical hardware, giving applications the illusion of dedicated, trustworthy FM instances with effectively unbounded capabilities. Internally, the FMOS orchestrates knowledge across memory tiers, model selection and resource allocation, and verification and policy enforcement. Like the human brain switching between fast intuition and slow deliberation, the FMOS learns when to intervene and when to let inference proceed directly and continuously adapting its policies based on operational experience.

---


### 165. [Open ultrasound foundation model for robust segmentation and clinical measurement across heterogeneous settings](https://arxiv.org/abs/2609.19230)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chao Qin, Fahad Shahbaz Khan, Salman Khan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound is the most widely deployed imaging modality worldwide, yet clinical AI remains fragmented into narrow single-task models that fail when device, operator, or anatomy changes. Here we present SonoCorpus, an open resource unifying 456,963 images and 1,626,085 expert masks from 53 public datasets spanning 24 clinical applications and 17 countries, and SonoBase, an interactive segmentation foundation model pretrained on it. Across fifteen evaluation datasets introducing new organs, devices, operators, and geographies, SonoBase outperforms SAM2, MedSAM2, and the concept-promptable MedSAM3 on every dataset and matches per-dataset specialist models trained on the same data; on fully external data it exceeds the accuracy these baselines achieve on their own in-distribution benchmarks. Ejection fraction derived from its segmentations falls within inter-observer variability (6.63\% error), with fewer misclassifications at the defibrillator-candidacy threshold than either promptable baseline (13\% versus 18--42\%); fetal head-circumference (1.81~mm) and gestational-age (1.2 days) errors fall below inter-observer variability. Where a baseline fails outright, one in four test cases, SonoBase recovers a usable segmentation in 81\% of them, including on handheld probes operated by minimally trained users in two low- and middle-income countries (Sierra Leone and Tanzania). Five labeled examples can help the model adapt to a new setting, and the identical training protocol transfers well to newer models such as SAM3, locating the advantage in ultrasound-specific pretraining rather than any single architecture. To ensure reproducibility and enable the community to build on SonoBase as a platform, we release all checkpoints, optimizer states, data-split indices, deduplication hashes, and starter code.

---


### 166. [Towards Active Cross-View Object Geo-Localization](https://arxiv.org/abs/2609.19662)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shunyu Yao, Xiaohan Zhang, Zhuoran Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view object geo-localization (CVOGL) typically assumes a fixed query image, overlooking the ability of mobile agents to actively acquire more informative observations. To address this limitation, we introduce Active Cross-View Object Geo-Localization (ActiveGeo), where an agent sequentially selects new viewpoints and determines when to stop, aiming to improve localization with minimal observations. We further propose ActiveMoPT, an ActiveGeo framework with three-stage training. First, Multi-View Prompt-Preserving Adaptation enables the model to aggregate multiple query views while reusing the initial prompt. Second, Trajectory-Guided Policy Initialization uses supervised agent trajectories to learn viewpoint selection and initial stopping behavior. Third, Cost-Aware Policy Refinement employs GRPO with a gain-cost reward to jointly optimize localization accuracy and observation efficiency. We also construct ActiveGeo-858, a zero-shot test set containing 858 scenes and 1,716 target annotations. Experiments show that ActiveMoPT achieves state-of-the-art performance on MoP-UAV using only 1.45 query views on average, and substantially outperforms previous CVOGL approaches under zero-shot evaluation on ActiveGeo-858.

---


### 167. [Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation](https://arxiv.org/abs/2609.19729)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tri Cao, Hung Nguyen, Phong Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video generation degrades over long horizons due to an overlooked train-inference discrepancy we term KV eviction mismatch: models train on short clips where all context frames reside in the KV cache, but at inference, memory constraints force distant frames to be evicted from the KV cache - removing context the model was conditioned on. Rather than simulating eviction via context truncation - which discards temporal information the model still needs and degrades motion coherence - we keep the context but while progressively reducing the influence of distant frames, making their eventual eviction negligible. To guide this design, we introduce the positional response $R( \Delta, \, t_{\text{denoise}})$, a perturbation-based sensitivity measure revealing that context influence decays steeply with temporal distance and varies systematically across denoising steps. Motivated by this analysis, we propose Recency Forcing, which applies a non-positive, timestep-dependent bias, termed Temporal Response Bias (TRB), on pre-softmax attention logits derived directly from $R$, closing the train-inference gap without modifying context length or training objectives. We further introduce Biased Attention Reparameterization (BAR), an exact reformulation that moves the bias outside the softmax, making TRB a standard FlashAttention call at zero overhead. Recency Forcing operates in both training-free mode and training-based mode. Experiments on VBench and VBench-Long demonstrate state-of-the-art long-horizon generation quality at no additional inference cost.

---


### 168. [OceanMoE: Structured Conditional Sparse Computation for Long-Horizon Multivariate Ocean Forecasting](https://arxiv.org/abs/2609.19768)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yishun Zhu, Jian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate ocean forecasting must exploit shared evolution in a coupled ocean system while adapting to the heterogeneous statistical and dynamical characteristics of different prediction variables and locations. Fully shared models may lack the flexibility to handle this heterogeneity, whereas fully independent models discard the common ocean context shared across variables. The key question is how to retain shared context in a unified model while allowing computation to specialize according to the prediction target and local state. We propose OceanMoE, a structured conditional sparse Mixture-of-Experts framework that combines sharing and specialization for multivariate ocean forecasting. OceanMoE fuses cross-variable information to construct target-specific local representations and uses them to perform content-conditioned sparse routing at each spatial location, with the number of active experts adapted to router confidence. In the decoder, routing is augmented with a learned geographic bias parameterized by spherical-harmonic spatial bases, while shared residual and seasonal pathways provide common cross-variable and month-dependent context. Experiments on long-horizon autoregressive ORAS5 forecasting show that OceanMoE lowers aggregate forecasting error in both evaluated settings and maintains lower geometric-mean normalized RMSE than the corresponding baselines over most later rollout months. Routing analyses further show that expert allocation varies with prediction targets and spatial locations. These results support structured conditional computation as a modeling strategy for balancing shared ocean context with adaptive specialization.

---


### 169. [Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy](https://arxiv.org/abs/2609.19820)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Luis Leal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Regularized self-play -- the family behind DeepNash's Stratego play -- drives a two-player zero-sum policy to a Nash equilibrium by best-responding to a slowly moving, entropy-regularized reference policy $\rho$. When the game has a polytope of value-equivalent equilibria, the regularizer silently breaks the tie: with a uniform reference it selects the maximum-entropy member, the I-projection of $\rho$ onto the Nash set. Can the reference be used to choose the equilibrium on purpose? On five exactly solvable games plus a 2-D polytope, with exact best responses and equivalence tests over independent seeds, anchoring the reference at a target member and refining steers self-play to that member with mean coordinate error 0.007 at median exploitability $5\times10^{-5}$, TOST-equivalent to the request within $\pm0.05$; the anchoring persists through refinement and follows the reference, not the initialization. Selection follows the reach-weighted I-projection (slope 0.969 [0.950, 0.987]). We report with equal emphasis where the story breaks: fixed off-manifold references cost 0.08-0.25 exploitability; stiff or flat families require a smaller mirror step, set by a pre-registered rule; boundary targets undershoot; curvature predicts where boundary saturation bites (rank correlation 0.90, p=0.037) while interior precision is curvature-independent. Table and MLP steering maps are equivalent within $\pm0.03$ at every target (30 seeds); matched control arms show attention's robust signature is excess seed variance, any systematic shift bounded at 0.018 and not significant. Against a best response the selection-robustness trade-off is degenerate: steering matters only against fixed, non-equilibrium opponents. The recipe -- anchor the reference at the desired member and refine -- reinterprets the KL anchor of RLHF-style RL as a selection knob, not only a stability leash.

---


### 170. [TRACE: Accountable Agentic Retrieval for Source Discovery in Digital Archives](https://arxiv.org/abs/2609.19897)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Donghan Bian, Marie Puren, Florian Cafiero  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Historical archives pose a difficult retrieval problem for retrievalaugmented generation systems: documents are OCR-degraded, heterogeneous across genres and sources, and require strong source traceability for scholarly and institutional use. We introduce TRACE, a training-free agentic retrieval framework designed for accountable source discovery over historical corpora. The system was developed in the context of DECIDON, an interdisciplinary project on the circulation of political discourse between parliamentary debates and the press during the French Third Republic, involving digitised historical collections and institutional use cases. The prototype is currently deployed internally within the project and accessible to 24 researchers across six partner institutions. We evaluate TRACE on HistoriQA-ThirdRepublic, a benchmark of 1,752 French historical questions over parliamentary debates and newspapers from 1887, with documents derived from Biblioth{è}que nationale de France digitised collections. TRACE achieves R@10 = 0.856 and MRR = 0.653, outperforming sparse, dense, graph-based, and agentic RAG baselines, with the largest gains on multi-hop and cross-corpus questions. At approximately $0.02 per question under the default hosted inference configuration, TRACE also remains economically feasible for heritage institutions, laboratories or companies that cannot rely on costly local GPU infrastructure. These results suggest that, for large digital libraries and archives, retrieval accountability and corpus-aware agent design can provide a practical alternative to heavier training-based or graph-construction approaches.

---


### 171. [FreqDINO++: A Frequency-Guided Multi-Task Routing Vision Foundation Model for Universal Ultrasound Analysis](https://arxiv.org/abs/2609.20340)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qing Xu, Yixuan Zhang, Yue Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound image analysis plays a crucial role in cancer screening and prenatal diagnosis, yet comprehensive assessment requires jointly addressing tasks such as lesion segmentation and benign-malignant classification. While recent vision foundation models have shown remarkable universal representations, unlocking their potential for ultrasound is bottlenecked by the considerable domain gap from natural images. Existing methods typically fine-tune heavy vision encoders for isolated tasks, incurring substantial computational overhead while overlooking the underlying commonalities across heterogeneous tasks. In this work, we propose FreqDINO++, a frequency-guided multi-task routing vision foundation model for universal ultrasound analysis. We first introduce a Multi-task Routing Adapter (MR-Adapter) to support parameter-efficient integration of task-common and task-specific knowledge, a Frequency-aware Feature Enhancer (F$^2$-Enhancer) is then designed to capture the rich multi-scale frequency characteristics of ultrasound images, and a Task-aligned Collaborative Decoder (TC-Decoder) is devised to promote collaboration between dense and global prediction tasks through global-local token interaction. Extensive experiments on large-scale multi-task and external single-task ultrasound benchmarks demonstrate that FreqDINO++ consistently outperforms strong baselines and recent foundation models across 27 diverse clinical task scenarios, while also showing promising generalization to unseen data. The code is at this https URL.

---


### 172. [SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models](https://arxiv.org/abs/2609.20419)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaodong He, Xincheng Wang, Zhao Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models (GFMs) aim to learn transferable representations across severely heterogeneous graph domains. However, severe domain shifts in topology, graph scale, and feature semantics impede the construction of a unified, domain-agnostic representation space. To address this, we propose SCGFM-ART, a structure-centric GFM framework that aligns arbitrary graphs onto a shared relational atlas via Amortized Relational Transport (ART). The relational atlas serves as a universal coordinate system defined by a finite set of relational landmarks (bases), while ART directly predicts reusable, end-to-end graph-to-base transport plans, bypassing costly runtime Gromov-Wasserstein optimizations. Under this formulation, SCGFM-ART decomposes a graph into a unified representation: globally via its relational response coordinates relative to the atlas, and locally via its node-to-role structural correspondences. These correspondences project disparate node attributes into a canonical role space, resolving structural and semantic heterogeneity within a singular alignment interface. Rigorously modeling graphs and atlas bases as finite measured relational spaces, we establish coordinate fidelity bounds, prove stability under predicted transport plans, and derive an amortized coverage bound that guarantees our learning objective tightly surrogates ideal relational coverage. Benchmarked across 14 cross-domain graph- and node-level classification tasks, SCGFM-ART achieves state-of-the-art transferability, securing superior average ranks of 2.29 and 1.14, respectively. Topological perturbation analyses demonstrate that node-role transport retains fine-grained structural nuances beyond global coordinates. On real-world benchmarks, the amortized formulation yields 44.2 to 85.1 times faster frozen target-domain inference by avoiding iterative alignment at test time.

---


### 173. [Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation](https://arxiv.org/abs/2609.20441)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fabian Schmalstieg, Karsten Mueller, Wojciech Samek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware. We distill a 300-million-parameter Prithvi-EO-2.0 teacher, fine-tuned on the 252 manually labeled Sen1Floods11 training scenes, into a 0.7-million-parameter EfficientViT-B0 student. The teacher supervises additional unlabeled Sentinel-2 imagery, allowing the student training set to grow without new manual annotations. At the matched budget of 252 scenes, teacher-supervised training is competitive with direct training and improves STURM-Flood performance across tested configurations; a geometry-matched control shows that label source alone does not explain the difference. Scaling the teacher-supervised pool to 2,500 scenes narrows the remaining student--teacher gap: the float student reaches 0.787 water intersection over union on the Sen1Floods11 test split against 0.822 for the teacher, matches the teacher on STURM-Flood under our evaluation protocol, and remains below it on WorldFloods-v2. After activation replacement and quantization-aware training, the student runs as a 1.5-megabyte 8-bit integer (INT8) TensorRT engine on a Jetson Xavier NX at 5.57 milliseconds of graphics processing unit (GPU) compute per 512-by-512 image, with approximately 14 megabytes of runtime device memory. A fixed modified normalized difference water index (MNDWI) threshold is competitive with both models on the two clean external benchmarks, so we interpret those benchmarks as generalization tests rather than as evidence of learned-model superiority over a spectral rule. The results support the conclusion: foundation-model supervision can amplify a fixed manual annotation budget into a substantially larger training set and yield a compact, deployable edge model.

---


### 174. [FreqCondNorm: Towards Cross-domain Predictive Maintenance through a Frequency-Conditioned Transformer Foundation Model](https://arxiv.org/abs/2609.20535)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zaynab Raounak, Camille LHermine, Zhiguo Zeng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning predictive maintenance models suffer from poor transferability across machines and operating conditions, especially when labelled data are scarce and signals span five orders of magnitude in sampling frequency (1 Hz to ~100 kHz). We propose FreqCondNorm, a Transformer-based architecture that introduces a FiLM-style frequency-conditioned normalization layer to unify heterogeneous time-series within a single model. The architecture is pretrained on five public predictive maintenance datasets (CWRU, MFPT, UOC18, PRONOSTIA, CMAPSS) using masked auto-encoding and contrastive learning with balanced domain sampling. On fault diagnosis, the model achieves 99.2% accuracy on CWRU (+6.4 pp over CNN) and 82.1% zero-shot accuracy on MFPT, demonstrating strong transfer across sampling frequencies. However, the approach does not improve remaining useful life prediction, suggesting a mismatch between pretraining and RUL objectives that warrants future investigation.

---


### 175. [UniPolicy: Unified Objective-Specific Policies for Generative Search Advertising](https://arxiv.org/abs/2609.20630)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kun Yao, Yuhang Zhou, Yichi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search advertising connects user intent with commercial content and plays a critical role in platform monetization. Recent systems typically align pretrained generative models with a single business reward, such as eCPM, or use naive reward fusion for preliminary multi-objective alignment. However, an ideal search advertising system must jointly account for heterogeneous objectives, including relevance, click propensity, and commercial value, to balance user experience and business value while mitigating globally suboptimal performance caused by gradient competition. We propose UniPolicy, an objective-aware multi-policy alignment framework. UniPolicy combines objective-specific prefix tokens, sparse MoE-LoRA routing, and objective-specific residual FFNs to hierarchically decouple parameters within a shared backbone, providing differentiated parameter and policy-expression spaces for different business objectives. It further constructs pairwise preferences from multi-stage behavioral feedback, supplementing the relative preference information in exposed-but-unclicked samples and strengthening the relative advantage of clicked candidates in the generation distribution. At inference, UniPolicy supports parallel, business-customizable multi-policy beam search, flexibly allocating candidate quotas across objectives under a fixed retrieval budget. Large-scale offline experiments show that UniPolicy delivers balanced improvements across multiple metrics while preserving retrieval quality, outperforming single-objective reinforcement learning and naive reward-fusion baselines. In a 7-day online A/B test on a real search advertising system, UniPolicy improves CTR by 0.71%, RPS by 1.58%, and advertising revenue by 1.32%, while maintaining stable serving latency.

---


### 176. [Can 4D Foundation Models Remember?](https://arxiv.org/abs/2609.20819)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceiving and remembering the visual world is fundamental to navigating and interacting with our environment. Current 4D foundation models, such as camera-controllable video models or 4D reconstruction models, can perceive and reconstruct dynamic environments, but how well they remember what they have perceived remains an open question. Existing benchmarks largely rely on pixel-level metrics and lack ground truth for objects once they leave the field of view, making them unable to evaluate visual memory in an object-centric manner against references. To fill this gap, we introduce PersistBench, a dataset and metric suite that leverages 360° videos as omniscient ground truth and proposes three evaluation aspects: object permanence, motion continuity, and appearance preservation. Evaluating various models across diverse categories reveals that current models can only maintain short-term consistency that degrades significantly once objects leave the field of view. Our findings highlight the gap between current model capabilities and robust visual memory ("seeing is not remembering"), providing guidance for future development of 4D foundation models. Dataset and code are available on the project page: this https URL.

---


> [!TIP]
> 当前位于：**151-176**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-176**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
