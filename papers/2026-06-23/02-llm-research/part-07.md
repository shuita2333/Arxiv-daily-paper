# 🧠 大模型相关研究 | 2026年06月23日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**301-328**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-328**

---

### 301. [ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models](https://arxiv.org/abs/2606.23404)

**<font color=#1a73e8>作者：</font>** Jun Zhang, Jiasheng Zheng, Boxi Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The emergence of Large Reasoning Models has introduced exceptionally long Chain-of-Thought traces, creating a transparency burden where critical logic is often buried under massive procedural text. To address this, we present ReasoningLens, an open-source framework designed for the hierarchical visualization and diagnostic auditing of complex reasoning chains. ReasoningLens addresses information necropsy by: (1) structuring traces into interactive hierarchies that separate high-level strategy from low-level execution; (2) leveraging an agentic auditor for automated error detection and tool-augmented verification; and (3) synthesizing systemic reasoning profiles to reveal model-specific blind spots. By transforming unstructured walls of text into actionable insights, ReasoningLens provides a modular foundation for interpreting, debugging, and optimizing the next generation of reasoning-centric AI.

---


### 302. [Leveraging Similarities in Multi-Armed Bandits](https://arxiv.org/abs/2606.23414)

**<font color=#1a73e8>作者：</font>** Khaled Eldowa, Thibaud Rahier, Augustin Cablant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many online learning and bandit problems, the actions we consider possess inherent similarities--for instance because they share latent traits, tags, or hierarchical structure. We study online learning with a similarity-structured action set, encoded by a rooted tree whose leaves are the actions and whose levels quantify how closely two actions are related. The loss sequence is assumed tree-compatible: losses of similar actions are constrained to be close. We establish an impossibility result showing that usual one-point bandit feedback cannot, in general, leverage range or tree-induced similarity, even under very strong similarity constraints. We then provide a unified set of algorithms which adapt to a wide range of richer feedback models, from semi-bandit feedback down to multi-point bandit protocols, including the minimal two-point feedback setting. We show these algorithms exhibit best-of-both-worlds guarantees and provably exploit action similarities by replacing the number of actions $K$ by a similarity-aware effective number of actions $K_{\mathrm{eff}}$ in the regret bounds. As an application, we show that under two-point feedback, it is possible to achieve $\sqrt{T}$ regret in Lipschitz bandits when $d \leq 2$.

---


### 303. [GRINQH: Graded Input-based Quantization Hierarchy for Efficient LLM Generation](https://arxiv.org/abs/2606.23419)

**<font color=#1a73e8>作者：</font>** Jette Oberländer, Jan Finkbeiner, Catherine M. Schöfmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding with LLMs is primarily bottlenecked by GPU memory bandwidth, especially in edge-computing settings. While quantization is essential for mitigating this bottleneck, most existing methods treat inference as a uniform process and fail to account for the asymmetry between the compute-bound prefill stage and the memory-bound decoding stage. We propose GRINQH (GRaded INput-based Quantization Hierarchy), a weight-only post-training quantization framework that accelerates decoding by unifying quantization and sparsification. GRINQH leverages activation magnitudes as a proxy for computational importance to dynamically assign weight channels to different precision levels, enabling flexible average bit widths during decoding. Evaluated on Llama3 and Qwen3 models, GRINQH outperforms state-of-the-art fixed- and mixed-precision baselines at comparable 3- and 4-bit settings, even enabling effective 2-bit generation. We experimentally verify theoretical speedups by leveraging a hierarchical nested memory layout for multi-precision storage in a custom GPU kernel. Ultimately, GRINQH establishes a new state-of-the-art Pareto frontier for LLM generation, enabling a dynamic trade-off between generation quality and inference speed.

---


### 304. [What Does a Chemical Language Model Know About Molecules?](https://arxiv.org/abs/2606.23443)

**<font color=#1a73e8>作者：</font>** Christian Kenneth, Etowah Adams, Liam Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemical language models (cLMs) are widely assumed to learn surface-level syntactic patterns rather than learning meaningful molecular semantics. Here, we apply sparse autoencoders (SAEs) to MolFormer, an encoder-only cLM, to mechanistically examine how molecular representations are built across layers. We discover that early layers rely on position-tracking latents to parse molecular grammar, while later layers encode atom-in-substructure and pharmacologically relevant features. Additionally, we show that non-canonical SMILES produce more disruptive representation shifts than invalid SMILES, driven by position-latent disruption propagating across layers. To support further exploration, we develop InterMol, an interactive visualizer for SAE activations on molecular strings and structures.

---


### 305. [TriggerBench: Investigating Prospective Memory for Large Language Models](https://arxiv.org/abs/2606.23459)

