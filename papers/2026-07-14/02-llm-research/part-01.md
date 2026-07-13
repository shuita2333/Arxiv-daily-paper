# 🧠 大模型相关研究 | 2026年07月14日

> 本类共 **68** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-68](./part-02.md)

---

### 1. [CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions](https://arxiv.org/abs/2607.08774)

**<font color=#1a73e8>作者：</font>** Vanessa Figueiredo, Wilter Franceschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliability in large language model (LLM) systems is typically framed as a function of model capability. We challenge this by demonstrating that reliability is significantly influenced by \emph{inference-time control} -- the computational layer governing task framing and context selection. We introduce \emph{CogniConsole}, an architectural instantiation that externalizes this control into a structured interface combining programmatic coordination with bounded prompt-based reasoning. Through \emph{controllability-oriented probes} ($N=489$) in a multi-step interactive environment, we show that increasing structural scaffolding -- from unstructured to fully scaffolded -- \textbf{systematically reduces output variance and failure rates under a fixed model architecture}. Our results indicate that many observed failure modes, such as context drift and inconsistent constraint adherence, arise from under-specified control rather than insufficient capability. This work provides an empirical basis for treating inference-time control as a first-class abstraction, opening new directions for designing and evaluating LLM systems beyond scaling alone.

---


### 2. [HALO: Hybrid Adaptive Latent Reasoning for Language Models](https://arxiv.org/abs/2607.08775)

**<font color=#1a73e8>作者：</font>** Micah Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how to improve a frozen pretrained language model with a small amount of adaptive extra computation. A simple approach is to add additional refinement steps on top of the backbone hidden states, but fixed extra refinement can be wasteful: a one-step refinement head may be too weak, while forcing a second full-sequence refinement step everywhere can increase compute without improving transfer. We introduce HALO, a hybrid adaptive latent-refinement method that combines a coarse refinement stage with selective second-stage latent refinement on a subset of tokens chosen by token scoring and monotonic token halting. On the main public benchmark comparison built from MMLU-Pro and GPQA-Diamond, HALO achieves the best overall average among the paper-facing methods, outperforming the frozen backbone, fixed-1, and fixed-2. Internal analysis further shows that HALO reaches nearly the same token-accuracy level as fixed-2 while using fewer average applied refine steps than fixed-1 and far fewer than fixed-2. These results suggest that the key advantage is not simply more refinement, but a better allocation of refinement: HALO achieves the strongest paper-facing result while also using less measured controller compute than either fixed baseline.

---


### 3. [A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions](https://arxiv.org/abs/2607.08776)

**<font color=#1a73e8>作者：</font>** Qingzhuo Wang, Ruiyang Qin, Zhenxin Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the success of knowledge distillation (KD) in Large Language Models (LLMs), the underlying mechanism behind its efficacy remains unclear. In this paper, we propose a unified approach to explore the common mechanism of various KD methods using interactions. Specifically, we decompose the output score of the LLM into the sum of numerous interactions. Each interaction represents a nonlinear relationship involving a set of input variables (e.g., words). Based on the decomposed interactions, we discover that the common mechanism underlying various KD methods is the sparsification of interactions, i.e., student models retain fewer interactions for inference while suppressing other interactions to zero effects. Furthermore, we discover that the performance variance across different KD methods arises from their capabilities in handling complex interactions. A KD method typically yields better performance if it enables the student model to achieve higher sparsity of complex interactions. Motivated by these insights, we propose a plug-and-play loss function called Complex Interaction Penalty (CIP) to explicitly enforce the sparsity of complex interactions during the distillation process. Extensive experiments demonstrate that integrating CIP consistently improves the performance of diverse KD methods on both in-domain and out-of-distribution benchmarks.

---


### 4. [iLENS: Interpretable LLM-Guided Mixture-of-Experts for Neuroimaging Survival Analysis](https://arxiv.org/abs/2607.08778)

**<font color=#1a73e8>作者：</font>** Farica Zhuang, Seong Woo Han, Zixuan Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimer's Disease (AD) is a complex neurodegenerative disorder that continues to impact millions of people worldwide. Predicting AD conversion during the prodromal stage remains critical for disease understanding and patient care. As such, survival models are widely used for AD risk prediction, yet they are typically static predictors with limited interpretability and no capacity for natural language reasoning. In this work, we propose iLENS, an interpretable large language model (LLM) guided framework based on mixture-of-experts (MoE) for survival prediction in AD conversion. Our approach uses LLM to synthesize structured neuroimaging measurements and unstructured information to guide expert routing. Our framework demonstrates competitive predictive performance and capability in patient subtyping. Furthermore, our framework provides transparent, biologically grounded rationales for its routing decisions, bridging the gap between high-performance survival analysis and interpretable clinical decision support.

---


### 5. [Signed Symmetric Quantization for Few-Bit Integers](https://arxiv.org/abs/2607.08779)

**<font color=#1a73e8>作者：</font>** Ian Colbert, Eashan Dash, Pablo Monteagudo-Lago 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The signed integer alphabet contains one more negative representable value than positive. Yet, by convention, the standard symmetric integer quantizer fixes its scale to be strictly positive, which assigns this extra representable value to the negative tail and can force clipping of positive outliers. In this work, we show that, at few-bit precision, such clipping is a non-trivial source of quantization error. Asymmetric quantization addresses this problem with a zero point, shifting the grid toward the observed data range; however, this flexibility is well-known to carry a runtime penalty. For example, in this http URL on an AMD EPYC(TM) "Turin" CPU, a 4-bit symmetric format uses up to 9% less memory with up to 2.45$\times$ higher throughput than its asymmetric counterpart. We highlight signed symmetric quantization as a third option that retains the runtime profile of symmetric quantization without the penalty of the asymmetric format: our signed absmax grid places the extra representable value on the dominant-outlier tail through a principled and lightweight sign selection rule while keeping the zero point at zero. Our theoretical analysis offers two main results. First, we establish the signed absmax grid as conditionally bound-optimal on $\ell_2$ quantization error, and show that the condition holds for 88-99% of weight groups across pre-trained large language models (LLMs) at low bit widths. Second, we show that negating the scale of a standard symmetric quantizer is analytically equivalent to a unit zero point shift on the same signed integer alphabet. We empirically validate our proposal on models from the Qwen3, Qwen3.5, and Llama3 families, and observe improvement in perplexity and downstream few-shot accuracy over the standard unsigned symmetric quantizer at no extra inference cost

---


### 6. [Sticky Routing: Training MoE Models for Memory-Efficient Inference](https://arxiv.org/abs/2607.08780)

**<font color=#1a73e8>作者：</font>** Ali Kayyam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models activate only a sparse subset of experts per token, yet consecutive tokens frequently activate different experts -- causing constant weight swapping between slow storage and fast memory on edge devices. Existing remedies are either system-level (caching heuristics) or post-hoc (router fine-tuning), leaving the root cause unchanged during pretraining. We propose StickyMoE, a differentiable routing consistency loss that penalises abrupt expert switches between adjacent tokens, encouraging the router to maintain the same expert assignment across semantically coherent spans. StickyMoE requires no architectural changes, adds a single hyperparameter lambda, and unlike post-hoc methods, allows expert representations and routing decisions to co-adapt from the first training step. Experiments on small-scale MoE language models show that StickyMoE reduces the expert switch rate by up to 60% with less than 4% perplexity degradation, Pareto-dominating post-hoc fine-tuning on the quality-locality frontier. Routing temporal locality is most efficiently instilled at training time.

---


### 7. [Reward Transport: Property Control in Flow Matching via Noise-Space Alignment](https://arxiv.org/abs/2607.08781)

**<font color=#1a73e8>作者：</font>** Kehan Guo, Yili Shen, Yujun Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The coupling in flow matching -- the rule pairing noise vectors with data points -- is typically treated as a computational choice. We show that this coupling can instead serve as an alignment interface: by matching noise and data according to a target molecular property, it embeds controllable structure directly into the learned flow field. Building on this view, we introduce Reward Transport, which uses optimal transport coupling at training time to align a scalar noise-space coordinate with molecular rewards; at inference, varying this coordinate steers the generated distribution without requiring an oracle, reward model, gradient guidance, or additional computation. In the coupling-preserving limit, thresholding this coordinate recovers the Cross-Entropy Method's truncated reward distribution, providing a principled, continuously adjustable distribution-level control knob. Empirically, on ZINC-250K and GuacaMol, sweeping the scalar induces monotone control of logP and consistent QED control over its operating range; most tellingly, the same knob produces opposite structural responses for different targets, growing molecules for logP but shrinking them for QED, which rules out a generic size bias. The interface is complementary to classifier-free guidance and conditional flow matching, while a negative result under epsilon-prediction diffusion clarifies where coupling-level alignment is structurally absent. Code: this https URL

