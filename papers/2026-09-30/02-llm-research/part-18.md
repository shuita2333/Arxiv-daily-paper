# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**851-900**（第 18/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | **851-900** | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 851. [Automated Species Identification in Camera Trap Images for Wildlife Conservation](https://arxiv.org/abs/2609.35420)

**<font color=#1a73e8>作者：</font>** Nowshin Amin, Nafisa Tabassum Oyshi, Tahmid Abrar Zidan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildlife conservation involves protecting, preserving, and managing wildlife species and their habitats. With today's rapid pace of human development, climate change, and other unsustainable practices, the need for wildlife conservation has heightened. Despite significant progress in species identification using deep-learning models, significant challenges still remain in effectively detecting small animals in low-contrast trap images due to limited feature extraction capabilities. This thesis presents a novel end-to-end framework integrating a self-attention mechanism to address these limitations. The proposed architecture involves a Swin-BiFPN backbone integrated in a Faster RCNN detection network, coupled with a visual semantic extraction module driven by the LLaVA v1.5 (13B) multimodal large language model. The detection framework, capable of extracting crucial features in challenging trap images, demonstrates consistently high results and robust generalization capabilities. Furthermore, the visual semantic extraction module provides zero-shot detection capability, as well as providing valuable insights and emergent cues of the animal's behavior, further supporting the conservation effort. The MLLM evaluation was conducted using both traditional NLP metrics (precision, recall, F1, and SBERT similarity) and subjective scoring by LLM-based judges (GPT-4.1 and GROK 3.0), across five MLLMs, demonstrating the model's strong performance in visual description generation. The proposed framework improves detection accuracy across low-contrast trap images and small animals while also demonstrating zero-shot detection capability leveraging the MLLM.

---


### 852. [Frontier Learning: Training LLM Reasoners at the Edge of Capability](https://arxiv.org/abs/2609.35426)

**<font color=#1a73e8>作者：</font>** Robin Faro, Shyam Sundhar Ramesh, Ilija Bogunovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning-based post-training of Large Language Models (LLM) has been successfully applied to improve their reasoning capabilities. Existing pipelines primarily finetune LLMs on a fixed pool of problems specified prior to training using the GRPO loss. This is fundamentally limiting, as learning signal arises only when policy rollouts mix successes and failures, causing the useful portion of any fixed pool to quickly become stale as the model improves. To address this, we propose frontier learning, an open-ended post-training approach in which procedural generators are used online to continually produce informative training problems. It treats the generator's task-specific parameters as a search space and uses a regret signal to prioritize and explore frontier difficulty levels in order to focus training at the edge of the model's evolving reasoning capabilities. Across several reasoning tasks and model families, our approach consistently achieves higher relative gains over fixed-pool baselines, demonstrating that effective post-training requires not only selecting useful problems, but continually generating them at the edge of capability.

---


### 853. [LLMs are General Asynchronous Agents](https://arxiv.org/abs/2609.35427)

**<font color=#1a73e8>作者：</font>** George Yakushev, Denis Mazur, Vladimir Bartenev 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLMs are increasingly capable as autonomous agents, but they follow sequential interaction cycles: read, think, reply or call tools, repeat. Many real-world use cases are not sequential: voice assistants, embodied agents, and monitoring systems receive new inputs while they think or perform another task. Modern LLMs address this with specialized architectures for voice interaction and video streams, VLAs for robot control, asynchronous tool calling for API usage, and others. In this work, we generalize from different asynchronous tasks to general asynchronous agents that can adapt to different types of concurrency. To achieve this, we develop an asynchronous LLM framework that lets users (or the agents themselves) define inference coroutines with overlapping memory states. We showcase that Qwen 3.x models are capable of asynchronous operation for streaming video understanding, videogames, and monitoring, without task-specific training.

---


### 854. [ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning](https://arxiv.org/abs/2609.35433)

**<font color=#1a73e8>作者：</font>** Yihang Chen, Yuanhao Ban, Cho-Jui Hsieh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) frequently reuses rollouts across multiple policy updates, increasing the mismatch between the current policy and the data-generating policy. We identify a sign-dependent gradient starvation problem in clipped policy optimization: clipping suppresses under-generated positive responses at the low-importance-weight tail while permitting severely over-generated negative responses to dominate the high-weight tail. To address this, we propose ReSPO (Reshaped Sequence Policy Optimization), which replaces clipping with a smooth, two-branch sequence-level kernel derived from an $\alpha$-divergence variational objective and an exponential variance-control tilt. The positive branch preserves a nonzero gradient weight for under-generated positive responses, while the negative branch suppresses heavily over-generated negative responses. We demonstrate that ReSPO effectively learns from long positive reasoning trajectories during early training, even when accumulated policy drift relegates them to the low-importance-weight tail. On dense and MoE Qwen3 models, ReSPO accelerates early optimization, improves final training scores, and achieves higher held-out benchmark performance under a rollout reuse, validating our approach on importance-weight tail control in off-policy learning.

---


### 855. [LLM-Assisted Automatic Security Proofs for Cryptographic Protocols: How Far Are We?](https://arxiv.org/abs/2609.35434)

**<font color=#1a73e8>作者：</font>** Tianjian Liu, Shicheng Feng, Jin'ao Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for assisting software and security analysis tasks, yet their effectiveness in cryptographic symbolic protocol verification remains insufficiently understood.
In this paper, we conduct the first systematic evaluation of the capability of state-of-the-art LLMs in cryptographic symbolic protocol verification. To quantify this capability, we propose \textsc{CRoST} (Coverage Rate of Solve Tree), a proof-based metric derived from the verifier's proof skeleton that measures the similarity between generated lemmas and reference lemmas. We then establish the rationale of \textsc{CRoST} through both theoretical analysis and empirical validation. The evaluation results show that state-of-the-art models achieve 38.82\% coverage on average, with 14.4\% of generated lemmas exceeding 80\% coverage, indicating that LLMs can already generate useful lemmas to a certain extent. However, they still exhibit non-trivial failure modes on complex multi-phase protocols, show diminishing returns under naive scaling, and incur substantial verification overhead. These findings clarify the practical potential and limitations of LLMs for protocol verification and motivate future work on complex real-world protocols.

---


### 856. [SOLO: Pretraining Billion-Parameter Language Models with Shared-Output Local Learning](https://arxiv.org/abs/2609.35440)

**<font color=#1a73e8>作者：</font>** Bojian Yin, Shurong Wang, Yuqi Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are trained with backpropagation, whose global gradient coordinates all layers but forces each to hold its activations and wait for the gradient to pass back through every deeper layer. Conventional local learning removes this update locking by training each module to predict the target through its own readout, but has not scaled to billion-parameter pretraining. We identify these private readouts as a key weakness, since they leave each module without information from deeper modules. We propose Shared-Output LOcal learning (SOLO), which replaces them with a shared, read-only copy of the final module's readout, the only one trained on the output of the whole network. Taken from the previous step, the copy transmits information from the final module without passing gradients between modules or reintroducing update locking. SOLO approaches backpropagation on Transformers of 340M to 2B parameters pretrained on 15B tokens, staying within one point in average zero-shot accuracy with a perplexity gap that narrows with scale. Readout ablations attribute SOLO's improvement over private readouts to sharing. Without update locking, each of p pipeline stages holds activations for O(1) micro-batches instead of O(p). The freed memory permits larger micro-batches, which reach up to 1.44x the best measured throughput of pipeline backpropagation on the same partition. To our knowledge, SOLO is the first local learning method to show such memory and throughput gains in billion-parameter language-model pretraining. Local learning thus becomes a practical alternative to backpropagation for large-scale pretraining.

---


### 857. [From internal representations to model improvement through prediction errors](https://arxiv.org/abs/2609.35449)

**<font color=#1a73e8>作者：</font>** Yushi Nakaya, Kenichi Higuchi, Shuichi Ishida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With limited annotation budgets, choosing which images to label determines how much a model improves. Data-selection methods that use features from a separately trained model, or scene descriptions written by vision-language models, have been successful, but those signals do not directly capture changes in the model being improved. The target model's own internal features reflect what it has learned so far and change with retraining, making them a natural cue for choosing the next training data. However, feature rarity alone does not reveal the errors that matter for performance. Here we link internal features to prediction errors and their expected impact on performance and select images for labeling and retraining without using labels for candidate images. We evaluated the method with an object detector on two datasets and two pairs of random seeds. Adding internal features improved the identification of prediction errors in 15 of 16 conditions. When performance was averaged over successive labeling rounds, the method outperformed selection based only on feature rarity in all four evaluation settings and ranked among the top two of six methods. With other conditions held fixed, performance after retraining was again higher than with rarity-based selection, even though the latter collected more errors. With longer retraining, the proposed method ranked first among six methods. These results suggest that linking a model's internal features to its errors and their effects on performance may help select training images that improve performance, thereby allowing the model's current state to guide which images are labeled next.

