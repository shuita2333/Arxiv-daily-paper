# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**751-800**（第 16/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-810](./part-17.md)

---

### 751. [PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts](https://arxiv.org/abs/2610.18857)

**<font color=#1a73e8>作者：</font>** Ruixiao Dong, Jianmin Bao, Bozhi Luan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion models provide an appealing alternative to latent-space diffusion models by directly modeling raw images without relying on a learned tokenizer. However, scaling pixel-space models has predominantly followed dense strategies, tightly coupling model capacity with active computation. In this work, we show that standard LLM-style Mixture-of-Experts (MoE) architectures can be effectively transferred to pixel-space diffusion. Building on this finding, we introduce PixelMoE, a pixel-space generative framework that sparsely scales model capacity with standard LLM-style MoE, without diffusion-specific routing mechanisms or auxiliary routing objectives. Specifically, PixelMoE combines standard Token-Choice (TC) routing with fine-grained routed experts for input-adaptive sparse computation, a shared expert for capturing common representations, and a bias-based load-balancing strategy. To complement sparse capacity scaling, PixelMoE further introduces Pixel-Space Hierarchical Flow Matching, which varies spatial resolution along the denoising trajectory from global structure formation to fine-grained detail refinement. At comparable active parameter counts, PixelMoE consistently outperforms its dense counterparts across model scales, demonstrating effective sparse capacity scaling in pixel space. On class-conditional ImageNet-1K, PixelMoE achieves FID scores of 1.47 at 256x256 and 1.53 at 512x512 without representation alignment or perceptual losses, comparing favorably with leading pixel-space and latent-space generative models. Code and models will be released soon.

---


### 752. [Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs](https://arxiv.org/abs/2610.18858)

**<font color=#1a73e8>作者：</font>** Aimon Rahman, Joymallya Chakraborty, Vidit Bansal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have advanced rapidly, but most remain optimized for single-image inputs. Multi-image reasoning is costly because each image adds many visual tokens, increasing encoding and attention demands. Existing techniques that address the above issue, including visual token pruning, token merging, visual token compression, learned resampling, hierarchical compression, retrieval-augmented visual reasoning, and memory-based architectures, have largely been designed for single-image scenarios, where redundancy is primarily spatial and local. Multi-image reasoning introduces additional challenges: redundancy may occur across images, task-relevant evidence may be sparse or distributed, and aggressive per-image compression can remove details needed for comparison, counting, temporal reasoning, retrieval, or evidence grounding. Moreover, existing token-reduction methods are often either (i) training-free but inference-inefficient, typically relying on accessing attention matrices to get token-importance that may be impractical to access with memory-efficient attention implementations such as FlashAttention, or (ii) training-dependent, requiring the base MLLM to be retrained or adapted to a new compressed-token paradigm. In this work, we study scalable multi-image reasoning and understanding without retraining the base model and without accessing attention matrices at inference time. To this end, we propose mmVB, a lightweight plug-and-play module that assigns query-conditioned per-image token budgets via cross-image context, adding only 1.6M trainable parameters while reducing visual input tokens by 9x. This reduction yields 5x faster time-to-first-token and 7x fewer prefill FLOPs, while maintaining 94.4% of full-resolution accuracy across eight multi-image reasoning benchmarks.

---


### 753. [AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards](https://arxiv.org/abs/2610.18860)

**<font color=#1a73e8>作者：</font>** Xin Gao, Yifan Yang, Xin Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and aesthetic quality. Image generators excel at visual design but can misrender requested content, making their outputs unreliable targets for direct reproduction. We therefore introduce AesCode, which generates code grounded in the content prompt while using an image generated from the same prompt as an aesthetic guidance. To do so, AesCode represents the target as a design graph that describes the whole canvas and makes each property attributable. From this graph, we derive complementary cross-modal rewards: deterministic verifiers score properties parsable from code and rendering, while a VLM judge assesses the non-parsable ones with a sample-specific Visual Graph Rubric (VGR) tied to graph elements and relations. We optimize these decoupled rewards through reinforcement learning with per-channel normalization to jointly improve spatial planning, aesthetic quality, and verifiable correctness. To evaluate this setting, we build a benchmark that scores verifiable correctness and visual quality separately, with visual scores highly consistent with human judgments. We find that reference images substantially improve the visual quality of code generated by existing models, and ablations show that AesCode benefits from references both as model input and as a source of visual rewards. Relative to same-scale Qwen3-VL baselines given the same references, AesCode-8B and AesCode-32B improve visual quality by 31.1 and 22.4 percentage points, reaching scores comparable to those of closed-source frontier models such as GPT-5.5 and Claude Opus 4.8.

---


### 754. [Hybrid Reasoning Agents](https://arxiv.org/abs/2610.18861)

**<font color=#1a73e8>作者：</font>** Jiaru Zou, Yunzhe Qi, Sirui Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturally, a lightweight HybridLink enables seamless transitions between text and latent modes, while the agent's continuous working memory preserves lossless hybrid context across multiple turns. These designs preserve tool-integrated agentic capabilities while making latent thoughts directly inspectable. Building on this architecture, we further develop dedicated post-training algorithms for hybrid reasoning: HybridSFT stabilizes tool-integrated hybrid generation by teaching the backbone to coordinate with HybridLink, then HybridRL scales reasoning by learning when to think in latent space and when to act through text. We evaluate HybridAgent at 3 model scales across 11 benchmarks covering mathematics, science, medicine, search, and agentic reasoning. Compared with frontier LLM Agents and agentic frameworks spanning both text-based and latent methods, HybridAgent consistently improves performance by 10.4%, while delivering 35.5%-54.7% token reduction, 1.8x-2.6x faster inference, and 2.7x-3.7x cost savings. Code and data are available at this https URL.

---


### 755. [DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](https://arxiv.org/abs/2610.18862)

**<font color=#1a73e8>作者：</font>** Minghao Luo, Liang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heuristics such as stopping early or banning words like "wait", which can reduce accuracy. We propose DoubtLess, a training-free decoding method in which a much smaller reasoning model steers the large one towards brevity. The small model reads the large model's CoT so far twice, once prompted to be brief (the brief thinker) and once prompted to be verbose (the verbose thinker), and the difference between its two logit vectors, scaled by a strength, is added to the large model's logits at every step of the CoT. On seven benchmarks of competition mathematics, graduate-level science and competitive programming, DoubtLess shortens the CoT of Qwen3-32B by 31% with unchanged accuracy, outperforming five inference-time baselines. We also show that DoubtLess reduces thinking tokens per turn by 20% in a self-debugging coding agent with unchanged task performance. It also generalizes to two other model families with unchanged accuracy. When combined with training-based compression, it further shortens the CoT of a model already trained for brevity. Ablations and behavioral analysis show that DoubtLess reduces repeated checking, with most token savings coming after the correct answer first appears in the CoT. Our code is available at this https URL.

---


### 756. [PLAYGROUND: Progressive Layout Generation with Render-Grounded Planning](https://arxiv.org/abs/2610.18865)

**<font color=#1a73e8>作者：</font>** Jaeho Lee, Junhwan Heo, Junghyun Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating editable graphic designs requires arranging visual and textual elements into a coherent composition while preserving their content and editability. Although recent MLLM-based approaches employ iterative generation and visual refinement to reflect the real-world design workflows, their high-level plans are predetermined prior to execution, limiting their adaptability as the design evolves. To address this limitation, we propose PlayGround, a progressive layout generation framework that dynamically adapts to the current rendered canvas. PlayGround establishes a progressive design loop comprising a Progressive Planner, a Layout Generator, and a Visual Verifier, guided by a Structure-Aware Retriever. Given an initial set of unordered elements, the Structure-Aware Retriever initially infers a coarse layout structure to retrieve structurally similar reference designs. Subsequently, at each turn, the Progressive Planner examines the current rendered canvas alongside the remaining elements, forms the next functional group, and plans its composition. The Layout Generator then predicts editable layout attributes, while the Visual Verifier evaluates rendered candidates and provides feedback when refinement is necessary. To train the Progressive Planner with step-wise supervision, we construct a two-stage data generation pipeline that extracts functional groups and turn-level planning trajectories from completed designs. Experiments on Crello and LICA demonstrate the effectiveness of PlayGround over existing methods. Our code and weights will be publicly released.