---


### 8. [Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement](https://arxiv.org/abs/2607.08782)

**<font color=#1a73e8>作者：</font>** Qianli Liu, Kaibin Guo, Zicong Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expert parallelism has become the prevailing paradigm to serve Mixture-of-Experts (MoE) models. Its efficiency depends on the communication and computation latencies of the GPUs, which are linked to the placement of experts in the GPUs. Existing works for optimizing expert placement focus on leveraging past requests' expert activation patterns. However, they demonstrate deficiencies facing diverse and rapidly changing request patterns, calling for an online, proactive approach. Implementing such an approach requires addressing several challenges: the uncertainty associated with incoming requests' expert activation, the cost of expert migration, and the NP-hard complexity in optimization. Therefore, we present Director, a new distributed MoE serving system that minimizes end-to-end latency via prediction-driven, online expert placement. Director uses either a lightweight cascaded predictor or a low-bit quantized replica for expert activation patterns of incoming requests. An online migration module then enacts the changes with near-zero downtime by executing migrations in compute-bound phases, keeping disruption bounded. At its core, a relaxation-based expert placement optimizer operates under capacity constraints, runs in polynomial time, and achieves a $(1+\epsilon)$ approximation ratio. Finally, we implement a prototype and demonstrate, through extensive experiments, a reduction in end-to-end latency of $11\sim55\%$ for popular MoE models (e.g., Mistral, DeepSeek and Qwen) compared to existing work.

---


### 9. [Accelerating GPU Inference of Large Language Models with Moderately Unstructured Sparse Weight Matrices](https://arxiv.org/abs/2607.08786)

**<font color=#1a73e8>作者：</font>** Tao Lu, Haoyu Wang, Zonghui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing deployment of large language models (LLMs), LLM inference cost has become a key challenge. Pruning techniques that introduce sparsity into weight matrices can accelerate inference. However, maintaining model quality typically limits pruning to moderate unstructured sparsity (around 50\%). At these sparsity levels, none of the existing GPU kernels for sparse matrix multiplication (SpMM) can outperform their dense counterparts. This paper proposes an efficient GPU inference method for LLMs with moderate sparsity. We propose a three-layer matrix storage format comprising: (i) a Sparse-TC layer enabling sparse tensor cores to accelerate SpMM; (ii) a Slot-Filling layer using parallel differential distance for matrix compression while supporting low-cost on-chip decoding; (iii) a lightweight Residual Layer ensuring correct SpMM computation. Building on this format, we design a SpMM kernel that jointly utilizes sparse tensor cores and CUDA cores. This design enables an efficient execution pipeline and overlaps on-chip computation with memory access. Evaluations show that our work is the first to outperform dense matrix multiplication on modern GPUs equipped with high-bandwidth memory (HBM). It achieves up to 1.64x kernel-level speedup over SpInfer (EuroSys'25, Best paper) and up to 1.41x end-to-end speedups over FlashLLM (VLDB'24). Our source code: this https URL.

---


### 10. [Prompt-Driven Exploration](https://arxiv.org/abs/2607.08837)

**<font color=#1a73e8>作者：</font>** Sunshine Jiang, John Marangola, David Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration is essential to RL since a policy cannot improve by repeatedly sampling the behaviors it already prefers. Standard methods inject stochasticity in the action space, but such jitter only yields rollouts close to the original. Escaping a weak policy often requires global perturbations that action noise cannot produce. Large language models (LLMs) and vision-language-action (VLA) models offer a pathway: they condition the policy on a natural language prompt, and since the rollout follows from it, modifying the prompt induces global changes. The challenge is finding prompts that induce useful global changes. With a weak policy that rarely succeeds, reward is too sparse to select on. Our idea is to refine prompts from the rollouts themselves: a vision-language model (VLM) reasons over the rollout video, diagnoses how the policy responded, and rewrites the prompt to elicit better behavior next time. This procedure realizes posterior sampling, a classical RL exploration framework, at the level of prompts: the VLM maintains an implicit distribution over useful prompts and updates it from observed rollouts. We call this strategy Prompt-Driven Exploration (PDE). Across manipulation and reasoning tasks, PDE enables RL to learn successful policies even from zero-reward starts, and improves sample efficiency more broadly. Our website is available at this https URL.

---


### 11. [Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing](https://arxiv.org/abs/2607.08839)

**<font color=#1a73e8>作者：</font>** Dominick Reilly, Qiyu Wu, Hiromi Wakaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are typically designed under the assumption that all modalities available during training will also be accessible at inference. However, many real-world settings violate this assumption, requiring models to operate under a privileged modality setting, where auxiliary modalities are available only during training. While these modalities contain valuable information, existing MLLMs largely fail to leverage them effectively, as they treat modalities as interchangeable inputs rather than sources of complementary supervision. We propose Mixture of Probes (MoP), a novel framework that disentangles modality-specific and modality-general signals within the MLLM, allowing the model to preserve modality-dependent structure while learning transferable representations across modalities. At its core, MoP achieves this through a structured probing mechanism that extracts and organizes information from intermediate representations of a shared modality encoder, rather than relying only on final-layer alignment as done in existing MLLMs. To support this disentanglement, we further introduce MoP Cross-modal Training (MoP-X), a training strategy for MoP centered around a probe disentanglement loss that prevents probe collapse and encourages cross-modal learning. We evaluate MoP across two domains spanning eight tasks and four modalities under a comprehensive evaluation protocol tailored to the privileged modality setting, where each modality is independently treated as the sole input at inference time. MoP consistently outperforms strong MLLM baselines, achieving up to 65% relative improvement, demonstrating that auxiliary modalities, even when unavailable at inference, can provide substantial gains when effectively leveraged during training. Code, model checkpoints, and evaluation protocols will be made available at this https URL.

---


### 12. [Optimizing Against Safety Representations: Activation-Guided Adversarial Suffixes and the Geometry of Refusal](https://arxiv.org/abs/2607.08883)

**<font color=#1a73e8>作者：</font>** Ege Çakar, Hannah Guan, Kayden Kehe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral alignment in large language models often masks fragile internal safety representations. Recent work suggests that refusal behavior is mediated by low-dimensional directions in activation space. This raises questions about how such representations are structured, localized, and accessed by optimization. We study adversarial suffix attacks as a probe of representational alignment. We introduce Activation-Guided GCG, which replaces output-based objectives with losses that directly target a model's internal refusal direction. Across several objective variants, we find that suppressing refusal globally across all layers and positions is more effective than targeting a single layer-position pair. This suggests that safety representations are distributed across the forward pass rather than causally localized to a single site. We further introduce Soft-GCG, a continuous relaxation of discrete suffix optimization using Gumbel-Softmax. Soft-GCG achieves a 33 $\times$ speedup over standard GCG while improving attack success rates. Evaluating across model scales, we find that smaller models remain vulnerable while larger models resist both activation- and suffix-based attacks at our compute-constrained settings, consistent with larger and better safety trained models being harder to jailbreak. Together, our results clarify how safety mechanisms are encoded and can be broken in contemporary models. These insights provide concrete guidance for designing more robust and representation-aware alignment strategies.

---


### 13. [GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning](https://arxiv.org/abs/2607.08894)

**<font color=#1a73e8>作者：</font>** Maureese Williams, Dymitr Nowicki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have shown promise in multi-step planning tasks, but existing approaches like LATS (Language Agent Tree Search) and ReAct rely heavily on LLM inference during planning, leading to high computational costs and stochastic behavior. We present \textbf{GATS} (Graph-Augmented Tree Search), a planning framework that combines systematic UCB1-based tree search with a layered world model to eliminate LLM calls during inference while achieving superior planning performance. Our three-layer world model integrates: (L1) exact symbolic action matching, (L2) statistics learned from execution logs, and (L3) LLM-based prediction for unknown actions. On synthetic planning tasks with branching paths and dead-ends, GATS achieves \textbf{100\% success rate} compared to 92 % for LATS and 64\% for ReAct. On a comprehensive stress test spanning 12 challenging scenarios -- including coding workflows, web navigation, and long-horizon tasks -- GATS maintains \textbf{100\% success} while LATS drops to 88.9 % and ReAct to 23.9%. GATS requires \textbf{zero LLM calls per task} during planning (vs. 37 per task for LATS) and produces deterministic plans with zero variance across runs. Our results demonstrate that systematic search with learned world models can substantially outperform LLM-guided exploration for agent planning.

