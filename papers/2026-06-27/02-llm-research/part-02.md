# 🧠 大模型相关研究 | 2026年06月27日

> 本类共 **135** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-135](./part-03.md)

---

### 51. [Perception, Verdict, and Evolution: Hindsight-Driven Self-Refining Forensics Agent for AI-Generated Image Detection](https://arxiv.org/abs/2606.26552)

**<font color=#1a73e8>作者：</font>** Yangjun Wu, Keyu Yan, Yu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative models presents a significant challenge to existing deepfake detection methods, particularly given the widespread dissemination of highly realistic AI-generated images. Although Multimodal Large Language Models (MLLMs) show strong potential for this task, existing approaches suffer from two key limitations: insufficient sensitivity to fine-grained forensic artifacts and reliance on static synthetic supervision from frontier models, leading to limited flexibility and high-cost. To address these issues, we propose ForeAgent, an agentic forensics framework for AI-generated image detection with iterative self-evolution. First, ForeAgent adopts a Perception-Verdict architecture that aggregates multi-view cues spanning semantic, spatial, and frequency-domain features, and leverages an MLLM as a verdict module to fuse these signals for a logical-grounded verdict. Second, to enable continual self-improvement, we introduce a Hindsight-Driven Self-Refining strategy following a Sampling-Reflection-Evolution paradigm. The agent performs inference rollouts on training instances. Guided by ground-truth labels as hindsight, it reflects on failure cases and low-quality reasoning trajectories to regenerate higher-quality reasoning traces. These synthesized samples are then strictly filtered through a dual-expert quality gating module. ForeAgent continuously evolves via fine-tuning on self-curated high-quality samples. Extensive experiments demonstrate that ForeAgent achieves state-of-the-art performance on the Chameleon benchmark, reaching 82.18% accuracy (+16.41% over AIDE), and achieves 93.3% mean accuracy on AIGCDetect-Benchmark across 16 generators. In addition, external evaluation shows that ForeAgent produces more consistent and causally grounded reasoning compared to GPT-5 and GPT-5-mini.

---


### 52. [EvoOptiGraph: Weakness-Driven Coevolution via Graph-Based Structural Generation for Optimization Modeling](https://arxiv.org/abs/2606.26578)

**<font color=#1a73e8>作者：</font>** Qingcan Kang, Mingyang Liu, Xiaojin Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating optimization modeling from natural language with large language models (LLMs) faces two key challenges. First, training corpora lack structural diversity. Second, data generation pipelines remain static and decoupled from model learning. To address these challenges, we propose EvoOptiGraph, a novel framework where data and model co-evolve, driven by model weaknesses. EvoOptiGraph represents each mixed-integer linear program (MILP) as an attributed bipartite graph and applies validity-preserving evolutionary operators to generate structurally diverse instances. The evolved graphs are converted into solver code and natural language via deterministic compilation and verified back-translation. Training proceeds in two stages: supervised fine-tuning (SFT) on an initial dataset, followed by reinforcement learning with verifiable rewards (RLVR), where graph-derived weakness signals guide the generation of new instances targeting the model's failures. This forms a closed loop that continuously updates the training distribution. Empirical results on six public datasets show that EvoOptiGraph significantly outperforms larger generalist models, agentic methods, and specialized baselines in accuracy, executability, and generalization. These results demonstrate that targeted data-model coevolution is an effective strategy for improving LLMs on optimization modeling tasks.

---


### 53. [SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference](https://arxiv.org/abs/2606.26587)

**<font color=#1a73e8>作者：</font>** Haoqian Meng, Yilun Luo, Yafei Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit floating-point formats and semi-structured sparsity are increasingly supported by modern accelerators, yet combining them for LLM activation compression remains challenging: activations contain input-dependent outliers that dominate block scales in FP4 quantization, and directly applying N:M sparsity masks discards moderate values, coupling sparsification loss with quantization error. We introduce SharQ, a training-free inference method that bridges activation sparsity and FP4 quantization through an online sparse--dense decomposition. For each activation tensor, SharQ generates an input-adaptive N:M mask to extract an outlier-dominated sparse backbone, quantizes it to FP4, and defines a dense residual relative to the quantized sparse backbone rather than the unquantized sparse values. A sparse FP4 GEMM processes the backbone while a dense FP4 GEMM compensates for both mask-induced activation loss and sparse-path quantization error. The two paths share a single FP4 weight payload with path-specific scale views, and a fused preparation kernel absorbs mask generation, residual construction, and layer normalization into one operator. SharQ requires no calibration data, retraining, or model-specific tuning. Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. On an RTX 5090, SharQ delivers 2.2--2.4$\times$ latency reduction over FP16 and 1.2--1.4$\times$ throughput improvement over FP8 in language model serving, and up to 1.58$\times$ speedup on Wan2.2-T2V-A14B video generation when combined with SageAttention. Our code is available at this https URL.

---


### 54. [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590)

**<font color=#1a73e8>作者：</font>** Manar Alsaid, Chimdumebi Nebolisa, Faris Abbas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Security misconfigurations in Terraform Infrastructure-as-Code are a growing risk in cloud deployments, and large language models are increasingly used as automated repair agents. Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. This paper presents TerraProbe, a five-layer oracle framework for evaluating LLM-assisted Terraform security repair. We apply TerraProbe to 288 first-pass repairs generated by gemini-2.5-flash-lite, GPT-4o, and Claude 3.5 Sonnet across 68 real-world TerraDS modules and 28 controlled injected-defect modules. The results show that targeted Checkov removal overstates repair success. Although targeted removal reaches 83.3 percent for the primary model, full-scanner cleanliness drops to 10.4 percent, Terraform planning succeeds for 39.6 percent, and plan comparison is reachable for 38.5 percent. Human adjudication further shows that 71.4 percent of plan-compared real-world repairs are deceptive fixes that pass automated checks while leaving the underlying vulnerability in place. This pattern is statistically indistinguishable across the three models, with deceptive-fix rates from 57.1 percent to 71.4 percent and pairwise Fisher exact p-values above 0.10. The paper introduces a four-dimensional taxonomy of deceptive fixes, validated with Cohen kappa of 0.78 and Krippendorff alpha of 0.76. IAM permission analysis confirms that wildcard Resource grants persist in all nine CKV2 AWS 11 deceptive-fix cases. TerraProbe contributes an evaluation methodology, a replication package, and the Multi-Layer Oracle Evaluation framework for distinguishing intent-aligned security repairs from scanner-passing false successes.

---


### 55. [Content-Based Smart E-Mail Dispatcher Using Large Language Models](https://arxiv.org/abs/2606.26593)

**<font color=#1a73e8>作者：</font>** K. Paramesha, K R Sriram, Sujan Shetty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Email communication has become an integral part of personal and professional life, but handling its vast volume is still a significant issue for large organisations. Manual perusal of emails and forwarding their contents and attachments to intended recipients using other instant messaging platforms has proved to be error-prone and time-consuming leading to losses in terms of productivity and creating undue stress. The main objective of this paper is to explore an alternative mechanism that is to automate the task of dispatching emails based on their contents to the respective WhatsApp groups of students of various semesters of programs in an engineering college, facilitating a smooth flow of information from one end to another end in an organisation. The dispatcher system is built using agents querying large language models (LLMs) to enable it to analyze the contents of emails and route them to the relevant groups of students for their information and consumption. The system harnesses the capabilities of LLMs in analysing the textual contents for decision-making. With a well-structured agent framework prompt that includes email content as input with instructions and context, the system figures out the relevant groups to which the email message is dispatched, thus providing the required information on time. The proposed system does not rely on labelled datasets and provides several benefits, including enhanced productivity and a reduction in the cognitive load associated with reading emails.

---


### 56. [LLM-based Models for Detecting Emerging Topics in Service Feedback](https://arxiv.org/abs/2606.26595)