---


### 757. [Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868)

**<font color=#1a73e8>作者：</font>** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce Tev-Gym, the first long-horizon agent training dataset with verifiable, dense, progressive rewards -- 1,170 verified task environments across 7 domains. It is built on a latent-world-first approach that first constructs a latent world: a complete and correct hidden specification of the task domain, workflow, and expected state after each step. Each task is then progressively rendered from this specification into an agent-facing environment, enabling controllable complexity and a natural progress metric. Second, we turn this metric into a training recipe: via progress-potential reward shaping (PPRS), we convert progress into a dense per-step reward that improves training efficiency and makes otherwise-intractable tasks trainable. Training with this recipe yields Tev-27B, which achieves substantial gains on the Agents' Last Exam computing and math sciences domains (ALE-CM), matching GPT-6 Astra and Claude Opus 5 at Pass@5. Despite training only on ALE-related data, it generalizes to the Terminal-Bench (TB) 3.0 and 4.0 subsets, surpassing GLM 5.2 and Gemini 3.7 Flash, and reaches Claude Opus 4.8-level performance on middle-horizon tasks such as TB 2.1.

---


### 758. [Dog-Breed Text-to-image Flow Matching from Pretraining to Fine-Tuning on 4 Consumer GPUs](https://arxiv.org/abs/2610.18870)

**<font color=#1a73e8>作者：</font>** Reyhaneh Esmailizadeh, Xingjian Leng, Zhanhao Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We generally perceive that training text-to-image diffusion models requires heavy compute: it is true if we aim at a comprehensive frontier model. This understanding prevents people from training their own models when getting started in the field. We develop MiniDog, a framework that enables pretraining diffusion transformers in 55 minutes and fine-tuning in another 15 minutes on four 3090 GPUs. For data, we use 26k dog images from ImageNet and caption them for pretraining and use 2k images generated by FLUX.1-schnell for fine-tuning. We precompute the image and text features and cache them for efficiency. For architecture, we use E2E-INVAE for its semantic latent space, a small transformer with 22M parameters, a small Qwen model for text encoding, and in-context conditioning. For training, we use iREPA and an EUPE perception encoder for acceleration. For evaluation, our repository supports FID, HPSv2 score, PickScore, and various VAE reconstruction metrics.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 759. [Splicing Hints into Reasoning Traces: Learning from Demonstrator Failures](https://arxiv.org/abs/2610.13996)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hamed Mahdavi, Pouria Mahdavinia, Majid Farhadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards improves mathematical reasoning when a final answer can be checked, but a correct answer does not certify the derivation behind it, and proof problems offer no answer to check. Replacing the check with a reasoning model as an in-loop verifier faces a fundamental obstacle: the policy must already produce occasional correct attempts for any reward to exist, which it may never do at olympiad level. We instead move verification and repair out of the training loop and into offline data generation with SPLICE, a workflow in which a second model, given only a reference solution, edits a reasoning model's traces as they are generated: it verifies progress, truncates a failed trace at its last verified step, and splices in an adaptively strengthened hint until progress resumes. The resulting dataset includes repaired examples whose sampled unaided trajectory failed, with failed continuations removed and progress repeatedly checked against the reference solution. A model finetuned on SPLICE traces outperforms the same model distilled from the reasoning model's unedited traces on AIME and, under a grading protocol validated against human grades, on olympiad proofs. The trained model's own traces show a corresponding behavioral signature: at difficult points it announces a branch in the style of the spliced hints and takes riskier steps, with predictive entropy rising there and just after, a pattern absent from the model trained on unedited traces.

---


### 760. [ANASSA: From High-Level Framework to Low-Level Architecture for Spatial Agentic AI](https://arxiv.org/abs/2610.14382)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Constantinos Papantoniou, Brian Hilton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems operating over geospatial data require more than autonomous reasoning and tool use; they must also support explicit orchestration, spatial validation, governance, provenance, failure handling, and human decision authority. Prior work introduced ANASSA, an agentic AI orchestration framework for spatial intelligence that established high-level components and responsibility boundaries for governed agentic execution (arXiv:2609.14824). However, the framework did not specify how those high-level responsibilities should be systematically decomposed into an implementation-facing low-level architecture. This paper addresses that gap by applying Design Science Research (DSR) to refine the ANASSA framework from high-level architectural (HLA) responsibilities into a low-level architecture (LLA). The resulting design preserves the responsibility boundaries of the foundational framework while translating them into executable architectural structures, including 47 logical roles, versioned task graphs, capability-based agent selection, typed contracts, explicit runtime states, spatial validation mechanisms, governance controls, failure and recovery paths, and provenance records. The architecture is demonstrated through an end-to-end execution trace and analytically evaluated for requirements traceability, internal consistency, responsibility preservation, and technology independence. The resulting high-level-to-low-level design provides an implementation-facing bridge between the ANASSA framework and future system implementations, defining how governed spatial agentic workflows can be made inspectable, reconstructable, and testable without binding the architecture to a specific AI model, geospatial platform, communication protocol, or deployment environment.

---


### 761. [DEFT: Disentanglement-Enhanced Fine-Tuning for EEG Foundation Models](https://arxiv.org/abs/2610.14497)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuqiu Deng, Muyun Jiang, Zongpeng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models (EFMs) have improved EEG representation learning by transferring knowledge from large-scale multi-subject pretraining to downstream tasks. However, their pretrained embeddings often retain substantial subject-related variation, placing an additional burden on the downstream classifier, especially in cross-subject settings. To address this issue, we propose Disentangled EFM Fine-Tuning (DEFT), a plug-and-play adapter for EFM fine-tuning. DEFT encourages branch disentanglement of pretrained tokens into task-oriented content and subject-consistent style, then performs downstream prediction from the content branch. It instantiates this factorize-before-classify design with recursive Gaussian refinement, temporal-variance regularization, subject-aware contrastive learning, and reconstruction. Experiments across multiple EEG datasets and four EFM backbones show that DEFT improves matched fine-tuning baselines. Further ablations and analyses support the intended content/style branch organization.

---


### 762. [Learning after Execution with Action-Specific Credit](https://arxiv.org/abs/2610.14573)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yufeng Tian, Jiahao Tang, Minghao Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Execution is often used as terminal feedback: it scores a generated program, but the resulting state is not used for another learning action. Learning after execution instead uses the execution result as an intermediate state that supports an additional learning interaction for the same policy. This creates a credit-assignment problem because the two actions share the same final objective but play different roles in the trajectory. Accordingly, action-specific credit assigns the initial action credit from the final trajectory outcome and the corrective action credit for improvement over the intermediate state. Image-to-TikZ serves as an executable visual testbed for this setting. On 945 held-out examples, learning after execution strengthens the shared policy under single-call inference and also produces a post-execution corrective capability. Single-call render success reaches 92.70\%, compared with 88.25\% for continued single-stage GRPO after the same number of additional training iterations. This corrective capability is not reproduced by continued single-stage training and depends on the intermediate state. Alternative credit definitions also induce different group-relative preferences over the same trajectories. Together, these results suggest that executable tasks contain useful learning structure beyond a terminal reward. Code is available at this https URL.

---


### 763. [MHWA: Multi-timescale Hierarchical World-Action Model](https://arxiv.org/abs/2610.14727)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pengcheng Pan, Guoqing Ma, Yuhan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive world models have emerged as a powerful paradigm for sample efficient decision making, yet their open loop rollouts often exhibit increasing drift that leads to error accumulation even within a relatively small planning horizon. Hierarchical temporal abstraction is a natural candidate to mitigate such drift by reducing the effective prediction horizon; however, existing hierarchical designs can introduce added structural and conceptual complexity, sometimes making them difficult to control and limiting gains over flat baselines. To this end, we introduce MHWA (Multi-timescale Hierarchical World-Action model), which employs a strided high level context channel to reduce global context update frequency, effectively curbing the propagation of compounding drift. Crucially, via context aware routing, the gating network dynamically reconfigures a low level mixture of experts by using both global context and current observations, thereby enabling flexible high-low coordination, helping alleviate interference commonly observed in static hierarchies. Empirically, using RLiable's seed-by-game aggregation, MHWA (77M parameters) achieves an IQM human normalized score (HNS) of 0.884 across three training seeds on a 14-game Atari subset using 10% subsampled offline data, outperforming a matched JOWA-70M baseline (0.529) and achieving numerically comparable performance to JOWA-150M while using nearly half the parameters and 70.88% fewer training FLOPs per sequence.