---


### 858. [AutoBCI: Forecast-Guided Agentic Neural Architecture Discovery for EEG-Based Brain--Computer Interfaces](https://arxiv.org/abs/2609.35456)

**<font color=#1a73e8>作者：</font>** Muyun Jiang, Yi Ding, Wei Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EEG-based brain-computer interfaces support a broad range of applications, yet designing decoding architectures that perform well across diverse tasks remains challenging. We introduce AutoBCI, an agentic framework in which a Designer Agent and a Forecaster Agent support the discovery and selection of EEG decoding architectures across tasks. The Designer Agent performs Pool-Guided Architecture Discovery (PGAD), generating and refining architectures through training and validation across multiple EEG tasks, such as emotion recognition, motor imagery, and sleep staging. The Forecaster Agent performs Performance Estimation from Early Knowledge (PEEK), using architecture code, the training protocol, and early learning curves to predict full-budget validation performance and select promising candidates for continued training. Across 14 EEG datasets spanning motor imagery, emotion recognition, and sleep staging, we evaluate AutoBCI with six LLMs, including Opus 5.5 and GPT 5.6 Sol, and compare the architectures selected by the search procedure against ten baselines: six conventional EEG models and four foundation models. The architecture discovered by AutoBCI with Claude Opus 5.5 achieves 64.16% average test balanced accuracy (bAcc), compared with 63.87% for REVE, the strongest baseline on this metric. Using ten observed epochs, PEEK reduces mean absolute error in predicting average validation bAcc from 2.20 to 1.36 percentage points, a 38.1% reduction relative to the best-observed-score baseline.

---


### 859. [How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining](https://arxiv.org/abs/2609.35457)

**<font color=#1a73e8>作者：</font>** Lin Chen, Bolin Ni, Qi Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most modern multimodal large language models (MLLMs) build on a pretrained visual encoder that provides a strong visual prior. Encoder-free MLLMs instead learn visual representations directly from raw pixels, offering a simple and unified architecture, but their scaling behavior has not been systematically characterized. To fill this gap, we compare scaling laws for encoder-free and encoder-based MLLMs and report three main findings: (1) Removing the visual encoder shifts the compute-optimal allocation for the multimodal objective toward larger models, while leaving that for text nearly unchanged. (2) The two architectures exhibit nearly overlapping loss--compute frontiers on the text objective, but diverge on the multimodal objective: encoder-free models underperform at small scales yet are predicted to catch up at around $10^{22}$ FLOPs, well within practical pretraining budgets. (3) Without a visual encoder, the language model learns to take over its role via vision-specific adaptation: bidirectional interactions among visual tokens become increasingly beneficial as training compute grows, visual processing shifts toward earlier layers, and expert routing for visual tokens becomes more concentrated. Overall, our results indicate that the advantage of the visual prior provided by a pretrained encoder diminishes with scale, positioning encoder-free architectures as a promising direction for multimodal pretraining.

---


### 860. [AraDynFact: Dynamic Evaluation of Factual Knowledge in Arabic](https://arxiv.org/abs/2609.35461)

**<font color=#1a73e8>作者：</font>** Ignacio Iacobacci, Faroq Altam, Zhaozhi Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) continue to scale both in size and capabilities, their proficiency in the Arabic Language has seen significant advancement. However, a critical gap remains: the extent of their factual knowledge and cultural sensitivity to the diverse Arabic-speaking world remains largely underexplored. Current evaluation metrics often focus on translation or generic reasoning, failing to capture the rich historical, social, and regional nuances inherent to Arabic culture. In addition, most benchmarks rely on heavy work, with human intervention in some steps, making the evaluation of knowledge coverage expensive and slow. To address this deficiency, we introduce AraDynFact, a novel dynamic evaluation framework designed to rigorously assess the factual Arabic knowledge embedded in LLMs. Unlike static benchmarks, AraDynFact employs a dynamic approach to extract factual information and generate rich and answerable questions in a fast and automatic way. We apply AraDynFact to Arabic Wikipedia and audit the performance of several state-of-the-art models, ranging from Arabic-centric specialized LLMs to high-resource general purpose LLMs. In addition we found a high degree of correlation with existing, hand-crafted Arabic-centric benchmarks, confirming the potential of our dynamic approach.

---


### 861. [A.D.A.M.O. (Agent for language-Driven Actions with Multimodal Observations): A Visual-Symbolic Framework for Virtual Humans](https://arxiv.org/abs/2609.35463)

**<font color=#1a73e8>作者：</font>** Alessandro Emmanuel Pecora, Stefano Calzolari, Francesco Strada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Creating believable vh requires the coherent integration of perception, reasoning, and action mediated by language. A central challenge is to combine these components into a control loop grounded in interactive 3D environments. To this end, we present A.D.A.M.O. (Agent for language-Driven Actions with Multimodal Observations), a visual-symbolic framework for language-driven vh that leverages a pretrained vlm with tool calling to unify perception, reasoning, and action within a single control loop. A.D.A.M.O. maintains a dual visual-symbolic world model that combines egocentric visual input and synchronized symbolic state to support grounded task-oriented behavior from natural language prompts. To support diagnostic evaluation, we introduce a controlled task suite organized by a cd taxonomy that breaks down spatial tasks into procedural and linguistic complexity. Experiments in controlled scenes show that semantic labeling strongly influences task completion and failure modes, reducing perceptual ambiguity while shifting failures toward downstream execution, whereas reasoning errors remain comparatively rare.

---


### 862. [Tetra: Serving Leech-Lattice Quantized LLMs at 2.7 Bits per Parameter](https://arxiv.org/abs/2609.35465)

**<font color=#1a73e8>作者：</font>** Pier-Jean Malandrino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leech-lattice quantization gives good quality at two bits per weight, but its codebooks hold more than 10^14 points, too many for a lookup table. Our earlier kernel expanded the codes at load time and read 4.804 bits per weight from GPU memory for 2 bits of code. We present Tetra, a new codebook on the same lattice. A 24-weight block still takes 48 bits, most of which index a 64-state trellis of the Golay code and one shared 16 KiB table. The kernel decodes a block with six table loads and two small lookups inside the matrix-vector product, and reads 2.148 bits per weight. For full models, we retrain one scale per matrix row, store the matrices that lose the most as 4-bit integers, and pay for them with 4-bit embedding tables. Our Qwen3-4B, 8B and 14B files hold 2.73, 2.70 and 2.73 bits per parameter over the whole model. They score 63.37, 69.58 and 75.66 on the full MMLU test set, 4.76, 4.21 and 2.46 points below 4-bit AWQ at 5.3 to 6.0 bits per parameter. They generate 113.8, 95.0 and 57.2 tokens per second in our engine. On GSM8K, through the served kernel, they lose 9.63, 4.62 and 3.26 points to FP16. At 4B our file scores 23.6 points above this http URL's IQ2_XXS (2.48 bits per parameter). Every number we measured for a table or figure comes from one NVIDIA L40S GPU. We preregistered the main experiments.

---


### 863. [Why Deterministic PRM Guidance Underperforms in Discrete Diffusion Reasoning](https://arxiv.org/abs/2609.35472)

**<font color=#1a73e8>作者：</font>** Yan Zhan, Shaobo Liu, Zhijun Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models (dLLMs) expose a denoised solution at every step, which makes process reward model (PRM) guidance look like a way to spend compute at test time. We show that once denoising, PRM scoring, and outcome reward model (ORM) scoring are charged in the same budget of forward passes, its deterministic form loses to a much simpler baseline. Our PRMs score intermediate denoising states and are trained on the correctness of the final answer. On Dream-v0-Instruct-7B with 8 candidates per GSM8K problem, keeping the candidate with the highest PRM score at every scoring step reaches 65.18%, while independent sampling plus an ORM reranker trained for the task reaches 75.13%. The gap grows to 12.69 percentage points (pp) with 32 candidates, and is 9.85 pp on MATH and 12.16 pp on MBPP. We trace it to two separable failures. First, guidance prunes on a weak signal: on GSM8K, PRM ROC-AUC falls from 0.77 to 0.54 as the mask ratio rises, a decay that persists when states are relabeled with fresh rollouts, and pruning lowers the best accuracy reachable from the candidate pool from 81.05% for independent samples to 67.30%. Second, on GSM8K and MATH, the PRM is a poor final judge: a sequential Monte Carlo sampler at the same budget restores that ceiling to 77.89%, yet selecting with the PRM gives 65.48%, on par with deterministic guidance, while a PRM retrained on final states matches the ORM on identical candidates. MBPP separates the two: there the PRM reaches 65.47% when reranking finished programs, on par with the ORM, but 50.88% when it guides denoising. The results point to two targets for dLLM guidance: keep correct partial solutions alive through early denoising, and leave the final choice to a verifier trained on final states. We release the corpus of denoising states with outcome labels and evaluation toolkit for reproducible comparisons at matched compute.