**<font color=#1a73e8>作者：</font>** Mahsa Tavakoli, Ruth Bankey, Cristián Bravo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enhancing the analysis of service feedback is essential for public sector organizations, particularly tax administrations, where trust and compliance depend on fair and effective service delivery. As feedback volumes grow, identifying emerging service quality issues and potential disparities across diverse populations becomes increasingly challenging. Traditional approaches often rely on manual review or static expert-defined indicators, limiting scalability and the ability to capture complex patterns in textual feedback.
This paper presents a novel methodology that integrates large language models (LLMs), statistical techniques, and human-AI collaboration to improve multilingual customer feedback analysis. The primary objective is to detect emerging service quality topics that may also reveal potential inequities in service delivery. Our framework combines fine-tuned, quantized LLMs with expert oversight to produce accurate, computationally efficient, and context-aware analyses.
The proposed approach was evaluated using similarity analysis and assessments from experienced tax officers, demonstrating stronger alignment with expert judgments than baseline models. By incorporating a human-in-the-loop framework, the methodology reduces LLM fabrication while improving the reliability and relevance of generated insights.
The results demonstrate the practicality of combining LLMs with human expertise to support scalable, evidence-based decision-making in public sector organizations. This work contributes to the development of responsible AI systems that enhance service quality, responsiveness, fairness, and public trust through more effective analysis of multilingual customer feedback.

---


### 57. [DiCoBench: Benchmarking Multi-Image Fine-Grained Perception via Differential and Commonality Visual Cues](https://arxiv.org/abs/2606.26602)

**<font color=#1a73e8>作者：</font>** Geng Li, Yuxin Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated impressive fine-grained perception capabilities. However, existing benchmarks predominantly rely on explicit textual cues or low-resolution inputs, failing to evaluate a model's ability to autonomously perceive implicit visual cues in high-resolution. To bridge this gap, we introduce DiCoBench, a comprehensive, multi-image high-resolution benchmark designed for cross-image fine-grained perception. DiCoBench consists of 765 meticulously curated samples categorized into two progressive tracks: Differential Visual Cues and Commonality Visual Cues, covering 8 distinct perception tasks. By formulating the benchmark as a multiple-choice question task and utilizing high-resolution imagery (approaching 2K), we eliminate evaluation metric bias and pose a substantial challenge to current state-of-the-art MLLMs. Our extensive evaluation of 18 diverse MLLMs reveals a striking performance gap compared to human accuracy (98.3\%), with top-performing models struggling significantly with micro-scale detail capture. We believe DiCoBench will serve as a challenging testbed to drive future research in autonomous, high-resolution multi-image perception.

---


### 58. [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614)

**<font color=#1a73e8>作者：</font>** Kuangshi Ai, Patrick Phuoc Do, Chaoli Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents enable natural language interaction for scientific visualization (SciVis). Still, prior systems have essentially prioritized autonomy over human analytical control, thereby limiting transparency and human oversight. We present HiLSVA, a human-in-the-loop agentic system that supports mixed-initiative SciVis workflows. HiLSVA integrates a plan-first multi-agent architecture with explicit human oversight, stepwise provenance tracking, and learn-at-test-time adaptation from user feedback. The system supports fluid handoff between humans and agents through both natural language and direct manipulation of visualizations, while sandboxed execution ensures safe, reproducible workflows. In doing so, HiLSVA reframes agentic SciVis as a collaborative process that augments, rather than replaces, human analytical reasoning. We evaluate HiLSVA through representative case studies and a controlled user study with twelve participants of varying expertise across multiple autonomy settings. Results show that mixed-initiative interaction improves task completion, user control, and workflow transparency across different levels of user expertise, while revealing a tradeoff between execution efficiency and human oversight. These findings highlight the importance of human-centered design in agentic SciVis and guide the development of future collaborative visualization systems. We encourage readers to explore our demo video, case studies, and source code at this https URL.

---


### 59. [Closing the Quality Gap in Low-Resource Text-to-Speech: LoRA Fine-Tuning of VoxCPM2 for Khmer and Korean](https://arxiv.org/abs/2606.26618)

**<font color=#1a73e8>作者：</font>** Phannet Pov, Sovandara Chhoun, Hyun Woo Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large pretrained text-to-speech (TTS) models sound almost human for well-resourced languages, but much worse for languages that are rare in their training data. We study this quality gap for Khmer and Korean using VoxCPM2, a 2.4B-parameter, tokenizer-free TTS model that joins a MiniCPM-4 language-model backbone with a flow-matching diffusion decoder. We build one shared, language-tagged corpus of about 26 hours and adapt VoxCPM2 with a single Low-Rank Adaptation (LoRA) adapter, trained on both languages at once and added to both the language model and the decoder. The adapter is zero-initialized, so training starts exactly at the original (zero-shot) model. In native-speaker listening tests, the Khmer Mean Opinion Score (MOS) rises from 3.85 to 4.23 with the best adapter (rank 64), a highly significant gain (paired Wilcoxon test, p<0.001), while training only 0.19 to 3.03 percent of the parameters. The automatic loss and the human ratings, however, disagree on the best rank: validation loss is lowest at rank 128, yet MOS peaks at rank 64. The same adapter brings no gain for Korean, a language the base model already handles well, and at a high rank it even degrades quality. Adaptation therefore helps mainly where the base model is genuinely weak.

---


### 60. [Reviving Reflection-in-Action: Instilling Designerly Thinking in AI-Supported Ideation through Multimodal Prompting](https://arxiv.org/abs/2606.26626)

**<font color=#1a73e8>作者：</font>** Samangi Wadinambiarachchi, Jenny Waycott, Greg Wadley  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current AI-powered creativity support tools (AI-CSTs) primarily use text prompting to generate solution-oriented outputs. However, the potential value of multimodal prompting in designer-AI interaction, specifically the introduction of productive friction to encourage iteration and reflection, has not been fully explored. To address this, we developed SketchifAI, a prototype AI-CST, and evaluated it with design students. In a mixed-methods, within-participants study, we examined how different input modalities (text, sketch, and sketch-plus-tags) affected design students' perceived ability to express their intent, their perception of creativity support, and their divergent thinking performance. Our preliminary findings suggest that the sketch modality tended to enhance fluency, with inconclusive evidence for differences in variety, originality, or quality compared to text modality. Yet, paradoxically, participants showed a strong preference for text prompting. We discuss how AI tools might be designed to reintroduce reflection-through-sketching, ensuring that designer-AI interaction supports, rather than erodes, essential design skills in students.

---


### 61. [From Weights to Features: SAE-Guided Activation Regularization for LLM Continual Learning](https://arxiv.org/abs/2606.26629)

**<font color=#1a73e8>作者：</font>** Evan Ning, Wei Xue, Dong Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space regularization methods such as Elastic Weight Consolidation (EWC) are the standard approach to catastrophic forgetting in continual learning. However, those methods tend to underperform when applied to large language models. We argue that such underperformance can be partly explained by the ``polysemantic'' nature of large language models: per-weight importance estimates utilized by EWC-style regularization are too coarse and cannot isolate the knowledge that needs protection. In this paper, we propose regularizing instead in the model's activation space, using pretrained Sparse Autoencoders (SAEs) as a monosemantic feature dictionary. From the perspective of constrained optimization, we derive a new loss function that uses the SAE feature dictionary to explicitly balance stability and plasticity, and show that EWC is a special case in the one-sided weight-space penalty setting. Unlike replay-based methods that store or revisit examples from earlier tasks, our method requires no previous-task data after mask construction: current-task data is used to compute a compact SAE feature mask, and only this mask is retained for later training. Further, since the feature space has significantly lower dimensionality than the parameter space, the proposed method is more memory efficient. On the TRACE and MedCL continual learning benchmarks, the method achieves the strongest result among approaches without introducing task-specific architectural components, also surpassing traditional weight-space regularization methods like EWC. Beyond performance comparisons, we provide empirical evidence for the polysemanticity thesis: task-relevant representations are linearly separable in the SAE feature basis but indistinguishable from chance in the weight basis, and weight-space protection is nearly non-selective at the concept level.

---


### 62. [Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning](https://arxiv.org/abs/2606.26631)

