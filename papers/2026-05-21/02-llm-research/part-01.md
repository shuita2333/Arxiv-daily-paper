# 🧠 大模型相关研究 | 2026年05月21日

> 本类共 **172** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-172](./part-04.md)

---

### 1. [Interoceptive Divergence in Aesthetic Evaluation and Implications for Human-AI Alignment](https://arxiv.org/abs/2605.18759)

**<font color=#1a73e8>作者：</font>** Yoshia Abe, Tatsuya Daikoku, Yasuo Kuniyoshi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI), exemplified by large language models (LLMs), is rapidly approaching and in some cases surpassing human performance across a wide range of cognitive tasks. However, human nature is not limited to intelligence alone; it also encompasses sensibility, including the capacity to perceive and experience beauty in visual scenes. This raises a fundamental question: how humans and AI systems converge or diverge in such aesthetic experiences. Aesthetic evaluation depends not only on objective properties of images but also on internal processes within the observer. As part of ongoing efforts in AI alignment, building upon prior human studies that have examined the relationship between beauty ratings, bodily sensations, and emotions, we adopt a comparable set of questionnaire items and present them to LLMs, enabling a direct comparison between human and AI responses. Our comparative analyses revealed that, while humans and AI exhibited broadly similar patterns in the correlations between beauty ratings and emotions, as well as in the image features they prioritized, notable divergences emerged in both the distribution of emotional responses and the relationship between beauty ratings and bodily sensations. These findings suggest that state-of-the-art LLMs, trained on large-scale textual data, can approximate average human tendencies in aesthetic evaluation to a certain extent. However, they also indicate limitations, particularly in relation to interoceptive aspects, which may reflect insufficient representation in training data or unintended consequences of alignment processes. These findings highlight key challenges for AI alignment and suggest important directions for developing AI systems with human-like aesthetic processing.

---


### 2. [HELLoRA: Hot Experts Layer-Level Low-Rank Adaptation for Mixture-of-Experts Models](https://arxiv.org/abs/2605.18795)

**<font color=#1a73e8>作者：</font>** Jia Wei, Zhonghao Zhang, Ping Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) dominates parameter-efficient fine-tuning of large language models, yet most variants target dense architectures. Mixture-of-Experts (MoE) models scale parameters at near-constant per-token compute, and their sparse activation patterns create untapped opportunities for more efficient adaptation. We propose Hot-Experts Layer-level Low-Rank Adaptation (HELLoRA), which attaches LoRA modules only to the most frequently activated experts at each layer. This simple mechanism reduces trainable parameters and adapter-induced FLOPs while improving downstream performance, an effect we attribute to a form of structured regularization that preserves pretrained expert specialization. To stress-test HELLoRA under extreme parameter budgets, we further compose it with LoRI to form HELLoRI, which freezes the up-projection and sparsifies the down-projection. Across three MoE backbones, namely OlMoE-1B-7B, Mixtral-8x7B, and DeepSeekMoE, and three task families covering mathematical reasoning, code generation, and safety alignment, HELLoRA consistently outperforms strong PEFT baselines. Relative to vanilla LoRA on OlMoE, HELLoRA uses 15.7% of the trainable parameters, reduces adapter FLOPs by 38.7%, achieves 1.9x the training throughput, and improves accuracy by 9.2%. On DeepSeekMoE, HELLoRA outperforms LoRA while using only 23.2% of its trainable parameters. These results demonstrate that activation-aware adapter placement is an effective and practical route to scaling PEFT for MoE language models.

---


### 3. [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)

**<font color=#1a73e8>作者：</font>** Varun Kotte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM cascades and model routing promise lower inference cost by sending easy queries to a small model and escalating hard ones to a large model, but most deployed routers use uncalibrated confidence scores and require per-workload threshold tuning. We present UCCI, a calibration-first router that maps token-level margin uncertainty to a per-query error probability via isotonic regression and selects the escalation threshold by constrained cost minimization. Under three explicit assumptions, threshold policies on the calibrated score are cost-optimal, and isotonic calibration achieves O(n^{-1/3}) sample complexity for expected calibration error (ECE). On a production named entity recognition workload of 75,000 queries served by 4B and 12B instruction-tuned LLMs on H100 GPUs, UCCI cuts inference cost by 31% (95% CI: [27%, 35%]) at micro-F1 = 0.91 while reducing ECE from 0.12 to 0.03. At the same operating point, UCCI beats entropy thresholding, split-conformal routing, and a FrugalGPT-style learned threshold. All cascade results use end-to-end routing on actual model outputs and measured H100 latency, not simulated routing from global accuracies or nominal API prices.

---


### 4. [ReCrit: Transition-Aware Reinforcement Learning for Scientific Critic Reasoning](https://arxiv.org/abs/2605.18799)

**<font color=#1a73e8>作者：</font>** Wanghan Xu, Yuhao Zhou, Hengyuan Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can fail in critic interaction not only by answering incorrectly, but also by abandoning an initially correct scientific solution after user criticism. This is especially risky in scientific reasoning, where user criticism can turn a valid answer into an incorrect one. We frame critic interaction as an inter-turn correctness-transition problem rather than a final-answer accuracy problem, and identify three challenges: transition awareness, decoupling useful correction from harmful sycophancy, and scalable rollout. We propose ReCrit, a transition-aware reinforcement learning framework that decomposes Initial-to-Critic behavior into four quadrants: Correction, Sycophancy, Robustness, and Boundary. ReCrit rewards correction and robustness, penalizes sycophancy, and treats persistent errors as weak boundary signals. To make interaction training practical, ReCrit further uses dynamic asynchronous rollout with tail-adaptive completion to reduce rollout waiting. On three scientific reasoning benchmarks, ChemBench, TRQA, and EarthSE, ReCrit improves average Critic accuracy from 38.15 to 51.49 on Qwen3.5-4B and from 45.40 to 55.59 on Qwen3.5-9B. Ablations show that final-answer rewards provide little interaction-level gain, while transition-aware rewards and quadrant weighting produce more distinguishable training signals and larger net Critic-stage improvement. The code is available at this https URL .

---


### 5. [Theory-optimal Quantization Based on Flatness](https://arxiv.org/abs/2605.18800)

**<font color=#1a73e8>作者：</font>** Xiusheng Huang, Zhe Li, Xuanwu Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization has emerged as a widely adopted technique for compressing and accelerating the inference of Large Language Models (LLMs). The primary challenges in LLMs quantization stem from activation outliers, which significantly degrade model performance especially at lower bit precision. While recent approaches attempt to mitigate outliers through linear transformations across feature dimensions, our analysis reveals that the transformed weights and activations still exhibit persistent outlier patterns with concentrated magnitude distributions. In this paper, we first model the mathematical relationship between quantization error and outliers, and then introduce a new metric Flatness to quantify the distribution of outliers. Based on this, we derive the theoretical optimal solution with respect to Flatness. Building on these insights, we propose Bidirectional Diagonal Quantization (BDQ), a novel post-training quantization framework that effectively disperses outlier patterns through optimized matrix transformations. BDQ strategically distributes outlier magnitudes across matrix dimensions via learned diagonal operations. Extensive experiments demonstrate that BDQ establishes a new quantization benchmark. It achieves less than 1\% accuracy drop in W4A4 quantization on the LLaMA-3-8B model. In the more challenging W2A4KV16 experiment, compared to state-of-the-art approaches, BDQ reduces the performance gap by 39.1\% on the DeepSeek-R1-Distill-LLaMA-70B model.

---


### 6. [Position: Let's Develop Data Probes to Fundamentally Understand How Data Affects LLM Performance](https://arxiv.org/abs/2605.18801)

**<font color=#1a73e8>作者：</font>** Shiqiang Wang, Herbert Woisetschläger, Hans Arno Jacobsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data is fundamental to large language models (LLMs). However, understanding of what makes certain data useful for different stages of an LLM workflow, including training, tuning, alignment, in-context learning, etc., and why, remains an open question. Current approaches rely heavily on extensive experimentation with large public datasets to obtain empirical heuristics for data filtering and dataset construction. These approaches are compute intensive and lack a principled way of understanding the essence of how specific data characteristics drive LLM behavior. In this position paper, we advocate for the need of developing systematic methodologies for generating synthetic sequences from appropriately defined random processes, with the goal that these sequences can reveal useful characteristics when they are used in one or multiple stages of the LLM workflow. We refer to such sequences as data probes. By observing LLM behavior on data probes, researchers can systematically conduct studies on how data characteristics influence model performance, generalization, and robustness. The probing sequences exhibit statistical properties that can be viewed using theoretical concepts, such as typical sets, which are generalized to describe the behaviors of LLMs. This data-probe approach provides a pathway for uncovering foundational insights into the role of data in LLM training and inference, beyond empirical heuristics.

---


### 7. [PROWL: Prioritized Regret-Driven Optimization for World Model Learning](https://arxiv.org/abs/2605.18803)