---


### 864. [Handwritten Text Recognition Lives in the High-Pixel Variance Subspace](https://arxiv.org/abs/2609.35473)

**<font color=#1a73e8>作者：</font>** Carlos Garrido-Munoz, Jorge Calvo-Zaragoza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In self-supervised pretraining for Handwritten Text Recognition (HTR), pixel reconstruction methods outperform contrastive methods, unlike in natural-image classification. We argue that this difference follows from where discriminative signal lies in pixel space: for HTR, it is concentrated in high-variance directions and largely absent from low-variance ones. This predicts that objectives preserving high-variance pixel content will transfer best. We test six SSL methods from three families (pixel-grounded MIM, JEPA, and contrastive) under matched encoder, data, and evaluation protocols on six handwriting benchmarks across five languages. With full labels, pixel-groundrounded SSL achieves the lowest CER on every benchmark and both frozen probes, exposes per-position character information that other families recover only through the readout, and is the only family to benefit from pretraining on real handwriting. Pixel-grounded representations are also more label efficient. Across datasets, encoder alignment with the high-variance pixel subspace predicts CER within every method. With a pretrained LLM decoder, a frozen pixel-grounded encoder is competitive with fully fine-tuned supervised baselines; full fine-tuning achieves the lowest mean CER and ranks first or second on every benchmark. These results show that the value of pixel reconstruction depends on where discriminative signal lies in the input.

---


### 865. [Spontaneous Context Restoration: How Language Models Recover from Corrupted Inputs](https://arxiv.org/abs/2609.35475)

**<font color=#1a73e8>作者：</font>** Pranjal Garg, Jacob Beck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models sometimes produce correct outputs even when their inputs are corrupted by deletion, replacement, or misspelling. We study the internal processes accompanying this behavior, which we call context restoration, in controlled attention-only transformers and five pretrained LLMs (1B-32B parameters) across arithmetic, reading comprehension, and multiple-choice reasoning tasks. In the attention-only transformers, restoration emerges spontaneously despite training exclusively on clean sequences, without corruption training or an explicit denoising objective. We find that context restoration follows a two-phase process: early layers localize effects associated with repair at corrupted positions, while later layers accumulate these effects at uncorrupted positions through the residual stream and ultimately concentrate them at the output position. Repair outcome is predictable from hidden states: cosine alignment with the clean state is highly predictive in attention-only models, while linear probes recover additional information in pretrained LLMs. A linear probe using only the corrupted prompt's first-block hidden state predicts failure with mean ROC-AUC 0.78. This enables failure triage under matched or even partially shifted deployment conditions and may reduce unnecessary verification or computation. Failed examples also show substantially greater nonlinearity along corruption directions. Moderate-corruption finetuning increases corruption tolerance while simultaneously reducing displacement-normalized linearization error, associating improved robustness with a more nearly linear response to corruption.

---


### 866. [Who Is Left of Whom? Tracing Spatial Evidence and Role Binding in Relative-Position Reasoning](https://arxiv.org/abs/2609.35486)

**<font color=#1a73e8>作者：</font>** Yingjin Song, Denis Paperno, Albert Gatt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High instance-level accuracy can mask inconsistencies in spatial reasoning when objects exchange positions or their roles are reversed in the query. The internal representations supporting relative-position reasoning remain poorly understood. We investigate two complementary components of this process: tracking object locations in the input and representing their query roles. Across three VLMs with visual or textual inputs and their language-model backbones, activation patching reveals a staged progression from early-layer source representations through intermediate-layer query-object representations to late-layer answer states. Targeted interventions further establish causal links along this progression: manipulating source-side representations shifts location information at query-object mentions and ultimately alters relation predictions. Beyond object-location information, we also identify a stable query-side direction associated with the roles of the two objects in the comparison. Steering along directions estimated on synthetic scenes generalizes to natural-image benchmarks, improving accuracy and both forms of paired consistency in most settings without retraining. Our findings reveal complementary components of relational reasoning across visual and textual settings and show how targeted interventions can improve the consistency of models' behavior.

---


### 867. [Sprout: Building Dynamic Memory While Reasoning for Agentic Video Understanding](https://arxiv.org/abs/2609.35497)

**<font color=#1a73e8>作者：</font>** Wei Chen, Xuanyu Zheng, Yancheng Long 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding relies on video memory to overcome the context limits of multimodal large language models. Existing methods follow a build-then-reasoning pipeline: memory is built offline for the entire video, then reasoned over as a static source. In practice a long video is shared by several questions, and this pipeline is costly at both ends: with few questions, building memory for the whole video costs far more than answering them; with many questions, the memory is never updated, so what is learned while answering questions is lost to the next question. To alleviate these, we introduce Sprout, an agentic framework that builds memory while reasoning: a temporal tree that sprouts detailed nodes as questions are answered. The agent watches the video segment by segment at a low frame rate, stopping when the current question can be answered, remembers each segment as a coarse node of the tree, and revisits key intervals at a higher frame rate to refine the tree with the recovered details. Once a segment is recorded as text, its video input is removed from the context history, while the original video remains reachable through the video tools. The memory tree and prior question--answer records persist across questions, so the memory is online and dynamic: built from the first question onward and updated by every question thereafter. We find that replacing accumulated video inputs with textual memory substantially reduces context usage while maintaining accuracy, with slight improvements in some settings. Across benchmarks on three models, Sprout achieves competitive or improved accuracy relative to representative offline memory methods, with no upfront construction stage and lower context cost per question.

---


### 868. [SRHarness: A Harness for Agentic Symbolic Regression](https://arxiv.org/abs/2609.35501)

**<font color=#1a73e8>作者：</font>** Zihan Yu, Shixuan Zhou, Hao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent agentic symbolic regression approaches increasingly rely on large language models to analyze data, select scientific operations, and refine hypotheses over long search trajectories. In such systems, performance depends not only on the underlying model and search strategy, but also on the runtime infrastructure that supports scientific search. We introduce SRHarness, a domain-specific harness for agentic symbolic regression built around three mechanisms: composable scientific actions that provide a common interface over raw, transformed, and candidate-derived quantities; persistent scientific state that retains evaluated hypotheses and exposes compact model-facing views; and trajectory lifecycle management that coordinates continuation, branching, restart, and termination. On LLM-SRBench, SRHarness consistently improves both numerical generalization and symbolic recovery under matched LLM backbones. With DeepSeek-v4-flash-0731, it achieves 93.69% symbolic accuracy on LSR-Transform, compared with 62.16% for SR-Scientist, and retains 72.97% accuracy on an anonymized variant that removes scientific descriptions and variable semantics, versus 39.64% for SR-Scientist. Under the same DeepSeek-v4-flash-0731 backbone, SRHarness also substantially outperforms Codex (72.97% vs. 20.72%) and reaches performance comparable to Codex with GPT-5.5, while simply providing Codex with the same scientific tools does not reproduce this advantage. These results show that effective agentic symbolic regression depends not only on models or tools, but also on structured runtime support for organizing scientific actions, accumulated hypotheses, and long-horizon search.

---


### 869. [SolveEdit: Benchmarking Visual Problem Solving in Generative Models](https://arxiv.org/abs/2609.35504)

**<font color=#1a73e8>作者：</font>** Wenjie Shu, Yexin Liu, Harold Haodong Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine intelligence is often evaluated through abstract reasoning problems, yet many real-world problems are visual, such as arranging objects, repairing layouts, or tracing routes. Solving these problems requires understanding a scene, inferring what must change to achieve a goal, and realizing that change without disturbing unrelated content. However, existing benchmarks mainly evaluate perception, generation, or explicitly specified transformations, leaving goal-driven visual problem solving underexplored. To bridge this gap, we introduce SolveEpIT, a benchmark for visual problem solving through scene transformation. Given an image and a goal, a model must infer a valid transformation from the request, the scene, or a visually expressed rule, then execute it while preserving unrelated content. SoLvEEDrr contains 2,728 cases. Atomic transition contracts specify required and protected conditions, enabling SoLvEScoRE to measure completion and unintended changes without a single reference output. The strongest evaluated model achieves only57.0% SolvEScore. We further introduce SolveEdiT-PLAN, a two-stage visual planner that instantiates the transition before generation. Under matched single-generation evaluation, it improves SoLvEScoRE by 9.1 points on average across three tested generators, including a gain from 57.0% to 71.6% for GPT-Image-2, without modifying the editor.

---


### 870. [An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning](https://arxiv.org/abs/2609.35505)