**<font color=#1a73e8>作者：</font>** Mengzhao Wang, Yanli Ji, Wangmeng Zuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. A natural shortcut is to reuse the historical visual key-value (KV) cache directly. However, we identify a critical failure mode of this strategy: cached visual keys are already bound to their original positional context. Such stale positional binding distorts attention under later decoding contexts and can trigger severe autoregressive decoding collapse. This failure suggests that effective cache reuse requires reconstructing visual evidence under positions compatible with the current decoding state, rather than directly copying position-bound historical cache entries. To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. PRCR stores raw visual KV cache together with their original spatial coordinates, then reassigns position-compatible coordinates to select entries and rebinds their keys before injecting the reconstructed cache into the active decoder cache. This design reuses historical visual evidence while preserving textual positional continuity and relative visual structure. Experiments across multiple multimodal reasoning benchmarks show that PRCR achieves replay-level or better performance, improving average accuracy by 5 percent and reducing visual-revisiting computation by up to tens of thousands of times.

---


### 63. [CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs](https://arxiv.org/abs/2606.26650)

**<font color=#1a73e8>作者：</font>** Shigeng Wang, Chao Li, Yangyuxuan Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we present CAT-Q, Cost-efficient and Accurate Ternary Quantization, for compressing and accelerating LLMs. Unlike existing state-of-the-art ternary quantization methods that rely on data-intensive and costly quantization-aware training to mitigate severe performance degradation, CAT-Q is a simple yet effective post-training quantization scheme that is readily applicable to LLMs with diverse architectures and model sizes. It has two key components, learnable modulation (LM) and softened ternarization (ST), which are coupled from an optimization perspective. LM leverages a composition of learnable factors to modulate the distribution of pre-trained high-precision weights and the ternary threshold, making them less sensitive to ternarization. ST further introduces a differentiable transition function to guide the ternarization process toward stable convergence. We show that, for pre-trained LLMs with 1.7B to 8B parameters, CAT-Q can efficiently quantize them into ternary models using only 512 calibration samples, while achieving superior performance than the seminal BitNet 1.58-bit v1 and v2 families (with 1.3B to 7B parameters) trained with 100B tokens, yielding about a 100,000X reduction in training tokens. Moreover, we show for the first time that CAT-Q can quantize much larger pre-trained LLMs having 14B to 235B parameters into leading ternary models within just 8 to 60 hours on 8 A100-80GB GPUs. Code is available at this https URL.

---


### 64. [SocialPersona: Benchmarking Personalized Profiling and Response with Multimodal Social-Media Context](https://arxiv.org/abs/2606.26654)

**<font color=#1a73e8>作者：</font>** Qinkai Zhang, Yanyan Zhao, Xin Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized language-model assistants are often evaluated through a memory lens: can a model recall preferences users have explicitly stated in dialogue? More comprehensive personalization demands a harder capability -- inferring what users care about from the multimodal traces they naturally leave behind. We introduce SocialPersona, a benchmark for evaluating whether multimodal large language models (MLLMs) can recover revealed preferences from longitudinal social-media timelines and use them in dialogue. Built from longitudinal timelines of 171 everyday, non-promotional social-media users, SocialPersona contains text, images, timestamps, and 2,597 human-verified preference tags across seven interest domains, separating stable interests from recent interests. It supports two tasks: constructing structured user profiles from multimodal context and generating responses aligned with inferred profiles. Experiments with proprietary and open-weight MLLMs show that models can identify broad interest domains, yet their performance drops on fine-grained and recent interests and degrades further when inferred profiles must be used to personalize dialogue. Together with evidence that text and images provide complementary preference signals, these results indicate that robust cross-modal, long-horizon user modeling remains a key challenge, and that SocialPersona can help measure and advance progress toward assistants that infer and act on revealed preferences.

---


### 65. [PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs](https://arxiv.org/abs/2606.26666)

**<font color=#1a73e8>作者：</font>** Muhammad Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive large language model (LLM) serving is increasingly limited by key-value (KV) cache movement rather than dense matrix multiplication. Modern paged-attention systems reduce KV-cache fragmentation and mature kernels such as FlashInfer provide highly optimized native-paged decode attention. However, the best single-kernel implementation is not always the best serving schedule: low-active long-context decode can under-utilize commodity GPUs, while mixed sequence lengths introduce a tension between many exact-length launches and coarse padded batches. We present PersistentKV, a native block-table decode attention engine and page-aware scheduling study for grouped-query attention (GQA). PersistentKV maps work by KV-head group, is designed to reuse K,V tiles across grouped query heads, supports native page tables, and adds a compact workqueue schedule that executes only non-empty row-KV-head-sequence-split tasks. On an RTX 3060 with FP16, page size 16, Hq=32, Hkv=8, d=128, and identical correctness tolerance against FlashInfer, a calibrated adaptive policy selects FlashInfer for small active batches, PersistentKV sequence splitting for B1 long-context steps, and PersistentKV workqueue scheduling for B8 long-context steps. With thresholds and split counts fixed on calibration traces, one held-out trace seed improves synchronized wall throughput by 1.063-1.265x on B8 bimodal, uniform, and Zipf-like workloads and by 1.399x on a B1 bucketed trace. On the B4 bimodal boundary case, the policy avoids the PersistentKV regression by selecting FlashInfer. These results identify a concrete systems niche for adaptive page-aware decode scheduling and show that work assignment, not only attention math, is a decisive serving-system variable.

---


### 66. [NebulaExp-8B: An Empirical Post-Training Pipeline via Full-Scale Ablation Research](https://arxiv.org/abs/2606.26671)

**<font color=#1a73e8>作者：</font>** Qiaobo Hao, Yangqian Wu, Shunyi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training alignment determines the reasoning and human preference following capabilities of large language models, yet most existing works withhold detailed data construction, filtering rules and training recipes, which hinders community reproducibility and lightweight model optimization. This work presents NebulaExp, a fully transparent, ablation-driven post-training pipeline built on Qwen3-8B-base, covering two orthogonal model branches: general instruct model and complex reasoning-specialized model. We curate a raw corpus of 3.84M multi-source SFT samples and a 200K verifiable RL candidate pool, and design an end-to-end data processing stack including response distillation, multi-dimensional cross-verification filtering, fine-grained difficulty grading, task classification and diversity-aware sampling. For the Instruct branch, our three-stage optimized supervised fine-tuning approach NebulaExp-Ins-SFT improves the average benchmark score from the 55.01 baseline of Qwen3-8B-nothink to 60.99. GRPO reinforcement learning then further elevates the average score to 61.85. For the Reasoning branch, medium-difficulty GRPO RL improves average reasoning score from 73.88 to 75.17. To address RL's dependency on task verifiers, we systematically investigate single-teacher and multi-teacher OPD (MOPD): utilizing merely 4K instruction-following samples and outperforms RL baseline by 3.26 points on IFEval with +4.43 average overall gain; MOPD fuses four domain-specialist teachers with merely 10K samples, lifting average performance by 4.18 over the base model. This report provides a fully reproducible empirical post-training recipe for 8B-scale LLMs, and comprehensively dissects the capability trade-offs among instruction adherence, mathematical reasoning, code generation and general knowledge.

---


### 67. [PhysEditWorld: A Large-Scale Dataset Toward Physics-Editable World Models](https://arxiv.org/abs/2606.26694)

**<font color=#1a73e8>作者：</font>** Bin Hu, Yanwen Ma, Jiehui Huang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent game world models can synthesize visually plausible, action-conditioned rollouts. However, their interaction behaviors often remain limited to exploratory or wandering trajectories, and physical dynamics are typically learned as implicit correlations from data rather than as controllable variables. This limitation hinders their applicability to authored game environments, where physical rules are deliberately designed and require explicit manipulation. We introduce PhysEditWorld, a multimodal dataset with physical parameters, with a primary focus on gravity in this initial version. At its core, PhysEditWorld is built upon a replay paradigm implemented with a UE5 replay-and-rendering pipeline. Each scenario records a normalized action trace and replays the same initial state, character controller, action sequence, and camera policy under multiple gravity configurations, enabling controlled and attributable physical variation. PhysEditWorld contains 12 cinematic UE5 scenes, over 100 hours of gameplay interactions, and more than 60 million rendered rollout frames. Each sample provides synchronized multimodal signals, including RGB, depth, normals, audio, action traces, camera trajectory, engine states, semantic annotations, and explicit gravity labels. We further conduct initial utility studies on both generative video models and world understanding models, demonstrating that PhysEditWorld enables improved gravity-faithful dynamics modeling, enhances consistency under physical edits, and provides a scalable foundation for controllable world modeling research.