**<font color=#1a73e8>作者：</font>** Ahmet H. Güzel, Jenny Seidenschwarz, Benjamin Graham 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern action-conditioned video world models achieve strong short-horizon visual realism, yet remain unreliable on rare, interaction-critical transitions that dominate downstream planning and policy performance. Because passive demonstration data systematically under-samples these high-impact regimes, improving robustness requires actively eliciting model failures rather than relying on their natural occurrence. We introduce a KL-constrained adversarial curriculum in which a policy is trained to expose high-error trajectories of a diffusion-based world model while remaining close to the behavior distribution. The world model is continuously fine-tuned on these adversarially discovered trajectories, yielding an adversarial training loop that converts rare failures into a stable, near-distribution training signal without drifting into out-of-distribution exploitation. To maintain pressure on unresolved weaknesses as the model improves, we propose a Prioritized Adversarial Trajectory (PAT) buffer that re-ranks trajectories based on prediction error, action fidelity, and learning progress, focusing training on unresolved failure modes rather than repeatedly revisiting solved cases. We implement our approach in the MineRL framework and evaluate it on held-out out-of-distribution trajectories; PROWL improves robustness over models trained on passive data alone, reveals reward-hacking behaviors under weak behavioral constraints, and demonstrates that effective adversarial world-model training critically depends on balancing exploratory failure discovery with explicit behavioral regularization. Our results suggest that scalable world models benefit not only from larger datasets, but also from selectively generating informative training data.

---


### 8. [Compositional Literary Primitives in Instruction-Tuned LLMs: Cross-Architectural SAE Features for Self, Style, and Affect](https://arxiv.org/abs/2605.18808)

**<font color=#1a73e8>作者：</font>** Joao Paulo Cavalcante Presa, Savio Salvarino Teles de Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We characterize a compositional architecture of literary primitives in two instruction-tuned large language models (Llama 3.1 8B-Instruct and Gemma 2 9B-IT) via sparse autoencoders on mid-depth residual streams. Four feature classes emerge: naming-gates that promote lexical tokens of a target affect, an eleven-self cluster of first-person register features, stylistic register modulators (show-don't-tell and defamiliarization), and compositional emotions that arise only from multi-feature steering. Under a forced-choice 5-LLM judge panel applied to a 27-category emotion taxonomy (Cowen-Keltner), Llama reaches full 27/27 coverage by combining naming-gates, multi-feature recipes, and single self-feature steering; Gemma reaches 23/27 with adoration as the single residual strict-fail. Under random judging, the per-cell pass probability is on the order of $10^{-3}$ and the expected number of two-seed false-positive cells across the catalog is negligible, so the observed coverage is not consistent with chance. A cross-architectural asymmetry sits in the strict-versus-soft judge contrast: on the same generations, judges agree more often on Llama outputs than on Gemma outputs because Llama outputs name the target affect more directly while Gemma outputs evoke it through scene and imagery. Both architectures contain self-features that serve simultaneously as register markers and as emotion emitters, including a single most-RLHF-loaded self-feature per architecture that intensifies the institutional Helper-AI persona at one operating regime and produces affect-categorizable output at the same calibrated coefficient. Methodologically, the paper presents a three-stage validation pipeline (logit-lens, LLM-rate, 5-LLM judge) with documented anti-patterns; the total compute is single-GPU and about 15 minutes per emotion-feature discovery cycle.

---


### 9. [PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines](https://arxiv.org/abs/2605.18812)

**<font color=#1a73e8>作者：</font>** Varun Kotte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern NLP and LLM systems are pipelines: named entity recognition (NER) -> entity disambiguation (NED) -> entity typing, retrieval-augmented generation (retriever -> reader), and agentic chains of planner -> tool -> critic. Errors compound across stages, but existing uncertainty quantification methods either calibrate each stage independently (no joint coverage) or apply a Bonferroni union bound (joint coverage, but conservative). We present PASC (Pipeline-Aware Split Conformal), which reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score. PASC provides a finite-sample distribution-free guarantee that all K stages are simultaneously covered with probability at least 1 - alpha, and is nearly tight up to a 1/(n+1) factor. On a three-stage NER -> NED -> entity-typing pipeline over CoNLL-2003, PASC achieves 96.4% end-to-end coverage versus 93.4% for Bonferroni and 86.5% for independent CP, at identical average prediction set size (1.083). Under distribution shift to WNUT-17 Twitter and WikiNEuRal Wikipedia data, PASC empirically maintains the target coverage in the tested shift settings while independent CP collapses to 59%. PASC requires a single quantile computation, runs 1.7x faster than Bonferroni, and scales to K = 6 stages where independent CP drops to 0.53 end-to-end coverage. The same joint-maximum-score reduction applies directly to compound LLM systems and agent pipelines.

---


### 10. [Composition of Memory Experts for Diffusion World Models](https://arxiv.org/abs/2605.18813)

**<font color=#1a73e8>作者：</font>** Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models aim to predict plausible futures consistent with past observations, a capability central to planning and decision-making in reinforcement learning. Yet, existing architectures face a fundamental memory trade-off: transformers preserve local detail but are bottlenecked by quadratic attention, while recurrent and state-space models scale more efficiently but compress history at the cost of fidelity. To overcome this trade-off, we suggest decoupling future-past consistency from any single architecture and instead leveraging a set of specialized experts. We introduce a diffusion-based framework that integrates heterogeneous memory models through a contrastive product-of-experts formulation. Our approach instantiates three complementary roles: a short-term memory expert that captures fine local dynamics, a long-term memory expert that stores episodic history in external diffusion weights via lightweight test-time finetuning, and a spatial long-term memory expert that enforces geometric and spatial coherence. This compositional design avoids mode collapse and scales to long contexts without incurring a quadratic cost. Across simulated and real-world benchmarks, our method improves temporal consistency, recall of past observations, and navigation performance, establishing a novel paradigm for building and operating memory-augmented diffusion world models.

---


### 11. [DynaTrain: Fast Online Parallelism Switching for Elastic LLM Training](https://arxiv.org/abs/2605.18815)

**<font color=#1a73e8>作者：</font>** Yuanqing Wang, Yuchen Zhang, Hao Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language model (LLM) training is inherently dynamic: resource fluctuations, RLHF phase shifts, and cluster elasticity continually reshape the optimal parallelism layout, posing a significant challenge to existing training frameworks built around a static execution model. We present DynaTrain, a distributed training system for sub-second, online reconfiguration across arbitrary multi-dimensional parallelism. At its core, we propose a Virtual Parameter Space (VPS) abstraction that unifies all distributed training states under one logical coordinate space, turning any parallelism configuration into a deterministic mapping and collapsing complex transition into manageable geometric intersections. On top of VPS, a state routing-and-transition layer executes rank-local transfers under a memory-aware, deadlock-free schedule, and an Elastic Device Manager overlaps new-world construction with ongoing training to mask topology-change cost. On dense and MoE models up to 235B parameters, DynaTrain reconfigures a 70B dense model in under 2s and a 235B MoE model in 4.36s, outperforming state-of-the-art checkpoint-based and elastic systems by up to three orders of magnitude while preserving correctness.

---


### 12. [Operationalizing Document AI: A Microservice Architecture for OCR and LLM Pipelines in Production](https://arxiv.org/abs/2605.18818)

**<font color=#1a73e8>作者：</font>** Yao Fehlis, Benjamin Bengfort, Zhangzhang Si 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Academic research tends to focus on new models for document understanding creating a wide gap in the literature between model definition and running models at production scale. To close that gap, we present a microservice architecture that encapsulates pipelines of multiple models for classification, optical character recognition (OCR), and large language model structured field extraction as well as our experience running this pipeline on thousands of multi-page documents per hour. We describe our primary design decisions, including a hybrid classification, separation of GPU-bound inference from CPU-bound orchestration, use of asynchronous processing for the many IO-bound operations in the pipeline, and an independent, horizontal scaling strategy. Using batch profiling, we identified two surprising qualitative findings that shape production deployments: OCR, not language-model parsing, dominates end-to-end latency, and the system saturates at a concurrency determined by shared GPU-inference capacity rather than worker count. Our goal is to provide practitioners with concrete architectural patterns for building document understanding systems that work beyond the benchmark; effectively operationalizing models in production.

---


### 13. [Hybrid-LoRA: Bridging Full Fine-Tuning and Low-Rank Adaptation for Post-Training](https://arxiv.org/abs/2605.18822)