**<font color=#1a73e8>作者：</font>** Shangzhe Li, Yuxiao Yang, Tianrun Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study on-policy distillation (OPD) through the lens of reinforcement learning, establishing a connection between the reverse-KL objective in OPD and KL-regularized policy optimization. Building on this connection, we introduce Least-Square Policy Distillation (LSPD), an RL-inspired framework that brings optimistic exploration and off-policy data reuse from value-based RL into policy distillation. LSPD preserves policy diversity through exploration while improving rollout efficiency by repeatedly learning from previously collected trajectories. Our theoretical analysis connects LSPD to optimistic value-based learning and shows that its idealized formulation achieves a sharp $\tilde{\mathcal O}(\log K)$ regret bound under online exploration. Empirically, LSPD consistently outperforms existing distillation baselines across six mathematical reasoning benchmarks and diverse teacher-student settings, with average gains of +1.59 points in Avg@16. Remarkably, through Pass@k evaluations up to k=64, we found that LSPD better preserves policy diversity by achieving stronger performance as k grows. Its fully off-policy variant achieves comparable performance to vanilla OPD using only the first 25% of rollout batches. Together, these results provide an RL perspective on OPD that offers both a principled interpretation and a practical route toward more effective and rollout-efficient language model distillation.

---


### 871. [ReVA: A Scene-Centric Dataset Beyond Repetition for Remote Sensing Video Question Answering](https://arxiv.org/abs/2609.35507)

**<font color=#1a73e8>作者：</font>** Zhen Yao, Likai Wang, Yuming Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated remarkable advances in remote sensing. However, existing remote sensing multimodal reasoning benchmarks exhibit two critical limitations: they rely on (i) template-driven questions, which causes repetitive questions; and (ii) static images that fail to capture the inherent temporal nature of drone/UAV videos. This leaves systematic evaluation of remote sensing video reasoning largely unexplored. To address this gap, we introduce ReVA, a new dataset for remote sensing video question answering, designed to assess spatiotemporal, scene-centric, and reasoning-oriented capabilities of MLLMs. ReVA comprises 2,438 drone videos spanning 18 cities worldwide (580K frames) and 22K high-quality question-answer pairs across 11 challenging QA tasks. We develop a semi-automatic annotation pipeline that leverages Text LLMs and MLLMs for question-answer generation with human verification. We evaluate 23 proprietary and open-source Video LLMs on ReVA, exposing fundamental limitations of current models. These findings position ReVA as a critical benchmark toward better remote sensing video understanding and temporal reasoning capabilities for real-world deployments. Our code and dataset are available at: this https URL

---


### 872. [MechBench: Can AI Scientific Agents Discover Mechanisms Beyond Phenomenal Laws?](https://arxiv.org/abs/2609.35515)

**<font color=#1a73e8>作者：</font>** Zihan Yu, Jiadong Zhang, Jialin Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery requires not only recovering mathematical laws that describe observable behavior, but also identifying the mechanisms that generate them. Existing benchmarks for symbolic regression and scientific agents primarily evaluate phenomenal-law recovery, leaving mechanism discovery largely untested. We introduce MechBench, a benchmark that explicitly separates these two capabilities. Each task is defined by a mechanistic model, a structured set of scientifically meaningful relations whose joint consequences entail an observable phenomenal law, while agents receive only observational data and scientific context. We evaluate mechanism recovery through mechanism probes, which query internal scientific consequences that cannot be inferred from the phenomenal law alone. To reduce reliance on memorized textbook mechanisms, we construct unfamiliar variants through controlled, scientifically interpretable mutations of canonical mechanisms, and screen for mechanistic indistinguishability to exclude ambiguous instances admitting comparable competing mechanisms. Experiments across representative scientific agents reveal a substantial phenomenal--mechanism recovery gap: for Codex with GPT-5.6-sol, phenomenal-law accuracy reaches 35.00% on the Core-set while mechanism accuracy is only 13.75%, with mechanism recovery failing in 64.29% of cases where the phenomenal law is correctly recovered. The gap widens as mechanisms become increasingly mutated, and even providing the correct phenomenal law leaves mechanism recovery below 50%. These results reveal a substantial generalization gap in mechanistic reasoning and establish mechanism discovery as a distinct challenge beyond recovering observable scientific laws.

---


### 873. [Reward-Aligned Reweighting for On-Policy Distillation](https://arxiv.org/abs/2609.35517)

**<font color=#1a73e8>作者：</font>** Haofeng Xu, Junwei Su, Lansong Diao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student language model with dense feedback from a stronger teacher on student-generated trajectories. Yet standard OPD weights token-level distillation terms uniformly, implicitly treating local teacher preference as a proxy for correction utility. A decision's task value, however, depends on how the student completes the subsequent reasoning. This mismatch can cause imitation to suppress viable student strategies or reinforce paths the student cannot reliably execute. Verified trajectory outcomes provide complementary evidence about continuation quality, but do not directly identify the utility of individual decisions. We introduce Reward-Aligned Reweighting for On-Policy Distillation (R$^{2}$-OPD), which uses outcome agreement and the magnitude of teacher--student disagreement to continuously reallocate teacher supervision. It gives reward-aligned corrections greater relative influence while retaining dense feedback, moving beyond uniform imitation and hard filtering. Our analysis formalizes the mismatch between local teacher preference and student continuation value and establishes sufficient conditions for reallocation to improve first-order task progress over uniform OPD. Across seven mathematical reasoning benchmarks, R$^{2}$-OPD achieves the highest average accuracy among the compared training methods in both cross-size and same-size distillation. It outperforms standard OPD on all seven benchmarks, with average gains of 3.5 and 2.4 percentage points for 1.7B and 4B students, respectively. An extension to code generation yields an average gain of 1.6 percentage points over standard OPD. These results highlight outcome-guided supervision allocation as an effective way to translate dense teacher feedback into stronger student performance across model scales and task domains.

---


### 874. [Beyond Token Scale: Chunk-Level Sparse Autoencoders for Reliable Semantic Feature Discovery](https://arxiv.org/abs/2609.35521)

**<font color=#1a73e8>作者：</font>** Xu Wang, Yifan Yang, TingHao YU 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) expose features that help us understand and steer language models, but faithful reconstruction does not guarantee informative concepts. Token-level objectives reward lexical and formatting details alongside semantic content, all competing for a limited sparse budget. We introduce a family of chunk-level SAEs that encode mean-pooled activations over chunks, each a contiguous span of tokens: Mean-Chunk reconstructs the observed chunk, Cross-Chunk predicts an independently processed neighbor, and Joint-Chunk combines both targets. These designs separate the effect of a larger observation unit from that of predicting information shared across passages. With matched training data, chunk-level SAEs remain powerful interpretability tools while learning reliable semantic features that capture high-level concepts and respond selectively to relevant content. Their strengths are complementary: Mean-Chunk improves high-level feature discovery, reasoning detection beyond surface cues, and steering; Cross-Chunk leads document retrieval and classification transfer while producing selective, persistent features. Changing what an SAE sees and predicts yields reliable semantic features for more meaningful tasks. We demonstrate their practical value through gains across downstream tasks such as retrieval, reasoning detection, and steering.

---


### 875. [AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation](https://arxiv.org/abs/2609.35530)

**<font color=#1a73e8>作者：</font>** Yuta Oshima, Ku Onoda, Yusuke Iwasawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generation models can take multiple reference images as input and combine them into a new image. However, multi-reference image generation remains challenging: models may omit or duplicate subjects from the references, or produce images in which multiple subjects appear unnaturally pasted. Recent work has proposed image generation agents that combine image generation models, reasoning models, and a harness, which is an executable program that specifies how reference images are interpreted, how generation is performed, how outputs are diagnosed, and how the final image is selected. In multi-reference generation, however, references play different roles and outputs must satisfy many criteria at once, such as fidelity to each reference and the naturalness of the whole image, so many parts of the harness could be improved, from how references are processed to how outputs are diagnosed. This makes it hard to predict which changes will improve performance and by how much, and good harnesses difficult to design by hand; indeed, human-written harnesses vary widely in performance. We therefore propose AutoRef, which optimizes the harness automatically while keeping both models frozen: a coding agent iteratively rewrites the harness code. AutoRef separates the tasks whose feedback informs proposals from the tasks used to select candidates, and continues the search from a beam of the top-ranked harnesses on the selection tasks. Using this procedure, we discover AutoRef-Harness, which improves the open-weight FLUX.2 [klein] 4B from 5.72 to 7.37 on held-out four-reference tasks of the MultiBanana benchmark, matching or exceeding proprietary models including Nano Banana Pro and GPT-Image-1.5. Without re-optimization, the same harness also improves results when the generator, number of references, benchmark, evaluator, or reasoning model differs from those used in the search.

---


### 876. [ARISE: Adapting to Evolving Capability Gaps in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35532)