---


### 14. [BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving](https://arxiv.org/abs/2607.08930)

**<font color=#1a73e8>作者：</font>** Yuanjie Zhu, Liangwei Yang, Ke Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient serving of diffusion large language models (dLLMs) is hindered by convergence heterogeneity: when batching multiple requests, different sequences converge at different rates, causing faster requests to stall behind slower stragglers and introducing compute bubbles and tail latency. We present BlockServe, a continuous batching framework that integrates block-grained scheduling -- immediately evicting completed requests at block boundaries -- with mixed-state execution that extends dual cache and parallel decoding to heterogeneous batches via gather-scatter indexing. Furthermore, a compute-aware admission controller expands effective batch capacity through token-budgeted refill. On Dream and LLaDA across five benchmarks, BlockServe achieves 1.9--10.6$\times$ throughput over Fast-dLLM with comparable generation quality, establishing block-grained scheduling as a foundation for high-throughput offline dLLM inference.

---


### 15. [TSRouter: Dynamic Modality-Model Selection for Time Series Reasoning](https://arxiv.org/abs/2607.08940)

**<font color=#1a73e8>作者：</font>** Fangxu Yu, Tao Feng, Dehai Min 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series reasoning is essential for real-world problem-solving. While both Large Language Models (LLMs) and Vision-Language Models (VLMs) can reason about time-series data, their capabilities are complementary: LLMs process time series as text sequences and thus preserve exact numerical understanding, but struggle with global patterns, whereas VLMs efficiently capture these patterns by visualizing time series but may lose fine-grained details. Moreover, models vary significantly in task-specific expertise and inference costs. Dynamically selecting the most suitable modality and model for each query is therefore crucial, yet challenging because it requires modeling the complex interactions among tasks, queries, modalities, and models, which carry rich contextual signals. To this end, we introduce TSRouter, a graph-based dynamic routing framework. TSRouter constructs a heterogeneous graph of task, query, modality, and model nodes to contextualize the interactions among query characteristics, modality attributes, and model capabilities. TSRouter formulates routing as a candidate scoring problem, where each modality-model pair is evaluated based on user-defined performance-cost preferences to select the optimal candidate. Comprehensive evaluations on 4 distinct time series reasoning tasks reveal that TSRouter substantially outperforms diverse baselines with 16\% to 46\% relative improvements. Furthermore, TSRouter demonstrates robust zero-shot plug-and-play generalization to unseen models and novel tasks and preserves high performance while reducing computational overhead through cost-aware optimization. Our code is available at this https URL.

---


### 16. [Micro-level AI Feedback Features and Student Responses in Consecutive LLM Tutoring Interactions](https://arxiv.org/abs/2607.08952)

**<font color=#1a73e8>作者：</font>** Shayla Sharmin, Mohammad Fahim Abrar, Roghayeh Leila Barmaki  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-assisted feedback research has shown that micro-level feedback features, such as concrete elaboration, affective language, and response length, are associated with learning outcomes. Existing studies have primarily examined these features using session- or task-level measures. We examine how feedback provided in one user-AI interaction is associated with student confusion and understanding in the immediately following interaction in a naturalistic tutoring setting. We focus on three micro-level features of AI feedback: concrete elaboration (analogies, comparison-based explanations, or worked examples), affective language (encouragement, empathy, or apology), and response length. We analyzed 16,851 conversational user-AI interactions from the StudyChat dataset, a naturalistic record of student interactions with an LLM tutor in an undergraduate AI course, and identified 1,718 cases in which students expressed confusion and continued to a subsequent interaction. Using chi-square tests and Generalized Estimating Equations (GEE), we found that concrete elaboration was associated with higher understanding and lower re-confusion in the student's next interaction. Empathetic language showed no significant association with either outcome, while longer responses were independently associated with lower understanding. These findings highlight the value of examining feedback across consecutive user-AI interactions and suggest that concrete elaboration may play an important role in supporting immediate student understanding.

---


### 17. [Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution](https://arxiv.org/abs/2607.08960)

**<font color=#1a73e8>作者：</font>** Ning Liu, Kalle Kujanpää, Zhaoxuan Zhu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Warehouse operations are governed by Standard Operating Procedures (SOPs) that encode complex, multi-system decision logic, which must be executed reliably under strict time constraints, yet LLM agents lack mechanisms to enforce procedural compliance and degrade under the context overload full SOP specifications introduce. We present Eluna, a production-deployed agentic system for reliable SOP execution. Eluna is a graph-guided, multi-agent framework that encodes SOPs as directed acyclic graphs with progressive disclosure and delegates independent tasks to parallel sub-agents, each with persistent code execution and live data access. To meet production latency and accuracy needs, we use asymmetric episodic distillation where a strong teacher is improved through episodic error memories, then a smaller student is fine-tuned on the corrected trajectories with memory stripped, internalizing corrections without inference-time overhead. On a 13-task benchmark and two production applications, our fine-tuned models match or exceed their teacher, beat all larger off-the-shelf baselines, and reach 94% expert agreement on the ticket processing application.

---


### 18. [NL-PAC: Specification Ambiguity and Certified Minimax Risk Floors in LLM-Mediated Supervision](https://arxiv.org/abs/2607.08961)

**<font color=#1a73e8>作者：</font>** Berkay Anahtarci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly provide labels, evaluations, and feedback for tasks specified in natural language. When a specification admits multiple readings but the supervision channel does not reveal which is operative, additional labels reduce sampling error without resolving the resulting identification problem. We introduce Natural Language PAC (NL-PAC), a framework that uses a fixed model's thresholded decoding law to define admissible labels and candidate targets. The probability that multiple labels are admissible equals the diameter of the pointwise-admissible target class, and under target-blind supervision every learner incurs worst-case risk of at least half this diameter, at every sample size; the exact randomized minimax risk over this class is attained by a data-independent strategy. Finite-sample confidence bounds make these quantities certifiable from held-out unlabeled inputs. In a frozen Qwen~2.5--3B audit, one prespecified prompt yields a positive model-relative certificate, whereas a paraphrase and exact-rule controls yield zero. A held-out bridge audit finds that supplied candidate reading clauses fail the admissibility condition needed to transfer the certificate to coherent readings. The guarantee is specific to the audited model, prompt, threshold, and input distribution; extending it to human interpretations requires external validation.

---


### 19. [Sensitivity-Aware Thresholding and Token Routing for Activation Sparsification in Large Language Models](https://arxiv.org/abs/2607.08991)

**<font color=#1a73e8>作者：</font>** Bishmoy Paul, Youngmin Yi, Hoeseok Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient inference in Large Language Models (LLMs) requires deciding where computation can be reduced while preserving model quality. We study this problem through multilayer perceptron (MLP) activation sparsification and token-level conditional routing. We first propose Sensitivity-Aware Thresholding for Sparsity (SATS), a threshold calibration method to choose layerwise gate thresholds using a local MLP output sensitivity proxy rather than calibrating thresholds directly from activation percentiles. While SATS retains the existing mechanism of sparsifying MLP activations by thresholding gate activations, it replaces percentile-based calibration with a sensitivity-aware selection rule. We then introduce a lightweight token routing framework that dynamically selects between a base path and a modified path on a per-token basis, rather than applying the modified computation uniformly to all tokens. We evaluate both methods on multiple recent open-weight LLMs. Our results show that SATS improves over the threshold-based sparsification baseline at matched actual sparsity and that token routing yields a more favorable quality-throughput trade-off than static activation modification baselines. Overall, our results suggest that improved threshold calibration and token routing can improve the quality-throughput trade-off in LLMs.

---


### 20. [C-GAP: Class-Aware and Online Prompting Improves Vision-Language Models on Imbalanced Classes](https://arxiv.org/abs/2607.09008)