**<font color=#1a73e8>作者：</font>** Chengqian Zhang, Wei Zhu, Kyumin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training has become essential for adapting large language models (LLMs) to complex downstream behaviors, including instruction following, preference alignment, and multi-step reasoning. Reinforcement learning with verifiable rewards (RLVR) has recently emerged as a particularly effective post-training paradigm for improving reasoning capabilities, with critic-free algorithms such as GRPO and GSPO enabling scalable optimization. However, RLVR post-training with full fine-tuning (FFT) requires substantial GPU memory and incurs high training costs. Although parameter-efficient fine-tuning (PEFT) methods, such as Low-Rank Adaptation (LoRA), effectively reduce computational costs, they often suffer from a noticeable performance gap compared to full fine-tuning in post-training for complex reasoning tasks. In this paper, we propose Hybrid-LoRA, an efficient hybrid post-training framework that selectively applies full fine-tuning to a small subset of modules less suited to low-rank adaptation, while adapting the remaining components with LoRA. We introduce a novel Hybrid-LoRA Score to rank candidate modules according to their sensitivity to low-rank adaptation under a fixed parameter budget. Experiments show that Hybrid-LoRA closely matches full fine-tuning performance under a 10% full fine-tuning module budget, with the remaining candidate modules adapted by LoRA, consistently outperforming four state-of-the-art PEFT post-training baselines, achieving improvements of up to 5.65% and on average 4.36% over the best baseline.

---


### 14. [Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models](https://arxiv.org/abs/2605.18824)

**<font color=#1a73e8>作者：</font>** Mohammed Saidul Islam, Negin Baghbanzadeh, Farnaz Kohankhaki 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluation of foundation models often rely on aggregate scores from benchmarks that lack comprehensive coverage and metadata for a fine-grained evaluation. We introduce a framework for automated benchmark generation. Our framework generates evaluation problems grounded in reference material, such as textbooks, producing benchmarks with broad coverage, rich metadata, and robustness to contamination. The pipeline employs a multi-agent architecture for problem generation and a solution-graph-driven strategy that significantly improves the reliability of ground truth solutions. Using the framework, we generate three benchmarks in Machine Learning, Corporate Finance, and Personal Finance. Expert review finds a significantly lower ground-truth error rate than previous benchmarks such as MMLU and GSM8K. Evaluation of 12 commercial and open-source models shows that our benchmarks achieve near-uniform competency coverage and surface performance differences across models that existing benchmarks fail to capture. We will open-source the framework and our curated benchmarks soon.

---


### 15. [Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches](https://arxiv.org/abs/2605.18825)

**<font color=#1a73e8>作者：</font>** Shaoke Fang, Ziang Li, Wenfei Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prefix caching is a key optimization in Large Language Model (LLM) serving, reusing attention Key-Value (KV) states across requests with shared prompt prefixes to reduce expensive prefill computation. However, its benefit depends critically on the eviction policy as GPU memory is scarce, and existing policies such as LRU largely treat cached blocks uniformly. This view ignores a fundamental property of LLM prompts: not all tokens are equally worth caching. We show that different token types within a prompt, including system prompts, user queries, tool outputs, model responses, and chain-of-thought reasoning, exhibit up to 756x variation in reuse rates, yet no existing eviction policy exploits this signal. In this paper, we present SAECache (Semantic-Adaptive Eviction for prefix caches), a semantic-adaptive prefix cache eviction policy that addresses this gap through three innovations: (1) a multi-queue architecture that routes KV blocks to task-specific queues with tailored priority metrics, capturing both session reuse in multi-turn requests and structural reuse in templated single-turn requests; (2) a semantic-aware token weighting mechanism that learns the reuse value of different token types online through eviction feedback; and (3) a fully adaptive online learning schema for all parameter updates, including log-normal timing parameters, position decay power, queue weights, and meta-parameters, which eliminates manual tuning and enables automatic adaptation to deployment-specific workload characteristics. Through extensive evaluation across heterogeneous workloads, we demonstrate that SAECache achieves 1.4x-2.7x TTFT improvement over production-style baselines, while fixed-parameter alternatives can degrade by up to 2.7x under workload mismatch -- a failure mode our adaptive approach avoids entirely.

---


### 16. [In-Context Learning Operates as Concept Subspace Learning](https://arxiv.org/abs/2605.18830)

**<font color=#1a73e8>作者：</font>** Wei Tang, Xinyan Jiang, Fakhri Karray 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regression and Bayesian accounts of in-context learning (ICL) explain how demonstrations can induce predictors, while mechanistic analyses often identify compact activation directions that steer prompted behavior. However, it remains unclear whether structured demonstrations induce low-dimensional concept inference. We study this question through a concept-subspace view of ICL, in which tasks vary only along intrinsic concept coordinates, although inputs are observed in a high-dimensional ambient space. For ridge and least-squares ICL proxies, prediction decomposes exactly into concept-coordinate regression and off-subspace leakage. Under block-diagonal or near-block-diagonal covariance assumptions, the leading estimation and nuisance-sensitivity terms scale with the dimension of the concept subspace, while residual effects are controlled by cross-subspace coupling. This separation gives a mechanistic prediction: recoverable task information should concentrate in a low-dimensional, task-aligned activation subspace. On CounterFact-derived multi-relation prompts with Llama-3-8B, a 68--73-dimensional subspace of the 4096-dimensional residual stream restores 78.8% of the clean--corrupted accuracy gap, whereas patching the complementary subspace restores 0%. Concept swaps redirect predictions toward injected relations, while random and cross-task matched-rank controls are largely ineffective. Additional experiments on Qwen2.5-7B and a controlled cross-lingual rule task show the same qualitative pattern. These results support concept subspaces as compact, task-aligned mediators of recoverable ICL behavior in structured task families, without implying full-circuit recovery.

---


### 17. [Precision Tracked Transformer via Kalman Filtering, Kriging and Process Noise](https://arxiv.org/abs/2605.18832)

**<font color=#1a73e8>作者：</font>** Bo Long, Deepak Agarwal, Jelena Markovic-Voronov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Transformer is the foundational building block of modern AI, yet offers no principled handling of \emph{uncertainty}, which is prevalent in real applications: cold-start tokens with sparse histories in sequential recommendation, heterogeneous signal quality in language models, and attention sinks induced by unconstrained softmax. Every token is treated with uniform confidence. We show this uniformity is a degenerate case of our \emph{Bayesian Filtering Transformer} (BFT): attention becomes precision-weighted kriging, the residual connection becomes a Kalman update with adaptive gain, and the FFN becomes a dynamics model propagating precision via a Jacobian--plus--process-noise rule. Observation precision comes from a parameter-free Restricted Maximum Likelihood (REML) estimator with a conjugate Bayesian prior. BFT replaces any Transformer layer with negligible overhead. On sequential recommendation, BFT applied to three major architectures yields significant gains on six benchmarks, with the largest improvements on cold-start users and rare items where uncertainty is highest. On supervised fine-tuning of large language models with noisy data, BFT improves robustness in two regimes: noisy supervision (token-label corruption in question answering) and noisy context (retrieval-augmented QA with real RAG distractors). A single principled modification -- restoring precision -- unlocks substantial headroom across both classical sequence-modeling and modern LLM regimes.

---


### 18. [StampFormer: A Physics-Guided Material-Geometry-Coupled Multimodal Model for Rapid Prediction of Physical Fields in Sheet Metal Stamping](https://arxiv.org/abs/2605.18835)

**<font color=#1a73e8>作者：</font>** Jiajie Luo, Mohamed Mohamed, Osama Hassan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional sheet metal forming relies on time-consuming and expensive Finite Element Analysis (FEA) for design validation, a process that significantly prolongs design cycles. While surrogate models offer faster iteration, current approaches have limitations: scalar-based methods cannot capture comprehensive field-based FEA results, while existing image-based models often ignore the critical role of material properties by focusing solely on geometry. To address this gap, we develop a physics-guided deep learning framework, namely StampFormer, which simultaneously uses component geometry and material stress-strain responses to predict FEA outcomes. The StampFormer framework uses three core components to process data. A Material-Augmented Geometric Network (MAGN) first fuses geometric and material data. This information is then integrated at various levels by a Hierarchical Material Embedding Injection Unit (HMEIU) before being processed by the primary network backbone, an adapted Swin-UNet. We evaluated our model on the stamping of a crossmember panel with two simulation datasets for steel and aluminium panels, and results demonstrate that StampFormer provides high-fidelity predictions of critical physical fields - including thinning, major strain, minor strain, plastic strain, and displacement - in under a second. Compared with ground truth FEA, our model achieved an average relative error of less than 8.5% on the four 2D fields and a mean squared error of less than 1.2 mm2 for the 3D displacement field. In summary, we introduce a practical and efficient framework that integrates multimodal information, namely geometry and material properties, to provide fast and accurate predictions, enabling designers to perform real-time manufacturability assessments.

---


### 19. [Lying Is Just a Phase: The Hidden Alignment Transition in Language Model Scaling](https://arxiv.org/abs/2605.18838)

