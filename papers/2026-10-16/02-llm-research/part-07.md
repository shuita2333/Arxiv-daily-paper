# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-313**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-313**

---

### 301. [GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence](https://arxiv.org/abs/2610.20592)

**<font color=#1a73e8>作者：</font>** Haoyuan Li, Qihang Cao, Huanyuan Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference introduces substantial latency and computational overhead. We propose GeoThinker-$F$, an efficient framework that internalizes spatiotemporal perception by transforming causal MLLM hidden states into predictive latent world representations. Our key insight is that intermediate semantic representations contain sufficient information to predict useful representations of current geometry and future semantics, without requiring an exact reproduction of features from a dedicated 3D encoder. To realize this idea, GeoThinker-$F$ adopts a decoupled two-stage training strategy. In the first stage, the MLLM backbone is frozen while lightweight Latent Frame Prediction (LFP) heads learn from an offline 3D geometry expert and next-frame semantic targets. In the second stage, the external expert is removed, and the model is jointly optimized to generate and selectively integrate its self-predicted priors through a specialized Spatial-Grounded Temporal (SGT) Fusion module. Extensive evaluations show that GeoThinker-$F$ eliminates runtime dependence on external 3D geometry encoders while maintaining competitive performance across diverse spatial intelligence benchmarks. It achieves up to a $3.6\times$ inference speedup, reducing latency from $1.45\,\mathrm{s}$ to $0.40\,\mathrm{s}$ while retaining strong spatial reasoning performance.

---


### 302. [Co-Evolving Acting and Forecasting for Language Agents](https://arxiv.org/abs/2610.20597)

**<font color=#1a73e8>作者：</font>** Haofei Yu, Yixing Chen, Yining Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to construct well: (1) value targets come from the same single scalar signal for each step in the trajectory, and (2) observation targets, such as web pages and terminal logs, are long and noisy and reach only one step ahead. We propose \name, which adds a third kind of multi-step action targets. On successful on-policy trajectories, \name trains the policy backbone to generate the action sequences that follows each history. Each action is also supervised when forecast from the preceding histories, forming a temporal ensemble that the shared backbone absorbs during training, and this enables acting and forecasting to co-evolve. The policy still acts one step at a time at inference, with no overhead. Across five benchmarks (ALFWorld, ScienceWorld, WebShop, $\tau^2$-bench, and AppWorld), \name (1) achieves stronger aggregate performance than GRPO and RL baselines with predictive auxiliary targets across simulated environments, while improving overall performance on both realistic applications; (2) delivers up to $1.9\times$ and $2.0\times$ higher sample efficiency than ECHO and GRPO, respectively, on ScienceWorld; and (3) achieves these gains with a single policy backbone, without additional models, separate pretraining, or inference overhead. The codebase is available at this https URL.

---


### 303. [DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning](https://arxiv.org/abs/2610.20598)

**<font color=#1a73e8>作者：</font>** Qihang Cao, Haoyuan Li, Zihan Guo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. Our analysis reveals that this spatial--dynamic interference is highly non-uniform across parameter groups, with the balance between static and dynamic capabilities particularly sensitive to changes in late-layer MLPs. To address this interference, we propose DynThinker, a unified framework for jointly strengthening static and dynamic spatial reasoning. Decoupled Exponential Moving Average (D-EMA) applies configurable group-wise averaging to constrain drift in interference-sensitive pretrained parameters while preserving flexibility for capability enhancement. Spatial-Dynamic Fusion (SDF) complements D-EMA by selectively integrating spatial and temporal priors from a dynamic geometry encoder into intermediate VLM representations under semantic guidance. Across ten metrics spanning nine static 3D and dynamic 4D benchmarks, DynThinker achieves the highest average score among all evaluated models. Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

---


### 304. [CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation](https://arxiv.org/abs/2610.20603)