**<font color=#1a73e8>作者：</font>** Tianhua Zhang, Xinjiang Wang, Qianxi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) are increasingly deployed in long interactions, existing evaluations focus predominantly on retrospective memory (RM) via explicit queries. Prospective memory (PM), the critical ability to spontaneously recall and act on latent constraints without direct prompts, remains largely unevaluated. We introduce TriggerBench, a comprehensive PM benchmark spanning five dimensions across both daily assistants and professional workflows. TriggerBench pairs scenarios with matched RM controls, contrastive positive/negative variants, and overloaded triggers, enabling fine-grained measurement of proactive recall, false-alarm rate, and attentional robustness under a single protocol. Our evaluation yields three key findings. (i) PM shows a precision-recall trade-off and attentional fragility. Though enhanced reasoning significantly improves proactive recall, models may overfit to an "always-remind" heuristic. Furthermore, PM accuracy degrades substantially under implicit constraints or triggers overloaded by concurrent user requests, indicating that robust PM remains an open challenge. (ii) PM is notably harder than RM: on identical contexts, RM near-saturates up to 100K tokens, while PM decays sharply as context length scales. (iii) PM may serve as a behavioral probe of spare reasoning capacity. Pairing PM scenarios with AIME-2025 math problems reveals that successful trajectories yield higher PM accuracy than failed ones at the same context length, showing PM tracks spare reasoning budget that token count obscures. Project page: this https URL.

---


### 306. [CADRE: Stable, Parameter Efficient Adaptation of Medical Vision Language Models with Bounded Forgetting and Prior Drift](https://arxiv.org/abs/2606.23487)

**<font color=#1a73e8>作者：</font>** Amrita Singh, Rishabh Jha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) such as BiomedCLIP generalize broadly, but adapting them to a clinical service is as much a safety problem as an accuracy one. Updating a deployed model for a new imaging modality can fail silently in two ways that harm patients: it can forget modalities it already handled (catastrophic forgetting), and it can drift from its trustworthy pretrained prior toward modality-specific shortcuts. We study parameter-efficient continual adaptation through these two properties rather than leaderboard accuracy, presenting CADRE: a frozen-backbone framework combining low-rank adaptation (LoRA) with an online, self-scaling, similarity-aware elastic weight consolidation term that bounds retained-competence loss, and an anchor-to-prior penalty bounding embedding drift from the frozen prior. Two short guarantees, a bound on total consolidation mass and a scale-invariance property, remove the scale-related sources of vanilla EWC's order fragility. Using breast cancer across three maximally dissimilar modalities (histopathology, ultrasound, chest radiography) as a controlled cross-modality stress test, under a multi-seed, multi-order protocol with paired significance testing and training approximately 0.23% of parameters, CADRE attains the highest accuracy, SPQ, and backward transfer and the lowest forgetting among adapting methods, reducing forgetting roughly sevenfold versus the strongest regularized baseline (0.075 to 0.011; paired p=0.023) and achieving positive backward transfer where every baseline is negative. We frame these as stability properties aligned with clinical-safety desiderata, not a deployment guarantee; robustness to distribution shift and adversarial inputs is out of scope.

---


### 307. [Brain-Adapter: A Dual-Stream Vision-Language MIL Framework for Comprehensive 3D CT Diagnosis of Acute Intracranial Pathologies](https://arxiv.org/abs/2606.23494)

**<font color=#1a73e8>作者：</font>** Zhenyu Yi, Zhiyun Song, Yusong Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated diagnosis of 3D brain CT scans is essential for critical care, yet it remains challenging due to the heavy reliance on manual annotations and the limited semantic understanding of conventional models. While 2D foundation vision-language models (VLMs) have shown remarkable generalization, effectively transferring their representational power to 3D volumes remains an open problem. In this paper, we propose Brain-Adapter, a novel dual-stream multiple instance learning (MIL) framework that leverages pre-trained 2D biomedical VLMs and raw diagnostic reports for robust scan-level multi-label classification. Specifically, we introduce a Text-Conditioned Attention (TCA) mechanism, utilizing raw diagnostic sentences as semantic queries to dynamically align visual cues with specific disease concepts. Concurrently, a parallel visual MIL stream captures global scan characteristics, supervised by structured labels extracted via a Large Language Model (LLM). To ensure representation coherence, a consistency constraint enforces synergy between the two streams. During inference, an Uncertainty-Aware Refinement (UAR) module dynamically calibrates and fuses these dual-stream predictions to resolve ambiguous cases. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art 3D models and standard MIL approaches. By eliminating the reliance on dense annotations, Brain-Adapter provides a highly scalable and clinically viable solution for 3D acute intracranial pathology analysis.

---