**<font color=#1a73e8>作者：</font>** Francis Fernandez, Arash Jahangiri, Salimeh Sekeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safety-critical perception systems must reliably detect rare object classes within small label spaces, a setting that long-tailed detection methods, designed for hundreds of classes with dense annotation, fundamentally do not address. Open-vocabulary detectors offer a promising alternative, as they use natural language queries at inference time, making prompt quality a first-class lever for detection performance. We exploit this property to address class imbalance: rather than retraining models or collecting additional annotations, we ask whether iteratively refining the language prompts, fed to frozen detectors, can improve minority class detection. We introduce C-GAP Caption-Guided Augmentation and Prompting), a detector-agnostic, annotation-free framework that operates in two phases. First, we establish a composite caption baseline combining per-image scene descriptions with class-quantity context, which we show outperforms scene-description only or class-quantity-only prompts across multiple open-vocabulary architectures and benchmarks. Second, an LLM iteratively refines each image's caption individually, with trials triaged into accept, tentative, or regenerate buckets based on minority-class AP@0.5 against a dynamic threshold derived from the composite baseline. Refinement terminates early once sufficient AP@0.5 gain is achieved. No detector weights are updated at any stage. Our experiments shows that C-GAP improves minority-class average precision up to 53% over the baselines. On COCO, C-GAP improves minority-class AP@0.5 by ~81% relative over the composite baseline (17.69 -> 32.09). Experiments confirm that composite captions provide the critical foundation for effective refinement: using scene-description-only or class-quantity-only prompts as the refinement starting point yields diminishing returns, supporting both stages of C-GAP as necessary contributions.

---


### 21. [Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing](https://arxiv.org/abs/2607.09015)

**<font color=#1a73e8>作者：</font>** Ajay Narayanan Sridhar, Ronak Singh, Mehrdad Mahdavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study contextual bandit problems with correlated arms and access to surrogate reward signals produced by a machine learning model, motivated by applications such as large language model (LLM) routing. Unlike classical contextual bandits that rely solely on bandit feedback and assume conditional independence across arms, our setting allows context-dependent inter-arm correlations and auxiliary reward information that may be noisy or misspecified. We propose algorithms that leverage such surrogate rewards through two complementary designs. A coupled reward-mixing approach pools true and surrogate rewards to accelerate learning when surrogate signals are reliable, while a decoupled prediction-mixing approach maintains separate estimators for bandit feedback and surrogate rewards and adaptively combines their predictions. This decoupling yields robustness to surrogate misspecification, recovering regret guarantees comparable to reward-only bandit methods in the worst case, while achieving improved regret when surrogate predictions are sufficiently informative. We provide theoretical regret analyses for both approaches and evaluate them on LLM routing benchmarks under varying accuracy versus cost trade-offs. The results demonstrate improved sample efficiency and consistently better accuracy-cost trade-offs compared to standard contextual bandit baselines and strong static routing methods.

---


### 22. [Video Generation Models are General-Purpose Vision Learners](https://arxiv.org/abs/2607.09024)

**<font color=#1a73e8>作者：</font>** Letian Wang, Chuhan Zhang, Rishabh Kabra 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by next-token prediction, NLP shifted from task-specific models into powerful generalist foundation models. What, then, is the equivalent catalyst needed to achieve a general-purpose model in computer vision? In this paper, we contend that large-scale text-to-video generation serves as a strong pre-training paradigm for computer vision, providing the necessary spatiotemporal priors, vision-language alignment, and scalability required for general visual intelligence. We introduce GenCeption, which leverages a pre-trained video generative diffusion backbone to define a feed-forward perception model, capable of performing various vision tasks steered by text instructions. Empirical results demonstrate that GenCeption achieves state-of-the-art performance across a diverse suite of tasks, including depth, surface normal, and camera pose estimation, expression-referring segmentation, and 3D keypoint prediction, often matching or surpassing specialized models (e.g. DepthAnything3, SAM3, D4RT, VGGT-Omega, Sapiens, David, Genmo, and Lotus-2). Furthermore, the video generative pretrained backbone outperforms alternative pretraining paradigms (e.g., V-JEPA, and Video MAE) under comparable settings. Importantly, GenCeption exhibits preliminary data and model scaling properties along with exceptional data efficiency, where it achieves comparable performance with leading models like D4RT and VGGT-Omega with 7 to 500 less training data. Finally, GenCeption also exhibits intriguing emergent behaviors: a model trained exclusively on synthetic human videos generalizes to real-world footage and out-of-distribution object categories (e.g., animals and robots). These findings suggest that video generation is not merely a synthesis tool, but a foundational path toward generalist vision intelligence for the physical world. Project page: this https URL

---


### 23. [MOSAIC: Adaptive Inter-layer Composition for Efficient Heterogeneous Vision-Language Models](https://arxiv.org/abs/2607.09029)

**<font color=#1a73e8>作者：</font>** Yuncheng Yang, Feiyang Ye, Shixian Luo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved success using homogeneous Transformers to process multimedia data. Recent studies show that heterogeneous structures interleaving efficient mechanisms, like linear attention, improve both performance and inference latency over homogeneous designs. However, these efforts rely on handcrafted static mixing patterns, which are sub-optimal and difficult to adapt to specific hardware. To bridge this gap, we propose Multi-Objective Search for Adaptive Inter-layer Composition (MOSAIC), a hardware-aware search method that automatically transforms homogeneous models into optimized heterogeneous architectures. MOSAIC integrates diverse efficiency mechanisms--including linear, sparse, and low-rank operators--into a unified search space. By formulating the selection as a multi-objective Mixed Integer Programming (MIP) problem, our method identifies optimal configurations that maximize downstream performance under strict hardware latency constraints. To mitigate performance degradation from structural transitions, we introduce a two-stage parameter recovery process: global off-policy distillation to stabilize internal representations, followed by a dual-teacher on-policy distillation leveraging a 235B oracle for knowledge expansion and the original 4B teacher for distributional stability. We validate MOSAIC through MOSAIC-4B, derived from Qwen3-VL-4B-Instruct. Results demonstrate that MOSAIC-4B matches the baseline's performance across multiple benchmarks while requiring less than 2% of the original training cost. Furthermore, it substantially improves inference efficiency, achieving 1.76x prefilling and 2.54x decoding speedups.

---


### 24. [COBS: Cumulant Order Block Sparse Attention](https://arxiv.org/abs/2607.09052)

**<font color=#1a73e8>作者：</font>** Alexander Tian, Aditya Ghai, Sanjit Neelam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block sparse attention is a hardware friendly way to alleviate the key-value (KV) cache read bottleneck in large language models (LLMs). However, it is not prevalent among leading open-weight LLMs, which rely instead on dense attention or fine-grained selection, thereby motivating our analysis. We study DeepSeek's Native Sparse Attention (NSA) as a representative method, whose three-branch design lets us isolate block selection, the most challenging and consequential stage. We formalize selection and reduce it to ranking blocks by a single quantity, the attention mass: the sum of a block's attention scores. We show that if selection retrieves the blocks with the largest attention mass, block sparse attention can match the quality of dense attention. However, computing the exact attention mass requires reading every key, so the problem of block selection ultimately reduces to approximating this mass from a compact summary instead of the full keys. Via a cumulant expansion, we show why existing methods falter: their selection strategies attempt to estimate the attention mass, but are confined to a first-order approximation. Therefore, we propose COBS (Cumulant Order Block Sparse Attention), an attention method that builds on NSA, incorporating a novel selector that stores a compressed second-order statistic per block. On the 32k RULER long-context retrieval benchmark, COBS raises the NSA baseline's mean score from 0.2999 to 0.8195, approaching dense attention at 0.9040 and closing about 86% of the gap, while using only 1.21x the KV cache read traffic of the NSA baseline and 15.15x less read traffic than dense. The same model preserves short-context behavior and attains lower position-wise negative log-likelihood (NLL) than dense attention in our comparison.

---


### 25. [An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon?](https://arxiv.org/abs/2607.09053)

**<font color=#1a73e8>作者：</font>** Abhinav Rao, Liancheng Gong, Bin Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has reported Emergent Misalignment (EM), where language models fine-tuned on narrow, domain-specific misaligned datasets abruptly acquire broadly misaligned behavior, alongside evidence that this behavior can be reversed through limited realignment. We systematically study repeated alignment and misalignment cycles using controlled fine-tuning loops while tracking behavioral performance, and LoRA representations throughout training. Although we reproduce EM, we find that both misalignment and realignment are highly sensitive to superficial dataset characteristics, with apparent rapid realignment largely disappearing after controlling for response-length differences. We further find that previously reported mechanistic signatures, including representational phase transitions in LoRA space, do not consistently correlate with behavioral misalignment across training. Our results suggest that current evidence for EM is less robust than previously claimed and highlight the need for evaluation protocols that carefully control for these surface level dataset artifacts to identify the robustness of the EM phenomenon.