---


### 764. [No, Your Tools Are Not Enough: It's Time to Bring Agents to the Hunt](https://arxiv.org/abs/2610.14729)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ati Priya Bajaj, Xiang Mei, Tiffany Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern software systems are large and complex, demanding scalable and autonomous techniques for vulnerability discovery. Existing approaches still depend on human expertise for domain knowledge, and on human intervention throughout the process of vulnerability discovery. AI agents offer us an opportunity to make vulnerability discovery more adaptive, scalable, and autonomous. Agents bring the ability to make continuous decisions and adapt, and general knowledge that can be augmented.
In this paper, we present our experience using AI agents to find vulnerabilities across diverse programs such as Windows drivers, the Linux kernel, XNU, firmware, and web applications. We use an iterative agentic workflow and find that it generalizes across these targets. We discuss tasks that agents help with, which were previously challenging, and some future research directions we consider important for advancing autonomous vulnerability discovery.

---


### 765. [MCPDisCo: Seesaw-Mitigated Tuning for MCP-Native Agents](https://arxiv.org/abs/2610.14956)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kounianhua Du, Jianxing Liu, Shuai Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol provides a shared interaction substrate for the agentic web, allowing heterogeneous services to expose capabilities through a standardized interface. Learning to use this ecosystem entails a hierarchy of capabilities: tool-format skills, server-level transfer, and cross-server composition. We present MCPDisCo, an ecosystem-scale reinforcement learning framework for MCP-native agents. Using a Thought-Markov Decision Process (Thought-MDP), the framework explicitly represents internal reasoning alongside routing, execution, and termination and trains on real-server, long-horizon interactions spanning 70 MCP servers and 527 tools across six domains. We study the reasoning--tool seesaw, a joint-learning failure mode in which improvement in one objective can accompany deterioration in the other. To mitigate potential interference, MCPDisCo combines token-masked reward attribution with bidirectional gradient surgery: the former separates direct supervision for reasoning and action spans, while the latter removes conflicting components from both objective gradients in shared parameters. MCPDisCo achieves higher success with fewer chain-of-thought tokens. On the out-of-distribution MCP-Atlas and the GAIA benchmark, MCPDisCo maintains monotone gains, confirming that the learned behavior generalizes beyond the training server distribution and broader agentic tasks. Model weight and implementation are available.

---


### 766. [Toward a Multimodal Foundation Model for Plasma State Reconstruction](https://arxiv.org/abs/2610.15076)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bin Xia, Chuanfei Dong, Boting Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plasma experiments observe coupled physical states through sparse, heterogeneous, and incomplete diagnostics. We present a proof of concept toward a multimodal foundation model for plasma state reconstruction during magnetic reconnection, motivated by the Facility for Laboratory Reconnection Experiments (FLARE). Using 250 synthetic VPIC simulations at fixed reference electron beta $\beta_{e0}=0.2$, with 225 training runs and 25 disjoint validation runs, we train a 5.5M-parameter residual 3D U-Net to reconstruct three magnetic-field components and electron density from incomplete observations. The model combines spatial-only pooling, which preserves all 24 temporal frames, with global spatiotemporal self-attention and rotary positional encoding. Independently masking magnetic and density modalities across random, grid, block, and temporal patterns enables sparse sensing, cross-modal completion, density super-resolution, and temporal completion with a single set of weights and no task-specific retraining. With density fully hidden, just 0.1% magnetic spatial visibility reduces median density NRMSE from approximately 0.9 to 0.1. Conversely, observed density improves current-density reconstruction when magnetic data are absent or extremely sparse. With no magnetic observations, roughly 1% density visibility approaches the density reconstruction accuracy achieved with fully observed magnetic fields, although current structure remains more dependent on direct magnetic measurements. Full magnetic conditioning also stabilizes completion of missing future density frames. These results demonstrate bidirectional cross-modal predictive coupling within this simulation regime. Generalization across plasma regimes or to experimental measurements remains untested.

---


### 767. [Knowledge transfer between simple discrete worlds](https://arxiv.org/abs/2610.15081)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Silvère Gangloff, Jan Hula  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting to a new world and reasoning correctly about which outcomes are possible under rules one has not met before is a basic capacity underlying general intelligence. We study it in small discrete worlds: sets of grid configurations consistent with a shared set of rules, concretely Sudoku-like puzzles built from a common base and a handful of extra rules. We train a single depth-recurrent model on many combinations of rules and test it at four levels of novelty: a new puzzle, a new combination of known rules, a pairing of rules never seen together, and a rule instance not seen at all during training. The model receives the active rules either as a symbolic description or as two solved examples, and a model that gets no rule information is used as a baseline. At recombining rules it was trained on, the description matches or exceeds examples ($99\%$ against $95\%$ on new combinations). On rule instances whose components never co-occurred in training, the description falls below the no-information baseline while examples stay above it. The framework allows us to test many such generalization regimes in more systematic way than benchmarks such as ARC-AGI and provides new ground for evaluating depth-recurrent reasoning models, which are typically tested on saturated Sudoku benchmarks.

---


### 768. [Drive3R: Block-wise Streaming Geometric Foundation Models for Autonomous Driving](https://arxiv.org/abs/2610.15112)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianyi Yang, Haojun Yang, Jipeng Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity closed-loop simulation for autonomous driving increasingly relies on dense multi-view 3D reconstruction. While recent feed-forward geometric foundation models have revolutionized per-scene optimization, applying them to continuous, long-horizon driving sequences is computationally intractable due to GPU memory limits and the quadratic complexity of global attention. Existing scaling strategies are fundamentally limited, as causal streaming suffers from compounding scale drift and trajectory deviation, while rigid "chunk-then-align" heuristics fragment global context and produce trajectory discontinuities. To address these limitations, we introduce Drive3R, a block-wise streaming geometric foundation model. Its block-wise causal attention resolves the scalability bottleneck of fully bidirectional attention while avoiding the loss of local future context in purely causal streaming. Its confidence-aware re-anchoring further mitigates long-range drift by detecting unreliable streaming states, re-initializing the KV cache, and stitching refreshed segments through SE(3) alignment. Extensive experiments demonstrate that Drive3R establishes a new state-of-the-art on nuScenes, KITTI, and Waymo. Specifically, on nuScenes, it improves over the recent DVGT-2 baseline from 0.1806 to 0.1081 in AbsRel, from 0.6750 to 0.5344 in point-cloud Accuracy, and from 1.5812 to 0.9092 in ATE.

---


### 769. [SuperAI: Merging Capabilities Across Heterogeneous Foundation Models](https://arxiv.org/abs/2610.15322)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jingtong Dou, Chuancheng Shi, Wenhua Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enabling the reuse and composition of knowledge and capabilities distributed across foundation models is an important step toward building scalable artificial intelligence (AI) systems. However, architectural differences and incompatible representations make it difficult to transfer and integrate these capabilities through a unified cross-model interface. To address this challenge, we propose SuperAI, a cross-architecture multi-model fusion framework that integrates complementary capabilities from multiple source models into a host model through orthogonal alignment of low-dimensional task-relevant representations. Specifically, we first extract task-relevant representations from the source models and the host model using shared anchor samples, and apply principal component analysis (PCA) to construct low-dimensional functional subspaces with the same dimensionality. Next, we use orthogonal Procrustes mappings to align the source and host coordinate systems, establishing cross-model correspondences while preserving the internal geometry of each source subspace. Finally, we train a lightweight residual multilayer perceptron (MLP) with joint supervision on task outputs and source-model increments, learning input-dependent residual increments that are injected into the host model for multi-model capability fusion. Experiments on three host models across 15 capability domains show that SuperAI achieves higher average domain scores than the evaluated cross-architecture fusion methods and better preserves general capabilities as the number of source models increases. Ablation studies further support the effectiveness of orthogonal alignment, nonlinear residual mapping, and joint supervision.

---