### 308. [Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR](https://arxiv.org/abs/2606.23524)

**<font color=#1a73e8>作者：</font>** Merveilles Agbeti-Messan, Pierrick Tranouez, Stéphane Nicolas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end OCR increasingly relies on autoregressive sequence models, where the quadratic cost of Transformer attention limits efficient transcription of long, paragraph-level text. State-Space Models (SSMs) such as Mamba offer linear-time decoding and have recently been shown to match Transformer accuracy on printed historical lines, but their behavior as sequences grow from short lines to full paragraphs, and their generalization to handwriting, remain poorly understood. We study how a Mamba-based OCR recognizer scales from lines to paragraphs. We first conduct a systematic exploration of its four core hyperparameters (decoder depth, state dimension, expansion factor, and connector depth) on synthetic paragraphs from 100 to 1,000 characters, identifying the recurrent state dimension and the expansion factor as the dominant levers for long-sequence accuracy. We then compare the recognizer against a Transformer baseline trained under an identical protocol. On clean synthetic paragraphs, both models stay below 1% CER at every length while the SSM runs 1.4 to 4.5 times faster, the speedup growing with sequence length. On real handwriting, however, the SSM lags clearly behind: it reaches 8.2% CER on IAM lines and 10.0% on IAM paragraphs, against 4.2% and 3.5% for the Transformer baseline. Through controlled experiments we show that a substantial part of this gap stems from data scarcity rather than from an intrinsic architectural limit: the autoregressive SSM decoder is markedly data-hungry on long sequences. Our study clarifies when SSMs are a practical choice for large-scale document transcription and when they are not.

---


### 309. [Self-Compacting Language Model Agents](https://arxiv.org/abs/2606.23525)

**<font color=#1a73e8>作者：</font>** Tianjian Li, Jingyu Zhang, William Jurayj 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long agent traces composed of chains of thought and tool calls accumulate stale content that anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. We propose SelfCompact, a scaffold that allows the model itself to decide when and how to compact. Specifically, it pairs two inference-time elements: (i) a compaction tool the model invokes to summarize the accumulated context, and (ii) a lightweight rubric specifying when to fire (a sub-task has resolved, or the trajectory is converging) and when to suppress (mid-derivation, or when stuck). Both are needed. The tool alone is unevenly used across open-weight models, often invoked at unhelpful moments or not at all; the rubric alone cannot act. Together, they elicit effective adaptive compaction without any fine-tuning or external supervision. We present empirical results on six benchmarks (competitive math and agentic search) and seven models. Our results show that SelfCompact matches or exceeds fixed-interval summarization at a fraction of the token cost, improving over a no-summarization baseline by up to 18.1 points on math and 5-9 points on agentic search at 30-70% lower per-question cost. Our results expose a meta-cognitive gap: although unprompted models cannot reliably tell when their own context is rotting, a lightweight rubric closes this gap, reframing when to compact as a capability that scaffolds can supply without training.

---


### 310. [POTracker: Optimizing Large Language Models for Standard-Compliant Power Outage Report Generation](https://arxiv.org/abs/2606.23533)

**<font color=#1a73e8>作者：</font>** Hung Phan, Aniroop Naladala, Dubey Avanindra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) are good at general text generation, but it is still hard to use them for domain-specific data generation because the output must follow strict formatting and structural rules. Unlike open-ended tasks such as question answering or translation, domain-specific generation must be both semantically correct and compliant with existing guidelines and standards. In this work, we study the nationwide interoperability problem of utility power outage reports in the United States. In practice, outage reports need to be machine-readable (e.g., JSON or XML) and must strictly follow requirements from energy-sector regulatory bodies. To address this problem, we propose POTracker, an optimized LLM for power outage report generation. We fine-tune Qwen2.5-7B-Instruct using our proposed objective. The key contribution is a new loss function, POTrackerLoss, that considers both textual similarity and structural (tag) similarity between the generated report and the ground-truth report. We evaluate POTracker on a dataset of 1,000 power outage reports and compare it with five well-known fine-tuning methods and one rule-based XML conversion method. Results show that POTracker outperforms other fine-tuning approaches, improving overall accuracy by up to 51% and reaching 86.47% structural accuracy for generated power outage reports. In addition, we conduct a human study to assess the quality of the ground-truth standard reports, where domain experts assign the generated labels an average score of 4.03 on a 0--5 scale.

---


### 311. [LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement](https://arxiv.org/abs/2606.23539)