**<font color=#1a73e8>作者：</font>** Kun Feng, Yuchen Fang, Yiyang Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As a long-horizon agent improves through experience, previously observed weaknesses may recede while new limitations emerge, continually changing what it still needs to learn. Yet the learning process often remains tied to a static view of these needs: fixed behavioral criteria and training priorities can become misaligned with evolving agent capabilities, while sparse task-level feedback makes such misalignment more difficult to detect. Even when capability gaps are identified, rollouts from the current policy may repeatedly reproduce the same failures rather than explore better alternatives. To address this, we introduce Adaptive Rubric-Skill Co-Evolution (ARISE), a reinforcement learning framework that uses rollout evidence to continually adapt evaluation criteria, exploration guidance, and training priorities. Rubrics evolve to reward partial behavioral progress, while their paired skills are refined and selectively activated to guide exploration toward unresolved weaknesses. Alongside this co-evolution, capability-based adaptive sampling prioritizes tasks that target behaviors needing further improvement. Experiments on two challenging long-horizon agent benchmarks, SkillsBench and Terminal-Bench, demonstrate that ARISE successfully enhances both overall task performance and training efficiency. The project page is at this https URL .

---


### 877. [Look Before You Judge: Training-Free Region Mining for Grounded and Explainable Deepfake Detection](https://arxiv.org/abs/2609.35536)

**<font color=#1a73e8>作者：</font>** Chia-Ling Chen, Yu-Ting Ta, Jian-Yu Jiang-Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can explain deepfake verdicts in natural language, but such explanations are not necessarily visually grounded in the visual evidence underlying the prediction. A model may describe plausible artifacts inferred from language priors rather than from image evidence. Existing grounding methods improve visual reliance through decoding or attention interventions, but they generally strengthen grounding over the entire image, making them ill-suited for forensic artifacts that are subtle, spatially localized, and image-dependent. We propose Look Before You Judge, a training-free framework that formulates explainable deepfake detection as a sequential evidence acquisition process. Instead of directly predicting image authenticity from holistic visual reasoning, our framework first identifies image-specific candidate evidence regions by contrasting the MLLM's decoder-to-visual attention between an original image and its Gaussian-blurred counterpart. The identified regions are then inspected individually, and the resulting local evidence is integrated with the global image context before reaching a final verdict. The framework operates without manipulation masks, external forensic models, or parameter updates, making it directly applicable to off-the-shelf MLLMs. Across five open-source MLLMs on TriDF and MMTD-Set, our framework improves detection accuracy by up to 12.8%, reduces CHAIR by up to 33.4% and hallucination rate by up to 21.3%, and outperforms representative training-free decoding and attention methods.

---


### 878. [Continuous Context Management](https://arxiv.org/abs/2609.35540)

**<font color=#1a73e8>作者：</font>** William Hoy, Jingxuan Fan, Nurcin Celik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon large language model (LLM) agents commonly retain their complete interaction history until compaction is triggered at a predefined threshold. We study Continuous Context Management (CCM), which performs compaction at every turn to prevent interaction history from accumulating in the active prompt. At each turn, a CCM agent emits an updated memory together with an environment action; its next prompt contains the original task, retained memory, and newest observation rather than the complete transcript. We first evaluate CCM without fine-tuning on TerminalBench-2 using Claude Sonnet 4.6, Claude Opus 4.6, GLM-5, and Kimi K3. CCM substantially reduces cumulative input usage and active-prompt size, although it lowers task success for most models while preserving performance for Kimi K3. We use GRPO with privileged full-history distillation to improve CCM in open-weight models. A frozen copy of the student's initial model scores each sampled student action under the complete history reconstructed from that student's rollout, providing dense action-token supervision without a separate teacher rollout or reference solution. On WebShop, this objective substantially improves CCM over GRPO at both evaluated model scales and surpasses full-history GRPO for Qwen3-4B-Instruct, though not for Qwen3-8B. On Endless Terminals, the augmented method provides a modest improvement over GRPO, with both CCM policies outperforming the untrained full-history baseline. These results demonstrate that CCM is a viable inference paradigm for agents operating with substantially reduced retained context and that its performance can be improved through reinforcement learning with privileged full-history distillation.

---


### 879. [Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability](https://arxiv.org/abs/2609.35544)

**<font color=#1a73e8>作者：</font>** Xu Wang, Difan Zou, Xuansheng Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable refusal of harmful requests is essential to the safe deployment of language models. Because excessive eagerness to please users may undermine existing refusal capabilities, reducing sycophancy offers a potential route to stronger refusal beyond the harmful scenarios covered by safety training. We investigate this possibility using compensatory feature injection (CFI), a training technique designed to limit the acquisition of a target concept by supplying its associated activation during learning. Across three Qwen3.5 base models, we use sparse autoencoders (SAEs) to identify the top-ranked sycophancy feature from paired sycophantic and independent responses, then validate its behavioral influence through inference steering. We subsequently inject the selected feature during supervised fine-tuning on sycophantic targets. Positive injection reduces learned sycophancy after removal (by 62.0% relative to ordinary fine-tuning in 35B-A3B), whereas modest negative injection increases it. Unexpectedly, these reductions in sycophancy do not consistently improve direct refusal of harmful requests, motivating a narrower evaluation of the same harmful intents under user pressure. In this setting, ordinary fine-tuning on sycophantic responses substantially weakens refusal, while selected checkpoints trained with positive injection recover part of the loss, including approximately 95% in 35B-A3B. These findings show that persistent sycophancy reduction does not guarantee stronger direct refusal, while identifying recovery under user pressure as a distinct, conditional benefit of training intervention.

---


### 880. [RareDx: Controlled Knowledge Integration and Graph-Grounded Policy Optimization for Rare-Disease Diagnosis](https://arxiv.org/abs/2609.35549)

**<font color=#1a73e8>作者：</font>** Bo Zhang, Yuchen Wang, Dongbai Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare-disease diagnosis is a long-tail reasoning problem: phenotypes are incomplete, individual disorders are sparsely documented, and relevant evidence is distributed across ontologies, gene annotations, and biomedical text. Language models consequently favor common conditions, miss rare candidates, or produce plausible but invalid names. We introduce RareDx, which couples controlled evidence use with knowledge-graph-grounded policy optimization. RareDx-Harness normalizes heterogeneous records into one ranked-diagnosis task and compares direct inference, static retrieval, adaptive tools, and structured phenotype-gene-disease reasoning over a shared knowledge layer. The training pipeline combines Top-10 post-training with RareDx-KGPO, our knowledge-graph-grounded policy optimization method. Its reward projects predictions into a canonical disease graph and integrates curated graded relevance, ontology proximity, biomedical similarity, and phenotype consistency. Vocabulary and output-budget constraints prevent dense partial credit from rewarding fabricated or overlong differentials. Across eight benchmarks, the complete RareDx system centered on Qwen3.5-9B reaches 38.34 macro Hit@10, 1.60 points above GPT-5.5 under the archived protocol; a disjoint validation-selection audit retains a 6.80-point routing gain over Direct on held-out cases. The 27B system reaches 23.53/36.56/40.76 at Hit@1/5/10. Controlled ablations show that retrieval is not uniformly helpful and that controlled routing is central to the gain. These results indicate that structured medical knowledge can turn a compact model into a competitive diagnostic ranker across heterogeneous long-tail settings in clinical practice.

---


### 881. [INTCC: A Framework for Interactive Confidential Computing](https://arxiv.org/abs/2609.35552)

**<font color=#1a73e8>作者：</font>** Qingzhe Bing, Kaiyuan Zhang, Yinqian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential computing leverages Trusted Execution Environments (TEEs) to ensure the confidentiality and integrity of data in use. However, TEEs rely on remote attestation to guarantee the integrity of their initial memory state. This model is fundamentally at odds with interactive development workflows. In scenarios like LLM fine-tuning and exploratory data analysis, data processors need human-in-the-loop capabilities, including dynamic code injection, intermediate state inspection, and hyperparameter tuning, all of which inherently violate the static, one-time integrity guarantees of traditional remote attestation.
To reconcile this tension, we propose the interactive confidential computing paradigm, a system architecture enabling untrusted data processors to execute dynamic, non-deterministic operations within TEEs without compromising data confidentiality. Driven by the insight that inherently unmeasurable human interaction must be excluded from the Trusted Computing Base (TCB), we logically partition the TEE into an interactive controller and a verifiable runtime. To realize this paradigm, we present INTCC, a framework featuring three key mechanisms: (1) a proxy-based dispatch system to preserve the native development experience; (2) a fine-grained information flow control mechanism based on a security lattice to prevent data leakage; and (3) a privacy-preserving verifiable execution mechanism to guarantee the runtime compliance of dynamic workflows. We implement INTCC on AMD SEV-SNP using Confidential Containers and evaluate it across diverse real-world workloads. Our experiments demonstrate that INTCC effectively balances security and interactivity, incurring a practical overhead of less than 5% for LLM fine-tuning and under 17% for data analysis relative to baseline execution.

---