### 770. [DC-Flow: Target-Conditioned Cyclic Peptide Design via Delayed-Coupling Flow Matching](https://arxiv.org/abs/2610.15391)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yitian Wang, Minjie Cheng, Yaning Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Target-conditioned cyclic peptide design requires coordinating interfacial side chains with macrocyclic closure. Existing end-to-end generators concurrently update geometric and chemical variables from noise, assigning residues to disordered coordinates. Meanwhile, predictor-assisted workflows often get stuck in local traps because they lack feedback in the propose-and-filter stage and ignore 3D structural proposals during sequence search. To overcome the drawbacks of these two paradigms, we propose DC-FLOW, a staged generative framework built around Delayed-Coupling Flow Matching. In principle, DC-FLOW postpones sequence and side-chain activation until a target-conditioned backbone takes shape, resolving structural ambiguity before chemical assignment. Then, it feeds delayed activations back into the backbone, achieving co-evolution of backbone geometry and emerging residue identities by coupling their flows. This mechanism enables more reliable macrocyclic closure and favorable interface packing. For predictor-assisted workflows, DC-FLOW supplies 3D proposals with in-trajectory guidance, enabling cascaded test-time scaling to prune redundant backbones and terminate unpromising refinement early. Extensive experiments show that DC-FLOW improves cyclization fidelity, diversity, and interface energetics, substantially increasing the yield of confident cyclic peptide binders under a fixed final-candidate budget. Our code is available at this https URL.

---


### 771. [CacheLink: Functional KV Transport for Zero-Prefill Cross-Model Context Handoff](https://arxiv.org/abs/2610.15509)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haomiao Qiu, Yining Tang, Zijia Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV caches make long-context serving efficient by reusing past computation, but model switching breaks this reuse and forces the receiver to prefill the context again. We study \emph{zero-prefill cross-model context handoff}: translating a sender cache into a receiver-compatible state so that the receiver can continue directly without prefilling same context. Existing affine transport methods show that receiver KV states can be substantially reconstructed from sender caches. However, through extensive analyses, we find that reconstruction fidelity is a poor proxy for receiver utility. Similar K/V reconstruction errors can lead to substantially different attention patterns, predictive distributions, and downstream accuracy, because conventional reconstruction objectives overlook the query-dependent functional importance of K and V in receiver attention. We thus introduce CACHELINK, which learns a coupled K/V correction through the receiver behavior directly. Across four independently trained sender--receiver pairs and seven evaluation panels, CACHELINK improves the equal-weight mean over all methods for every pair. In matched diagnostics, CACHELINK changes K/V squared error by less than 0.4% while substantially changing receiver attention and next-token behavior. At 32K context, it reduces handoff latency by up to $7.27\times$ relative to receiver re-prefill. Our findings verify that reconstruction fidelity alone is insufficient and that preserving the receiver computation induced by the transported cache is important for effective cross-model KV transport.

---


### 772. [MERIT: Scaling KG Foundation Models with Relation Transformers](https://arxiv.org/abs/2610.15638)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Cosimo Gregucci, Daniel Hernandez, Antonio Vergari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph (KG) foundation models (KGFMs) predict links on unseen graphs zero-shot. KGFMs have been pioneered by ULTRA which builds a relation graph from co-occurrences that match motif templates, and passes messages over it to obtain relation representations. More recent KGFMs such as MOTIF and TRIX increase the size of this relation graph, and FLOCK replaces message-passing with probabilistic random-walk ensembles. However, larger relation graphs mean more messages, and more walks mean more sequences to encode, so they improve performance at higher training and inference cost. This cost hinders their use in more complex reasoning tasks, such as complex query answering. To reverse this trend, we design MERIT, the first KGFM with a transformer relation encoder: every relation name attends to every other, and the motifs enter as a soft prior rather than as edges. Over 56 benchmarks, MERIT matches the zero-shot MRR of SoTA KGFMs while being 6x faster than TRIX and over 100x faster than FLOCK at inference. Fine-tuned for complex query answering like UltraQuery, MERITQuery improves over it at matched cost.

---


### 773. [TabMosaic: Unified In-Context Diffusion for Tabular Generative Tasks](https://arxiv.org/abs/2610.15699)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jayoung Kim, Sanghyun Hong, Noseong Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling for tabular data has advanced to the point where models can synthesize realistic records, recover missing values, and generate samples conditioned on class labels or observed attributes. Despite recent advances, existing approaches either require table-specific training or restrict in-context learning to single-cell prediction. In this work, we formulate these tabular generative tasks as a single problem: modeling the joint conditional distribution of an arbitrary set of target cells given the observed cells of an unseen table. To this end, we turn to diffusion, whose denoising objective is defined jointly over all target cells rather than one cell at a time. Under the pretraining distribution, this objective is minimized by the posterior predictive distribution over the target set. Building on this, we propose TabMosaic, a unified in-context diffusion model for generating mixed-type target cells in unseen, potentially incomplete tables without table-specific training. We further show that its pretraining objective bounds the conditional negative log-likelihood and the divergence from the posterior predictive for arbitrary target sets, extending the Bayesian account of in-context learning from a single-value prediction to joint multi-cell generation. Across 48 real-world tables, TabMosaic ranks first on all evaluated generative tasks against 20 baseline approaches

---


### 774. [What DNA Foundation Models Learn Beyond Sequence Composition](https://arxiv.org/abs/2610.15711)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vincenzo Yuto Civale, Andrew David Bagdanov, Alberto Magi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Do genomic foundation models (FMs) provide predictive information beyond simple sequence composition? We evaluate frozen representations from five DNA FMs against normalized k-mer frequencies across 57 genomic classification datasets and two exploratory gene-expression regression tasks. Simple k-mer features remain competitive with most models, whereas NTv3 shows a consistent advantage; the ranking is robust to globally fixed and multi-scale k-mer baselines and alternative downstream probes. To test incremental predictive utility directly, we compare global 6-mer features with their concatenation with each FM embedding under a matched Random Forest protocol. NTv3 improves 46 of 57 datasets (mean $\Delta$MCC = +0.072), while Caduceus provides smaller gains and the other models do not improve mean MCC. We separately decompose embeddings into a component linearly predictable from 6-mer frequencies and a ridge residual, finding that linear recoverability does not reliably indicate downstream utility. Exact 6-mer-preserving shuffles further reveal task-relevant sequence-order sensitivity, most pronounced for NTv3, although order sensitivity alone does not guarantee predictive improvements. Our results establish compositional features as essential controls and offer complementary diagnostics for evaluating the added value of frozen genomic representations, without making claims about fine-tuning capacity.

---


### 775. [SpikeOcc: Towards Resilient Multimodal 3D Occupancy Perception via Spiking Experts](https://arxiv.org/abs/2610.15745)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yiding Sun, Zijie Xu, Hongqiang Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal 3D occupancy prediction underpins safe autonomous driving through comprehensive scene understanding. However, existing methods have largely pursued higher accuracy through sophisticated fusion, leaving resilience to missing sensors underexplored. In this paper, we investigate spiking neural networks (SNNs) as a means of building more resilient multimodal perception. Still, the discrete nature of spiking neurons makes optimization challenging. To overcome this difficulty, SpikeOcc is introduced with two complementary components, a Spiking Mixture-of-Experts (SMoE) and Sensor Availability Learning (SAL). Specifically, SMoE organizes RGB, LiDAR, and joint fusion into specialized pathways, enabling full-width unimodal representations while retaining the original multimodal features via a bounded residual. Beyond sensor dropout, SAL employs a staged curriculum with explicit routing supervision, progressively improving robustness under severe sensing conditions. Remarkably, SAL also yields notable gains for conventional models, highlighting its broader potential for resilient multimodal learning. Extensive experiments demonstrate that SpikeOcc maintains competitive full-sensor accuracy while markedly raising the performance floor under sensor outages. SpikeOcc illustrates the promise of neuromorphic computing, pointing toward more reliable and energy-efficient autonomous driving.

---