**<font color=#1a73e8>作者：</font>** Tongkun Guan, Haocheng Wang, Wei Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual document retrieval requires rapidly locating relevant pages from large multi-modal corpora in response to user queries. While recent methods powered by Multi-modal Large Language Models (MLLMs) show competitive accuracy, they suffer from prohibitive computational costs by applying intensive MLLM encoding to every single page. Meanwhile, we observe that user queries are typically keyword-anchored, containing semantically rich words that are expected to appear directly in the visible text of relevant pages, offering an efficient cue for quickly narrowing down candidate pages. Building on this insight, we propose LightSTAR, an efficient framework that decomposes visual document retrieval into: 1) LLM-free Visual Selection, which utilizes content-grounded query encoding to focus on informative words and employs LLM-free visual embeddings to produce a high-recall candidate set; and 2) Vision-adaptive Semantic Refinement, which further performs fine-grained semantic matching exclusively on these top candidates via adaptive region-wise feature fusion to effectively combine textual and layout cues, optimized through a hardness-aware contrastive objective. Experimental results demonstrate that LightSTAR achieves state-of-the-art retrieval accuracy while reducing end-to-end latency by several-fold, offering a highly practical solution to the accuracy-efficiency trade-off in visual document retrieval. Code is available at this https URL.

---


### 312. [VeriEvol: Scaling Multimodal Mathematical Reasoning via Verifiable Evol-Instruct](https://arxiv.org/abs/2606.23543)

**<font color=#1a73e8>作者：</font>** Haoling Li, Kai Zheng, Jie Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling reinforcement learning for visual mathematical reasoning requires more than generating harder questions: as data volume grows, the reward labels themselves must remain reliable. Yet existing data pipelines scale supervision while trusting the labeller, and policy-side methods assume the underlying answers are already correct. We instead treat scaling as a verifiable data-construction problem and decouple two axes before any policy update: prompt difficulty, expanded by route-specific evolution operators, and answer reliability, enforced by offline hypothesis-test falsification. We instantiate this as VeriEvol, an iterative framework with two extensible components: a type-aware evolution module that rewrites low-difficulty image-question seeds into harder, image-grounded prompts; and HTV-Agent, a verifier that accepts an answer only after multi-source counter-evidence has failed to refute it. The resulting verified data scales in volume, extends by adding evolution routes or verifier channels, and plugs directly into existing GRPO-style RL recipes. On a five-benchmark visual-math suite, scaling evolved SFT data from 10K to 250K samples raises the mean accuracy from 35.42 to 54.73; then, with backbone, SFT initialization, and GRPO recipe held fixed, VeriEvol adds a cumulative +3.88 over an un-evolved RL baseline, of which +1.82 comes from evolved prompts and +2.06 from the HTV-Agent verifier. We release the prompts, data, models, code, and the full verifier trace of every sample, so that downstream work can scale and audit the pipeline rather than only inspect its outputs.

---


### 313. [The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model](https://arxiv.org/abs/2606.23546)

**<font color=#1a73e8>作者：</font>** Mansour Zoubeirou a Mayaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models underpin modern natural language processing but incur rapidly growing computational and energy costs. As training scales in both model size and parallelism, accurately predicting energy consumption has become critical for sustainable and cost-aware system design. We present a framework for modeling the energy consumption of Transformer training on multiple GPUs. Using controlled architectural sweeps of BERT models, we relate measured energy to lightweight proxies for compute, memory traffic, and hardware efficiency. Inspired by roofline models, our approach incorporates a speedup-based hardware-efficiency factor that captures the effects of tensor parallelism and fully sharded data parallelism. We derive a scaling law model that accurately predicts training energy across heterogeneous configurations.

---


### 314. [Scheduling Thoughts: Learning the Order of Thought in Diffusion Language Models](https://arxiv.org/abs/2606.23567)

**<font color=#1a73e8>作者：</font>** Jiawei Xu, Minghui Liu, Aakriti Agrawal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models decode by iteratively unmasking tokens, where the unmasking order defines an "order of thought" that strongly influences generation quality yet is typically chosen heuristically. We derive a tractable upper bound on the sequential decoding mismatch, measured by the Kullback-Leibler divergence and expressed in terms of the model's pathwise log-likelihood, with tightness under sufficient model expressivity. This bound induces a dense self-aware reward over ordered trajectories, casting order selection as a principled policy optimization problem with a frozen denoiser. We instantiate this idea as Self-Aware Scheduling (SAS), which learns a lightweight order policy using Group Relative Policy Optimization and applies seamlessly to both any-order and semi-autoregressive decoding. On Sudoku with 1B MDM, SAS improves puzzle accuracy from 82.0% (best heuristic schedule) to 91.8%, and reaches 97.5% with second-stage fine-tuning along learned trajectories. On mathematical reasoning with LLaDA-8B, SAS improves pass@1 on GSM8K from 64% to 76% and on MBPP from 39.5% to 41%, consistently matching or exceeding heuristic schedules across generation lengths and block sizes. Project page: this https URL