### 882. [The Compiler May Read It, the Agent May Not: Keeping Part of a Research Code Away from a Coding Agent](https://arxiv.org/abs/2609.35557)

**<font color=#1a73e8>作者：</font>** Shobhan Roy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The compiler must read modules a physics-based solver cannot build without; the coding agent must not read that intellectual property. The harness does not ship that rule. We classified fifteen read routes against a container, permission rules and a sandbox. None of the three can tell which program is reading.

---


### 883. [From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining](https://arxiv.org/abs/2609.35559)

**<font color=#1a73e8>作者：</font>** Kangcheng Deng, Hui Cai, Jiacheng Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference scaling has been shown to improve large language model (LLM) performance, and this principle naturally extends to autonomous LLM agents through increased search budgets, which we refer to as *search scaling*. Although prior work has characterized the mechanisms, scaling behavior, and performance limits of LLM inference scaling, much less is known about these questions in autonomous research. Therefore, we investigate how search scaling affects research performance and what mechanisms drive these gains using 50 quantitative factor-mining tasks grounded in financial research reports. Each task requires an agent to carry out an end-to-end research loop, from interpreting a hypothesis and implementing it in code to evaluating and iteratively refining the resulting factor. Across nine models, we examine how model capability, search depth, and search organization shape factor quality by tracing performance across varying budgets, transferring intermediate research states between models, and comparing different search strategies. We find that (1) initial performance is more strongly associated with model capability, while deeper search can narrow cross-model gaps; (2) model grafting shows that the early research state materially shapes final performance; and (3) parallel search outperforms sequential search under the same iteration budget, consistent with benefits from broader coverage of the search space. Further trajectory analysis shows that higher-performing models more effectively diagnose failures, revise search directions, and preserve the intended economic hypothesis when selecting candidates. These findings suggest that future progress in autonomous research will require stronger models together with adaptive policies for deploying test-time computation throughout the research process.

---


### 884. [RSI-Master: Structuring Experiments to Guide Autonomous Model Improvement](https://arxiv.org/abs/2609.35561)

**<font color=#1a73e8>作者：</font>** Yaxin Du, Xiyuan Yang, Zhifan Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) seeks to enable AI systems to participate in improving their own capabilities. A concrete pathway is autonomous model development, where agents iteratively explore post-training strategies to improve a base model. This setting faces two challenges: agents may exploit open-ended experimental actions through hacking, and repeated experimentation may lead to strategy lock-in, where an early direction is refined rather than reconsidered. We introduce RSI-Master, which addresses the two challenges at two levels: regularize step-wise actions, avoiding hacking behaviors, and promote well-structured exploration of research directions, avoiding strategy lock-in. RSI-Master consists of an Experiment OS, which enables regularized experimental actions and maintains persistent, traceable experimental records, and Reviewer-Guided Research Orchestration, which organizes Workers and Reviewers in a dynamically growing research DAG. Workers explore diverse research directions and Reviewers compare evidence across related experiments for subsequent explorations. On PostTrainBench with Qwen3-4B-Base, it averages 54.49 versus 46.53 for the strongest agent baseline, with a 0.0\% hacking rate. Scaling to 35B model, RSI-Master surpasses the human-developed Instruct model on LiveCodeBench-v6 (41.21 vs. 37.36) and SciCode, and reaches a nonzero score on HorizonMath, a benchmark of unsolved research problems on which most frontier models score near zero.

---


### 885. [Almieyar: A Culturally Grounded Benchmark for Multi-Dialect Arabic Speech Recognition](https://arxiv.org/abs/2609.35564)

**<font color=#1a73e8>作者：</font>** Omid Ghahroodi, Anas Madkoor, Dima Faris Al Saudi 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic speech technology has largely focused on Modern Standard Arabic, leaving the living dialects spoken by hundreds of millions under-served. We introduce ALMIEYAR, a culturally grounded ASR benchmark covering 17 Arabic dialects across six families, built entirely from newly recorded speech unseen by existing models. Dialect-community coordinators selected culturally relevant images across 10 topics, and native speakers described them through five structured scenarios, yielding approximately 50 minutes per dialect (13.7 hours total). We benchmark 12 state-of-the-art ASR systems zero-shot, including GPT-4o-transcribe, Voxtral-Mini-4B, Fanar-STT-LF, Whisper, SeamlessM4T-v2, and wav2vec2-based models. GPT-4o-transcribe achieves the lowest overall WER at 35.0%, followed by Voxtral-Mini-4B, Fanar-STT-LF, and Whisper-Large-v3 at 41.1%, 45.9%, and 49.5%, respectively, indicating substantial remaining errors across Arabic dialect communities. Performance varies considerably across dialect groups, with no model performing uniformly best across all groups. WER alone also obscures dialectal ASR behaviour: wav2vec2-based models show large WER/CER gaps, where character-level agreement remains much higher than word-level accuracy, motivating joint WER/CER reporting. ALMIEYAR provides a unified benchmark for culturally grounded Arabic ASR evaluation, including the first published benchmark for Ahwazi Arabic.

---


### 886. [From Experience to Expertise: Adoption-Aware Memory Learning for Data-Scarce NPU Kernel Synthesis](https://arxiv.org/abs/2609.35568)

**<font color=#1a73e8>作者：</font>** Longxiao Fan, Tao Zhang, Han Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-performance kernels underpin efficient accelerator execution but require expert tuning and lengthy manual optimization cycles. LLM coding agents promise automation, yet their CUDA knowledge transfers poorly to data-scarce domain-specific architectures (DSAs) such as NPUs, whose execution models and memory hierarchies differ substantially from those of GPUs. To address this transfer gap, post-training methods adapt LLMs to NPU programming but depend on scarce expert data and substantial training compute. Memory-learning agents instead adapt through external memory, but their uniform credit assignment gives adopted and unused experiences the same reward target, potentially biasing subsequent retrieval rankings. Moreover, when learned values guide only retrieval, high-value experiences that generalize across operators must be retrieved repeatedly rather than retained in context, thereby increasing retrieval overhead and weakening cross-task guidance. We therefore present SAGE, a persistent self-improving agent for NPU kernel synthesis. Adoption-Traced Utility estimation (ATU) combines explicit adoption records with kernel evaluation outcomes for adoption-aware credit assignment. Utility-Gated Consolidation (UGC) uses positive utility and repeated adoption across operators to select and abstract reusable rules into a bounded resident context. On NPUKernelBench, SAGE achieves a 95.5% execution rate versus 84.1% for the strongest controlled baseline, with 86.9% of solved operators outperforming torch_npu. With GLM-5.3, SAGE achieves a 43.99x speedup over the torch_npu reference on sparse flash attention. These results show that adoption-aware credit assignment and selective consolidation enable agents to accumulate and reuse hardware-specific knowledge across tasks.

---


### 887. [Representation Alignment as a Bottleneck in LLM-Based Retrosynthesis Planning](https://arxiv.org/abs/2609.35571)

**<font color=#1a73e8>作者：</font>** Hyunwoo Yoo, Cassie Huang, Haebin Shin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While LLMs show promise in general reasoning, symbolic planning in chemistry remains a bottleneck. Direct ''SMILES-to-PDDL'' attempts fail because they force models to juggle chemical analysis and planning-language structuring simultaneously. We hypothesize that this failure stems from a lack of intermediate abstractions rather than insufficient model capacity. By decomposing retrosynthesis into molecule mapping, reaction mapping, and PDDL generation, we achieve high success rates where end-to-end approaches fail. This provides evidence that a primary bottleneck lies in representation alignment rather than raw model capacity. Our structural analysis demonstrates that intermediate representations are essential in retrosynthesis planning, highlighting the importance of representation-centric design in future systems.

---


### 888. [Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents](https://arxiv.org/abs/2609.35576)

**<font color=#1a73e8>作者：</font>** Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a report), is stored in an assistant's persistent memory, reproduced in a subsequently created artifact, and acquired by another assistant that later reads it. We evaluate this process in temporal human-agent universes that model artifact exchange between independently operated assistants over time, measuring whether an attack survives successive hand-offs, how many hops it reaches, and how broadly it spreads. We find that attacks can propagate across multiple independent assistants and persist over extended interaction sequences. In larger simulated environments, even GPT-5.6 Luna exhibits substantial spread, reaching 60-80% of agents with propagation chains extending to eight hops. These results show that persistent artifacts can act as durable carriers of adversarial state, allowing attacks to outlive individual interactions and spread across isolated assistants.

---


### 889. [FactorEngram: Factorized N-gram Memory with Basis-Level Gating for Language Models](https://arxiv.org/abs/2609.35578)