### 776. [Variance-Optimal State Resampling for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.15888)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yibo Wang, Yuanxin Liu, Zhaoran Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards spends much of its rollout budget on states that yield no learning signal. We recast this as a question about the sampling distribution itself: under a fixed rollout budget, which distribution over states minimizes the variance of the policy-gradient estimator? The answer admits a closed-form Neyman allocation, $\mu_{\mathrm{var}}^\pi(s) \propto d^\pi(s)\,\sigma_\pi(s)$, which connects naturally to GRPO's group-relative advantage and induces an emergent reverse curriculum as the policy improves, with no externally imposed schedule. Building on this principle, we propose VSR (Variance-driven State Resampling), a plug-in modification to GRPO using a prefix replay buffer and a zero-cost variance proxy. On mathematical reasoning benchmarks and long-horizon agentic tasks (Sokoban, BabyAI), VSR outperforms GRPO and GiGPO on most benchmarks with fewer generated tokens per update.

---


### 777. [Fisher information and the geometry of memorization in neural networks](https://arxiv.org/abs/2610.16161)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Daniel T. Bernstein, Chase Goddard, Luca Di Carlo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fruitful approach towards understanding generalization in machine learning involves characterizing how models separate generalizable structure from idiosyncratic or even corrupted features of training data. Fisher information has emerged as a diagnostic tool for this separation, leveraging loss geometry to distinguish generalization from memorization. Here we investigate this connection in vision models trained on CIFAR-10 with controlled noise that can be learned only through memorization. We show that projecting model weights onto the top Fisher eigenvectors decouples general task performance from noisy sample memorization, and we investigate how this decoupling presents differentially across layers. We show that the same phenomena are present in small transformers trained to solve a synthetic in-context learning task, and are reproduced in closed form in a simple, analytically solvable linear model. Our results reveal that Fisher information captures aspects of the geometric structure underlying how neural networks allocate capacity between generalization and memorization.

---


### 778. [From Simulated Fluids to Living Tissue: Zero-Shot Foundation Model Transfer to Perturbed Embryos](https://arxiv.org/abs/2610.16236)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Louisa Cornelis, Haewon Jeong, Irina Espejo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Morphogenesis is driven by the interplay of genetic regulation and tissue mechanics. In vivo video data is limited, particularly under genetic mutations and environmental perturbations, making generalization beyond the most representative conditions in the dataset challenging. However, at tissue scales, the dynamics of Drosophila can be described as a continuum flow, motivating the usage of representations learned across other physical systems as priors for developmental dynamics.
We investigate finetuning Walrus, a Continuum Dynamics Foundation Model pretrained across a broad set of simulated continuous systems, on tissue velocity fields from only 12 wild-type Drosophila blastoderm videos. We evaluate autoregressive prediction both in-distribution and zero-shot under unseen temperature and genetic perturbations. Zero-shot refers to evaluation on perturbation conditions never seen during wild-type finetuning, without any additional training. In-distribution, a Fourier Neural Operator model trained from scratch achieves best performance on VRMSE. However, Walrus (CRPS) is the strongest model under the most severe distribution shift of unseen samples of mutated embryos and temperature conditions. Interestingly, predictions capture the shape of the mean surface tissue velocity trajectory and its separation between 17°C and 27°C, including the timing of the peak at Germ Band Extension onset, a biologically meaningful milestone of embryo development.
Our results provide preliminary support that representations learned from different dynamical systems can transfer to experimental morphogenesis in developmental regimes, provided they admit a continuum description. More broadly, our results motivate further study of physics foundation models as a new complementary tool for the simulation of morphogenesis in low-data regimes.

---


### 779. [Building age estimation based on widely available multi-source1 geospatial data](https://arxiv.org/abs/2610.16320)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jialu Sui, Hongsheng Zhang, Rui Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building age is fundamental for urban infrastructure safety, operation, and planning, as it directly affects structural safety, and sustainable development. Existing methods mostly rely on detailed building information such as street view, function, or materials, which are harder to obtain than geospatial data like satellite imagery and Digital Surface Models (DSMs). However, existing methods based on those geospatial data mainly rely on optical imagery and local texture features, limiting their ability to capture structural information and distinguish buildings from different periods. Moreover, the inherent temporal ordering among building age categories is often overlooked. To address these limitations, we propose the first deep-learning framework for multi-building age estimation using widely available multi-source geospatial data, including remote sensing data and their derived products, as well as building footprint information that estimates age at both pixel and instance levels within a unified pipeline. Specifically, a large pretrained backbone with fine-tuning adapters extracts representative features, and raster-derived and property-derived fusion modules support pixel-wise and instance-wise predictions. Pixel-level estimation employs a pyramid decoder with Cosine-guided Mixture-of-Experts (CMoE) to fuse multi-source raster data across scales, capturing fine-grained building age differences, while instance-level prediction uses attention pooling and Property-Conditional Adaptive Instance Normalization (PCAdaIN) to extract instance-level representations and integrate property attributes. A Temporal Ordinal Constraint Loss (TOCL) enforces the sequential ordering of predicted ages. We also construct a building age benchmark for Hong Kong to enable comprehensive evaluation. The source code and datasets are available at this https URL.

---


### 780. [Resample the Answer: Where to Spend Test-Time Compute in Recursive Reasoning](https://arxiv.org/abs/2610.16427)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Maxime Illouz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive reasoning models such as the Tiny Recursive Model (TRM) iteratively refine two latent states: an answer state y, decoded into the output, and a reasoning state z, which is never decoded. Many of their failures have been attributed to bad basins, regions of latent space that trap the recursion on wrong answers. Recent test-time approaches perturb y, z or both to recover these failures, but the impact of this choice on performance, test-time compute efficiency and scaling properties remains unclear. Through controlled experiments on TRM, we find that a failed trajectory carries its failure in its answer state. At equal compute, in depth and in width, resampling y recovers more failures than any perturbation of z we tested, and the performance gap widens as the test-time compute budget grows. Our approach, Gated Answer Resampling (GAR), pairs this resampling of the answer state with the model's own halting head and restarts only the puzzles that the head rejects. With at most 64 restarts per puzzle and no training or hyperparameter search, GAR takes TRM from 85.9% to 99.4% on Sudoku-Extreme and from 68.8% to 85.6% on Pencil Puzzle Bench validation. On the same checkpoints, GAR also outperforms Probabilistic TRM (PTRM), which perturbs z at each step, even when PTRM uses 42 to 197 times as much compute.

---


### 781. [ECHO: Correcting Time Series Foundation Model Forecasts with Historical Analogues and Errors](https://arxiv.org/abs/2610.16433)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Boya Zhang, Xilin Dai, Yilin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) provide general-purpose forecasting capabilities, yet their forecasts can remain misaligned with the temporal characteristics of a target domain. This motivates lightweight forecast correction even when only black-box access to the TSFM is available. Our key observation is that two forms of historical information provide complementary correction signals: historical analogues reveal how similar contexts evolved, while past forecast errors reveal a TSFM's characteristic deviations in the target domain. Based on this observation, we propose ECHO, a black-box forecast correction framework that learns from both sources. ECHO uses AnalogE to assess retrieved historical analogues together with the current context and base forecast, learning transferable corrections through cross-domain pretraining. In parallel, RecentE learns target-specific residual corrections from past forecast errors and refines them as causally available feedback accumulates. ECHO dynamically combines the two corrections according to their observed forecasting performance. Across 5 representative TSFMs and 9 real-world datasets, ECHO reduces MSE in all 45 backbone--dataset settings, yielding an average relative reduction of 9.26\% in macro-average MSE. Its gains also extend to long-horizon forecasting.

---


### 782. [SLEM: Spectrum-Aware Latent Expert Merging](https://arxiv.org/abs/2610.16484)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dohyeon Kim, Bedionita Soro, Bruno Andreis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale model capacity efficiently by activating only a small subset of experts for each input, while still requiring all parameters to be stored in memory, resulting in substantial memory overhead. Expert merging techniques have recently emerged as a promising compression paradigm that reduces this overhead by consolidating multiple experts into a smaller set. However, existing approaches have two key limitations: (i) direct convex interpolation in parameter space is not generally guaranteed to yield meaningful interpolation of expert functions; and (ii) estimating expert similarity or merging coefficients often relies on calibration data, introducing dependence on the calibration distribution. To address these limitations, we propose Spectrum-Aware Latent Expert Merging (SLEM), a calibration-free expert merging framework that occurs in a structured latent representation of expert weights using a VAE. SLEM groups experts within and across layers based on latent similarities and derives merging coefficients from expert weight spectra. It then performs geometry-aware latent interpolation and decodes the resulting representations into merged expert weights. Compared with existing expert merging methods, SLEM achieves comparable or better performance on general knowledge benchmarks and higher average performance on generation benchmarks involving mathematical reasoning and code generation.