---


### 26. [Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls](https://arxiv.org/abs/2607.09076)

**<font color=#1a73e8>作者：</font>** Saroj Gopali, Bipin Chhetri, Deepika Giri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyberattacks on operational technology are increasingly causing costly downtime and physical damage, exposing the limitations of traditional rule-based monitoring in industrial IoT environments. While Large Language Models (LLMs) have strong semantic reasoning abilities to assist in decision support, their hallucinatory nature presents unacceptable safety liabilities for closed-loop control. This paper introduces a neuro-agentic control framework, a novel architecture that couples an LLM-based planner (i.e., such as Gemini 2.5 Flash-Lite) with a pre-trained Time-Series Foundation Model (TimesFM), to achieve physics-grounded autonomous defense. The paper introduces a ``Counterfactual Physics Injection'' mechanism that simulates the impact of LLM-proposed interventions within the numerical latent space of the foundation model before actuation, while allowing the system to reject hallucinatory or unsafe actions. Evaluated on an industrial dataset (e.g., the Secure Water Treatment (SWaT)) in the context of stochastic attack scenarios, the framework exhibited better performance compared to LSTM and TCN baselines. The Neuro-Agentic Loop prevented five breaches (33.3%) below the threshold versus LSTM (26.7%) and TCN (13.3%), with zero physically invalid (hallucinated) actions executed. These results demonstrate the efficacy of using foundation models as deterministic ``Sentinels'' to safeguard agentic AI in critical infrastructure.

---


### 27. [GeoTrace: Geometry-Aware Trajectory Token Compression for Video Large Language Models](https://arxiv.org/abs/2607.09080)

**<font color=#1a73e8>作者：</font>** Guohuan Xie, Mengqi Lei, Chuan Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Video Large Language Models (Video LLMs) have shown strong performance in video understanding, their efficiency is still limited by the large number of visual tokens. Existing video token compression methods typically rely on frame-wise saliency or heuristic token merging, which can over-focus on locally salient regions and produce ambiguous fused features. To address these issues, we propose GeoTrace, a training-free spatiotemporal token compression framework that decomposes video evidence into exact skeleton tokens and traceable residual event tokens. Specifically, Contextual Farthest-Point Anchoring (CFPA) preserves salient, context-consistent, and high-coverage skeleton tokens, while Trajectory-Constrained Residual Condensation (TCRC) compresses residual tokens through one-to-one temporal trajectories and constrained near-manifold condensation, producing traceable event tokens with reduced ambiguity. We evaluate GeoTrace on four Video LLMs across four video understanding benchmarks, and the results demonstrate its effectiveness and generalization across different model architectures and scenarios. On LLaVA-OneVision, with only 10\% visual tokens retained, GeoTrace achieves a \(12.99\times\) TFLOPs reduction while preserving 99.1\% of the vanilla performance. Overall, GeoTrace offers a compact and traceable token representation for efficient and robust Video LLM inference. Code is available at \href{this https URL}{\texttt{Code}}.

---


### 28. [Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models](https://arxiv.org/abs/2607.09091)

**<font color=#1a73e8>作者：</font>** Yijie Qian, Juncheng Wang, Chao Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As audio-visual generative models evolve into world simulators, cross-modal synchronization stands as a critical proxy for assessing the consistency of world dynamics and causality in generated content. However, existing evaluation metrics presume structural correctness, reducing synchronization to mere temporal alignment. Consequently, they fail on generative outputs, especially when exhibiting structural hallucinations and asymmetric cross-modal relations, which currently \textbf{mandate expert human annotation to assess synchronization.} This dependency introduces a critical paradox: \emph{human evaluators rely on relative, reference-dependent comparisons, whereas automated metrics require reference-free, absolute scalars.} We resolve this paradox by proposing a framework that distills relative human perception into a continuous, globally consistent metric. First, we introduce SynthSync, a dataset of generative failures ranked via pairwise human annotations. Second, we adapt the Omni-LLM equipped with a continuous latent projection to translate relative human rankings into continuous absolute values. Third, we propose Real-Valued Group Relative Policy Optimization ($\mathbb{R}$-GRPO) to internalize the global causal structure of synchronization via listwise score distributions. Empirically, our metric achieves state-of-the-art human preference alignment. We leverage this estimator to establish a standardized benchmark, advancing AV-Gen assessment from low-level signal correlation to visually grounded causality.

---


### 29. [AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs](https://arxiv.org/abs/2607.09092)

**<font color=#1a73e8>作者：</font>** Yumin Heo, Hyeon-gu Lee, Sumin Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) are often automatically constructed from large-scale corpora, but they inevitably contain factual errors due to noisy sources and extraction failures, and verifying them reliably at industrial scale remains a critical challenge. To address this, we propose AgentKGV, the Agentic LLM-RAG framework for KG fact Verification, that integrates dynamic routing and iterative query rewriting, which handles surface-form mismatch in document-level retrieval. To make this framework more accurate and cost-efficient for industrial deployment, we further introduce a two-stage training strategy: turn-level distillation-based SFT that transfers reasoning ability from a large teacher model into a small model for stable query rewriting and reasoning, and trajectory-level GRPO that optimizes the search policy to reduce unnecessary retrieval at scale. On the long-tail-predicate split of the open-domain T-REx benchmark, our framework improves macro-F1 over single-turn RAG by 5.5 \%p, and two-stage training does it further by 9.4 \%p. GRPO also cuts the average number of search calls from 3.24 to 1.63 without lowering accuracy.

---


### 30. [Integrating Large Language Models and Graph Convolutional Networks for Semi-Supervised Image Classification](https://arxiv.org/abs/2607.09104)

**<font color=#1a73e8>作者：</font>** Camila Piscioneri Magalhães, Lucas Pascotti Valem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the growing availability of image data has driven significant advances, labeling datasets remains costly and time-consuming. Therefore, semi-supervised approaches such as Graph Convolutional Networks (GCNs), which learn from both labeled and unlabeled data, have emerged as a promising solution. One of the primary challenges in applying GCNs to image classification is graph construction, since, unlike in citation networks or similar domains, images typically do not come with a predefined structural representation. For visual data, most studies construct graphs based on the similarity between feature vectors from pretrained deep learning backbones, typically by employing kNN or reciprocal kNN algorithms. Although Large Language Models (LLMs) have shown remarkable capability in capturing high-level semantics, their integration with GCNs for image classification remains underexplored. Aiming to fill this gap, our approach uses a Vision Language Model (VLM) to generate textual image descriptions, which are then processed by an LLM to estimate semantic similarity scores between connected images. These scores guide the pruning of edges in kNN and reciprocal kNN graphs, filtering out semantically irrelevant neighbors. Experimental results reveal that leveraging LLMs for graph refinement can improve classification accuracy, particularly for kNN graphs and some backbones. The source code is publicly available at this http URL.

---


### 31. [Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs](https://arxiv.org/abs/2607.09121)

**<font color=#1a73e8>作者：</font>** Bartosz Ziółko, Kacper Dobrzeniewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this study, we examine the opportunities brought by Large Language Models (LLMs) to various aspects of fundamental analysis of companies based on their reports as well as data and documents describing macroeconomic situation like GDP and inflation changes as well as documents filled to the U.S. Securities and Exchange Commission (SEC) which can be found in EDGAR. We were preprocessing those data and than sending via API to gpt-4o model in a Retrieval-Augmented Generation (RAG) like regime. We prepared as well a document describing an exemplar investor knowledge based on Kitchin cycles. We were scanning data important for analysis of 9 companies for 4 weeks. Using LLM we were producing automatic briefs about them. They were sent to nine participants who are individual investors to evaluate usefulness of such approach to data analysis.

---


### 32. [VTaMo: Video-Text Alignment Model for Sign Language Translation](https://arxiv.org/abs/2607.09126)