---


### 68. [Beyond Logical Forms: LLM-Extracted Patterns for Fallacy Classification](https://arxiv.org/abs/2606.26698)

**<font color=#1a73e8>作者：</font>** Eleni Papadopulos, Firoj Alam, Giovanni Da San Martino  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In today's fast-paced information era, logical fallacies, defined as defective patterns of reasoning, inevitably contribute to the growth of information disorder. However, often fallacies appear in nuanced forms that complicate automated classification. In this study, we investigate whether merging abstract logical structures with context-level linguistic cues proves beneficial for fallacy classification, developing a framework that inductively extracts such patterns from fallacious examples and their explanations using Large Language Models (LLMs). We evaluate the impact of these patterns across different LLMs and experimental zero- and one-shot configurations, showing statistically significant improvements over zero-shot baselines and outperforming competing approaches. Cross-dataset experiments validate generalization, establishing data-driven pattern extraction as an effective method for generating logical representations.

---


### 69. [LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography](https://arxiv.org/abs/2606.26713)

**<font color=#1a73e8>作者：</font>** Yuqi Jiang, Yumeng Liu, Zimu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As semiconductor technology nodes scale, computational lithography is essential for ensuring yield and performance. However, lithography is a continuous physical process involving mask optimization, optical imaging, resist exposure, and development, which existing models fail to capture. To overcome this limitation, we present LithoDreamer, the first physics-informed World Model (WM) framework for computational lithography, which formulates the ``Layout-Mask-Resist Image-After Development Image (ADI)'' pipeline as a decision-driven multi-step evolution system. LithoDreamer captures feature changes between adjacent states to model stage-specific physics-informed latent spaces, in which it controls process intervention exploration and drives subsequent state transitions. To achieve interpretable intervention optimization without continuous supervision, we propose a contrastive variational optimization paradigm that contrasts the latent differences between intervention paths with variational evolution constraints, guiding the model to generate evolutions consistent with real lithography physics. Experiments show LithoDreamer achieves state-of-the-art performance in forward evolution and inverse planning. Our lithography dataset is publicly available at GitHub (this https URL).

---


### 70. [Depth-Semantic Alignment and Affinity-Guided Fusion for Structured Radar Point Cloud Generation](https://arxiv.org/abs/2606.26743)

**<font color=#1a73e8>作者：</font>** Amjad Hussain, Xin Qiu, Fuyuan Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point clouds are an important carrier of three-dimensional spatial information, and their quality directly affects the performance of downstream perception tasks such as object detection and tracking. However, millimeter-wave radar point clouds are typically sparse, noisy, and structurally incomplete. To address these limitations, this paper proposes a multimodal point cloud generation method based on vision-radar fusion. The proposed method leverages image semantic information to impose structural constraints and achieve spatial alignment for radar point clouds, while incorporating a sparse completion strategy to enhance point density and recover missing structures. The generated point clouds are further evaluated in object detection and tracking tasks. Experimental results demonstrate that the proposed method effectively improves point cloud quality and enhances the detection accuracy and robustness of perception models in complex environments, providing a practical solution for multisensor point cloud generation and intelligent perception systems.

---


### 71. [EGG: An Expert-Guided Agent Framework for Kernel Generation](https://arxiv.org/abs/2606.26758)

**<font color=#1a73e8>作者：</font>** Yaochen Han, Ke Fan, Hongxu Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-performance GPU kernels are critical for reducing the exponentially growing computational costs of large language models (LLMs), but their development heavily relies on manual tuning by domain experts. While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. This limitation primarily arises from the lack of domain-specific optimization guidance, hindering effective exploration of the optimization space. We propose EGG, an Expert-Guided Agent Framework for Kernel Generation, which incorporates expert optimization principles to guide LLMs' decisions. Inspired by expert workflows, we decompose kernel generation into two hierarchical stages: 1) algorithmic structure design, which establishes a high-quality computational structure foundation; 2) hardware-specific tuning, which performs targeted adjustments through parallel mapping, tensor tiling, and memory optimization. This staged decomposition defines explicit optimization objectives, structuring the design space to achieve progressive refinement. To this end, a stage-aware multi-agent collaboration mechanism is designed for inter and intra-stage context management, ensuring stable optimization trajectories. Experiments on KernelBench and real-world workloads show that EGG achieves a 2.13x average speedup over PyTorch, outperforming existing agent-based and RL-based approaches.

---


### 72. [Reproducibility Study of "AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models"](https://arxiv.org/abs/2606.26783)

**<font color=#1a73e8>作者：</font>** Ananth K S, Arya Hariharan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fang et al. (2025) introduced a null-space constrained projection, named AlphaEdit, for locate-then-edit knowledge editing methods, theoretically guaranteeing that edits do not disrupt previously preserved knowledge, and reports substantial gains over existing editing methods on LLaMA3, GPT2-XL, and GPT-J. In this work, we present a reproducibility study of AlphaEdit, reproducing its reported results under the original experimental setup and extending the evaluation along three axes: new model architectures, additional downstream benchmarks, and substantially longer sequential editing horizons. We successfully reproduce AlphaEdit's reported metrics across the original models, though we identify a discrepancy in the reported fluency and consistency metric. Extending AlphaEdit to newer model families, we find that its advantage does not generalize uniformly, which we trace to architectural assumptions in the locate-then-edit paradigm that are violated by these newer models. We further stress-test AlphaEdit's central sequential-editing claim by extending the number of edits well beyond those evaluated in the original paper, and find that performance, which is stable at the originally reported scale, degrades as edits reach a much higher count, indicating that the null-space projection's protection against catastrophic forgetting is bounded rather than unconditional. Finally, we extend evaluation of edited models on three extra benchmarks, namely, BoolQ, HellaSwag, and XSTest, and we find that large-scale sequential editing degrades both general downstream task competence and safety-relevant refusal behavior. Our results confirm that AlphaEdit performs as reported within its original scope, while showing that its core theoretical guarantees are sensitive to model architecture and editing scale in ways that have practical implications for its deployment.

---


### 73. [AIGP: An LLM-Based Framework for Long-Term Value Alignment in E-Commerce Pricing](https://arxiv.org/abs/2606.26787)

**<font color=#1a73e8>作者：</font>** Chennan Ma, Yanning Zhang, Siqi Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional dynamic pricing models in large-scale e-commerce suffer from limited interpretability, poor utilization of unstructured information, and misalignment with long-term business objectives such as cumulative Gross Merchandise Value (GMV), Return on Investment (ROI) and milestone achievement. We propose AIGP, a novel framework that leverages a Large Language Model (LLM) prompted with domain knowledge, structured data and textual context to make interpretable, knowledge-aware pricing decisions. For efficient deployment while maintaining high-quality outputs, we employ supervised fine-tuning for knowledge distillation. Central to AIGP is the Long-Term Value Estimator (LTVE), trained via offline reinforcement learning on historical data, which serves as a reward model to score candidate pricing actions and select preference pairs for Direct Preference Optimization (DPO), thereby aligning the pricing policy with long-term business objectives. Extensive offline evaluations and large-scale online A/B tests on Tao Factory demonstrate that AIGP achieves significant improvements: +13.21% in GMV, +7.59% in ROI, and +8.20% in milestone achievement rate over 14 days compared to the production baseline, while simultaneously providing interpretable and transparent pricing rationales.

---


### 74. [OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.26790)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Jinyang Wu, Zhengxi Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Outcome-based reinforcement learning provides a stable optimization backbone for language agents, but its sparse trajectory-level rewards provide little guidance on which intermediate decisions should be reinforced or suppressed. On-policy self-distillation offers dense token-level supervision, yet existing skill-conditioned variants often rely on external skill memories or retrieved privileged context, which are costly to maintain and can be mismatched with the state distribution induced by the current policy in multi-turn interaction. We propose \textbf{OPID} (\textbf{O}n-\textbf{P}olicy Sk\textbf{i}ll \textbf{D}istillation), a framework that extracts skill supervision directly from completed on-policy trajectories. OPID represents trajectory hindsight as hierarchical skills: episode-level skills capture global workflows or failure-avoidance rules, while step-level skills capture local decision knowledge at critical timesteps. A critical-first routing mechanism uses step-level skills when critical decisions are identified and falls back to episode-level skills as default guidance otherwise. The selected skill is injected into the interaction history, allowing the old policy to re-score the same sampled response under both original and skill-augmented contexts. The resulting log-probability shift yields a token-level self-distillation advantage, which is combined with the outcome advantage for policy optimization. OPID thus preserves RL as the primary training objective while introducing dense, distribution-matched hindsight supervision. Experiments on ALFWorld, WebShop and Search-based QA demonstrate that OPID generally improves agent performance, sample efficiency, and robustness over outcome-only RL and existing skill-distillation baselines. Our code is available at this https URL.