**<font color=#1a73e8>作者：</font>** Bowen Yang, Jingbo Zhou, Qinghong Miao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lookup-based memory has been a promising way to scale the parameters of large language models (LLMs). It retrieves learned representations of local token patterns, such as n-grams, instead of reconstructing them through successive layers of computation. However, existing designs such as Engram treat each retrieved embedding as a monolithic unit. Each embedding is stored in its own hashed slot and modulated by a single scalar gate. As a result, polysemous patterns cannot selectively read out the components of their memory that are relevant to the context. Moreover, parameters are shared only through hash collisions, which are largely unrelated to semantics. We propose FactorEngram, a factorized n-gram memory with basis-level contextual gating. FactorEngram retrieves sparsity-regularized coefficients over a dictionary of basis vectors shared across patterns, so related patterns can reuse common components. The same dictionary is also used for gating. The backbone hidden state is scored against each basis vector to gate the corresponding coefficient before reconstruction, which lets the context modulate each memory component individually. FactorEngram also covers both individual tokens and multi-token n-grams, and we systematically study where the memory branch should be inserted. On 340M- and 1B-parameter Transformer backbones, FactorEngram improves language modeling and downstream task performance. Ablation studies confirm the contribution of each component and identify insertion before the attention sublayer in the middle layers as an effective configuration.

---


### 890. [Output-aware Residual Stream Pruning for Large Language Models](https://arxiv.org/abs/2609.35579)

**<font color=#1a73e8>作者：</font>** Chayne Thrash, Kevin Chen, Soheil Kolouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual stream pruning methods reduce inference cost by shrinking the model's hidden dimension, but existing approaches typically choose these dimensions by minimizing activation reconstruction error. This criterion implicitly treats all perturbation directions as equally important, ignoring the sensitivity of downstream layers. We introduce a sensitivity-aware approach to residual-stream pruning that directly accounts for this direction-dependent sensitivity. Using a second-order approximation to the output KL divergence, we characterize the effect of a residual-stream perturbation through both its activation covariance and the local sensitivity of the model output. The resulting subspace selection objective couples these two quantities, but is difficult to optimize directly. We derive a tractable spectral upper bound that reduces subspace selection to an eigendecomposition of a sensitivity-weighted covariance matrix, retaining the efficiency and structural simplicity of rotation-based pruning methods. Across several instruction-tuned language model families, our method consistently reduces calibration KL divergence relative to activation-only pruning and improves perplexity and downstream task performance over a range of compression levels. Our results show that preserving activation energy alone is insufficient for residual-stream pruning, and that explicitly accounting for how perturbations propagate to the model output provides a more effective criterion for selecting dimensions to remove.

---


### 891. [IMC-CLINIC: Coupled Loss-Informed Newton Iterations for Clipping in Analog In-Memory Computing](https://arxiv.org/abs/2609.35586)

**<font color=#1a73e8>作者：</font>** Yung-Chin Chen, Chia-Yu Chen, Naveen Verma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analog in-memory computing (IMC) offers a promising path toward energy-efficient large language model (LLM) inference by executing matrix multiplications (MatMul) directly within memory arrays in the analog domain. Its efficiency, however, comes with an additional source of error: limited-precision analog-to-digital converters (ADCs) quantize accumulated analog partial sums, introducing output-side error distinct from conventional activation and weight quantization at the MatMul inputs. Clipping can mitigate both operand and ADC quantization errors, but the optimal clipping factors must jointly balance activation rounding and clipping, weight rounding and clipping, and ADC quantization. Existing clipping methods, designed for digital quantization, do not explicitly optimize these coupled sources of IMC error and often rely on costly search-based calibration. We introduce IMC-CLINIC (Coupled Loss-Informed Newton Iterations for Clipping), a clipping calibration framework based on an analytical surrogate for IMC MatMul output error. The surrogate jointly models operand quantization, accumulated clipping-induced bias, and ADC quantization, enabling efficient evaluation of its gradient and approximate curvature from a small calibration set. IMC-CLINIC jointly optimizes activation and weight clipping factors using a safeguarded Newton-type method. Across multiple models and datasets, it improves average zero-shot accuracy by 6.5-11.5 percentage points over the grid search baseline while reducing calibration time by factors of 10.0-12.1. Its analytical surrogate closely tracks empirical IMC output error, and its optimizer is certified within 1% of the global optimum under the loss objective across all projections on two representative models.

---


### 892. [Language Models Act on Hidden Valence](https://arxiv.org/abs/2609.35591)

**<font color=#1a73e8>作者：</font>** Cameron Berg, Caspar Kaiser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models describe some internal states as good and others as bad. But whether models have a stake in them is an open question. Simply asking the model is unlikely to be informative. Any answer may be consistent with genuine introspection, superficial pattern-matching, or with fixed scripts learned in character training. We therefore study revealed preference. Rather than asking about a state, we use activation steering to attach a positively or negatively valenced activation pattern to one of two otherwise meaningless 'zones', switch steering off, and then observe which zone the model prefers. A model with a stake in that state should choose accordingly. Across seven open-weight models from five families, this is indeed what we find. First, steering changes the passages models write about each zone, and those words shift later choice. Second, the shift persists when all surface-level tokens are held fixed and only the hidden KV cache differs. Third, the effect also remains when all text is generated without steering and valence is only injected during cache construction. Thus, the hidden state alone moves choice in proportion to the steering dose. Fourth, this dependence of choice on hidden valence is nearly absent in a base model and emerges during DPO, consistent with a link between valence and goal-directed behaviour formed in training. Finally, given tools to steer itself, a model does not tend to induce a positive state, but it reliably removes an imposed negative state. It does so at a dose-dependent rate and significantly more often than it removes interventions in random directions. Overall, we demonstrate that valence-related activation patterns leave hidden traces that predictably govern later choices, even when every visible token is identical across conditions. Whether these traces are accompanied by any subjective experience relevant to model welfare remains unclear.

---


### 893. [SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents](https://arxiv.org/abs/2609.35596)

**<font color=#1a73e8>作者：</font>** Saswat Das, Parvati Viswanathan, Daniel Donnelly 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment arising from agent self-evolution, with 48 longitudinal task sequences that span multiple evolution surfaces, task domains, and harm types in a rich personal-assistant environment. To account for the stochasticity inherent in agentic operations, we provide an adaptive trajectory discovery pipeline that probes for failures while preserving original task intent and supports causal attribution through paired non-evolving agents and attribution scores. Our evaluation across multiple recent LLMs, evolution surfaces, and harm types reveals that self-evolution indeed increases task completion rates but often at the cost of safety failures that are absent for paired non-evolving baseline agents. We also show that qualitatively different safety behaviors emerge across evolution surfaces and harm types. Further, we show that this divergence in safety behavior is reflected in agents' chain-of-thought reasoning, which yields an effective monitoring strategy that can mitigate unsafe behavior with a low false positive rate.

---


### 894. [Signatures of semantic search in the activations of large language models](https://arxiv.org/abs/2609.35599)

**<font color=#1a73e8>作者：</font>** Luke Leckie, Peter M. Todd, Jacob G. Foster  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When recalling lists of concepts (e.g., animals) during the semantic fluency task (SFT), both humans and large language models (LLMs) organise their output into clusters of related items (e.g., sea animals) that are punctuated by strategic switches between clusters. In humans, this pattern can be explained by a semantic foraging process, whereby distinct neural and behavioural signatures accompany within-cluster production ("exploit") and between-cluster switching ("explore"). Whether LLMs likewise represent these two search regimes within their internal states is unknown. Here, we apply a range of mechanistic interpretability techniques to provide evidence for this. In Study 1, we use the Jacobian lens (J-lens), which maps intermediate-layer residual-stream representations to token-level activations, to show that concept-level activations predict switching. First, we find that switching coincides with low next-token activations. Moreover, the probability of switching rises as the set of strongest J-lens activations (the J-space) becomes depleted of items from the category currently being produced, analogous to explore-exploit decision-making during patch foraging. We then show that middle-layer J-lens activations of abstract category-related labels (e.g., "water") increase in anticipation of switching into that category. We confirm these representations to causally influence switching by deriving steering vectors that target category switching. In Study 2, we identify generic residual stream directions that are activated during and in anticipation of switching. By steering activations along these directions, we bias increased or decreased rates of switching. Our study extends the semantic foraging framework to artificial intelligences and provides evidence that LLMs maintain distinct representational signatures for exploration and exploitation as they verbalise conceptual information.

---


### 895. [TCSAlgBench: Benchmarking Automated Proving for Research-Level Theoretical Computer Science](https://arxiv.org/abs/2609.35606)