**<font color=#1a73e8>作者：</font>** Junyi Hu, Zhewen He, Haomian Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language translation (SLT) converts continuous sign videos into spoken language text. Gloss-free approaches leverage pre-trained visual encoders and language models but rely on implicit cross-modal alignment from translation supervision alone. We present VTaMo, a framework that introduces explicit multi-granularity alignment at three levels: (1) local alignment via entropy-regularized optimal transport with a learnable null token for fine-grained frame-to-token correspondences; (2) global alignment via a learnable orthogonal transformation that calibrates embedding space geometry through Earth Mover's Distance; and (3) position-aligned contrastive learning for discriminative token-level representations. Experiments on Phoenix-2014T, CSL-Daily, How2Sign, and OpenASL demonstrate consistent state-of-the-art performance, with ablations confirming the complementary contributions of each component. Code is available at this https URL.

---


### 33. [MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation](https://arxiv.org/abs/2607.09142)

**<font color=#1a73e8>作者：</font>** Runhan Shi, Quan Zhou, Yuqian Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in online medical consultation, yet existing benchmarks remain poorly aligned with real clinical practice. Many rely on synthetic conversations or patient simulators, omit patient-uploaded medical images, or evaluate open-ended clinical responses using multiple-choice or lexical-overlap metrics that poorly reflect clinical quality. We introduce \textbf{MedRealMM}, a large-scale benchmark for multimodal online medical consultation built from de-identified patient-doctor interactions collected from a nationwide Chinese internet hospital. MedRealMM uses a Multimodal Clinical Challenge Point (MCCP) extraction framework to identify clinically demanding moments in authentic consultation trajectories and converts each into a standardized next-response generation task while preserving the preceding text-image context. Each instance is paired with a case-specific rubric refined by physicians that rewards clinically desirable behaviors and penalizes unsafe, unsupported, or contradictory responses. The current release contains 5,620 real-world multimodal cases spanning 64 clinical departments. We evaluate 19 general-purpose and medical-specialized LLMs, including text-only and multimodal systems. Our results show that image information is critical for reliable clinical performance and that current frontier models remain below the online physician response. Although some frontier models satisfy as many or more positive clinical criteria than physicians, they trigger more negative criteria, indicating that safety-sensitive error avoidance remains a central bottleneck. MedRealMM offers a realistic and reproducible benchmark for evaluating multimodal medical reasoning in real-world online consultation. The dataset will be publicly available on Hugging Face at this https URL.

---


### 34. [Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift](https://arxiv.org/abs/2607.09175)

**<font color=#1a73e8>作者：</font>** Dan C. Hsu, Luke Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed LLM agents rely on agentic context, the model-external textual control content assembled by an operational harness. In this work, the mutable component of that context is a persistent system-level instruction that is updated from operational experience while the model, tools, and harness remain fixed. Over long evolution horizons, flat-text maintenance makes verification increasingly difficult as accumulated instructions grow and interact. We propose Graph-Regularized Agentic Context Evolution (GRACE), which maintains the persistent instruction component as a typed semantic graph and validates proposed updates within the local typed neighborhoods of modified nodes. Accepted graph updates are reconstructed as incremental edits to the textual instruction checkpoint used at deployment. We evaluate GRACE within a fixed telecom agent harness derived from $\tau^2$-bench under a controlled distribution-shift protocol. Across five independent replications, GRACE improves strict reliability, measured by pass^3, from the Gemini 2.5 Flash zero-shot value of 0.091 to 0.673$\pm$0.136 at the final checkpoint. This exceeds a Gemini 3.1 Pro zero-shot reference of 0.242 on the same held-out set, while the flat-text HCE baseline finishes at 0.191$\pm$0.051. These results identify two requirements for reliable long-horizon context evolution, a structural substrate that makes verification local and a consolidation mechanism that keeps accumulated instruction content usable.

---


### 35. [Causally Debiased Latent Action Model for Embodied Action Conditioned World Models](https://arxiv.org/abs/2607.09185)

**<font color=#1a73e8>作者：</font>** Yufan Wei, Kun Zhou, Lingjun Mao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned world models (ACWMs) aim to simulate future observations conditioned on embodied actions, offering a promising foundation for robot planning, policy evaluation, and data augmentation. However, learning controllable ACWMs requires large-scale action-labeled data, which remains costly to collect in the real world. Latent action models (LAMs) mitigate this bottleneck by inferring latent actions from unlabeled videos, but existing LAMs are typically trained with reconstruction-only objectives and therefore entangle action-relevant dynamics with action-irrelevant visual factors such as backgrounds and untouched objects. In this work, we identify this action-irrelevant bias as a key obstacle to controllable ACWMs and introduce evaluation metrics to measure latent-action bias, action following, and robustness. We propose CD-LAM, a causally debiased framework for LAM-based ACWMs. CD-LAM introduces three efficient fine-tuning objectives: embodiment-centric reconstruction, action-centric contrastive learning, and latent space calibration, which together encourage embodiment-focused, action-aware, and calibrated non-collapsed latent action representations. Experiments on 2B and 14B ACWM backbones show that CD-LAM substantially improves latent-action controllability, downstream robot-action following, visual fidelity, and adaptation efficiency, requiring only 6k fine-tuning steps and more than 12$\times$ fewer robot-action adaptation updates than the baseline.

---


### 36. [Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents](https://arxiv.org/abs/2607.09195)

**<font color=#1a73e8>作者：</font>** Izumi Takahara, Teruyasu Mizoguchi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly expected to play a central role in AI-driven scientific discovery. Equipped with broad knowledge, flexible reasoning, and tool use, they have the potential to autonomously explore and solve scientific problems by repeatedly proposing hypotheses, testing them, and revising their beliefs in the light of the evidence. In current agents, however, these hypotheses, tests, and belief updates are buried in unstructured logs, and no mechanism lets the agent or the human researcher audit that process. Here we propose the Hypothesis Evolution Protocol (HEP), an agent harness that provides hypothesis generation, evaluation, and evolution as explicit, auditable operations. On materials-science research tasks, a HEP-equipped agent operates the hypothesis--test--evidence--belief cycle that planning-style agents lack, generalizes across research questions, and exploits the protocol more fully as the base LLM becomes more capable. These results mark a step toward auditable AI scientists, whose scientific reasoning can be inspected, verified, and built upon.

---


### 37. [When is Routing Meaningful? Diversity and Robustness in Language Model Societies](https://arxiv.org/abs/2607.09197)

**<font color=#1a73e8>作者：</font>** Fantine Huot, Michael Kaisers, Mirella Lapata  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Routing policies for multi-model systems are evaluated almost exclusively on task accuracy and inference cost. We argue that two properties, orthogonal to performance, determine whether routing is meaningful. First, the society of actors must be behaviourally differentiated: if all actors respond identically, routing is vacuous. Second, the routing policy must be stable: surface-form variants of a query should be assigned to the same actor. High task accuracy is compatible with violating both properties, since a router can operate over a redundant society or assign queries inconsistently, preventing specialisation regardless of performance. We adapt Hierarchic Social Entropy (HSE) to language-model societies and introduce a perturbation-based robustness metric to diagnose these failure modes. Applied to EmbedLLM and RouterBench, we find that HSE exhibits strong diminishing returns, suggesting that a curated subset of fewer than ten agents recovers most available diversity in a large pool -- a practical coreset heuristic for society design. We further find that KNN routers gain accuracy from specialist societies but collapse in robustness under perturbation, while prompted routing remains stable across all perturbation types -- illustrating that accuracy and meaningfulness can sharply diverge.

---


### 38. [Complexity-Guided Component-wise Initialization for Language Model Pretraining](https://arxiv.org/abs/2607.09204)

**<font color=#1a73e8>作者：</font>** Konstantin Garbers, Nicholas Oh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained language models often exhibit structured weight spectra, suggesting that training may repeatedly produce similar layerwise and component-wise organization. We ask whether these recurring spectral patterns can be reused as an initialization signal for GPT-2-style language-model pretraining. First, we analyze eleven pretrained GPT-2-style checkpoints that vary in size, language, tokenizer, and training corpus, measuring Frobenius norm and effective-rank entropy across layers and Transformer subcomponents. The checkpoints show shared depth trends, especially increasing scale and stronger spectral concentration in residual-writing matrices. We then construct initialization schemes that imitate the component-wise magnitudes and spectral profiles of pretrained models, and compare them with several weight initialization methods. These initializers visibly change the model's structural spectral patterns, but the evaluation results do not show a corresponding performance advantage. Pretrained-weight reuse remains competitive, while coarse spectral matching alone is not a reliable optimization strategy. Our results suggest that pretrained spectra are useful diagnostics of trained model structure, but that effective reuse likely requires preserving richer information than component-wise scale and singular-value shape.

---