---


### 75. [ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP](https://arxiv.org/abs/2606.26794)

**<font color=#1a73e8>作者：</font>** Sicheng Zhang, Muzammal Naseer, Binzhu Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visually grounded commonsense inference and compositional reasoning, it remains unclear whether CLIP-style encoders can support such reasoning without architectural changes. To address this, we present ReasonCLIP-58M, a continual pretraining framework that integrates large-scale reasoning supervision into CLIP-style models through our two-stage strategy, which progressively integrates reasoning signals while preserving descriptive alignment, followed by category-structured reasoning supervision. To support this framework, we construct two complementary datasets and a benchmark: ReasonLite-42M, with open-form, visually verifiable reasoning captions; ReasonPro-16M, with category-specific reasoning supervision; and RCLIP-Bench for diagnostic evaluation of visually grounded reasoning. We train a family of ReasonCLIP that improves visually grounded commonsense and compositional reasoning while also enhancing zero-shot retrieval performance. As a drop-in visual encoder for multimodal large language models such as LLaVA-NeXT, ReasonCLIP delivers consistent gains without additional inference cost, demonstrating that structured reasoning supervision enhances the expressive capacity of CLIP-style visual representations. All datasets, models, and training code are available at this https URL.

---


### 76. [Reasoning Quality Emerges Early: Data Curation for Reasoning Models](https://arxiv.org/abs/2606.26797)

**<font color=#1a73e8>作者：</font>** Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) on a small, high-quality set of long reasoning traces is an effective approach for eliciting strong reasoning capabilities in Large Language Models (LLMs). However, existing methods for curating high-quality SFT data rely heavily on strong reasoning models to filter examples based on diversity and difficulty, making the curation process costly while often yielding suboptimal data quality. In this work, we show that diverse and challenging reasoning examples can be identified using only the initial reasoning tokens. Specifically, we demonstrate that difficult problems can be reliably detected based on the loss of the first 100 reasoning tokens evaluated at a randomly perturbed checkpoint of the pretrained model. We further show that examples exhibiting similar loss patterns over their first 1k reasoning tokens across a small number of perturbed checkpoints extrapolating along the fine-tuning trajectory provably induce similar gradients. We validate our approach through extensive experiments on fine-tuning Qwen2.5-7B and Llama3.1-8B models on the M23K medical reasoning and OpenThoughts-Math datasets. Our method outperforms existing baselines by up to 1.7% while being 91% more token efficient.

---


### 77. [KARLA: Knowledge-base Augmented Retrieval for Language Models](https://arxiv.org/abs/2606.26807)

**<font color=#1a73e8>作者：</font>** Francois Crespin, Fabian M. Suchanek, Nils Holzenberger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a new method that allows an LLM to automatically pull in factual knowledge from a knowledge base during token generation. This means that (1)~factual knowledge in the LLM output can be updated without retraining the LLM, (2)~facts in the LLM output can be traced to the knowledge base for transparency and explainability, and (3)~smaller models can achieve the same factual accuracy as larger models. Our core idea is to train the model to produce special tokens that trigger a query to the knowledge base. Our experiments show that our method improves factual grounding in both short and long-form generation, and allows factual revisions to take effect through KB edits rather than parameter updates.

---


### 78. [FBK's Long-form SpeechLLMs for IWSLT 2026 Instruction Following](https://arxiv.org/abs/2606.26819)

**<font color=#1a73e8>作者：</font>** Zhihang Xie, Marco Gaido, Sara Papi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our submission to the IWSLT 2026 Instruction Following shared task. SpeechLLMs are developed for both short-form and long-form speech instruction following under constrained settings. For the short track, strong performance is achieved on MCIF, with a SIFS score of 2.0708. For the long track, three speech segmentation methods are explored, and the HIFS score is introduced to account for unstable long-form generation. Experimental results show that fixed 30-second segmentation provides the most robust long-form performance, achieving the highest HIFS score of 2.0663. Further analysis shows that hallucination mainly manifests as repetitive insertions in generated outputs, substantially affecting ASR and SSUM, while short-form capabilities are largely retained after long-form extension.

---


### 79. [LCAi: Life Cycle Assessment with big data fusion and retrieval-augmented generation-assisted interpretation](https://arxiv.org/abs/2606.26857)

**<font color=#1a73e8>作者：</font>** Georgios Tsironis, Juan D. Medrano-Garcia, Gonzalo Guillen-Gosalbez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The interpretation phase of life cycle assessment often lacks structured mechanisms for translating quantified improvement opportunities addressing environmental hotspots into actionable strategic pathways under technological, social, and policy uncertainty. To overcome this limitation, this study introduces a perspective-conditioned retrieval-augmented generation framework for LCA interpretation, where a multi-perspective retrieval and controlled synthesis is incorporated in the artificial intelligence (AI)-assisted LCA. To operationalise large language models in LCA interpretation, a perspective fusion RAG architecture was developed, covering academic, industry, public discourse, and European union (EU) funding datasets. Our approach comprises three steps: (1) a scenario anchor defining system boundaries and decarbonization targets, (2) a set of perspective-specific micro-queries with constrained retrieval, and (3) a neutral synthesis step integrating only ledger-stored outputs without further retrieval. The framework is demonstrated through a hydrogen-enabled diesel reduction use case in an Italian apple production facility using GPT-5 nano as the reasoning model. Overall, the structured retrieval and constrained synthesis are designed to mitigate the risk of hallucination while preserving cross-domain diversity. The approach presented can support more disciplined translation of impact results into strategic pathways and opens up new avenues for the use of advanced AI tools in LCA studies, particularly those focused on technologies that could be deployed at scale. This proof-of-concept demonstrates how AI-assisted, evidence-grounded interpretation can support implementation-oriented decision-making beyond conventional LCA studies.

---


### 80. [Cascaded Multi-Granularity Pruning for On-Device LLM Inference in Industrial IoT](https://arxiv.org/abs/2606.26861)

**<font color=#1a73e8>作者：</font>** Jinghan Wang, Yanjun Chen, Wei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) on Industrial Internet of Things (IIoT) edge devices demands extreme compression, yet existing structured pruning methods collapse at high compression ratios due to one-shot importance estimation, and their cross-architecture behavior remains unpredictable. This article presents a cascaded multi-granularity pruning framework that removes layers, attention heads, and feed-forward channels in coarse-to-fine order, with lightweight low-rank recovery between stages to re-estimate component importance. An information-theoretic analysis motivates this ordering, and the Structural Independence Assumption (SIA) is formalized as a checkable condition predicting whether per-component pruning criteria are reliable for a given architecture: Multi-Head Attention (MHA)+GELU designs satisfy the SIA, whereas Grouped Query Attention (GQA)+SwiGLU designs violate it. On bearing fault diagnosis spanning 88M to 6.25B-parameter models, the framework extends achievable compression to 13.8 times on MHA+GELU architectures with 83.82% accuracy (+3.70 percentage points (pp) over the strongest baseline), while exposing a ~74pp accuracy collapse on GQA+SwiGLU architectures that violate the SIA. Deployed on an industrial slewing bearing fault diagnosis platform with NVIDIA DGX Spark, compressed models reduce inference latency by up to 67.2% and peak memory by 62.5%, demonstrating viability for IIoT edge inference.

---


### 81. [TAVR-VLM: Risk-Conditioned Causal Grounding for Hallucination-Resistant Report Generation](https://arxiv.org/abs/2606.26874)