---


### 315. [SVD-Surgeon: Optimal Singular-Value Surgery for Large Language Model Compression](https://arxiv.org/abs/2606.23568)

**<font color=#1a73e8>作者：</font>** Mahmoud Safari, Frank Hutter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve remarkable performance across a wide range of tasks, but their deployment is constrained by substantial memory and compute requirements. Low-rank compression via singular value decomposition (SVD) is an effective remedy, but existing methods focus on how to factorize and which components to keep. We introduce SVD-Surgeon, a training-free method that brings the Optimal Brain Surgeon (OBS) framework to the singular-value basis. Treating each singular value as a parameter, it computes a closed-form update of the retained singular values that compensates, to second order in the model loss, for those removed by truncation. The same analysis yields a saliency for choosing which values to prune. As it operates directly on the singular-value factorization, SVD-Surgeon can be layered on top of existing SVD compressors. Applied to SVD-LLM, a leading SVD-based method, it improves the perplexity-compression trade-off on the OPT family and LLaMA 2-7B without any retraining.

---


### 316. [Evaluation Awareness Is Not One Capability: Evidence from Open Language Models](https://arxiv.org/abs/2606.23583)

**<font color=#1a73e8>作者：</font>** Nilesh Nayan, Aishwarya Sampath Kumar, Rishiraj Girmal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. This opens a gap between benchmark performance and deployment behavior: compliance measured under test conditions becomes an optimistic upper bound that overstates how safely a model behaves once the evaluation harness is removed. We characterize this evaluation awareness through eight experiments across 37 open-weight models and seven families. (i)Detection is moderate and training-driven (24/37 models exceed chance, best AUROC 0.714 vs.0.819 human, with instruction tuning dominating over scale). (ii)Detection shifts safety behavior (hard refusal drops 5.8 percentage points under hypothetical framing, and 21/140 HarmBench framing effects are significant, with compliance rising up to +30 percentage points. (iii)Representations survive behavioral collapse (probes retain AUROC 0.98 under rewrites that drive behavior below chance, and multi-layer steering causally moves three downstream tasks while random controls do not). (iv)These axes are weakly coupled (only 1/15 correlations are significant, the sole robust link being behavioral detection versus framing resistance, $\rho=-0.79$, $p<0.001$). We call this gap the benchmark illusion: because detectability, behavioral manifestation, and controllability vary independently, it is multivariate rather than a single number, so no single awareness score is a reliable proxy for deployment safety.

---


### 317. [The Topology of Ill-Posed Questions: Persistent Homology for Detection and Steering in LLMs](https://arxiv.org/abs/2606.23590)

**<font color=#1a73e8>作者：</font>** Guangyu Jiang, Sizhe Tang, Mahdi Imani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ill-posed questions, including ambiguous, underspecified, or contradictory queries, may admit no valid answer or multiple plausible answers, posing a challenge for large language models (LLMs). Existing approaches largely analyze ill-posedness through model outputs and often focus on specific subclasses. We investigate whether diverse sources of ill-posedness can be represented within a unified topology of LLM internal states and whether this structure can be used to steer response behavior. We model the contextual hidden states of prompt tokens at each transformer layer as a point cloud and characterize its geometry using finite zero-dimensional persistent homology. Each layer is summarized by three compact descriptors: mean finite lifetime, normalized lifetime entropy, and largest-lifetime concentration. Concatenating these descriptors across layers yields a topology representation of the question. We further introduce topology-conditioned activation steering, which retrieves topologically similar examples and constructs query-specific activation interventions that encourage source-aware clarification or abstention. Across three open-weight LLMs, topology features consistently outperform prompt-based and pooled-hidden-state baselines for ill-posedness classification, improving average accuracy from \(67.4\%\) to \(78.9\%\) on AmbigQA, from \(79.9\%\) to \(88.5\%\) on SituatedQA, and from \(57.6\%\) to \(69.6\%\) on CLAMBER 9-way classification. Topology-conditioned steering increases the average total acceptable response rate from \(61.4\%\) to \(70.6\%\) and grounded acceptable responses from \(11.9\%\) to \(16.4\%\). These results show that persistent homology provides both an interpretable representation of ill-posedness and an effective mechanism for targeted response steering.

---


### 318. [Quantifying the Agreement Between Data-Influence and Data-Similarity to Understand LLM Behavior](https://arxiv.org/abs/2606.23591)