**<font color=#1a73e8>作者：</font>** Xiaoli Xu, Zhengtao Wu, Zhengze Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. Layout Thinker Optimization (LTO) aligns the rewriter with both caption and rendered-image quality via alternating domain-specific policy optimization. SKU-DiT, trained under Reinforce-Distill-Reinforce (RDR) progressive training, conditions jointly on the white-background product image, the trademark crop, and the structured layout to hold subject fidelity, trademark integrity, and character-level text accuracy together. The framework runs in production at a scale of millions of main images per day with a latency of a few seconds per image, which we believe makes it among the first systems of this kind to operate at commercial scale. We also release CommerceGen-Bench, a benchmark of hard cases collected from live traffic across all product categories. On it, our framework achieves the highest overall scores among the evaluated open-source baselines on both editing tracks, with and without prompt enhancement. It also matches much larger closed-source models, and beats several of them at Instruction Following and Product Integration - the two properties that determine whether an image can be published.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 305. [DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision](https://arxiv.org/abs/2610.19118)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yifan Lan, Zhongye Liu, Yurui Chang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emerging decision models such as JEV provide typed interfaces that map task instructions and observations directly to choices, judgments, and scores. As these models are increasingly used for automated decision-making, understanding their reliability under adversarial manipulation becomes critical. We introduce DecisionRobust, a benchmark for systematically evaluating the robustness of decision models across textual and visual inputs. Our benchmark covers practical decision-making scenarios and a diverse suite of attacks, including semantics-preserving text perturbations, image perturbations, and prompt injection in both modalities. We curate evaluation sets through external validity checks and cross-model candidate selection. We evaluate 30 model configurations on text tasks and 17 on vision tasks, including 24 and 12 held-out models, respectively, that are excluded from candidate selection. Our experiments reveal several key findings. First, attacks expose vulnerabilities beyond the models used for construction and selection, although optimized image perturbations transfer weakly to many targets even with multiple surrogates. Second, relative model robustness varies across tasks and attack types, and resistance to input perturbations does not necessarily imply resistance to prompt injection. Third, label-consistency checks substantially reduce measured attack success across text and image settings, highlighting the importance of validating apparent failures. The benchmark is available at this https URL.

---


### 306. [DTDD: Divergence-Triggered Dynamic Distillation for Reliable On-Policy Supervision](https://arxiv.org/abs/2610.19302)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qijia He, Zequn Li, Spencer Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense token-level supervision on student rollouts, but this supervision can become unreliable when the student and teacher diverge, either because of a large initial policy gap or compounding errors in long-horizon reasoning and tool use. We introduce Divergence-Triggered Dynamic Distillation (DTDD), an adaptive OPD framework that uses segment-level student-teacher divergence to trigger teacher takeover during training. When divergence triggers an intervention during reasoning, the student prefix continues to receive standard OPD supervision. The teacher then generates a recovery suffix, which the student learns through behavior cloning, using cross-entropy on the teacher-generated tokens. We evaluate DTDD in three regimes: long-horizon reasoning, distillation from a base initialization without offline supervised fine-tuning (SFT), and multi-turn agents. We also compare alternative trigger designs and teacher-intervention rates. DTDD reduces the post-warmup peak gradient norm by $8.6\times$ and, from a base initialization, reaches $21.3\%$ held-out math accuracy in $2.6\times$ fewer optimizer updates than OPD; both methods finish near $22\%$. It improves best-observed performance by $4.8$ and $4.1$ percentage points on ALFWorld with LoRA and agentic code, respectively. Ablations show that segment-averaged triggers outperform token-spike triggers. Behavior cloning is also more effective than the tested OPD surrogate for training teacher-generated recoveries. Across 23 experimental arms, takeover tends to help when the teacher substantially outperforms the OPD-trained student, provided that the teacher can recover from student-visited states, the student can learn those recoveries, and teacher intervention is neither excessive nor insufficient.

---


### 307. [MIPS: Mitigating Mode Collapse in Reinforcement Learning for Large Outcome Spaces](https://arxiv.org/abs/2610.19457)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Armaan Sandhu, Abhijeet Sinha, Dianbo Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expected-reward maximization in reinforcement learning concentrates probability mass on a few outcomes, even in tasks that require many distinct, high-quality solutions, a failure known as mode collapse. Inverse Probability Scaling (IPS) counters this in group-based policy gradients such as GRPO by dividing each reward by the outcome's probability, estimated from its frequency within the sampled group. When the outcome space is large relative to the group, outcomes rarely repeat and these estimates become uninformative. Since an outcome can be constructed along many trajectories, its probability is a sum over all of them, and computing it directly is intractable. We propose Marginal IPS (MIPS), which performs marginal evaluation by combining the sampled trajectory with a learned model of the trajectories that lead to each outcome. On Hypergrids, where the exact sampling distribution is computable, MIPS stays near the reward-distribution target as the outcome space grows relative to the rollout group, while frequency-based IPS degrades. In molecular synthesis and phylogenetic inference, MIPS sustains diverse, high-quality sampling where GRPO and frequency-based IPS collapse, showing that MIPS serves as a reliable solution to mode collapse in RL.