**<font color=#1a73e8>作者：</font>** Zhixiang Lu, Xiwei Liu, Sifan Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transcatheter Aortic Valve Replacement (TAVR) planning requires meticulous multimodal reasoning. However, adapting Multimodal Large Language Models (MLLMs) to this high-stakes domain is severely impeded by diagnostic hallucinations, where generated text lacks anatomical grounding. To address this, TAVR-VLM is introduced: a novel framework featuring Risk-Conditioned Causal Grounding Attention (R-CGA) that instantiates a model-internal ``Risk $\rightarrow$ Region $\rightarrow$ Word'' structural grounding pathway. R-CGA compresses multimodal inputs into a causal risk bottleneck, purifying dense visual features into a global risk mask. During autoregressive generation, a support-projected causal consistency objective constrains token-level grounding within the risk-defined support mask. Evaluated on $\text{M}^3\text{TAVR}$, a comprehensive 1,482-patient cohort, TAVR-VLM establishes a new state-of-the-art. It achieves an AUROC of 0.896, boosts CIDEr to 0.936, and drastically reduces the hallucination rate to 8.1\%, thereby improving interpretability for evidence-based surgical AI.

---


### 82. [Information-Aware KV Cache Compression for Long Reasoning](https://arxiv.org/abs/2606.26875)

**<font color=#1a73e8>作者：</font>** Jushi Kai, Zhuiri Xiao, Alexandra Birch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning capability has advanced rapidly in large language models (LLMs), leading to an increasing size of key-value (KV) cache in both prefilling and decoding stages. Existing KV cache compression methods mainly rely on attention weights to estimate token importance. While attention effectively captures contextual relevance, it overlooks complementary information-theoretic signals related to predictive uncertainty and token informativeness. In this paper, we revisit token importance from a forward-looking perspective and introduce \textit{Forward Influence}, a metric that measures how compressed tokens affect future contexts. Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. Based on the observation, we propose \textbf{InfoKV}, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. It combines token-level predictive uncertainty with layer-wise representation evolution and integrates the resulting entropy scores with attention scores during reasoning. Experiments on long-context reasoning benchmarks with Llama-3.1, Llama-3.2, and DeepSeek-R1 demonstrate that InfoKV consistently outperforms existing attention-based KV compression methods in both long prefilling and decoding scenarios.

---


### 83. [A Pipeline for Generating Longitudinal Synthetic Clinical Notes Using Large Language Models](https://arxiv.org/abs/2606.26879)

**<font color=#1a73e8>作者：</font>** William Poulett  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic data is increasingly used to enable the development and evaluation of AI systems in domains where access to real-world data is restricted. In healthcare, clinical documentation presents particular challenges due to its sensitivity. This work introduces a synthetic clinical notes pipeline and dataset designed to support the development of clinical AI tools while avoiding the privacy risks associated with real patient data. The dataset is generated using a modular pipeline that combines structured patient generation, semi-structured patient journey simulation, and unstructured clinical note generation using large language models. The pipeline is designed to prioritise internal consistency across longitudinal patient records, while also capturing variation in writing style, note structure, and clinical detail. Additional mechanisms, including LLM-based validation and augmentation steps, are used to improve faithfulness, realism, and diversity of the generated notes. We release a dataset of 70 synthetic patients, each associated with 20-50 clinical notes spanning a full hospital journey. The dataset is provided at multiple levels of validation, enabling users to balance realism and scalability depending on their use case. This dataset supports the development, testing, and evaluation of clinical AI systems, including summarisation tools, coding models, and decision support systems, without reliance on real patient data.

---


### 84. [Heterogeneous Neural Predictivity from Language Models During Naturalistic Comprehension](https://arxiv.org/abs/2606.26880)

**<font color=#1a73e8>作者：</font>** Xiao Jia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model representations provide structured, high-dimensional annotations of naturalistic language stimuli and can serve as informative neural predictors during comprehension. We analyzed locked derived data from Brain Treebank, MEG-MASC, and Podcast ECoG with eight frozen language models, blocked encoding models, and matched temporal, nuisance, and representation-capacity controls. Positive held-out prediction and gains over low-level baselines were widespread in source-level summaries. Across Brain Treebank and Podcast ECoG, 67 of 432 evaluable rows met a controlled predictive-only criterion, and model-side feature ablations changed prediction scores in most evaluable source rows. Brain-derived, timing-linked, acoustic, and implanted-signal controls confirmed component-level sensitivity of the analysis pipeline. These findings show that language-model-derived quantities can annotate neural activity during natural speech and text comprehension. Participant-level matched-control advantages were localized rather than uniform, response-profile and feature-specificity contrasts bounded representational or computational interpretations, and complete co-indexed integrated interpretation will require future jointly indexed coverage. Together, the analyses identify language-model features as useful neural predictors and separate predictive usefulness from claims about shared neural organization or language-processing computations.

---


### 85. [MedSWFlow: An Open-Source LLM Workflow for Drafting Medical Social Work Case Plans](https://arxiv.org/abs/2606.26884)

**<font color=#1a73e8>作者：</font>** Yulin Mao, Shiyu Li, Shuping Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present MedSWFlow, an open-source, model-agnostic LLM workflow for drafting medical social work case plans. The framework translates professional case-planning tasks into six stages: assessment, problem analysis, goal setting, intervention planning, risk anticipation, and planned effect evaluation. Drawing on established social work and behavioral frameworks, MedSWFlow standardizes case inputs, builds structured case profiles, and generates reviewable assessment forms and service plans through staged prompting. The system is released as an open-source research framework for reproducible case-plan generation across LLM providers. Outputs are intended as practitioner-reviewed drafts rather than final service decisions. Source code: this https URL.

---


### 86. [Modeling Local, Global, and Cross-Modal Context in Multimodal 3D MRI](https://arxiv.org/abs/2606.26894)

**<font color=#1a73e8>作者：</font>** Minh Duc Do, Tillmann Rheude, Noel Kronenberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain MRI poses a fundamental challenge for machine learning: models must learn from high-dimensional 3D data spanning multiple co-registered modalities, despite the limited sample sizes typical of neuroimaging studies relative to the diversity in anatomy, pathology, and acquisition conditions. While multimodal imaging provides complementary information critical for clinical interpretation, effectively integrating these signals remains difficult. We propose Multimodal Intra- and Cross-Context Vision Transformer (MICViT), a 3D vision transformer that explicitly models both modality-specific representations and cross-modal interactions across local and global contexts. Concretely, MICViT combines four attention mechanisms: modality-specific local and global attention for intra-modal feature learning, and cross-modal local and global attention to capture interactions between modalities. We evaluate MICViT on brain age prediction across three heterogeneous datasets (UK Biobank, n=41,404; SOOP, n=1,062; Cam-CAN, n=613) using multiple MRI modalities (e.g. T1, FLAIR, DWI, SWI). MICViT consistently outperforms state-of-the-art CNN and transformer baselines in 3D settings. Notably, it benefits more strongly from multimodal inputs, yielding larger performance gains as additional modalities are incorporated. These results demonstrate that explicitly modeling intra- and cross-modal interactions is key to unlocking the full potential of multimodal brain MRI, highlighting a promising direction for representation learning in neuroimaging.

---


### 87. [Confidence-Aware Tool Orchestration for Robust Video Understanding](https://arxiv.org/abs/2606.26904)

**<font color=#1a73e8>作者：</font>** Yangfan He, Yujin Choi, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning language models implicitly assume that every input frame is equally reliable. This leads to what we term the Blind Trust Problem: under realistic perturbations such as motion blur, glare, or occlusion, frontier video reasoning models can suffer 15-30%p accuracy drops on real-world embodied benchmarks, while remaining unaware that their visual evidence has been degraded. To address this challenge, we propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. Robust-TO organizes heterogeneous visual perception tools under a unified evidence interface. Each tool receives a sub-query derived from the original question and a set of trustworthy frames selected by the reliability-relevance score. It returns evidence in a shared format: a concrete prediction (e.g., a bounding box, motion trajectory, recognized text, or action label), temporal grounding, and a calibrated reliability score. During reasoning, these calibrated scores guide evidence weighting in a three-tier synthesis process (high/medium/low) and define a confidence-cost GRPO reward that jointly optimizes correctness, evidence reliability, and efficiency. On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%). Under five realistic corruption types, Robust-TO maintains 54.3% average accuracy, 5.8%p above the strongest open-source baseline, while exhibiting the smallest clean-to-corrupted accuracy drop among all compared methods.