**<font color=#1a73e8>作者：</font>** Adil Amin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws predict loss from compute but not how capabilities interact. We measure the coupling between reasoning and truthfulness across 63 base models from 16 families and find a regime change invisible to loss curves: below a family-dependent critical scale $N_c$, capabilities anticorrelate; above it, they cooperate. $N_c \approx 3.5$B parameters [2.9B, 13.4B] (bootstrap 95% CI), but model size is not the only variable that determines phase. Architecture, data curation, and training recipe each shift $N_c$ independently: curated training eliminated the coupling dip between Qwen generations ($0.025 \to 0.830$ at matched scale), Gemma-4 at 4B achieves coupling 0.871, characteristic of 13B+ standard-trained models, through distillation and architectural innovation, and Phi at 1B matches web-trained coupling at 10B through data curation alone. Width normalization eliminates the anticorrelation across all tested families, supporting an output-projection bottleneck. Internally, 38 of 40 models show zero competing attention heads. A sparse-regression ODE cross-predicts held-out Llama-2 at 5.6% error. The diagnostic requires no model internals -- only public benchmark scores across a model family. The cooperative regime extends to the frontier ($r = +0.72$, 34 models, 10 labs). Code, data, and an open-source activation-steering tool for any open-weight model are released alongside an interactive dashboard that diagnoses any model's coupling phase, suggests concrete interventions (data curation, width, benchmark rotation), and provides ODE scaling predictions, frontier diagnostics, and eigenstructure analysis: this https URL.

---


### 20. [TEMPO: Temporal Enforcement via Mode-Separated Policy Optimization for Trustworthy LLM Backtesting](https://arxiv.org/abs/2605.18843)

**<font color=#1a73e8>作者：</font>** Zeyu Zhang, Bradly C. Stadie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backtesting large language models on historical events requires reasoning exclusively from information available before a specified cutoff date. Yet models routinely leak post-cutoff knowledge from pre-training into their reasoning, inflating apparent accuracy and undermining evaluation validity. Prompt-based constraints fail when suppressed content is causally related to the prediction, and knowledge unlearning cannot address this problem because temporal compliance is instance-specific: the same fact may be legitimate evidence for one cutoff date and a violation for another. Rather than erasing knowledge, the model must learn temporal discipline: selecting evidence conditioned on each instance's cutoff date. We propose TEMPO (Temporal Enforcement via Mode-separated Policy Optimization), which trains this discipline via two contributions: (1) a two-mode reward where a leakage mode drives post-cutoff claims to zero as a hard prerequisite before a performance mode optimizes task performance; and (2) a GRPO-based training pipeline that enables the model to discover temporally valid reasoning strategies. We prove that training monotonically decreases leakage, converges to the leak-free optimum, and improves task performance once compliance is achieved. On three prediction tasks and two models, TEMPO reduces leakage from 2~13% to 0.6~3.7% across all conditions, with task performance improving 6~13% where strong pre-cutoff signals exist and maintained where the prediction task is inherently difficult from valid information alone.

---


### 21. [Transformers Linearly Represent Highly Structured World Models](https://arxiv.org/abs/2605.18847)

**<font color=#1a73e8>作者：</font>** Roman Kniazev, Nathanaël Fijalkow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Do transformers, when trained on sequential reasoning traces, build internal models of the underlying task? And if so, does the structure of those internal representations mirror the structure of the domain? We train an 8-layer transformer on Sudoku solving traces and perform a mechanistic analysis of its internal computation. We establish two results. First, the model builds a substructure world model: it does not represent the board state cell by cell, as a human analyst would expect, but organizes information around the rows, columns, and boxes that Sudoku's constraints act on. Second, we identify a naked-single circuit: a small set of dedicated neurons in the final MLP layer, each individually detecting when exactly one digit remains possible for a specific cell, and reliably promoting that digit. These findings show that the geometry of an emergent world model is shaped by the constraint algebra of the domain, not its surface presentation, and that the resulting decision circuit is sparse, monosemantic, and fully interpretable. More broadly, they demonstrate that mechanistic interpretability tools can recover an end-to-end algorithmic account of how a transformer solves a combinatorial reasoning task.

---


### 22. [STRIDE: Learnable Stepwise Language Feedback for LLM Reasoning](https://arxiv.org/abs/2605.18851)

**<font color=#1a73e8>作者：</font>** Junjie Zhang, Guozheng Ma, Shunyu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Reinforcement Learning (RL) have underscored its potential for incentivizing reasoning capabilities of Large Language Models (LLMs). However, existing step-level efforts suffer from costly annotations that limit domain coverage, while scalar scores further impose an information bottleneck, offering insufficient semantic bandwidth to improve intermediate decisions. Alternative language-critique approaches, which rely on frozen or external critics, provide richer textual feedback but lack the scalability needed for sustained policy improvement. In this work, we propose language-driven stepwise trajectory redirection, termed as STRIDE, a novel training framework that shifts process supervision from scalar rewards to learnable stepwise language feedback. Specifically, we co-train a generator and a generative verifier using only outcome-based rewards, eliminating external annotations, while delivering sustained policy improvement through jointly aligned verifier training. The verifier's stepwise language critiques explicitly localize and explain failures, enabling the generator to redirect reasoning trajectories at intermediate steps toward alternative decisions. The trajectory redirection design guarantees harmless policy improvement, even under noisy or suboptimal verifier feedback. Experiments on diverse reasoning benchmarks show that STRIDE significantly outperforms state-of-the-art baselines, as well as achieving breakthroughs on zero-pass-rate problems where scalar methods yield no learning signal in our ablation studies, demonstrating the effectiveness of learnable stepwise language feedback for enhancing LLM reasoning.

---


### 23. [Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking](https://arxiv.org/abs/2605.18852)

**<font color=#1a73e8>作者：</font>** Qinwu Xu, Zhuoheng Li, Jessie Salas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Checkpoint selection for multimodal large language models (MLLMs) presents significant challenges when performance differentials are marginal and evaluation signals are prone to noise. Existing methodologies rely heavily on static benchmarks or pointwise scoring, which frequently misalign with in-the-wild usage and lack robust uncertainty estimation, particularly in OCR-heavy scenarios. In this work, we formulate checkpoint selection as a robust decision problem under evaluation uncertainty. We propose a multi-stage framework that integrates curated real-world data, structured LLM-based judgment, and multi-stage ranking protocols. The evaluation system orchestrates progressive refinement via pointwise filtering, listwise ranking, and pairwise comparison. To enhance reliability, we introduce subsampling-based confidence estimation and a percentile-based scoring formulation that captures distributional characteristics while penalizing tail failures. Furthermore, we demonstrate that data quality, specifically OCR readability, is a critical determinant of evaluation validity.

---


### 24. [TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing](https://arxiv.org/abs/2605.18859)

**<font color=#1a73e8>作者：</font>** Pei Yang, Wanyi Chen, Tongyun Yang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls. Routing each call to the cheapest sufficient model can cut costs without sacrificing quality, yet existing router benchmarks evaluate routers only on one-shot prompts. They never expose the router-visible prefix at an intermediate agent step, never test whether a cheaper replacement preserves downstream task success, and often rely on online LLM judges at evaluation time. We introduce TwinRouterBench, a step-level routing benchmark with two tracks. The static track provides 970 router-visible prefixes from 520 instances across SWE-bench, BFCL, mtRAG, QMSum, and PinchBench, each paired with an execution-verified target tier estimated under a released downgrade-and-cascade protocol; scoring is deterministic arithmetic over tier labels, trajectory membership, and token costs, with no online evaluator-side LLM judge. The dynamic track supplies a harness that runs routers on the full 500-case SWE-bench Verified suite; in this paper we report a 100-case held-out evaluation disjoint from the static SWE supervision split. At each LLM call the router selects a concrete model from a locked pool, and success is measured by official task resolution and realized API spend. The two tracks support fast offline iteration followed by end-to-end validation under live agent execution. Code and data are available at this https URL.

---


### 25. [From Llama to Cria: Scaling Down Neural Networks via Neuron-Level Spectral Structural Importance Evaluation](https://arxiv.org/abs/2605.18860)

**<font color=#1a73e8>作者：</font>** Yongyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a neuron pruning framework based on neuron-level spectral structural importance evaluation. Given a trained neural network, we record the hidden states of each hidden layer during inference and model neurons as graph nodes, with hidden states treated as graph signals. Using ideas from graph signal processing, we infer layer-wise input and output graphs that characterize the structural relationships among neurons before and after each layer transformation. We then evaluate the spectral structural importance of neurons by analyzing the transformation between these graphs based on spectral graph theory. Neurons with high spectral structural importance are regarded as strongly involved in the internal representation transformation and are therefore preserved, while neurons with low importance scores are selected as pruning candidates. The pruning process is conducted iteratively until a predefined effective parameter reduction target is reached. Instead of fine-tuning after every pruning step, the proposed strategy first removes low-importance neurons to obtain a compact architecture and then applies a final recovery fine-tuning stage to restore task performance. By connecting neuron pruning with graph signal processing and spectral structural analysis, the proposed framework offers a principled way to reduce neural network size while maintaining solution quality. Experimental results on CIFAR-10 image classification and SST-2 sentiment classification show that our method can effectively remove low-importance neurons and achieve compact networks with competitive performance after recovery fine-tuning.