---


### 783. [REEL: Learning to Retrieve, Evaluate, and Evolve Visual Memory for Any Long-Horizon Multi-Shot Video Generation](https://arxiv.org/abs/2610.16632)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hang Xu, Guohui Zhang, Xiaoxiao Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory-based long-video generation aims to combine user control with long-range visual consistency. We organize this process into three functional components: a planner, an adapter, and a generator. Representative multi-shot systems couple memory to generator-specific interfaces or use predefined agent workflows, rather than independently training a memory policy for cross-shot objectives. We introduce REEL, a general-purpose visual-memory planner. Through a unified tool interface, REEL learns to retrieve references, create missing visual evidence, and update persistent memory. Backend-specific adapters translate its evidence plans into supported conditioning inputs, allowing the same policy to guide different black-box video generators. To train REEL, we construct two high-quality datasets, REEL-SFT-4k and REEL-RL-1k, covering diverse interaction patterns and prompt types. Training proceeds in three stages: supervised fine-tuning, single-shot Group Relative Policy Optimization (GRPO), and multi-shot GRPO. Multi-shot GRPO carries policy-generated memory across consecutive shots, so later outcomes guide earlier reference selection and memory updates. REEL-Bench tests identity preservation and intended state changes under text-only requests and timed reference-image uploads. On JoyAI-Echo~1.5 and MiniMax-H3, REEL improves cross-shot consistency on ST-Bench by 15.1\% and 20.7\%, and Core-100 on our proposed REEL-Bench by 2.41 and 8.32 points, respectively, over the no-memory baseline.

---


### 784. [IND-Eval: Aligning Evaluation and Simulation for Industrial Time Series Foundation Models](https://arxiv.org/abs/2610.16652)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vebjørn Haugland, Pavel Gulin, David Foss 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce IND-Eval, a public benchmark that organizes industrial time series across domains into source-specific forecasting tasks. Relative to established benchmarks such as GIFT-Eval, it emphasizes finer sampling resolutions and a greater prevalence of multivariate forecasting. Evaluating Chronos-2, TiRex-2, and TimesFM-3, we find that TimesFM-3 achieves the lowest source-balanced aggregate nMASE and nCRPS and leads seven of nine sources under each metric; source-specific exceptions reinforce the need for domain-representative evaluation for model selection. These findings also motivate improving domain alignment during pretraining, where real industrial data are often too scarce to close domain-specific gaps directly; we therefore investigate whether a domain's statistical structure can guide simulator design. In a case study on two offshore well-monitoring regimes, we improve a general simulator's coverage using an oscillator-augmented simulation pipeline. This lowers forecasting error in the target domain but reduces performance on the subset of GIFT-Eval with natively univariate targets. A 50/50 mixture of the general and augmented simulation recipes achieves the lowest error among the three training recipes for all four event-metric pairs in the case study while recovering most of the lost GIFT-Eval performance. Together, these results illustrate how domain-representative evaluation can guide model selection and the composition of simulated data while revealing a trade-off between specialization and generality.

---


### 785. [Carve VFM: Carving Specialists out of Generalists, Automatic Task-Specific Compression of Vision Foundation Models](https://arxiv.org/abs/2610.16813)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lotfi Abdelkrim Mecharbat, Abdelrahman Elsayed, Ibrahim Almakky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) provide transferable visual representations, but their inference cost limits deployment in many settings. Fine-tuning specializes a VFM without shrinking it; distillation shrinks it, but through expensive teacher-guided training. Structured pruning offers a more direct route by extracting a compact subnetwork from the VFM. However, as compression gets aggressive, existing methods fail because they treat subnetwork selection and recovery as separate axes. Across layers, capacity must follow task sensitivity rather than spread uniformly. Within a layer, a removal cannot be judged by importance alone; its impact also depends on how well the lost contribution can be recovered from what remains. Selection and recovery must therefore be decided jointly. We introduce Carve VFM, which resolves this interdependence. Given a VFM, a calibration set, and a parameter budget, it (i) searches for task-specific capacity allocations across layers; (ii) guides the search via an adaptive recovery-aware fitness criterion; and (iii) reconstructs removed behavior through iterative closed-form low-rank corrections merged into the surviving weights. The result is a dense encoder produced in minutes on a single GPU without backbone retraining. Across twelve benchmarks and four models from DINOv3 and MetaCLIP-2, Carve VFM achieves the highest reported mean accuracy in seven of eight backbone-budget configurations among the evaluated dense structured-pruning methods. Further fine-tuning surpasses the strongest evaluated edge model (88.1% vs. 85.8%), and carved models cut compute and memory while delivering 1.3-2.0x higher GPU throughput than the uncompressed one. These results show that the compact model you need is inside the VFM; it only has to be carved out.

---


### 786. [DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning](https://arxiv.org/abs/2610.16822)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxiang Zeng, Kun Xie, Yang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computational semantics across node initialization, global spectral encoding, pairwise interaction, and feature update. DTA-GT realizes this principle with direction- and topology-aware node initialization, Magnetic Laplacian spectral encoding, direction-dual structural attention, and a Direction-Sensitive MoE-FFN. Across accuracy and latency prediction on NAS-Bench-101 and NAS-Bench-201, DTA-GT consistently outperforms representative sequence-, GNN-, Transformer-, and hybrid predictors under limited-budget settings. Ablations and Magnetic spectral controls show that the improvements come from coordinated direction-aware stages and edge-orientation-sensitive spectral information, while mechanistic diagnostics confirm that the modules exhibit the intended directional behavior. These results support encoder-wide directional consistency as an effective design principle for architecture DAG representation.

---


### 787. [Sequence Composition in EHR Foundation Model Pretraining](https://arxiv.org/abs/2610.16878)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joshua Placidi, Inigo Stibbe, Alfred J. Balston 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive electronic health record (EHR) foundation models predict the next event token in patient trajectories: sequences of structured medical events. A typical pretraining strategy is to concatenate all trajectories into a global stream and sample token windows from it. This gives patients with longer sequences more training exposure and allows tokens to attend across patient boundaries. We argue that these choices create a misalignment between pretraining and downstream clinical tasks. To explore this, we investigate how the composition of pretraining sequences affects clinical prediction performance. Using the global-stream approach as a baseline, we propose alternative sequence composition methods that control how patient trajectories contribute to pretraining sequences. Across four MIMIC-IV v2.2 tasks, our best method improves macro AUROC, AUPRC, F1, and balanced accuracy, with relative gains of 9.3% in F1 and 2.7% in AUPRC under a fixed training recipe. We find that these gains generalize across four additional evaluation settings, including the INSPIRE and eICU-CRD datasets, with improvements in macro AUROC, AUPRC, and F1 score. Our results show that simply changing how EHR data are presented to the model during pretraining can improve downstream performance, without changing the model or collecting additional data.

---


### 788. [FOCUS: A Subspecialty Foundation Model for Intraoperative Central Nervous System Pathology](https://arxiv.org/abs/2610.16914)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xing Liu, Yifan Guo, Hongtai Lv 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intraoperative frozen-section diagnosis of central nervous system (CNS) lesions guides surgical decisions but is challenged by artefacts, diagnostic complexity and time constraints. Most pathology foundation models have limited exposure to CNS frozen tissue. Here we present FOCUS, a subspecialty foundation model pretrained on 27,930 frozen-sections enriched for CNS tissue. FOCUS led 11 internal diagnostic and 12 biomarker-prediction tasks, with mean AUCs of 0.969 and 0.877, respectively, retaining leading performance in temporal and external cohorts. To provide more comprehensive diagnostic information, we further organized ten diagnostic tasks into a WHO-aligned diagnostic hierarchy and separately evaluated FOCUS for lymphoma detection, a critical task for intraoperative surgical decision-making. In reader assessments by six neuropathologists, FOCUS assistance enabled junior readers to approach or exceed unassisted senior readers in hierarchical diagnosis and raised junior readers' lymphoma sensitivity from 81.6% to 94.7%. FOCUS could improve diagnostic accuracy and granularity, inform lymphoma-related resection decisions and provide provisional molecular information. Such capabilities highlight the potential of FOCUS to provide robust, clinically actionable support for intraoperative CNS pathology.