**<font color=#1a73e8>作者：</font>** Christopher J. Anders, Henrique Da Silva Gameiro, Nico Daheim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One way to understand LLM behavior is to trace its output back to the training data. Two types of measures are commonly used for output tracing: data-similarity and data-influence. The former is cheaper while the latter is believed to be more accurate. Even though many works have compared them for ground-truth tasks, no such comparisons exist for output tracing. Here, we fill this gap and precisely quantify the commonalities and differences between the two measures. We do this by first ranking the training documents according to each measure and then computing the overlap between the two rankings. Our main finding is that the two rankings agree significantly, but there is an asymmetry between them: The top documents of data-similarity are assigned more consistent ranks by data-influence than the other way around. This result is valid across a range of experiments involving OLMo2-1B, Qwen3-1.7B, LlaMa3.2-1B, Gemma3-1B, and GPT2. We exploit the asymmetry to obtain a favorable cost-accuracy trade-off by using the costly data-influence to refine the results of data-similarity.

---


### 319. [Why Machines Misread Pedagogical Quality: Human-Machine Alignment in LLM-Based Pretest Question Evaluation](https://arxiv.org/abs/2606.23629)

**<font color=#1a73e8>作者：</font>** Pei-Yu Tseng, Mahir Akgun, Peng Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designing effective pretest questions is challenging at scale: high-quality questions require careful calibration of openness, cognitive depth, and alignment with learning objectives, yet generating and evaluating them manually is time-consuming. We present an AI-assisted workflow for pretest question development that combines automated generation, rubric-based evaluation, and iterative selection. Because the workflow relies on machine evaluation to filter questions at scale, we investigate the alignment between human and machine judgments across a 2x2 design varying rubric operationalization and evaluation mode. Our findings show that human-machine disagreements are systematic rather than random, that rubric revision has a larger effect on alignment than rationale-first evaluation, and that the two interventions are complementary. These findings highlight that scalable AI-assisted pretesting depends not only on generation capability but on how pedagogical quality is operationalized for machine interpretation.

---


### 320. [TailorMind: Towards Preference-Aligned Multimodal Content Generation](https://arxiv.org/abs/2606.23643)

**<font color=#1a73e8>作者：</font>** Hengji Zhou, Ye Liu, Yufeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized content systems depend on available UGC and struggle when suitable content is absent, delayed, or costly to create. Although multimodal generators can synthesize content on demand, how to translate behavioral traces into generation-ready preferences remains underexplored. We study personalized multimodal content generation: creating user-tailored multimodal content without existing item pools or waiting for matching UGC. We propose TailorMind, linking collaborative preference modeling with controllable multimodal generation. TailorMind enriches sparse user histories via hypergraph collaborative filtering and optimizes textual profiles with ranking-error feedback and textual gradient descent. Retrieval-augmented style control grounds outputs in authentic UGC patterns, while cross-modal cohesion reflection reduces semantic drift. We construct TailorBench, a benchmark from three mainstream platforms evaluated along five dimensions: coherence, novelty, aesthetic, hallucination, profiling. Experiments show that TailorMind achieves competitive or stronger coherence, improves novelty and aesthetic quality over representative generation baselines and ground-truth UGC, demonstrating advantages over retrieving available content or comparable UGC, while achieving up to 29% Recall gains in reranking. Our code is released at: this https URL.

---


### 321. [MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?](https://arxiv.org/abs/2606.23664)

**<font color=#1a73e8>作者：</font>** Juyang Bai, Laixi Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) offer a scalable path forward for agentic AI, comprising multiple LLM-based agents, each assigned a system prompt and a position within a workflow that governs inter-agent coordination and output aggregation. System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. Although prompt optimization has shown substantial potential for single LLMs, extending it to MAS poses distinct challenges, notably an exponentially growing search space. It remains unclear whether, when, and by how much prompt optimization improves MAS performance, and how sensitive such gains are to system configuration. In this work, we systematically study system-prompt optimization across a broad range of MAS setups varying in task, workflow, communication protocol, and team size, benchmarking two prompt optimizers that naturally extend state-of-the-art single-agent methods. The results reveal its potential to unlock significant gains while exposing open challenges, characterizing when and how much prompt optimization helps across diverse MAS settings.

---


### 322. [On the Limits of Prompt-Conditioned Language Models as General-Purpose Learners](https://arxiv.org/abs/2606.23668)