---


### 308. [Beyond Static Positional Encoding: Bayesian Time-aware Attention for Non-Stationary Long-term Time Series Forecasting](https://arxiv.org/abs/2610.19603)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinjie Lan, Yunbo Mei, Leheng Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have demonstrated strong performance in long-term time series forecasting (LTSF), yet modeling non-stationary temporal dependencies remains challenging. In this paper, we interpret self-attention as a Bayesian posterior over attended positions, combining a content-based prior induced by scaled dot-product similarity with a temporal-evidence likelihood induced by positional encoding. This formulation provides a probabilistic interpretation of how positional encoding shapes the temporal dependencies captured by self-attention. Building on this perspective, we derive a population-level evidence lower bound (ELBO) that characterizes the role of positional encoding in forecasting weakly stationary time series. Our analysis further highlights a limitation of static positional encoding: when temporal dependence structures vary across input windows, a fixed temporal bias must accommodate heterogeneous dynamics and can therefore be suboptimal for non-stationary forecasting. Motivated by this analysis, we propose Bayesian Time-aware Attention (BTA), which employs a mixture-of-experts (MoE) router to adaptively combine temporal kernels and generate input-conditioned, head-specific positional biases. Extensive experiments on standard LTSF benchmarks demonstrate that BTA consistently improves forecasting performance across multiple Transformer backbones and achieves competitive overall performance with modest computational overhead and stable training.

---


### 309. [When Does Depth Help? Understanding Layerwise Inference in Tabular Foundation Models](https://arxiv.org/abs/2610.19814)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenwen Gong, Haotian Gu, Zhen Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based tabular foundation models (TFMs) achieve state-of-the-art performance on small to medium-sized tabular prediction tasks while processing diverse inputs through a shared stack of layers. Recent layerwise analyses identify strong predictive performance in early TFM representations and substantial overlap in computation across layers. However, early predictive accessibility alone does not establish whether later layers are dispensable for every input, and aggregate accuracy can obscure which inputs benefit from additional computation. We study all 24 in-context-learning layers of TabPFN-3 across 272 classification datasets, combining representation geometry, prediction trajectories, truncation, and structural interventions, while also examining related representation dynamics in four additional TFMs. We uncover a pronounced expansion-compression trajectory, with stronger late dimensional contraction associated with larger increases in class-prototype separation. A targeted analysis of early-stabilizing samples shows that substantial representational changes persist after predicted classes stabilize, while locally ambiguous queries obtain larger accuracy gains from shallow to late layers than well-separated queries. Repeating a single pretrained block or perturbing layer order reduces predictive performance on average, constraining simple post-hoc substitutions in the frozen model. These findings distinguish predictive accessibility, class stability, and the benefits of continuing computation, supporting an input-dependent assessment of depthwise redundancy in TFMs.

---


### 310. [StreamErase: Towards Ultra-Fast Streaming Video Erasing](https://arxiv.org/abs/2610.20137)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhuobai Dong, Xiaobing Tu, Xiantao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current video object removal methods suffer from prohibitive latency (minutes per video) and non-causal processing that prevents real-time interaction. We present StreamErase, enabling sub-second latency with up to 26 FPS streaming generation on a single GPU. Our approach first augments a text-to-video model with mask input to generate high-quality videos that erase target objects and synthesize coherent backgrounds, but does not perform inference on the fly. As such, we progressively transfer the erasing capability from a powerful bidirectional foundation model to an efficient unidirectional streaming eraser, enabling long-horizon erasing without sacrificing visual fidelity. Several key challenges arise when generating videos over long, potentially infinite horizons: (1) bridging the domain gap from training on finite length and extrapolating to long horizons, (2) sustaining high quality by preventing error accumulation, and (3) maintaining fast inference, without increasing computational cost as the context grows. To address these challenges, we carefully designed sliding-window causal attention with attention sinks. By incorporating self-rollout with attention sinks and KV cache rolling during training, we simulate inference-time extrapolations with a fixed context window, enabling constant-speed generation of arbitrarily long videos. Finally, we establish a dedicated benchmark, LongErase, for streaming long-video object removal. Our model achieves strong performance compared to existing video object erasing models and generalizes well to real-world video scenarios, uniquely enabling infinite-length streaming. With StreamErase, users can input a mask and see the erasing results unfold in real-time, delivering a truly interactive experience.