---


### 789. [TabGift: A Context-Efficient Foundation Model for Tabular Data Generation](https://arxiv.org/abs/2610.16990)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu-Sheng Li, Jun-Peng Jiang, Han-Jia Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data generation aims to synthesize realistic samples from limited observations while faithfully capturing the underlying data distribution. Tabular foundation models (TFMs), pretrained on diverse tabular tasks and adapted through in-context learning, have demonstrated strong predictive capabilities, suggesting the potential of extending this paradigm to tabular data generation. However, the strong predictive performance of TFMs often relies on sufficiently large context sets, whereas tabular generation is typically needed precisely when target data are scarce. Extending the foundation-model paradigm to generation therefore requires reliable distribution inference from only a limited context. To this end, we propose TabGift, a context-efficient tabular foundation model enabling both efficient distribution modeling and effective generation from only a few context samples. TabGift maps heterogeneous tables into a shared latent space with a pretrained tabular encoder, where an in-context diffusion model learns to denoise latent samples conditioned on a small set of clean examples. This design transfers generative priors across datasets and enables distribution inference from limited context, while a lightweight dataset-specific MLP decoder maps generated representations back to the original data space. Experiments on 7 classification and 11 regression datasets show that TabGift consistently outperforms representative baselines in synthetic data quality, with particularly strong gains under limited-context settings, while achieving substantially faster adaptation and generation.

---


### 790. [MaskSense: Confronting the Visual Exploration Trap in Masked Image Generation](https://arxiv.org/abs/2610.17009)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yawen Shao, Jie Xiao, Kai Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has shown strong potential for aligning generative models with human intent, but adapting RL to masked generative models (MGMs) remains largely underexplored. Existing approaches that directly adapt Group Relative Policy Optimization (GRPO) to MGMs leave a foundational conflict unaddressed: MGMs' exploitative decoding nature is inherently at odds with the exploratory diversity that GRPO presupposes. In this work, we reveal a structural decoding bias termed the visual exploration trap: confidence-based sampling trades the exploration of diverse subject realizations for the greedy resolution of low-uncertainty background regions, causing premature collapse of the generative exploration space and starving GRPO of the rollout diversity it depends on. To this end, we propose MaskSense, a novel RL framework for MGMs that confronts the visual exploration trap at both the sampling and optimization stages. Specifically, we introduce a semantic anchored routing sampling mechanism that leverages semantic priors to preserve high-entropy subject token exploration while amplifying intra-group reward variance through exploratory-exploitative routing to yield more discriminative advantage estimates. Furthermore, we design a global entropy transition anchoring strategy to identify the most consequential decoding steps and concentrate gradient updates on them. Extensive experiments on multiple text-to-image benchmarks demonstrate that MaskSense substantially improves upon the base model, with GenEval accuracy improving from 54% to 86% and HPS from 28.89 to 36.39, achieving state-of-the-art performance.

---


### 791. [Size Generalization for Diffusion Routing Solvers](https://arxiv.org/abs/2610.17192)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Barak Itzchak Davidovitch, Eli Meirom, Ethan Fetaya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Routing problems, like the Traveling Salesman Problem (TSP) and the Capacitated Vehicle Routing Problem (CVRP), are NP-hard and slow to solve for large instances. Diffusion-based solvers can be trained in a supervised way using sets of optimal solutions, and then quickly solve new test instances. However, for large instances, optimal solutions are hard to find, and diffusion models fail to generalize to instance sizes outside their training distribution. Here we describe ResizeCO, a label free size-generalization approach that addresses both the change in statistical properties of larger instances, and the computational challenge of solving them quickly. It uses reinforcement learning on large-scale instances to adapt a diffusion model trained on small instances. Specifically, we adapt GRPO to this problem, using route length as the training signal. ResizeCO also formulates k-opt as a tree search, solved by a beam search on the GPU. In size-generalization experiments on TSP and CVRP instances with up to 10000 nodes, ResizeCO achieves a Pareto front over route quality and time that dominates learned solvers, and also outperforms other solvers at short run times, setting a new state of the art.

---


### 792. [Foundation Models for Event Prediction Across Heterogeneous Event Logs](https://arxiv.org/abs/2610.17503)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fabian Spaeh, Sean Jaffe, Shandian Zhe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event logs are ubiquitous across real-world domains, including business processes, manufacturing workflows, healthcare, and many other operational systems. Yet event logs can differ substantially in their event semantics, label spaces, interaction patterns, and temporal scales, making it difficult to build a single foundation model that generalizes directly to previously unseen systems. We address this challenge with the Foundation Event Predictor (FEP), a simple and scalable in-context architecture that performs next-event prediction through learned, event-level nonparametric inference. Causal self-attention encodes context and target histories into key and query representations, respectively, while the observed next context events are encoded as values. Cross-attention then performs learned, relevance-weighted aggregation of next-event outcomes over all context transitions, allowing the entire nonparametric prediction procedure to be expressed as standard attention operations and efficiently parallelized with modern kernels such as FlashAttention. To promote cross-system generalization, we introduce permutation-robust embedding learning and random fixed embeddings to decouple event IDs from persistent semantics, together with empirical quantile transforms and robust normalization to handle diverse temporal scales. We pretrain FEP on 696 real-world event datasets spanning heterogeneous event systems and evaluate it on 50 held-out datasets unseen during pretraining. Across these datasets, FEP generalizes effectively to new event systems without parameter adaptation, frequently approaching the performance of strong models trained separately on each target dataset while substantially outperforming existing foundation-model baselines, particularly on challenging prediction tasks.

---


### 793. [Benchmarking Self-Supervised 3D Medical Vision Foundation Models and Transferability Estimation](https://arxiv.org/abs/2610.17573)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaqi Tang, Yu Wang, Yang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining has expanded the pool of 3D medical foundation models, but published evaluations use different datasets, endpoints and fine-tuning protocols. Models also differ in architecture, pretraining objective and data, while downstream targets range from voxel-level masks to patient-level diagnoses and outcomes. As a result, published findings provide little directly comparable evidence for choosing a model for a new task. Direct comparison of adaptation performance requires fine-tuning candidates on labelled target data, at substantial computational cost. We benchmark 23 candidates across the same 14 segmentation, classification and regression tasks spanning multiple anatomies and modalities. No candidate ranked among the top three across all segmentation tasks or across all classification and regression tasks; a convolutional encoder could outperform a transformer trained with the same objective on one task but underperform it on another. We benchmark transferability estimators against the fine-tuned rankings and find that their agreement varies across dense segmentation, classification and regression. InsightRank uses task-appropriate frozen-feature statistics and architecture-aware pairwise comparisons to rank candidates before fine-tuning. Across the 23-model pool, mean Kendall tau-b was 0.431 for segmentation and 0.352 for classification and regression. The segmentation Top 3 contained a task winner on four of nine tasks; the image-level Top 3 contained none on the five tasks, despite better full-ranking agreement than the matched conventional estimators. A three-model shortlist reduced recorded extraction-plus-training job time by 85.8% across seven segmentation tasks. Together, the benchmark provides a common reference for model selection and InsightRank offers a lower-cost way to prioritize fine-tuning, with shortlist performance that differs by target type.

---


### 794. [Adaptive-Group Process Rewards for GUI Agents](https://arxiv.org/abs/2610.17710)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zirui Shang, Yang Liu, Xin Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training graphical user interface (GUI) agents with reinforcement learning suffers from sparse outcome rewards, leading to inefficient learning. Process rewards offer a promising direction for credit assignment to intermediate actions; however, accurately evaluating an action requires identifying evidence across long-horizon GUI trajectories, as its value may depend on information beyond its immediate state and observation. In this paper, we propose an adaptive-group process reward framework that dynamically partitions a GUI trajectory into semantically coherent subgoal groups, enabling process reward estimation at both the action and group levels. At the action level, a critic evaluates each action based on the visual changes and subsequent actions within the group for action correctness and contribution to the subgoal. At the group level, the framework aggregates action-level evaluations to assess subgoal completion and contribution to the overall task, and further refines these assessments by leveraging the context of all groups in the trajectory. The process reward of each action is obtained by combining its action-level evaluation with the refined group-level evaluation. We further augment GRPO's outcome advantage with the proposed process rewards to provide finer-grained guidance for GUI agent training. Experiments on process reward benchmarks and downstream RL training demonstrate the effectiveness of the proposed framework.