---


### 88. [Qwen-Image-Agent: Bridging the Context Gap in Real-World Image Generation](https://arxiv.org/abs/2606.26907)

**<font color=#1a73e8>作者：</font>** Zekai Zhang, Jiahao Li, Jie Zhang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While text-to-image (T2I) models have achieved remarkable progress, they struggle with real-world requests that are often underspecified, implicit, or dependent on up-to-date knowledge. We identify this challenge as the Context Gap: the mismatch between the user context and the sufficient generation context for T2I models. To bridge this gap, we propose Qwen-Image-Agent, a unified agentic framework that integrates plan, reason, search, memory and feedback in a context-centric manner. Qwen-Image-Agent treats user input as partial context and progressively constructs the generation context through Context-Aware Planning and Context Grounding. Specifically, Context-Aware Planning identifies missing context and plans how it should be acquired and used, while Context Grounding gathers this context from reason, search, memory, and feedback. To evaluate agentic image generation, we further introduce Image Agent Bench (IA-Bench), a benchmark covering four core image agent capabilities: Plan, Reason, Search, and Memory. Experiments on IA-Bench, Mindbench and WISE-Verified show that Qwen-Image-Agent outperforms strong baselines and achieves state-of-the-art performance.

---


### 89. [PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation](https://arxiv.org/abs/2606.26916)

**<font color=#1a73e8>作者：</font>** Kexu Cheng, Zicheng Liu, Mingju Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing physically aware video generation models remains a significant challenge due to the difficulty in capturing diverse physical phenomena, such as thermal dynamics, mechanics, and optics. In this work, we introduce PhysRAG, a novel pipeline that enhances physical awareness in video generation through Retrieval-Augmented Generation (RAG). To address the issue of limited high-quality data, we design a two-stage data filtering pipeline based on the WISA-80K dataset, resulting in a curated set of 7K high-quality videos for training. Furthermore, we construct a physical video database and develop a mechanism to inject physical knowledge into a video diffusion model using learnable queries. Our method achieves state-of-the-art performance in both visual quality and physical rule compliance, surpassing existing models in benchmarks such as PhyGenBench and VBench. We conduct extensive ablation studies to validate the effectiveness of our key components, including the data filtering pipeline, RAG mechanism, and method for physical information extraction. To facilitate future research, our code, data, and models are prepared for release at this https URL.

---


### 90. [GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning](https://arxiv.org/abs/2606.26917)

**<font color=#1a73e8>作者：</font>** Ting Zhou, Zhenqing Ling, Yiyang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning is widely used to align large language models (LLMs) with reward signals, yet training can be unstable under noisy or misspecified rewards. We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. We propose geoalign, a lightweight plug-in for rollout curation in iterative policy optimization. Geoalign (i) forms within-prompt preference pairs, (ii) learns an online projector on per-rollout hidden states to concentrate reward-ordered displacement directions, and (iii) detects directionally inconsistent rollouts via their angular deviation from a batch consensus prototype and rectifies them with within-prompt stable alternatives. Geoalign is forward-pass only and adds negligible overhead. Across dialogue alignment with a learned reward model and mathematical reasoning with binary verified rewards, Geoalign improves final performance and reduces training oscillation, outperforming PF-PPO, PAR, PODS, and Seed-GRPO. These results suggest latent directional consensus as an effective reliability signal for online LLM RL.

---


### 91. [Where Do CoT Training Gains Land in LLM based Agents?](https://arxiv.org/abs/2606.26935)

**<font color=#1a73e8>作者：</font>** Jingyu Liu, Zhiwen Wang, Yuxin Jing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? We study this question by comparing \emph{prompt actions} (predicting action without CoT) with CoT actions (predicting action with CoT). Across checkpoints, prompt-action quality improves substantially. While interacting with the environment, the relative advantage of CoT actions over prompt actions remains similar, showing that CoT training does not widen the advantage of CoT reasoning, and it helps to improve the quality of prompt actions. We further find that later checkpoints are less likely to revise the action in response to CoT, suggesting greater reliance on the prompt. Motivated by these patterns, we selectively mask action-token supervision on a fraction of training examples. This intervention improves out-of-domain generalization.

---


### 92. [Continuous Behavioral Synthesis for Adaptive Health Dashboards: An LLM-Mediated Architecture Integrating Explicit Preference, Spatial Reorganization, and Attention Allocation Signals](https://arxiv.org/abs/2606.26937)

**<font color=#1a73e8>作者：</font>** Tiziano Santilli, Mina Alipour, Mahyar T. Moghaddam  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The engineering of adaptive user interfaces has traditionally relied on either rule-based systems encoding designer intuitions about user needs or machine learning approaches requiring substantial historical data before achieving effective personalization. We present a technical architecture that leverages Large Language Models as behavioral synthesis engines to enable immediate adaptation from sparse, heterogeneous user signals. Our system integrates three distinct behavioral channels, i) explicit micro-feedback on individual interface elements, ii) spatial priority inferred from manual widget reorganization through drag-and-drop interaction, iii) and attentional investment measured through dwell time during hover events, within a structured prompt engineering framework that continuously regenerates dashboard layouts while maintaining explanatory coherence. The architecture addresses the technical challenge of translating low-level interaction patterns into high-level design decisions through a layered prompt construction methodology that separates temporal context determination, behavioral signal extraction, explicit preference enforcement, and user profile synthesis. The approach combines manually specified behavioral interpretations and temporal heuristics with LLM-mediated synthesis, enabling the reconciliation of multiple simultaneous signals that would be difficult to encode through explicit rules alone. We demonstrate the system through an instantiation in the personal health monitoring domain, including an analytical evaluation of adaptation behavior across multiple scenarios and a working implementation managing fourteen distinct health metrics across seven widget visualization modalities. The evaluation compares profile-driven initialization, multi-signal behavioral adaptation, and presents the resulting interfaces through representative post-adaptation screenshots.

---


### 93. [Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion MoE](https://arxiv.org/abs/2606.26938)

**<font color=#1a73e8>作者：</font>** Haoyou Deng, Keyu Yan, Chaojie Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have emerged as a powerful paradigm for scaling diffusion models in visual generation. Recent advancements have focused on adaptively allocating computational resources across diverse tokens to improve efficiency and performance. However, we identify a routing assignment problem in existing diffusion MoE frameworks: the router fails to accurately allocate more computational resources to salient tokens. Our analysis attributes this failure to the router's reliance on noise-corrupted latent features throughout the denoising process. Such stochastic noise obscures the critical structural and textural information, thereby preventing the router from effectively distinguishing salient tokens. To address this, we propose SharpMoE, a post-training framework with a saliency-harnessing accurate routing mechanism, which utilizes clean latent features as a noise-free guidance signal for routing. By bypassing the noise-distorted inputs, SharpMoE provides the router with clear saliency guidance, enabling the identification of salient tokens even in high-noise stages. Furthermore, we introduce a trajectory routing loss to constrain the compute allocation throughout the multi-step denoising trajectory, ensuring precise resource allocation along the generation rollout. Extensive experiments demonstrate that SharpMoE serves as a versatile, plug-and-play solution that further enhances the pretrained, converged MoE models, achieving state-of-the-art performance in visual generation.

---


### 94. [TraMP-LLaMA: Generative Interpretability with Decoupled Instruction Tuning for Facial Expression Quality Assessment](https://arxiv.org/abs/2606.26942)

**<font color=#1a73e8>作者：</font>** Shuchao Duan, Alan Whone, Hossein Rahmani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing facial expression quality assessment (FEQA) methods typically produce only a severity score, without explicitly communicating the observable facial motion evidence that supports the prediction. This limits interpretability and makes it difficult to inspect the basis of model outputs in Parkinson's disease assessment. To address this gap, we propose TraMP-LLaMA, a unified multimodal framework that jointly predicts severity scores and generates structured textual reports from facial motion cues. The framework integrates RGB appearance and landmark trajectory cues, and adopts a decoupled instruction-tuning strategy to reduce task interference between severity prediction and language generation. To support this task, we further extend the PFED5 dataset with expert-guided textual motion descriptions and construct PFED5-plus. Experiments on PFED5-plus show that TraMP-LLaMA outperforms competitive video-language baselines in report generation and achieves the best severity prediction performance among the compared methods under joint multi-expression training, improving Spearman's rank correlation by at least 4.39 percent over all competing methods. The text annotations and code are available at this https URL.