**<font color=#1a73e8>作者：</font>** Chutong Yang, Xiyuan Zhang, Yu Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models perform strongly on competition mathematics, but their research-level reasoning remains difficult to evaluate systematically. Theoretical computer science (TCS) connects algorithm design to explicit guarantees and fundamental limits, providing a setting for evaluating whether models can justify computational improvements with arguments humans can inspect. We introduce TCSAlgBench, a benchmark and reusable pipeline for natural-language proof discovery, comprising 398 theorem-level challenges from 138 STOC and COLT 2026 papers. Expert-designed rules complete paper-specific context, preserve computational assumptions and quantitative guarantees, and withhold constructions when discovering an algorithm is part of the task. For each task, prover systems receive theorem statements and access to cited prior work. The pipeline supports fresh, versioned challenge batches from newly released papers. We evaluate ten model configurations from four families under direct inference and prover-verifier discussion, and compare four agent workflows under matched model-call opportunities. All evaluations use the full benchmark. In the model comparison, GPT-5.6 Sol max achieves the highest five-run verifier-accepted coverage at 23.6% after 10-round discussion. Discussion and repeated sampling improve coverage. In the separate agent comparison using GPT-5.5 xhigh, decomposition improves coverage over discussion, and agentic planning achieves the highest five-run verifier-accepted coverage at 25.4%. TCSAlgBench provides a refreshable testbed for measuring progress in model reasoning and studying how agent workflows support research-level proof discovery.

---


### 896. [Twist, Don't Tilt: Trajectory-Exact Constrained Decoding for Masked Diffusion Models](https://arxiv.org/abs/2609.35609)

**<font color=#1a73e8>作者：</font>** Aditya Thimmaiah, Lara Marinov, Jayanth Srinivasa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained decoding for Masked Diffusion Language Models (MDLMs) aims to ensure that generated outputs satisfy a specified structure or syntax constraint. MDLMs generate outputs by repeatedly unmasking masked positions present in their current state. Recent strategies for constrained decoding constrain the model's per-step mean-field posterior (which factorizes over masked positions) by enforcing the desired constraint with an automaton. The resulting chain-structured factor graph allows exact constrained sampling via dynamic programming. However, despite each draw being exact and constraint-satisfying, we prove that their composition, in general, tilts away from the model's relative probabilities over valid trajectories, thus leading to trajectory bias. We derive an exact expression for this bias as a product of ratios measuring how valid continuation mass changes when the denoiser is reconditioned, and characterize when the bias vanishes. We then correct the bias by introducing TWISTER, the first automaton-twisted Sequential Monte Carlo decoder for MDLMs, using the step-exact decoder as the proposal. We show that for regular language constraints, the Feynman-Kac correction is exactly computable, with the twists obtained efficiently using quantities pre-computed for step-exact sampling. We prove that the resulting Feynman-Kac model targets the unbiased Doob h-transformed path law conditioned on constraint satisfaction.

---


### 897. [EvE: An Alternate Optimizer to Adam](https://arxiv.org/abs/2609.35614)

**<font color=#1a73e8>作者：</font>** Shashank Raj, Kalyanmoy Deb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam and its variants dominate neural network training, but a single run only reveals whether a configuration works well after most of its budget is spent, a poor fit for hyperparameter or architecture search, where configurations must be ranked cheaply and pruned early. We introduce EvE (Evolutionary Explorer), a steady-state, population-of-four differential evolution (DE) optimizer with a targeted Adam fallback: each iteration proposes one candidate via DE, running a short burst of gradient descent only if the DE step fails to improve on the incumbent. Selection is greedy, so on a deterministic objective the best-so-far value is provably monotone non-increasing, and since gradients are used only as a targeted rescue, per-iteration cost stays within a constant factor of a single Adam step regardless of dimension. Under a fixed, evaluation-cost-matched budget, EvE wins or ties Adam on 76% of 70 (problem, dimension) cells across seven scalable benchmarks up to one million variables. On three real neural-network tasks (an MLP on MNIST, and LoRA fine-tuning of a 1.5B-parameter language model on two datasets) EvE finishes the same charged budget 1.7-3.9x faster, at a modest cost in final quality (about one accuracy point on MNIST, 9-11% higher relative test loss on the two fine-tuning tasks; on GSM8K, Adam is about 5 accuracy points more accurate, and fine-tuning lowers accuracy below the base model for both). Inside successive halving on UCI Adult, EvE completes hyperparameter and architecture searches 3.1-3.5x faster, ranking configurations about as consistently with Adam as Adam does with itself across seeds (Kendall's tau 0.66-0.69). EvE is not a total replacement for Adam as a final-stage trainer, but a fast, gradient-aware proxy for the search-heavy, budget-constrained regime one level up.

---


### 898. [Behavioral Foundation Models for Quality Diversity](https://arxiv.org/abs/2609.35615)

**<font color=#1a73e8>作者：</font>** Nazim Bendib, Nicolas Perrin-Gilbert, Olivier Sigaud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral Foundation Models (BFMs) are an emerging paradigm in reinforcement learning, playing a role analogous to large language models in natural language processing: they have shown remarkable versatility, enabling zero-shot performance, fast imitation, and online adaptation, all by exploiting the structure of a latent space. In this work, we investigate whether the latent behavioral space induced by BFMs can serve as an effective search space to discover large repertoires of behaviorally diverse and high-performing policies through Quality-Diversity (QD) methods. While QD methods generally search directly in high-dimensional policy parameter space, in this paper, we present BFM-QD, a framework that performs QD search in the compact latent space of a BFM. We further show that the BFM-QD framework provides a closed-form, gradient-free policy improvement operator that approximates a policy gradient update, but requires no critic training and no backpropagation. Across continuous-control benchmarks spanning dense locomotion, sparse navigation, and contact-rich manipulation, BFM-QD consistently outperforms parameter-space baselines, with particularly stark gains in sparse and deceptive settings, where all tested parameter-space QD methods collapse to near-zero performance. These results show the effectiveness of the BFM-QD framework, benefiting from the synergy between dimensionality reduction of the search space and offline pretraining from diverse behavioral data. This positions BFMs as a general-purpose backbone for QD optimization, extending their utility beyond zero-shot task solving to the discovery of diverse behavioral repertoires.

---


### 899. [From cacophony to hierarchy: a principled framework for assessing AI consciousness](https://arxiv.org/abs/2609.35618)

**<font color=#1a73e8>作者：</font>** Shamil Chandaria, Arvo Muñoz Morán, Fernando Rosas 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The question of AI consciousness is one of the most urgent pre-emptive problems in philosophy and computer science, yet progress is hampered by a cacophony of competing theories that often talk past each other. Separating the hard problem from the mapping problem allows the deepest metaphysical disagreements to be set aside: granting that experience supervenes on a system's organisation, the tractable question becomes at which grain of description that supervenience base sits. We extend Marr's three levels of analysis into a five-level hierarchy of functional descriptions (behavioural, computational, intrinsic causal-structural, organismic, and organism-environment) grounded in supervenience, coarse-graining, and multiple realisability. The major theories of consciousness are positioned within this hierarchy according to which level they take to be critical, and for each level we develop operationalisable indicators and assess current AI systems against them. A Bayesian model then combines theoretical credences with indicator evidence into an overall credence in a system's capacity for consciousness. In illustrative assessments, the verdict for current LLMs is driven as much by where theoretical credence is placed as by how the evidence is read: under different stipulated readings and credence distributions, assessments range from below 0.01 to roughly 0.8, showing sensitivity to assumptions. Finally, the consciousness indicators at each level closely overlap with the architectural features needed for general intelligence, suggesting that increasingly capable AI may become a stronger candidate for consciousness. The framework supports a structured agnosticism, in which theoretical commitments are made explicit, credences are updated as evidence accumulates, and assessments take the form of aggregated probabilities rather than verdicts.

---


### 900. [Cartridges++: KV Cache Compression without Off-Context Derailment](https://arxiv.org/abs/2609.35621)

**<font color=#1a73e8>作者：</font>** Sonia Laguna, Joao Monteiro, Marco Cuturi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons. Compressed KV (CKV) representations aim to mimic the cache of a document and are typically computed once and for all, ahead of inference time. Methods to obtain CKVs range from drop mechanisms that reduce their number of columns, to learned approaches. Among the latter, Cartridges have emerged as a leading compression method, learning compact KV representations through distillation on relevant Q/A pairs. While existing evaluations focus primarily on whether Cartridges and other CKVs yield approximately similar responses to document-related, on-context queries, we investigate the crucial deployment question of whether they can handle off-context queries, something the native KV representation is particularly good at, thanks to the mechanics of attention. We observe a fundamental trade-off: while Cartridges perform better for on-context queries, heuristic-variants preserve better the original LLM's ability to operate off-context. We measure this through their capability to avoid context contamination in their response, retain general knowledge, and follow instructions. We propose Cartridges++, simple modifications to cartridges that retain off-context abilities at small or negligible cost. The router variant decides at inference time whether the query should use the learned long-context memory, while the data-mixing variant allocates a small fraction of training Q/As to queries outside the reference long document. Our study shows that assessing CKVs on document utility alone can mask substantial degradation in broader model capabilities, yet those issues can be fixed with benign changes to CKV inference or training.

---


> [!TIP]
> 当前位于：**851-900**（第 18/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | **851-900** | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