### 39. [OpenProver: Agentic and Interactive Theorem Proving with Lean 4](https://arxiv.org/abs/2607.09217)

**<font color=#1a73e8>作者：</font>** Matěj Kripner, Milan Straka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this system paper, we present OpenProver, an open-source system for LLM-driven automated theorem proving (ATP) with integrated Lean 4 formal verification. OpenProver integrates a Planner-Worker-Verifier architecture inspired by recent ATP agentic systems such as Aletheia. A Planner agent maintains a compact Whiteboard scratchpad and an unbounded Repository of intermediate findings, and decomposes mathematical work into parallel Workers.
OpenProver is fully open-source, offers reproducible evaluation through automatic formal verification of generated proofs, and provides an interactive terminal interface for human-guided proof search. In interactive mode, OpenProver allows the human operator to monitor and steer the proof search process, motivated by the established human-AI synergy in interactive code generation.
To showcase the potential for quantitative ablation experiments enabled by automatic formal verification, we evaluate OpenProver on ProofNet and compare it with a simple baseline. OpenProver is publicly available at this https URL.

---


### 40. [Glob3R: Global Structure-from-Motion with 3D Foundation Models](https://arxiv.org/abs/2607.09225)

**<font color=#1a73e8>作者：</font>** Junyuan Deng, Heng Li, Kejie Qiu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D geometric foundation models, such as VGGT, provide robust feed-forward 3D reconstruction by directly predicting camera poses and 3D scene points from input images. However, their results remain inaccurate, and scaling them to long sequences or large unordered image sets typically requires chunk-wise processing, which can introduce drift and inconsistency. We present Glob3R, a global SfM-style reconstruction built on 3D foundation models. Our key idea is to explicitly optimize feed-forward geometric predictions. To this end, we augment a frozen Pi3X backbone with a lightweight dense matching head that predicts image warps between selected reference frames and neighboring views. These dense warps are converted into sparse but reliable multi-view feature tracks, which provide correspondence constraints for global optimization. We further introduce a keyframe-based sliding-window association strategy that propagates tracks and relative poses across overlapping windows, enabling scalable reconstruction. Finally, we perform global motion averaging and bundle adjustment to refine camera poses, reduce scale inconsistencies, and recover dense scene geometry. Extensive experiments on indoor, outdoor, large-scale driving, and unordered SfM benchmarks demonstrate that Glob3R achieves robust and accurate reconstruction. It consistently improves over feed-forward foundation-model baselines and recent scalable reconstruction methods, while being more robust than classical SfM pipelines. The refined poses also lead to higher-quality neural rendering, validating the benefit of combining foundation-model priors with global geometric optimization. Project page: this https URL

---


### 41. [LLMs for health: Perceived benefits, risks, intention to use AI chatbots, and willingness to self-disclose across sensitive health topics](https://arxiv.org/abs/2607.09253)

**<font color=#1a73e8>作者：</font>** Gwenn Beets, Anniek Jansen, Saar Hommes 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI chatbots are increasingly used for answering health-related questions. This study examines the role of topic type discussed with an AI chatbot and individual characteristics on perceived benefits and risks, intention to use an AI chatbot, and willingness to self-disclose health information. We conducted an online experiment with a 2 (topic type: physical versus psychological, between-subjects) x 2 (topic sensitivity: low versus high, within-subjects) mixed design among a Dutch representative sample (N = 1,388). Results showed that perceived benefits were positively associated with intention and willingness to self-disclose, while perceived risks were negatively associated. Moreover, participants reported higher usage intentions for low-sensitive topics compared to high-sensitive topics. Furthermore, perceptions, intention, and willingness to self-disclose varied by individual characteristics. Overall, our findings suggest that intentions to use AI chatbots and self-disclosure of health-related information are primarily related to perceived benefits and risks and to personal characteristics rather than to topic type.

---


### 42. [Super-Tuning: From Activation-Aware Pruning to Sparse Fine-Tuning](https://arxiv.org/abs/2607.09287)

**<font color=#1a73e8>作者：</font>** Ivan Ilin, Philip Zmushko, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain expensive to fine-tune because full-parameter updates require substantial memory, compute, and per-task storage. We study whether saliency signals originally developed for pruning can be reused to choose where a model should adapt. We propose Super, a sparse parameter-efficient fine-tuning (PEFT) method that fixes a small trainable support using a Wanda-style activation-weighted magnitude score [Sun et al., 2023] computed from a calibration pass. We then introduce Supra, a hybrid adapter that combines this sparse update with LoRA while preserving a matched trainable-parameter budget through a simple budget-splitting rule. In single-seed Math17K arithmetic experiments on Llama-3.2-1B and Meta-Llama-3-8B, the best Super/Supra variants achieve the highest average accuracy among the tested schedule-selected adapter configurations. We also include a PaFi-style magnitude-only support as a closest training-free sparse baseline and find that low-score supports under both magnitude and Wanda-style orderings can be effective. These results suggest that simple pruning-inspired orderings can provide useful fixed sparse supports for PEFT, especially when combined with low-rank adapters.

---


### 43. [Creativity, honesty and designed forgetting emerge in small hyperbolic language models](https://arxiv.org/abs/2607.09306)

**<font color=#1a73e8>作者：</font>** Kwan Soo Shin, In Seok Kang, Yunkyung Min  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are optimised for scale, yet remain functional rather than companionable, and as an assistant personalises into a companion, accumulating memory of one user, it quietly becomes someone, and can silently acquire traits that harm that user. What a companion is becoming, and what would make it worth becoming, has no reliable instrument: trained human raters cannot agree on the answer (Fleiss kappa = 0.074). Here we show that three small language models (146 M to 3 B parameters) sharing a hyperbolic substrate answer both halves of that question. A 146 M behavioural auditor, trained from scratch, detects the compliance gap that those raters cannot (90.7% binary-compliance accuracy); a linear read-out of its frozen representation further detects companion-induced sycophancy, dependence-fostering and confabulated memories on generator families unseen in training (AUROC 0.804 under style-controlled, leave-one-generator-out evaluation, versus 0.721 for a frontier zero-shot judge on the same items). A creative frame-seeder is preferred in 100% of 311 decided pairwise comparisons over four prompting baselines. A memory operating system implements designed forgetting, M(t) = S*exp(-lambda*t), whose predicted skeleton-wallpaper partition emerges only under selective retrieval gating in a four-condition pilot. Creativity, honesty and designed forgetting constitute a small-model route to trustworthy companion AI.

---


### 44. [Automatic Thematic Indexing of Large Literary Corpora: A Machine Learning Approach to Voltaire's Complete Works](https://arxiv.org/abs/2607.09316)

**<font color=#1a73e8>作者：</font>** Miguel Arana-Catania, Gillian Pink, Glenn Roe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Thematic indexing -- the practice of assigning structured conceptual labels to sections of text -- is essential to scholarly access in large-scale literary and historical editions, yet it remains a largely manual, labour-intensive process. This paper explores the application of machine learning to automatic thematic indexing, using two substantial sub-corpora of the Complete Works of Voltaire as a test case: the Essai sur les mœurs et l'esprit des nations and the Questions sur l'Encyclopédie. The task is framed as a multi-label classification problem, in which a model must assign the set of index entries that a professional indexer would apply to a given page of text. We compare a range of approaches -- from encoder-based models with classification heads to generative large language models (LLMs) fine-tuned via Low-Rank Adaptation (LoRA) -- spanning model sizes from approximately 3 to 120 billion parameters. Our best-performing model, from the Mistral family in a 4-bit quantised configuration, achieves F1 scores of up to 0.67; we argue that these figures represent lower bounds, given the inherent subjectivity of professional indexing and the frequency with which model predictions prove semantically valid despite diverging from the print index. We further evaluate cross-corpus generalisation and conduct a detailed qualitative analysis of model behaviour on literary and rhetorical features of the source texts that prove particularly resistant to automated treatment. Our findings have implications for the broader challenge of providing structured thematic access to large-scale literary and historical corpora.

---


### 45. [Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks](https://arxiv.org/abs/2607.09330)