---


### 311. [Training Dynamics of Transformers on Unbounded Inputs: Attention Learning Can Lag Output Layer Learning](https://arxiv.org/abs/2610.20337)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yaomengxi Han, Debarghya Ghoshdastidar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of transformers is attributed to several factors, including their capacity to express formal languages over variable-length inputs, and ability of the attention mechanism to focus on relevant input features. However, there is limited understanding of the training dynamics of shallow transformers, specifically how to decouple the learning of the attention and the output (feedforward) layer. A natural extension of the theory of one-step gradient feature learning in feedforward networks suggests that one could first learn the attention weights with a single gradient step, and then train the output layer. We show that this fails for a shallow transformer trained to recognize a star-free language from unbounded-length input. We prove that the transformer can be trained to recognize the language with a three-phase gradient descent: the output layer is updated first, followed by an attention update, and the output layer is fine-tuned in the third phase. In contrast, the language cannot be learned by training only the attention or output layer, or by a single attention-layer update followed by finetuning the output layer. We empirically show that ``attention learning lagging output layer learning" is beneficial in other language recognition, regression, and in-context learning tasks as well.

---


### 312. [Learning by Examples: Power Grid Steady State Analysis with a Tabular Foundation Model](https://arxiv.org/abs/2610.20462)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Olayiwola Arowolo, Oluwadara Adedeji, Peter Palensky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models have shown strong generalization across scientific domains, but their use in power systems remains largely task-specific. We investigate whether a pretrained tabular foundation model (TFM), TabPFN, can serve as a general-purpose neural solver for power grid steady-state analysis. We evaluate the TFM on three tasks: power flow (PF) prediction, N-k contingency screening (NCS), and voltage stability margin (VSM) prediction. We performed experiments on 118- and 2000-bus systems, comparing the TFM against task-specific neural baselines. Without retraining or fine-tuning, the TFM matches or outperforms the best task-specific model in several settings across the three tasks. For 118-bus PF prediction, a variant of the TFM achieves errors of $1\times 10^{-3}$ pu for voltage magnitudes and $0.30^\circ$ for voltage angles, outperforming all baselines. On unseen N-1 contingency and close-to-infeasible PF cases, the TFM is competitive with the DCPF approximation. For millions of unseen N-2 contingencies, the TFM achieves AUCs of 0.92 and 0.95 for branch and voltage violation screening, respectively. The TFM also attains accurate VSM prediction performance for the 2000-bus system with limited labelled data. The TFM attains strong results across the tested tasks despite pretraining without any power-system-specific dataset and requiring no fine-tuning step. These results offer a glimpse into the potential of pretrained TFMs as a neural solver for a range of power grid analysis tasks.

---


### 313. [Quantifying privacy risks in foundation model representations of brain MRI](https://arxiv.org/abs/2610.20494)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Imen Bajar, Héber Hwang Arcolezi, Antoine Boutet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained representations are increasingly used to share and reuse information from medical images without exposing the original scans, but it is unclear how much patient-specific information these representations retain. We investigate this question for brain magnetic resonance imaging (MRI) by evaluating five frozen pretrained encoders spanning different architectures, pretraining objectives, and training domains on two longitudinal T1-weighted datasets, OASIS-2 and MIRIAD. Under an attacker model with access to released embeddings, the corresponding public encoder, and auxiliary MRI scans, we evaluate patient linkage and sensitive-attribute inference. Across the evaluated representations, we observe substantial subject-specific information: rank-1 patient linkage reaches up to 99\% on MIRIAD and exceeds 90\% on OASIS-2 for the highest-risk representation, despite the absence of an identification objective during encoder training. We further show that the released embeddings retain information about a demographic attribute, with recorded-sex prediction reaching balanced accuracy of 90.9\% on OASIS-2 and 95.5\% on MIRIAD. Overall, our results demonstrate that replacing raw brain MRI with learned embeddings does not, by itself, eliminate patient-linkage or attribute-inference risk, and is therefore insufficient on its own to establish anonymity.

---


> [!TIP]
> 当前位于：**301-313**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-313**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