---


### 795. [Understanding Machine Taste: Aesthetic Agreement Across Foundation Models in K-pop](https://arxiv.org/abs/2610.17731)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kaishen Wang, Yucheng Pan, Xuehao Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As foundation models enter creative industries, understanding their aesthetic preferences becomes an important step toward AI-assisted creative decision making. In this work, we investigate how foundation models evaluate creative content and characterize their ``machine taste'' using K-pop songs and music videos as a testbed. We formulate aesthetic evaluation as a pairwise ranking problem and systematically examine pairwise inter-model agreement, group-level consensus, and cross-modal preference alignment. Our results reveal stronger pairwise inter-model agreement and group-level consensus in visual evaluation than in audio evaluation, while preferences across the two modalities remain weakly aligned. We further examine how visual consensus rankings relate to real-world popularity using historical YouTube viewership data, finding positive but varying correlations across artist groups. These findings provide initial insights into machine aesthetic preferences and lay the groundwork for future AI-assisted creative decision making that considers creative content, artist identity, audience preferences, and market dynamics.

---


### 796. [Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking](https://arxiv.org/abs/2610.17767)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Taehyeon Kim, Hyunsoo Lee, Youngsoo Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) achieve strong performance by externalizing explicit reasoning traces before producing the answer, yet suffer from overthinking challenge that allocates uniformly heavy computation to queries of varying difficulty. While proprietary models mitigate this via opaque routing, open-source LRMs still lack an efficient mechanism to internalize adaptive reasoning due to both expensive training cost and limited disclosure of training recipes. In response, we introduce RPO (Root-token Policy Optimization), a framework that enables LRMs to self-determine when to reason by training only the initial root token (e.g., whether to invoke the <think> tag) via group relative reward and group-wise advantages. By focusing on this pivotal branching point, RPO drastically reduces training overhead and VRAM usage. Across multiple model families and scales, RPO learns difficulty-aware adaptive thinking at just ~2% of the training compute of prior adaptive-reasoning methods.

---


### 797. [PaceReasoner: Label-Free Learning to Answer Briefly from Long Reasoning](https://arxiv.org/abs/2610.17900)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Changguo Jia, Zhiyou Xiao, Xinbei Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extended chain-of-thought reasoning improves problem-solving performance but increases inference cost and latency, motivating more accurate answers with shorter reasoning. We introduce PaceReasoner, a label-free test-time reinforcement learning framework that uses a model's LONG responses to improve its SHORT-mode accuracy. Both modes share a trainable policy, creating a need for reliable supervision, sufficient SHORT training samples, and continued LONG responses to guide learning. PaceReasoner combines all-response and LONG-only answer consensus through progressive, confidence-weighted supervision. A behavior reward gradually shifts from encouraging SHORT exploration to rewarding agreement with LONG answers, while a ratio controller regulates the balance between modes. Across three model backbones and four benchmarks, PaceReasoner improves average SHORT accuracy over the baselines by 7.4--13.5 percentage points, with fewer than 25 reasoning tokens per response on average. Ablations support the key components, and cross-dataset results demonstrate transfer beyond the adaptation set.

---


### 798. [FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention](https://arxiv.org/abs/2610.17901)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guoxia Wang, Qianyue He, Siming Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context training of large language and multimodal models couples structured attention masks (document, prefix-LM, share-question, sliding-window, block-sparse) with multi-node context parallelism, making the mask a dominant bottleneck. FlashMask's column-wise sparse mask compresses them from $O(n^2)$ to $O(n)$ via four query-axis boundary vectors, covering broad structured patterns. Implemented for Ampere GPUs, it neither exploits FlashAttention-3's TMA/WGMMA warp-specialized pipeline on Hopper nor supports distribution. The column-wise sparse mask is indexed by key positions but stores query-axis interval boundaries. Under any multi-chunk context-parallel assignment, it reduces per-rank mask localization to a provably zero-communication \emph{clip--shift--max} on the boundary vectors, compatible with the single-GPU kernel. FlashMask-3 introduces a mask-aware Hopper kernel with three-role warp specialization atop FlashAttention-3's TMA/WGMMA pipeline, plus a mask-aware distributed extension: zero-communication mask localization, a sparsity-aware load balancer (HCC-IPO), and a mask-aware compute-communication overlap with mask-driven communication pruning, whose forward all-gather uses topology-aware hierarchical routing. On a single H100 across 12 masks at 4K--128K context, it improves achieved TFLOPs over FlashMask, FlexAttention, and MagiAttention by 45--141%, 34--71%, and 2--44%. At context-parallel degrees 4--32 with 8K sequence per device, it attains 31--75% compute-communication overlap efficiency and improves throughput over Megatron-Core CP ring, Megatron-Core CP all-gather, and MagiAttention by $1.80\times$--$3.71\times$, $1.71\times$--$2.92\times$, and $1.09\times$--$1.46\times$. In end-to-end training of a 118B-A14B MoE at 128K on 128 H100 GPUs, it raises throughput by 7.3--11.0% over a Dual Chunk all-gather baseline, with attention forward+backward 24.5--44.9% faster.

---


### 799. [dMRI-F: A Foundation Model for Generalizable Diffusion MRI Analysis from Sparse Acquisitions](https://arxiv.org/abs/2610.17968)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xi Zhu, Yijie Li, Xiaofan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion MRI (dMRI) probes water diffusion within the brain, providing unique information about tissue microstructure and white matter connectivity. High-quality dMRI enables advanced and accurate analyses but demands dense acquisitions, resulting in long scan times and hardware constraints that are often infeasible. Further, dMRI requires dedicated computational methods to support diverse analysis tasks (e.g., parcellation, registration, and synthesis) for both neuroscientific and clinical applications. Here, we present dMRI-F, a foundation model that unifies dMRI data enhancement and downstream tasks across diverse acquisitions and populations, while requiring only minimal acquisition input. dMRI-F is pre-trained with a q-space masked reconstruction task: predicting densely sampled multi-shell data from only six volumes. It learns generalizable latent feature representations of dMRI data, which serve as a core foundation for adapting to diverse downstream tasks, including brain parcellation, brain registration, and cross-modal synthesis. Across nine independently acquired datasets, we demonstrate that dMRI-F outperforms state-of-the-art methods with robust generalization across acquisitions, populations, and tasks. Our results demonstrate dMRI-F's versatility as a general-purpose framework that enables diverse dMRI applications from low-cost, sparse acquisitions.

---


### 800. [Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents](https://arxiv.org/abs/2610.18082)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiyang Wu, Zhichao Liu, Shengxin zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents often struggle to recover from failures whose causes lie several steps earlier, beyond what local reflection or backtracking can resolve. We introduce BELIEFWEAVER, a framework that combines persistent evidence across attempts with prospective reasoning over repair directions. It maintains a relational belief state over frontiers, attempts, observations, and checkpoints. Execution evidence updates related frontier priorities across attempts and rollback, while diagnostic evidence gates execution. An implicit world model (IWM) evaluates repair hypotheses, predicts progress, and identifies relations among frontiers to guide exploration. We further distill these recurring IWM reasoning components into a 9B student through supervised fine-tuning and on-policy distillation (OPD). Across three terminal-based benchmarks, BELIEFWEAVER improves aggregate final score by 5.1 percentage points over native Terminus-2 continuation, with positive trends in exploration efficiency. The distilled 9B student improves final score by 9.8 percentage points over the reported native baseline while reducing estimated teacher API cost by 54.8% relative to the matched teacher. These results show that persistent evidence and prospective reasoning can improve recovery in long-horizon agent tasks while substantially reducing reliance on teacher-model inference.

---


> [!TIP]
> 当前位于：**751-800**（第 16/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