---


### 95. [Einstein World Models](https://arxiv.org/abs/2606.26969)

**<font color=#1a73e8>作者：</font>** Munachiso Samuel Nwadike, Zangir Iklassov, Ali Mekky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does intelligence require the ability to reason about phenomena beyond direct experience? It is natural to suspect that some complex thought cannot be captured through language alone. However, of particular concern to this work, is whether visualising counterfactual events can complement language as a mechanism for complex thought. We ask whether LLMs can be trained to utilise such visualisation mechanisms, in a way that benefits their reasoning abilities. Motivated by this question, we propose Einstein World Models. EWMs are a blueprint for LLM-based reasoning systems that place visual-temporal rollouts inside the reasoning trace, allowing them to reason in ways that text alone may not support well. In an EWM, the LLM calls a world-module (not to be confused with a world model), to produce short rollouts of scenes under consideration. The returned rollout is treated not as the answer, but as an inspectable hypothesis that can support later reasoning. Einstein World Models extend the capability of LLMs for tool calling (such as web search or code execution), into the domain of visual thought experiments.

---


### 96. [Auditing Framing-Sensitive Behavioral Instability in Large Language Models for Mental Health Interactions](https://arxiv.org/abs/2606.26982)

**<font color=#1a73e8>作者：</font>** Abla Bedoui, Ashley L. Greene, Mohammed Cherkaoui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being integrated into mental health support tools and other psychologically sensitive conversational applications. In such settings, behavioral stability and consistency are important for trustworthy human-AI interaction. However, semantically similar concerns can be presented through different contextual framings, potentially eliciting different model responses. Such framing-sensitive variability may challenge user expectations regarding system behavior and complicate the assessment of AI reliability. While prior studies have primarily examined such effects at the behavioral level, less is known about how framing-related variation is reflected in the internal representations of aligned language models. In this work, we investigate these effects using controlled matched prompts spanning multiple contextual framing conditions across several instruction-tuned model families. Across architectures, framing systematically alters interpretive response tendencies. Layer-wise probing analyses show that behavior-associated information remains decodable throughout transformer depth, with architecture-dependent variation in decoding strength. Moreover, held-out framing probes remained consistently above chance across architectures despite strong lexical baselines. Activation steering experiments further suggest that framing-associated representational directions can partially modulate downstream behavioral outcomes. Finally, these findings indicate that robustness to contextual variation may represent an important consideration when evaluating the consistency and trustworthiness of conversational AI systems deployed in mental-health-oriented interactions.

---


### 97. [Unison: Benchmarking Unified Multimodal Models via Synergistic Understanding and Generation](https://arxiv.org/abs/2606.26984)

**<font color=#1a73e8>作者：</font>** Jinyu Liu, Xincheng Shuai, Henghui Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models capable of both understanding and generation have achieved remarkable strides. However, despite their unified designs, existing evaluations typically assess understanding and generation capabilities in isolation, overlooking the synergy between comprehension and generation. To bridge this gap, we introduce Unison, a comprehensive benchmark comprising 2,169 high-quality unified task samples, designed to evaluate joint understanding and generation in unified multimodal models. Unison offers three key strengths: 1) Comprehensive Dimensions: Unison encompasses internal consistency, understanding-guided generation, generation-guided understanding, and mutual enhancement to enable holistic evaluation. 2) Diagnostic Evaluation: it provides both unified and decoupled tracks for understanding and generation, allowing fine-grained attribution of failure modes and quantitative analysis of the gains from unified modeling. 3) Human Alignment: we also introduce Unison-Judge, an evaluation model well aligned with human judgments to ensure reliable assessment. Based on systematic evaluations of state-of-the-art models on Unison, we uncover critical limitations in current unified multimodal systems and highlight promising directions for future research. Codes, Unison and Unison-Judge are publicly available at this https URL.

---


### 98. [ReaORE: Reasoning-Guided Progressive Open Relation Extraction Empowered by Large Reasoning Models](https://arxiv.org/abs/2606.26986)

**<font color=#1a73e8>作者：</font>** Xin Lin, Liang Zhang, Guoqi Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open Relation Extraction (OpenRE) requires a model to extract unseen relations between head and tail entities from unstructured text for real-world applications. The core challenge of OpenRE lies in achieving reliable generalization to unseen relation types. Current OpenRE approaches either employ clustering techniques, which cannot generate relation labels and suffer from poor generalization, or rely on direct relation label generation via Large Language Models (LLMs), which lack sufficient discriminative capacity to distinguish easily confused relations. To address these limitations, we propose Reasoning-guided progressive OpenRE (ReaORE), a framework for performing relation extraction through coarse-to-fine relation reasoning. Specifically, ReaORE consists of two key stages: (i) relation filtering, which reasons over multiple aspects to understand relations and instances, yielding an initial relation set, and further supplements and filters relations via embedding-based similarity to ensure the target relation is included; (ii) relation prediction, which aims to predict the target relations from the above set via fine-grained comparative reasoning to better distinguish easily confused relations. Extensive experiments on two widely used OpenRE datasets demonstrate that ReaORE outperforms existing baselines.

---


### 99. [Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs](https://arxiv.org/abs/2606.26987)

**<font color=#1a73e8>作者：</font>** Sinie van der Ben, Raphaël Baur, Yannick Metz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work identified emotion vectors in Claude Sonnet 4.5, which are internal representations that encode emotion concepts, causally influence behavior, and exhibit geometry mirroring human psychological structure. We test the generality of these findings in two open-weight models, Apertus-8B-Instruct-2509 and Gemma-4-E4B-it, extracting emotion contrast vectors across all layers, using two model-generated corpora. We recover valence geometry for both models, with peak PC1--valence correlations of $r = 0.76$ and $r = 0.83$, approaching the $r = 0.81$ reported for this http URL replication, we observe notable differences in how valence representations emerge across model depth. In Gemma-4-E4B-it, valence is strongly encoded in early layers but collapses towards later layers, whereas Apertus-8B-Instruct-2509 exhibits the opposite pattern, with valence representations absent in early layers, but emerging at mid depths. Arousal encoding, in contrast, is sensitive to the extraction corpus: both models show stronger PC2--arousal alignment with Gemma-generated stories ($r$ up to $0.45$) than Apertus-generated ones ($r \leq 0.21$), suggesting arousal-relevant cues are unevenly distributed across generated corpora. We open-source our experiment code and dataset for reproducible investigation of emotion representations across language model architectures.

---


### 100. [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/abs/2606.27009)

**<font color=#1a73e8>作者：</font>** Sahil Shrivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. We study semantic early-stopping: the loop halts when consecutive draft embeddings stop changing in meaning (cosine distance with a patience window) and the answer's measured quality stops improving. Our work makes three contributions. First, an honest theoretical footing: we prove deterministic termination and well-definedness and machine-check these claims, while treating the convergence of the distance sequence as an empirically tested conjecture rather than a (previously over-claimed) Banach contraction. Second, a judge-efficient evaluation protocol: we generate each question's full trajectory once, replay every stopping policy over the identical drafts, and cache every LLM-judge call, yielding a strictly paired efficiency-versus-quality comparison at low cost; we further separate operational tokens (charged to a policy) from evaluation tokens (a measurement instrument). Third, an empirical study on multi-hop retrieval-augmented question answering (HotpotQA). On the 60-question test split, a judge-free semantic stopper reduces operational tokens by 38% relative to max_iterations at parity quality (Delta-IS = -0.004, p = 0.81), whereas the full quality-gated variant is counter-productive because its per-round judging dominates cost. An oracle that selects the best round attains +0.115 Information Score over every practical policy (p ~ 4e-11), reframing the problem from "when to stop" (easy) to "which round is best" (open).

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-135](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