**<font color=#1a73e8>作者：</font>** Nuocheng Yang, Sihua Wang, Zihan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agent teams powered by heterogeneous large language models (LLMs) are being widely deployed in physical artificial intelligence such as smart factories, warehouses, and service robotics. To enable collaboration among such an agent team, efficient coordination mechanisms that operate reliably under limited network resources are required. However, existing heterogeneous LLM-agent coordination frameworks that rely on multi-round natural-language-based conversations introduce three coupled challenges. First, inter-agent dialogue incurs communication overhead that grows rapidly with team size. Second, the quality of coordination is constrained by the heterogeneous capabilities of the agent team's LLMs. Third, agents may suffer from action delays due to iterative negotiation. To address these challenges, we propose LDT-Coord, a networked coordination framework built upon a lightweight digital twin (DT). Specifically, each agent independently selects its intended action and reports both the action decision and a structured temporal constraint over shared resources to the DT server, thereby decoupling coordination performance from natural-language reasoning ability. Then, DT executes a training-free, rule-based orchestrator algorithm to resolve cross-agent conflicts and returns coordination instructions to prevent such conflicts. To further reduce communication overhead, we formulate agent reporting control as a constrained partially observable Markov decision process (C-POMDP) and solve it with the PPO-Lagrangian algorithm. Simulation results show that LDT-Coord achieves a task success rate comparable to conventional coordination methods while reducing communication overhead by more than 70x and maintaining robustness under LLM heterogeneity.

---


### 46. [DKCD: Domain Knowledge-Enhanced Causal Discovery from Unstructured Data](https://arxiv.org/abs/2607.09348)

**<font color=#1a73e8>作者：</font>** Xin Li, Jin Li, Shoujin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal discovery from unstructured data is a challenging yet underexplored task in high-expertise domains such as healthcare, finance, and education. Existing methods typically leverage the general knowledge of large language models (LLMs) to identify causal factors from unstructured data and annotate them into structured data for causal graph construction. However, they remain limited by two key challenges (CHs): (CH1) insufficient identification of latent factors, which are implicit in the data yet essential for causal discovery, due to the lack of domain-specific knowledge; and (CH2) unreliable factor annotation, caused by the lack of domain-grounded reasoning, which propagates errors to the resulting causal graphs. To address these challenges, we introduce a novel Domain Knowledge-enhanced Causal Discovery framework (DKCD) for causal discovery from unstructured data in high-expertise domains with three interconnected components: (1) Knowledge Mining: It retrieves relevant domain knowledge based on observable factors to support subsequent causal reasoning. (2) Knowledge-guided Causal Reasoning: Reasoning with relevant knowledge, it discovers latent causal factors to address CH1 and generates key causal clues for more accurate data annotation to address CH2. (3) Causal Structure Discovery: It constructs the final causal graphs based on a more complete factor set and accurate annotations. Experiments on two domain-specific datasets show that DKCD significantly improves both causal factor identification and causal graph construction.

---


### 47. [Mach-Mind-4-Flash Technical Report](https://arxiv.org/abs/2607.09375)

**<font color=#1a73e8>作者：</font>** Foundation Model Team  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Mach-Mind-4-Flash, a 35B-parameter Mixture-of-Experts (MoE) agentic model with 3B activated parameters. Through post-training optimization alone without scaling pre-training compute, the model achieves performance on par with or surpassing that of 100B-parameter-class models. By introducing scalable agentic interaction environments for large-scale reinforcement learning, the model attains significant performance gains on real-world application tasks. Our pipeline comprises three stages: (1) a unified RL/OPD training infrastructure with dynamic multi-teacher scheduling and operator-level acceleration, delivering 17\% end-to-end training speedup; (2) multiple domain-specific RL experts trained in parallel across Reasoning, General, and Agent tracks, then fused into a single generalist via Multi-Teacher On-Policy Distillation (MOPD) -- a routed reverse-KL objective that eliminates the see-saw degradation of mixed-reward RL; (3) Hybrid Median-length Policy Optimization (HMPO), a single-stage token-efficiency method that compresses reasoning chains by 19--46\% with $\le$0.7 percentage-point accuracy loss. Mach-Mind-4-Flash scores 92.70 on AIME'26, 82.82 on IFBench, 80.74 on Behavioral-SafetyBench, 75.80 on BFCL-v4, 72.31 on BrowseComp-zh, and 84.20 on ClawBench -- leading or matching models with 10--30$\times$ its activated size at a fraction of the inference cost.

---


### 48. [Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review](https://arxiv.org/abs/2607.09403)

**<font color=#1a73e8>作者：</font>** Jingbo Chen, He Wang, Wei Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Worldbuilding, the construction of coherent fictional worlds, is a foundational task in game design and literary creation. Large Language Models (LLMs) offer new possibilities for automated content generation, but their application to worldbuilding faces three challenges: context explosion that grows linearly with the building process, the tension between creative diversity and content consistency, and the absence of automated quality assurance. This paper presents AutoWorldBuilder, a multi-agent collaborative system that addresses these challenges through five integrated components: a structured concept network with conflict detection; a DAG-based hybrid batch scheduler that groups tasks by semantic locality; a four-layer context compression mechanism achieving approximately 90% token reduction; an iterative review system with specialized Auditor agents that improves proposal pass rates from 42% to over 85%; and a skill-driven agent architecture supporting zero-code extension with differentiated temperature configuration. Two experiments across 20 diverse worldbuilding tasks, using GPT-OSS 120B and DeepSeek v3.2 as LLM backends, demonstrate a 95.0% success rate. The system generated 56-103 self-consistent concepts per world in 18-31 minutes with zero-conflict delivery. The architectural patterns validated here, including layer-as-budget compression, semantic-locality scheduling, and separation of generation and review, transfer to the broader class of knowledge-intensive, multi-agent LLM applications.

---


### 49. [Self-Guided Test-Time Training for Long-Context LLMs](https://arxiv.org/abs/2607.09415)

**<font color=#1a73e8>作者：</font>** Xinyu Zhu, Zhe Xu, Xiaohan Wei 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context processing has become increasingly important for large language models (LLMs), but simply extending the context window does not guarantee effective utilization of long inputs. As input length grows, accuracy often degrades, indicating that models still struggle to identify and use the evidence most relevant to a question. A promising way to improve long-context utilization is test-time training (TTT), which treats the test context as a training example for instance-specific parameter adaptation. However, applying TTT to the entire long context is prohibitively expensive, while adapting on randomly sampled spans introduces severe noise. Because most spans in a long context are irrelevant to the specific question, training on them may even degrade the base model's performance. Our preliminary study shows that TTT is highly sensitive to training-span quality: on LongBench-v2, TTT on randomly sampled spans hurts performance, whereas TTT on oracle spans substantially improves it. Motivated by this, we propose a simple method, Self-Guided TTT (S-TTT): before adaptation, the model identifies the evidence spans it should learn from, and the standard language-modeling training objective is applied only to those selected spans. On two challenging long-context reasoning benchmarks, LongBench-v2 and LongBench-Pro, S-TTT improves accuracy for both Qwen3-4B-Thinking-2507 and Llama-3.1-8B-Instruct, achieving up to a 15% relative improvement.

---


### 50. [SVF-CR: Synchronized Visual-Facial Cross-Refinement for Multimodal Ambivalence and Hesitancy Recognition](https://arxiv.org/abs/2607.09417)

**<font color=#1a73e8>作者：</font>** Hyein Park, Namho Kim, Junhwa Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ambivalence and hesitancy are subtle behavioral states that are expressed through a combination of verbal content, facial behavior, visual context, and acoustic cues. Effective recognition therefore requires not only extracting informative unimodal representations, but also modeling how temporally aligned behavioral evidence interacts across modalities. In this paper, we propose a synchronized visual-facial cross-refinement framework (SVF-CR) with pairwise multimodal evidence fusion for ambivalence and hesitancy recognition. The proposed method first extracts whole-video segment tokens and cropped-face segment tokens using the same temporal partition. The synchronized visual and facial tokens are refined through intra-modal self-attention and bidirectional visual-facial cross-attention, allowing whole-video context and local facial behavior to mutually refine each other before evidence construction. We then construct segment-level visual-facial evidence using consistency and discrepancy modeling, followed by temporal self-attention and attention pooling. Textual and acoustic features are lightly refined through context self-attention and are fused with the enhanced visual-facial evidence at the final decision stage using pairwise evidence fusion. Experiments on the BAH (Behavioral Ambivalence/Hesitancy) public evaluation split show that the proposed synchronized visual-facial cross-refinement improves public macro-F1 over both global visual-face token fusion and synchronized evidence baselines, achieving a public macro-F1 of 0.7156. Code is available at : this https URL\_SVF-CR.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-68](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