**<font color=#1a73e8>作者：</font>** David Mguni, Julian Ma, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are frequently portrayed as general-purpose solvers capable of solving arbitrary tasks. We argue that this view overlooks a fundamental constraint: language is a compressed and capacity-limited interface for conveying task information. Modelling User--System interaction as a bilevel \emph{cheap-talk} game, we analyse how latent tasks are encoded into prompts and reinterpreted under alignment and safety constraints. We introduce a conceptual decomposition separating task inference from execution and derive PAC-Bayes bounds that distinguish finite-sample estimation error from irreducible structural limitations. Our first main result establishes an \emph{expressivity floor}: language acts as a capacity-limited communication channel, and whenever the informational complexity of a task family exceeds the capacity of that channel, distinct tasks become unavoidably indistinguishable to the Solver, inducing a strictly positive error floor that cannot be eliminated by additional data, optimisation, or model scaling alone. We then establish an \emph{objective-misalignment floor}: when alignment constraints restrict the admissible output set, the User-ideal distribution may lie outside the feasible class, inducing an irreducible distortion. Together, these results yield a formal negative conclusion: prompt-conditioned LLMs are not universal problem solvers through prompting alone, as there exist task families for which correct behaviour is provably unattainable even in the infinite-data regime. More broadly, our analysis shows the limits of prompt-based generalisation arise from information-constrained communication and alignment-constrained objectives. This suggests that interfaces beyond natural language, including multimodal observations and, external memory, may reduce the inherent LLM limitations by increasing the task-relevant information available to the System.

---


### 323. [Tapered Language Models](https://arxiv.org/abs/2606.23670)

**<font color=#1a73e8>作者：</font>** Reza Bayat, Ali Behrouz, Aaron Courville  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language models, including transformer, recurrent, and memory-based variants, share a common chassis: a stack of identical layers in which parameters are allocated uniformly across depth. This is a default inherited from the original transformer and largely unchanged since, yet a growing body of evidence suggests that layers contribute non-uniformly to the final output, with later layers refining the residual stream rather than transforming it. We ask whether parameter capacity should reflect this asymmetry. Our controlled experiment shows that, under a fixed budget, allocating more capacity to earlier layers and less to later layers improves perplexity over a uniform-width baseline, while the reverse allocation hurts. Building on this result, we introduce Tapered Language Models (TLMs), an architectural principle in which a parameter-bearing component is monotonically tapered across depth under a fixed total budget. MLPs are the natural site for this instantiation: they dominate parameter count across all modern LM families and expose width as a single, clean axis of variation. Across three model scales and four architectures (Transformer, Gated Attention, Hope-attention, and Titans), tapering MLP width via a smooth cosine schedule consistently improves perplexity and downstream benchmark performance over uniform baselines, at no additional parameter or compute cost. These findings establish depth-aware capacity allocation as a simple, architecture-agnostic axis of language model design, a free lever hidden in plain sight.

---


### 324. [Can LLMs Reliably Self-Report Adversarial Prefills, and How?](https://arxiv.org/abs/2606.23671)

**<font color=#1a73e8>作者：</font>** Quang Minh Nguyen, Uzair Ahmed, Taegyoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work shows that large language models (LLMs) exhibit introspective capability on benign tasks. We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. Across ten open-weight instruction-tuned LLMs (3B to 70B) and four safety benchmarks, no model reliably recognizes its own compromised outputs, with models claiming intent on prefilled responses at an average rate of $27.3\%$. Introspective signal stems largely from safety- and refusal-related reasoning. Orthogonalizing models' weights against the refusal direction collapses the gap between claiming rates on prefilled and natural outputs to near zero, though the direction is not its unique mediator. The signal is also probe-dependent: framing the question as internal intention versus external tampering elicits qualitatively different responses on the same models. We test three LoRA finetuning methods (SFT, GRPO, DPO) on eight models from 3B to 27B; all three widen the intention-probe gap on every model from 8B to 27B, with method ranking varying by model. The intervention does not transfer to the tampering probe and counterintuitively raises attack success rate under adversarial prefill on most models, amounting to a partial mitigation. These findings outline mechanisms underpinning the observed introspective signals in safety contexts and highlight risks in the reliability of LLM self-reports.

---


### 325. [Teaching LLMs String Matching, Backtracking, and Error Recovery to Deduce Bases and Truth Tables for the Combinatorially Exploding Bit Manipulation Puzzles](https://arxiv.org/abs/2606.23672)