---


### 26. [SAGE: Shaping Anchors for Guided Exploration in RLVR of LLMs](https://arxiv.org/abs/2605.18864)

**<font color=#1a73e8>作者：</font>** Chanuk Lee, Minki Kang, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies observe that reinforcement learning with verifiable rewards (RLVR) reliably improves pass@1 on reasoning tasks, yet often fails to yield comparable gains in pass@k, raising the question of whether RLVR genuinely enables large language models to acquire novel reasoning abilities or merely enhances the efficiency of sampling reasoning modes already present in the base model. Prior analyses largely support the latter view, attributing this limitation to structural properties of standard RLVR objectives that result in insufficient exploration pressure. In this work, we argue that a central structural constraint arises from reverse-KL regularization, which stabilizes training but inherently anchors the policy to the reference distribution, thereby suppressing the emergence of alternative reasoning modes. However, we show that neither removing the KL term nor replacing it with forward-KL provides a satisfactory solution, as both disrupt the efficiency-coverage trade-off by either inducing reward hacking or allocating probability mass to off-target regions. To resolve this tension, we propose SAGE, a principled framework that enables controllable empirical support expansion by reshaping the reverse-KL anchor distribution itself through a guide function q(x,y), achieving consistent improvements in both pass@1 and pass@k across challenging mathematical reasoning benchmarks. Our code is available at this https URL.

---


### 27. [MO-CAPO: Multi-Objective Cost-Aware Prompt Optimization](https://arxiv.org/abs/2605.18869)

**<font color=#1a73e8>作者：</font>** Jan Büssing, Moritz Schlager, Timo Heiß 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance across a wide range of tasks but are highly sensitive to prompt design, motivating the need for automatic prompt optimization. Existing methods predominantly focus on performance alone, ignoring competing objectives such as inference cost or latency. At the same time, existing work on multi-objective prompt optimization relies on off-the-shelf NSGA-II, ignoring optimization efficiency. As a remedy, we introduce MO-CAPO, a novel multi-objective prompt optimization algorithm that jointly optimizes performance and inference cost while leveraging budget allocation for cost-efficient optimization. We further propose a deployment-oriented cost objective that captures the full computational profile of LLM inference. We evaluate our approach across four tasks and three LLMs and compare it to an NSGA-II-based multi-objective method and state-of-the-art single-objective prompt optimizers. Results show that MO-CAPO consistently identifies strong, robust, and diverse Pareto front approximations while maintaining cost-efficiency. It outperforms the NSGA-II baseline on 8 out of 12 cases in terms of the noisy R2 metric and achieves competitive performances often already at a considerably lower budget. The discovered solution sets span diverse performance-cost trade-offs that are omitted by single-objective optimizers, yet the top-performance candidates remain competitive with single-objective solutions. Additionally, we conduct the first evaluation of multi-objective machine learning experiments that considers generalization and robustness through noisy R2 and approximation gap, enabling a more realistic assessment of solution quality. MO-CAPO enables practitioners to select from an efficiently discovered set of multiple prompts offering different trade-offs between performance and cost.

---


### 28. [Distributional Energy-Based Models for Uncertainty-Aware Structured LLM Reasoning](https://arxiv.org/abs/2605.18871)

**<font color=#1a73e8>作者：</font>** Shireen Kudukkil Manchingal, Abhey Kalia, Fernanda Gonçalves 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When Large Language Models produce structured outputs such as travel plans, code solutions, or multi-step proofs, individual reasoning steps may appear correct while the output as a whole violates budgets, fails test cases, or contradicts earlier deductions. We propose a decomposed energy function that combines a learned quality scorer with deterministic analytical constraint penalties for verifying structured LLM outputs. The quality scorer is a heterogeneous ensemble of low-rank adapters on a single frozen encoder (3% trainable parameters); the ensemble mean ranks candidates while the standard deviation quantifies epistemic uncertainty, driving a two-pass inference loop that triggers targeted regeneration or abstention. Across five benchmarks (GSM8K, MuSR, TravelPlanner, TACO, Knights & Knaves), our 149M-parameter verifier orchestrating a pool of 7-26B open generators outperforms single-shot Qwen-72B on every benchmark, matches Claude Sonnet 4.6 on MuSR (67.7% vs. 68.0%), and reduces constraint violations by 53% relative to Opus 4.6 on TravelPlanner (oracle 0.028, random 0.231). The two routes are complementary: structural verification wins when constraints are checkable (the verifier captures signal frontier models cannot self-detect), while pretraining-scale priors win where they are not (narrative inference, code semantics). A cross-dataset confounding analysis confirms genuine quality discrimination on four reasoning tasks and identifies a model-identity shortcut on code, mitigated via last-layer retraining. Scorers trained on difficult data transfer zero-shot: a MuSR-trained scorer achieves 93.9% on GSM8K without seeing a math problem.

---


### 29. [ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models](https://arxiv.org/abs/2605.18879)

**<font color=#1a73e8>作者：</font>** Yujie Lin, Chengyi Yang, Zhishang Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models inevitably retain sensitive information, defined as inputs that may induce harmful generations, due to training on massive web corpora, raising concerns for privacy and safety. Existing machine unlearning methods primarily rely on retraining or aggressive fine-tuning, which are either computationally expensive or prone to degrading related knowledge and overall model utility. In this work, we reformulate machine unlearning as a precise knowledge re-mapping problem via model editing. We propose ZeroUnlearn, a few-shot unlearning framework. It overwrites sensitive inputs by mapping them to a neutral target state and removing their original representations. ZeroUnlearn enforces representational orthogonality through a multiplicative parameter update with a closed-form solution, enabling efficient and targeted unlearning. We further extend ZeroUnlearn to a gradient-based variant for multi-sample unlearning. Experiments demonstrate that our approach outperforms existing baselines while preserving general model utility. Our code is available at the github: this https URL.

---


### 30. [To Call or Not to Call: Diagnosing Intrinsic Over-Calling Bias in LLM Agents](https://arxiv.org/abs/2605.18882)

**<font color=#1a73e8>作者：</font>** Wei Shi, Ziheng Peng, Sihang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents exhibit a consistent tendency to over-call, invoking tools even in situations where none is needed. On the When2Call benchmark, six models from three families show high call accuracy but much lower no-call accuracy, leaving overall accuracy in the 55%-70% range. We trace this to an Intrinsic Bias Hypothesis (IBH): the call/no-call decision mapping carries an activation-independent call offset, so the model favors call even at activation parity. Using Sparse Autoencoders (SAEs), we recover behavior-aligned feature bases for the call/no_call decision, reduce them to a signed activation margin, and estimate the offset directly. Across all six models, the model is decision-neutral only when no_call activation outweighs call activation, consistent with IBH. We then causally test IBH with Adaptive Margin-Calibrated Steering (AMCS), a closed-form counter-bias shift along SAE decoder directions. Cancelling the diagnosed offset mitigates over-calling and improves overall accuracy with a negligible drop in call accuracy. Our work recasts over-calling from an empirical phenomenon into a mechanistic object amenable to causal correction. Code is available at this https URL.

---


### 31. [Navigating the Emotion Tree: Hierarchical Hyperbolic RAG for Multimodal Emotion Recognition](https://arxiv.org/abs/2605.18884)

**<font color=#1a73e8>作者：</font>** Zeheng Wang, Bo Zhao, Yijie Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition aims to integrate text, audio, and video sources to understand human affective states. Although multimodal large language models excel at multimodal reasoning, they typically treat emotion categories as independent labels, ignoring the rich hierarchical taxonomy of human psychology. Moreover, lacking external contextual knowledge makes them highly susceptible to over-interpreting noisy cues, further complicating fine-grained emotion classification. To address these issues, we propose \textbf{HyperEmo-RAG}, a retrieval-augmented generation framework that leverages a structured emotional knowledge base. Our framework introduces two key innovations. 1) Hierarchical hyperbolic grounding. Recognizing the inherent hierarchical tree structure of emotion taxonomies, we jointly embed hierarchical emotion labels and multimodal samples into a continuous hyperbolic space (Poincaré ball) and design a hierarchical beam-search deliberation process that progressively retrieves samples from coarse to fine-grained levels. 2) Structured evidence injection. Based on the retrieved evidence, we construct an evidence graph and inject the structured knowledge as explicit cognitive context into the LLM through a Tree-Aware Attention mechanism and an EmotionGraphFormer, preserving the integrity of graph-structured information. Experiments on multiple datasets demonstrate that HyperEmo-RAG significantly outperforms existing methods.

---


### 32. [A Two-Parameter Weibull Framework for Diagnosing Transformer Weight Distributions](https://arxiv.org/abs/2605.18898)