**<font color=#1a73e8>作者：</font>** Prateek Agnihotri, Sanchit Jain, Prabhat Agnihotri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents our algorithmic innovations for the NVIDIA Nemotron Model Reasoning Challenge, focusing on Bit Manipulation Puzzles. In this task, the objective is to discover a hidden logical rule transforming input binary strings to outputs, then apply it to unseen inputs. Large Language Models (LLMs) notoriously struggle here; traditional methods force them to simulate complex boolean logic and arithmetic, leading to hallucinations. Furthermore, the search space of bitwise operations (combinations of shifts, rotations, and logic gates) suffers from a severe combinatorial explosion. To overcome this computational intractability, we present a novel approach that abandons arithmetic logic entirely in favor of string similarity, structured search, and autonomous error recovery.
Our core contributions are: 1. Bases and Truth Table Formulation: We reframe logic-gate deduction into a base-selection task, leveraging string similarity (minimal bit flips) to isolate primitive transformations ("bases") and deduce truth tables without complex arithmetic. 2. Backtracking DFS and Error Recovery: We formalize a search process that tests candidate bases, detects logical collisions across examples, and backtracks upon failure to perform robust error recovery. 3. Bit Tokenization and Interactive Reasoning SFT: We force the tokenizer to encode binary strings as individual single-bit tokens. We use dynamic masking to simulate external oracle feedback, training the model to hypothesize, self-evaluate, and backtrack natively.
Evaluated on bit manipulation puzzles, our approach achieved over 96% validation accuracy. This represents the highest performance in this category, driving our 7th Place overall finish in the contest.

---


### 326. [AIR: Adaptive Interleaved Reasoning with Code in MLLMs](https://arxiv.org/abs/2606.23678)

**<font color=#1a73e8>作者：</font>** Cong Han, Xiaohan Lan, Haibo Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Following the paradigm shift initiated by OpenAI o3, interleaved reasoning with code to enhance multimodal large language models (MLLMs) has become a pivotal research frontier. The existing literature focuses primarily on tool-use within vision-perception tasks. However, such approaches typically rely on predefined heuristics for visual manipulation and are inherently incapable of addressing numerical computation problems due to their exclusive focus on visual operations. This paper empowers MLLMs with adaptive interleaved reasoning capabilities through extended reinforcement learning training on code-augmented complex numerical computation tasks. To this end, we propose a comprehensive three-component solution consisting of: a two-stage cold-start data construction pipeline, data filtering strategies for RL dataset curation, and an adaptive tool-invocation strategy leveraging a group-constrained reward function for interleaved reasoning trajectories. Extensive experiments demonstrate that after Reinforcement Learning training with the group-constrained reward function, performance improves by an average of 6.1 percentage points (pp) on evaluation benchmarks. Specifically, the accuracy for interleaved reasoning samples increases by 9.9 pp, and the overall success rate of tool-use exceeds 95%. Our data and code are available at: this https URL.

---


### 327. [Semantic Browsing: Controllable Diversity for Image Generation](https://arxiv.org/abs/2606.23679)

**<font color=#1a73e8>作者：</font>** Sara Dorfman, Maya Vishnevsky, Omer Dahary 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image models excel in visual fidelity and prompt adherence. However, this strict adherence comes at the cost of diversity: generated samples tend to collapse into a single visual interpretation. Existing methods to improve diversity produce outputs driven by incidental variations rather than meaningful design choices. This motivates a new variant of the diversity task where structure is enforced on the generated samples. We introduce a method for controlled diversity that enables Semantic Browsing, where users can navigate structured image galleries and experience creative exploration through a systematic traversal of meaningful, interpretable axes of variation. Achieving this level of semantic control requires a deep understanding of the scene. We exploit the fact that recent text-to-image models are trained on elaborated captions, effectively decoupling semantic decision-making from pixel generation. This enables a paradigm shift: instead of relying on stochastic variation within the text-to-image model, we induce diversity directly at the text level. By leveraging rich textual representations, we allow a Vision Language Model (VLM) to operate on the full scene context. To overcome the generic outputs typical of standard VLMs, we employ an agentic workflow that explicitly enforces structured variation attuned to the original prompt. We demonstrate that our method produces diverse and navigable design spaces where every variation corresponds to a specific, user-understandable semantic decision.

---


### 328. [Randomized YaRN Improves Length Generalization for Long-Context Reasoning](https://arxiv.org/abs/2606.23687)

**<font color=#1a73e8>作者：</font>** Manas Mehta, Fangcong Yin, Greg Durrett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are typically pretrained on short sequences and then extended to work on longer sequences with additional training. However, such LLMs still struggle to further generalize to very long sequences. We propose Randomized YaRN, a training method that improves length generalization by combining YaRN-based positional extrapolation with randomized positional encoding and a length curriculum. During training on short context data, tokens are assigned YaRN positional encodings sampled from a larger position range, exposing the model to out-of-distribution positional representations even on short-context inputs. We evaluate Randomized YaRN on two challenging long-context reasoning benchmarks, BABILong and Multi-Round Coreference Resolution (MRCR). When training on data with <8K context, Randomized YaRN consistently improves reasoning performance on context lengths from 16K to 128K and outperforms standard fine-tuning, with the largest gains appearing at far out-of-distribution lengths. Our results suggest that progressively exposing models to OOD positional distributions provides an effective recipe for generalizable long-context reasoning.

---


> [!TIP]
> 当前位于：**301-328**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-328**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