**<font color=#1a73e8>作者：</font>** Tiexin Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We apply the Weibull distribution -- a two-parameter family from extreme-value theory -- as a diagnostic framework for element-wise weight magnitude distributions in transformers. At initialization, i.i.d. Gaussian weights give |w| ~ HalfNormal, yielding k ~ 1.20 via middle-80% probability-plot fit (the protocol used throughout this work). This anchor makes k a principled, architecture-independent measuring stick for training dynamics; fitting each weight matrix independently at every layer at every checkpoint enables per-component, per-layer, and per-step diagnostics that aggregate statistics cannot resolve.
Applying this framework to 12 model entries spanning 7 architectural families (Pythia, OLMo-1/2, LLaMA-3, Mistral, Qwen2.5/3) reveals three findings. First, FFN modules and the attention output projection W_o -- the Transmission Class -- fall in a narrow k band: median terminal k in [1.186, 1.204] across 12 entries (cross-family CV = 0.51%), shared across SwiGLU/GeLU activations, Pre-LN/QK-Norm placements, and 70M-14B sizes. Second, the attention input projections W_q, W_k -- the Selection Class -- depart from the Weibull family, with severity shaped by storage: separately-stored Q/K (OLMo-1, OLMo-2) yields k in [0.76, 0.99] (deep); GQA models yield k in [1.10, 1.16] (mild); Pythia's merged W_qkv occupies a transitional zone tracking training budget T/tau monotonically. Third, lambda grows substantially during training and scales with sqrt(eta/lambda_wd) within the Pythia family (Pearson r = 0.94, three Transmission kinds), directionally consistent with Fan et al. (2025). The two parameters carry independent information: k labels the functional class, lambda labels training progress.
We release npm-weibull-py v0.4 (Python library) and DATABASE_v9_1 at this https URL .

---


### 33. [Don't Let Bandit Feedback Pull Continual LLM-Recommender Updates Off Target](https://arxiv.org/abs/2605.18899)

**<font color=#1a73e8>作者：</font>** Taesan Kim, Hyeongjun Yun, Jaegul Choo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative LLM-based recommenders (LLM-Rec) require continual post-deployment updates, yet deployment logs provide only policy-shaped contextual bandit feedback: outcomes are observed solely for items exposed by a prior serving policy, inducing exposure bias and yielding partial, asymmetric signals consisting of relatively reliable positive responses and ambiguous no-responses. We propose an Anchored Bandit Policy Optimization (ABPO) framework for continual LLM-Rec updates that combines group-relative policy optimization (GRPO) with explicit treatment of exposure bias and feedback ambiguity. Specifically, we insert the exposed recommendation as a logged anchor into each GRPO rollout group, so that group-relative normalization is calibrated against the action actually exposed by the prior policy rather than against newly sampled rollouts alone. Because both positive- and no-responses are observed only through prior-policy exposure, we apply self-normalized inverse propensity scoring to the fixed anchor for both feedback types to correct for policy mismatch. At the same time, we treat the two feedback types asymmetrically in reliability: positive responses provide relatively direct endorsement signals, whereas no-responses remain ambiguous because they may reflect either true disinterest or unobserved external factors. To avoid overly aggressive updates from ambiguous no-responses, we temper their penalties with self-certainty, using the model's output-token confidence as a verifier-free reliability signal. Across five domains from Amazon Reviews and MovieLens, our method yields consistent post-update gains in recommendation accuracy while mitigating prior-policy-induced exposure bias more effectively than prior baselines.

---


### 34. [Reasoning Portability: Guiding Continual Learning for MLLMs in the RLVR Era](https://arxiv.org/abs/2605.18903)

**<font color=#1a73e8>作者：</font>** Qiuhe Hong, Yuyang Liu, Shuo Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models in Continual Learning (VLM-CL) aim to continuously adapt to new multimodal tasks while retaining prior knowledge. The emerging paradigm that couples Multimodal Large Language Models (MLLMs) with Reinforcement Learning with Verifiable Rewards (RLVR) calls for a new pattern to guide continual adaptation. Advances in reasoning capability now make it feasible to impose constraints at the reasoning level. We formalize portability, a sample-level measure of how reusable the previous policy's behavior is on a new task, and empirically show that reasoning-level signals remain reliable on out-of-distribution samples while answer-level signals do not. We instantiate this as Reasoning Portability (RP) and propose Reasoning-based Dynamic Balance Continual Learning (RDB-CL), which modulates the per-sample Kullback-Leibler regularization in RLVR according to RP: a tight anchor preserves reusable reasoning on high-RP samples, while a relaxed anchor on low-RP samples permits exploration of new reasoning pathways. Experiments show that RDB-CL consistently outperforms baselines, improving Last accuracy by +12.0% over the vanilla RLVR baseline.

---


### 35. [HypergraphFormer: Learning Hypergraphs from LLMs for Editable Floor Plan Generation](https://arxiv.org/abs/2605.18932)

**<font color=#1a73e8>作者：</font>** Nikita Klimenko, Hesam Salehipour, Parham Eftekhar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we propose HypergraphFormer, a novel and efficient approach to floor plan generation based on learning hypergraph representations with a large language model (LLM). The model is trained via supervised fine-tuning to generate a hypergraph-based textual representation that encodes spatial relationships and connectivity information within floor plans. We train and evaluate our approach on the RPLAN dataset, and further demonstrate its generalizability on a separate out-of-distribution dataset, which we release in this paper. Our method outperforms state-of-the-art techniques based on rasterized or vectorized representations across a diverse set of metrics. We also show improved data efficiency, particularly under distribution shift. The hypergraph formulation enables the generation of floor plans for arbitrary, irregular, user-specified boundaries by decoupling apartment footprints from their functional and geometric subdivisions. Furthermore, we show that the proposed methodology offers a high degree of editability, making it particularly well suited to design-oriented workflows supported by LLMs.

---


### 36. [Evaluating the Utility of Personal Health Records in Personalized Health AI](https://arxiv.org/abs/2605.18937)

**<font color=#1a73e8>作者：</font>** Rory Sayres, Kejia Chen, Ayush Jain 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patient-managed Personal Health Records (PHRs) promises to empower patients to better understand their health; but information in the record is complex, potentially hindering insights. In this study, we assess the potential of large language models (LLMs, Gemini 3.0 Flash) to provide helpful answers to user health queries, when provided clinical data from PHRs as context. A total of 2,257 user queries were drawn from 3 different distributions to represent patient questions: shorter web search queries, longer questions derived from templates of chatbot conversations, and questions patients asked to their healthcare team (patient calls). Queries were matched with de-identified PHRs (from a pool of 1,945). Gemini responses were generated (1) without PHR context; (2) with a basic summary of demographics, conditions, and medications; (3) with full, extensive clinical notes. For evaluation, we leveraged an existing rating framework (SHARP), and developed a new framework for specific error modes when interpreting PHRs. Evaluation was performed using autoraters for the full set, and with clinician ratings for a subset (n=95), with both sets of raters knowing the full PHR context. We see significant improvements in the helpfulness of answers to all question types with PHR data (p < 0.001, paired t-test). We also observe potential gains in safety, accuracy, relevance and personalization of answers. Our PHR evaluation framework further identifies gaps in LLM understanding of particular aspects of complex PHRs, such as temporal disorientation, and rare but meaningful confabulations. These results suggest potential for PHR data to help people with a wide range of user needs; and provide a framework for monitoring for gaps in LLM answers based on PHR context. This study motivates further work to assess and realize potential benefits to users from understanding their health records.

---


### 37. [MotionMERGE: A Multi-granular Framework for Human Motion Editing, Reasoning, Generation, and Explanation](https://arxiv.org/abs/2605.18956)

**<font color=#1a73e8>作者：</font>** Bizhu Wu, Jinheng Xie, Wenting Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent motion-language models unify tasks like comprehension and generation but operate at a coarse granularity, lacking fine-grained understanding and nuanced control over body parts needed for animation or interaction. This stems from fundamental issues in both the model and the data, in which the model can't focus on motion's localized pattern, and the training data lacks fine-grained supervision. To tackle this, we propose MotionMERGE, a unified framework that bridges the granularity gap. First, we pioneer the study of fine-grained languageguided motion control, including detailed understanding and localized editing, by explicitly modeling motion at part and temporal levels within a single LLM, thereby endowing the model with robust priors for precise control. Second, we design ReasoningAware Granularity-Synergy pre-training, a novel strategy that employs joint supervision for cross-granularity alignment, temporal grounding, localized alignment, motion coherency, and motion-grounded chain-of-thought (CoT) reasoning. This equips the model with fine-grained motion-language alignment, crossgranularity synergy, and explicit reasoning ability. Third, we curate MotionFineEdit, a large-scale dataset (837K atomic + 144K complex triplets) with the first fine-grained spatio-temporal corrective instructions and motion-grounded CoT annotations, establishing a new benchmark for fine-grained text-driven motion editing and motion-grounded reasoning. Extensive experiments demonstrate the capability of MotionMERGE for more precise motion generation, understanding, and editing, and compelling zero-shot generalization to other complex motion tasks. This work represents a significant step toward models that interact with motion in finer granularity and human-like reasoning.

---


### 38. [Shaping the Prior: How Synthetic Task Distributions Determine Tabular Foundation Model Quality](https://arxiv.org/abs/2605.18971)

**<font color=#1a73e8>作者：</font>** Mohamed Bouadi, Nassim Bouarour, Varun Kulkarni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What determines the quality of a tabular foundation model? Unlike language or vision, tabular foundation models acquire their inductive biases almost entirely from synthetic pretraining distributions, yet the design of these distributions remains poorly understood. Standard synthetic priors are too well-behaved: they omit the irregularities and failure modes that determine deployment robustness. We introduce O'Prior, a compositional realism prior built around four coupled components: a hierarchical SCM meta-generator spanning diverse functional families; a modular realism engine covering heterogeneous marginals, missingness, and target transforms; an explicit stress module injecting confounding and support-query mismatch; and a curriculum-governed, leakage-safe generation protocol. To isolate prior design as the scientific variable, we hold architecture, optimizer, and compute budget fixed and vary only the synthetic task distribution. O'Prior yields consistent and substantial improvements in downstream accuracy and robustness across real tabular benchmarks, with gains concentrated in regimes characterized by distributional irregularities. Ablations confirm that mechanism diversity, realism composition, and shift-aware stress each contribute independently, their effects are not interchangeable. These results establish synthetic prior construction as a first-order and largely overlooked determinant of tabular foundation model quality

---


### 39. [TabQL: In-Context Q-Learning with Tabular Foundation Models](https://arxiv.org/abs/2605.18979)

**<font color=#1a73e8>作者：</font>** Qisai Liu, Zhanhong Jiang, Timilehin Ayanlade 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Tabular Q-Learning (TabQL), a reinforcement learning framework that replaces the conventional parametric Q-network in Deep Q-Learning (DQN) with a tabular foundation model endowed with in-context learning capabilities. The key idea is to represent Q-values through a sequence-to-sequence foundation model operating over a tabularized representation of state-action-Q-value tuples, enabling rapid adaptation from limited online interaction by conditioning on recent experience. TabQL departs from classical DQN by leveraging (i) zero- or few-shot Q-value inference via in-context updates, and (ii) a warm-up phase using standard DQN to bootstrap high-quality context. Particularly, to enhance the context quality, new transitions are generated by executing actions output by TabQL with predicted Q values from DQN. We formalize TabQL, analyze its convergence and sample complexity under mild assumptions, and show that TabQL interpolates between vanilla Q-learning and DQN with in-context learning. Our analysis demonstrates that TabQL achieves improved efficiency compared to DQN by amortizing Bellman updates through in-context learning. Extensive numerical experiments with several benchmarks showcase the effectiveness and efficacy of the proposed TabQL.

---


### 40. [Artifact-Bench: Evaluating MLLMs on Detecting and Assessing the Artifacts of AI-Generated Videos](https://arxiv.org/abs/2605.18984)

**<font color=#1a73e8>作者：</font>** Yuqi Tang, Yang Shi, Zhuoran Zhang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generative models have greatly improved the realism of AI-generated videos, yet their outputs still exhibit artifacts such as temporal inconsistencies, structural distortions, and semantic incoherence. While Multimodal Large Language Models (MLLMs) show strong visual understanding capabilities, their ability to perceive and reason about such artifacts remains unclear. Existing benchmarks often lack systematic evaluation of artifact-aware perception and fine-grained diagnostic reasoning, especially across diverse AI-generated video domains beyond photorealistic content. To address this gap, we introduce Artifact-Bench, a comprehensive benchmark for evaluating MLLMs on AI-generated video artifact detection and analysis. We first establish a three-level hierarchical taxonomy of realism artifacts, covering photorealistic, animated, and CG-style videos. Based on this taxonomy, Artifact-Bench defines three complementary tasks: real vs. AI-generated video classification, pairwise realism comparison, and fine-grained artifact identification. Experiments on 19 leading MLLMs reveal substantial limitations in artifact perception and reasoning, with many models approaching random or even below-random performance in challenging settings. We further observe significant misalignment between MLLM judgments and human perceptual preferences, highlighting their limited reliability as general evaluators for AI-generated video realism.

---


### 41. [EgoTraj: Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction](https://arxiv.org/abs/2605.19004)

**<font color=#1a73e8>作者：</font>** Ahmad Yehia, Abduallah Mohamed, Tianyi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately forecasting human trajectories from an egocentric perspective plays a central role in applications such as humanoid robotics, wearable sensing systems, and assistive navigation. However, progress in this direction remains limited due to the scarcity of egocentric trajectory datasets collected in real-world environments. Addressing this need, we introduce EgoTraj, an egocentric multimodal open dataset recorded using Meta Quest Pro (MQPro). EgoTraj contains 75 sequences of human navigation collected from multiple MQPro wearers in real-world urban environments. Each recording provides synchronized RGB video along with ground-truth data, including continuous time-synchronized 6-degree-of-freedom head poses, per-frame 3D eye gaze vectors, scene annotations. To the best of our knowledge, EgoTraj differs from typical egocentric trajectory datasets by capturing long-horizon, self-directed navigation across diverse urban routes with broad participant diversity. To demonstrate the potential of the dataset, we benchmark several state-of-the-art methods for egocentric trajectory prediction and conduct ablation studies to analyze the contributions of gaze, scene, and motion cues. The results highlight the utility of EgoTraj for AR-based perception, navigation, and assistive systems. The EgoTraj dataset, code, and EgoViz Dashboard are publicly available at this https URL.

---


### 42. [LoRA vs. Full Fine-Tuning: A Theoretical Perspective](https://arxiv.org/abs/2605.19018)

**<font color=#1a73e8>作者：</font>** Ali Zindari, Rotem Mulayoff, Sebastian U. Stich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning adapts a pre-trained model to downstream tasks using a small amount of labeled data. Low-Rank Adaptation (LoRA) is an efficient fine-tuning method that reduces memory and computation costs while often achieving performance close to full fine-tuning. Despite its widespread use, the theoretical behavior of LoRA is not yet well understood. In this paper, we study LoRA in a simple linear regression setting and compare its excess risk with that of full fine-tuning. Our analysis identifies regimes in which LoRA achieves lower excess risk than full fine-tuning in both overdetermined and underdetermined settings. Specifically, our theory predicts that LoRA can outperform full fine-tuning when the difference between the pretraining and the downstream tasks is effectively low-rank. We further show how the choice of LoRA rank affects generalization performance, explaining why using a very small rank can improve test accuracy in certain settings, even though it limits model expressivity. Finally, we support our theoretical results with experiments on practical tasks, suggesting that the identified tradeoffs and insights extend beyond linear regression.

---


### 43. [A Systematic Failure Analysis of Vision Foundation Models for Open Set Iris Presentation Attack Detection](https://arxiv.org/abs/2605.19020)

**<font color=#1a73e8>作者：</font>** Rahul Anand, Siddharth Singh, Dileep A D 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have demonstrated strong transferability across diverse visual recognition tasks and are increasingly considered for biometric applications. Their suitability for iris Presentation Attack Detection (PAD), particularly under realistic open-set operating conditions, remains insufficiently examined. This work presents a systematic failure analysis of general-purpose vision foundation models for open-set iris PAD using periocular imagery. Five representative foundation models are evaluated under three open-set protocols that explicitly separate different sources of distribution shift: unseen Presentation Attack Instruments (PAIs), unseen datasets captured with different sensors and cross-spectral transfer from near-infrared (NIR) to visible spectrum (VIS) imagery. Both frozen feature representations and parameter-efficient task adaptation using Low-Rank Adaptation (LoRA) are assessed within a unified experimental framework. The results indicate that foundation models can transfer across datasets with similar sensing characteristics, but fail to generalise reliably to unseen attack instruments and degrade sharply under cross-spectral evaluation. While LoRA improves performance in certain cross-dataset settings, it frequently amplifies failure under attack-level and spectral shifts. Additional validation experiments using segmented iris inputs, full backbone fine-tuning, joint cross-dataset and cross-PAI shifts, and reverse VIS to NIR transfer further confirm that these failures are not simply artefacts of periocular input, weak adaptation, or one-directional spectral evaluation. These findings show that strong closed-set or cross-dataset performance should not be treated as evidence of robust open-set security, and highlight the need for PAD representations that maintain sensitivity to presentation artefacts while remaining stable under realistic deployment variation.

---


### 44. [MedFM-Robust: Benchmarking Robustness of Medical Foundation Models](https://arxiv.org/abs/2605.19027)

**<font color=#1a73e8>作者：</font>** Xiangxiang Cui, Tianjin Huang, Yifang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical foundation models (MedFMs) have emerged as transformative tools in healthcare, demonstrating capabilities across diverse clinical applications. These models can be broadly categorized into two paradigms: Medical Vision-Language Models (Med-VLMs) and segmentation foundation models. Med-VLMs range from medical-specialized models such as LLaVA-Med and MedGemma, to general-purpose models like GPT-4o and Gemini, all capable of medical image understanding tasks including visual question answering (VQA), report generation, and visual grounding. Concurrently, the Segment Anything Model (SAM) has catalyzed a new generation of medical segmentation models, with adaptations like SAM-Med2D and MedSAM. The widespread clinical deployment of these models thus necessitates rigorous evaluation of their reliability under real-world conditions.

---


### 45. [Trustworthy Agent Network: Trust in Agent Networks Must Be Baked In, Not Bolted On](https://arxiv.org/abs/2605.19035)

**<font color=#1a73e8>作者：</font>** Yixiang Yao, Yuhang Yao, Xinyi Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Language Models has given rise to autonomous LLM-based agents capable of complex reasoning and execution. As these agents transition from isolated operation to collaborative ecosystems, we witness the emergence of the Agent-to-Agent (A2A) network, a paradigm where heterogeneous agents autonomously coordinate to solve multi-step tasks. While these networks may offer better task performance compared to simply using one agent to complete the entire task, they introduce systemic vulnerabilities, such as adversarial composition, semantic misalignment, and cascading operational failures, that existing agent alignment techniques cannot address. In this vision paper, we argue that the trustworthiness of A2A networks cannot be fully guaranteed via retrofitting on existing protocols that are largely designed for individual agents. Rather, it must be architected from the very beginning of the A2A coordination framework. We present a comprehensive conceptual framework that situates trust in A2A systems through four design pillars.

---


### 46. [Benchmarking Commercial ASR Systems on Code-Switching Speech: Arabic, Persian, and German](https://arxiv.org/abs/2605.19069)

**<font color=#1a73e8>作者：</font>** Sajjad Abdoli, Ghassan Al-Sumaidaee, Clayton W. Taylor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching -- the natural alternation between two languages within a single utterance -- represents one of the most challenging and under-studied conditions for automatic speech recognition (ASR). Existing commercial ASR benchmarks predominantly evaluate clean, monolingual audio and report a single Word Error Rate (WER) figure that tells practitioners little about real-world multilingual performance. We present a benchmark evaluating five commercial ASR providers across four language pairs: Egyptian Arabic--English, Saudi Arabic (Najdi/Hijazi)--English, Persian (Farsi)--English, and German--English. Each dataset comprises 300 samples selected by a two-stage pipeline: a heuristic filter scoring transcripts on five structural code-switching signals, followed by a GPT-4o and Gemini 1.5 Pro ensemble scoring candidates across six linguistic dimensions. This pipeline reduces LLM scoring costs by approximately 91\% relative to exhaustive scoring. We evaluate the systems on both WER and BERTScore, arguing that BERTScore is a more reliable metric for Arabic and Persian pairs where transliteration variance causes WER to penalise semantically correct transcriptions. ElevenLabs Scribe v2 achieves the lowest WER across all four language pairs (13.2% overall; 13.1% on Egyptian Arabic) and leads on BERTScore (0.936 overall). We further demonstrate that difficulty-stratified analysis reveals performance gaps masked by aggregate averages, and that BERT embedding projections confirm semantic proximity between reference and hypothesis despite surface-level script differences. The benchmarking dataset is publicly available at this https URL.

---


### 47. [CRAFT: Critic-Refined Adaptive Key-Frame Targeting for Multimodal Video Question Answering](https://arxiv.org/abs/2605.19075)

**<font color=#1a73e8>作者：</font>** Mahesh Bhosale, Abdul Wasi, Vishvesh Trivedi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounded multi-video question answering over real-world news events requires systems to surface query-relevant evidence across heterogeneous video archives while attributing every claim to its supporting source. We introduce CRAFT (Critic-Refined Adaptive Key-Frame Targeting), a query-conditioned pipeline that combines dynamic keyframe selection, per-video ASR with multilingual fallback, and a hybrid critic loop to iteratively verify and repair claims before consolidation. The pipeline integrates UNLI temporal entailment, DeBERTa-v3 cross-claim screening, and a Llama-3.2-3B adjudicator, with a final citation-merging stage that emits each fact once with all supporting source identifiers. On MAGMaR 2026, CRAFT achieves the best overall average (0.739), reference recall (0.810), and citation F1 (0.635). We further evaluate on a MAGMaR-style conversion of WikiVideo with 52 non-overlapping event queries, where CRAFT also performs strongly (0.823 Avg), showing that its claim-centric evidence aggregation generalizes beyond MAGMaR. Ablations show that atomic claims, ASR, and the critic loop drive the main gains over the vanilla query-conditioned baseline. Code and implementation details are publicly available at this https URL.

---


### 48. [ReacTOD: Bounded Neuro-Symbolic Agentic NLU for Zero-Shot Dialogue State Tracking](https://arxiv.org/abs/2605.19077)

**<font color=#1a73e8>作者：</font>** Yanjun Lin, Zimo Xiao, Kartik Natarajan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented dialogue systems -- handling transactions, reservations, and service requests -- require predictable behavior, yet the moderately-sized LLMs needed for practical latency are prone to hallucination and format errors that cascade into incorrect actions (e.g., a hotel booked for the wrong date). We propose ReacTOD, a bounded neuro-symbolic architecture that reformulates NLU as discrete tool calls within a self-correcting ReAct loop governed by deterministic validation. A bounded ReAct loop enables iterative self-correction, improving accuracy by up to 9.3 percentage points over single-pass inference on MultiWOZ. A symbolic validator enforces action compliance, schema conformance, and coreference consistency on every dialogue state update, achieving a 93.1% self-correction rate on intercepted errors and producing structured execution traces. Incremental state prediction and on-demand history retrieval keep prompts compact, empirically improving instruction adherence in parameter-constrained models. On MultiWOZ 2.1, ReacTOD achieves a new zero-shot state-of-the-art: gpt-oss-20B reaches 52.71% joint goal accuracy, surpassing the previous best by 14 percentage points, while Qwen3-8B achieves 47.34% with only 8B parameters. On the Schema-Guided Dialogue (SGD) benchmark, ReacTOD with Claude-Opus-4.6 achieves 80.68% JGA under fully end-to-end evaluation with predicted domains, and Qwen3-32B reaches 64.09% -- demonstrating cross-benchmark generalization without task-specific training data.

---


### 49. [ScheduleFree+: Scaling Learning-Rate-Free & Schedule-Free Learning to Large Language Models](https://arxiv.org/abs/2605.19095)

**<font color=#1a73e8>作者：</font>** Aaron Defazio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schedule-Free Learning has shown promise as a practical anytime training method for machine learning, showing success across dozens of standard benchmark problems. However, strong performance for LLM training has only been demonstrated at small scales. We identify a number of fixes necessary to scale up Schedule-Free Learning to larger batch sizes and model sizes, and present a learning-rate-free and schedule-free method (ScheduleFree+) for training large language models which greatly outperforms Warmup-Stable-Decay (WSD) schedules. We also demonstrate that Schedule-Free Learning is most effective for long duration training, and at 1000 tokens per parameter, it outperforms SOTA schedules by 31%. Schedule-Free Learning provides a theoretical foundation for the use of model averaging and checkpoint merging during pretraining.

---


### 50. [DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows](https://arxiv.org/abs/2605.19099)

**<font color=#1a73e8>作者：</font>** Yuxuan Gao, Megan Wang, Yi Ling Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce DecisionBench, a benchmark substrate for emergent delegation in long-horizon agentic workflows. The substrate fixes a task suite (GAIA, tau-bench, BFCL multi-turn), a peer-model pool (11 models, 7 vendor families), a delegation interface (call_model plus an optional read_profile channel), a deterministic skill-annotation layer, and a multi-axis metric suite covering quality, cost, latency, delegation rate, routing fidelity-at-k, vendor self-preference, and a counterfactual-delegation ceiling. The substrate is agnostic to how peer information is generated or delivered, so learned routers, richer peer memories, adaptive profile construction, and multi-step delegation can all be evaluated against it. We characterize the substrate with a five-condition reference sweep on the full pool (n=23,375 task instances). Three benchmark-level findings emerge: (i) mean end-task quality is statistically indistinguishable across the four awareness conditions (|beta| <= 0.010, p >= 0.21), so quality-only evaluation would miss the orchestration signal; (ii) routing fidelity-at-1 ranges from 7.5% to 29.5% across conditions at near-equal mean quality, with delivery channel (on-demand tool vs. preloaded description) dominating description content; (iii) a counterfactual ceiling places perfect delegation 15-31 percentage points above measured performance on every suite, locating large unrealized headroom for future orchestration methods. We release the substrate, annotation layer, reference intervention suite, analysis pipeline, and 220 per-condition run archives.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-172](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
