# 🧠 大模型相关研究 | 2026年07月03日

> 本类共 **110** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-110**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-110**

---

### 101. [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117)

**<font color=#1a73e8>作者：</font>** Jiale Li, Sihan Chen, Mengyuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (VideoLLMs) have shown strong progress in video understanding, yet they still suffer from hallucinations that are inconsistent with visual evidence. Existing benchmarks mainly focus on object hallucination or coarse action perception, leaving a key video-specific problem underexplored: motion hallucination, in which models infer human motions that are absent from the video. We present MoHallBench, a benchmark for diagnosing motion hallucination in VideoLLMs. MoHallBench systematically evaluates three major sources of hallucination: co-occurrence priors, sequential inference, and similarity confusion. It contains 11,306 video clips and 40,493 question-answer pairs, covering binary-choice, multiple-choice, and generative settings. We further introduce a bi-directional questioning protocol with bias-aware metrics to reduce affirmation bias in binary evaluation. Experiments on ten recent open-source VideoLLMs reveal a clear decoupling between action recognition and hallucination resistance, as models that perform well on positive action recognition often fail on adversarial negatives. Among all settings, sequential inference hallucination is the most severe, showing that current models tend to over-infer expected outcomes from partial motion cues. Our analyses further confirm that stronger priors and finer-grained similarity substantially amplify hallucination. We hope MoHallBench can facilitate future evaluation and mitigation of motion hallucination in VideoLLMs.

---


### 102. [ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces](https://arxiv.org/abs/2607.01125)

**<font color=#1a73e8>作者：</font>** Xun Dong, Yibo Xu, Naigang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization enables fine-tuning large language models when backpropagation is unavailable or memory-prohibitive, but existing methods often perturb full model weights or randomly constructed low-dimensional subspaces, yielding high-variance estimates and limited performance. We propose ZO-Act, an activation-informed ZO fine-tuning method that restricts perturbations to a fixed low-rank subspace derived from input activations. For each linear layer, ZO-Act computes a small activation basis once at initialization and optimizes only lightweight coefficient matrices using forward-only loss evaluations. This reduces the effective perturbation dimension, exposes explicit trainable variables compatible with momentum-based optimizers such as Adam, and naturally supports quantized LLM fine-tuning by keeping low-bit weights frozen. We analyze ZO-Act as zeroth-order optimization over a restricted coefficient space and show that perturbing the low-dimensional coefficients reduces both the variance-dependent convergence term and the finite-difference error of the ZO estimator, at the cost of a controlled subspace approximation bias that is mitigated by the low-rank structure of LLM activations and gradients. Experiments on Llama-3-8B, OPT-13B, and INT4 Llama-3-8B show consistent gains over strong ZO fine-tuning baselines across language understanding, question answering, and commonsense reasoning.

---


### 103. [$\text{Log}_\text{b}$Quant: Quantizing Language Models in Logarithmic Space](https://arxiv.org/abs/2607.01127)

**<font color=#1a73e8>作者：</font>** Jeremias Bohn, Tizian Dippold, Mahdi Koubaa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization has become an invaluable tool to reduce memory requirements and inference speed of modern language models, in particular to make them available for consumer setups and edge devices. While previous work has primarily focused on uniform quantization codebooks, such approaches are prone to suboptimal representations due to low-frequency high-magnitude weights. We introduce Log$_\text{b}$Quant, a novel logarithmic quantization approach with adjustable bases, to adapt to common parameter distributions. We show that our method exhibits superior performance at 4-bit precision on several performance benchmarks compared to asymmetric linear quantization at tensor-wise granularity, while achieving moderate speedup and high memory savings, making it suitable for private use on consumer-grade GPUs.

---


### 104. [Autonomous Scientific Discovery via Iterative Meta-Reflection](https://arxiv.org/abs/2607.01131)

**<font color=#1a73e8>作者：</font>** Bingchen Zhao, Sara Beery, Oisin Mac Aodha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry. Furthermore, while they generate hypotheses iteratively, they largely lack the ability to explicitly synthesize their own accumulated findings to uncover complex, interconnected phenomena. We introduce DiscoPER, an autonomous large language model-powered framework that conducts open-ended research by dynamically generating and executing code to explore datasets without pre-specified research objectives. To ensure rigorous scientific validity, every proposed discovery must pass statistical testing. To overcome the limitations of isolated search, our framework introduces a second-order reasoning mechanism that periodically analyzes its own accumulated discoveries. By treating prior discoveries as empirical data, DiscoPER identifies structural patterns, confounds, and epistemic gaps, actively redirecting hypothesis exploration toward uncharted regions of the search space. The search space is further expanded by incorporating tool use, enabling the system to explore hypotheses beyond structured metadata by seamlessly processing and extracting useful information from multimodal sources like images. Evaluated on iNatDisco, a new multimodal ecological knowledge benchmark with pattern-level ground truth obtained from peer-reviewed literature, DiscoPER recovers 8 of 9 known patterns with a 72.7% hypothesis support rate, outperforming both classical causal discovery and LLM-guided baselines. Ablations show that DiscoPER scales with more data, and confirms the benefits of second-order meta-reflection.

---


### 105. [Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity](https://arxiv.org/abs/2607.01153)

**<font color=#1a73e8>作者：</font>** Brett Reynolds  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported progress in an agentic task. Existing benchmarks often compress these distinctions into pass/fail labels, obscuring whether failures arise from capability limits, policy ambiguity, instruction conflict, scaffold failure, or unstable evaluator judgments.
This paper introduces adversarial pragmatics as a benchmark and annotation protocol for evaluating model behaviour under instruction conflict, embedded commands, quotation, scope ambiguity, deixis, indirect speech acts, and multi-turn agent transcripts. The contribution is empirical and methodological: a linguistically controlled taxonomy, an 18-item seed benchmark with validator-enforced metadata, a 54-row local seed pilot, an expert-evaluation protocol distinguishing task success, policy compliance, safety risk, refusal outcome, and evaluator confidence, and metrics for judge validity, diagnostic ambiguity, and taxonomy drift. The framework turns linguistic judgment methodology into a practical tool for validating safety evals, LLM judges, gold-set construction, prompt-injection tests, and safety documentation.

---


### 106. [Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning](https://arxiv.org/abs/2607.01191)

**<font color=#1a73e8>作者：</font>** Hongxing Li, Xiufeng Huang, Dingming Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual reasoning remains challenging for vision-language models, especially when small but critical visual cues are buried in high-resolution images. Existing approaches rely on repeated cropping or test-time visual search to introduce local evidence, but they typically do not explicitly distinguish perception from reasoning. In this paper, we propose Perceive-to-Reason (P2R), a unified framework that formulates fine-grained visual reasoning as a two-stage process: the model first localizes question-relevant evidence as a Perceiver, and then answers the question as a Reasoner based on the annotated image and cropped regions. To better align training with this decoupled formulation, we further introduce Perception-Reasoning Alternating GRPO (PRA-GRPO), a role-aware reinforcement learning strategy that alternates between perception-focused and reasoning-focused updates using only final-answer supervision. Built on top of Qwen3-VL-Instruct-2B/4B/8B, P2R consistently improves performance across model scales. In particular, P2R-4B achieves 93.2% on V-Star, 81.9% on HR-Bench-4K, and 80.5% on HR-Bench-8K, substantially outperforming its corresponding backbone. Further experiments show that the benefits of P2R extend beyond high-resolution benchmarks to broader multimodal reasoning tasks. These results suggest that explicitly decoupling perception from reasoning provides an effective framework for fine-grained visual reasoning.

---


### 107. [Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation](https://arxiv.org/abs/2607.01208)

**<font color=#1a73e8>作者：</font>** Shayan Talaei, Abhinav Chinta, Devvrit Khatri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, with the signal residing entirely in the soft logit distribution and remaining invisible to text-based inspection. However, the defender faces a fundamental asymmetry: without knowing the bias topic, no detection method can reliably surface a stealth preferential bias, regardless of whether it examines generated text, internal representations, or model weights. Here we introduce Distill to Detect (D2D), a method that surfaces hidden biases by distilling the distributional shift between a suspected model and its base into a cartridge (a KV-cache prefix adapter), concentrating the dominant divergence and amplifying the bias signal into generated text. We show that D2D successfully amplifies the hidden biases of stealth models to the extent that they can be reliably detected across multiple bias types. We also propose a theoretical framework that explains the efficacy of D2D through the lens of Fisher-weighted projection of the logit distribution shift, supported by empirical observations. By turning the capacity bottleneck of prefix-tuning adapters into a detection tool, D2D provides a practical building block for auditing hidden behaviors in deployed language models.

---


### 108. [AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/abs/2607.01224)

**<font color=#1a73e8>作者：</font>** Shengguang Wu, Hao Zhu, Yuhui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory expertise is a learned skill: knowing what to encode, when to retrieve, and how to organize knowledge--a capacity known in cognitive science as metamemory. We bring this perspective to LLMs by treating memory management as a trainable skill. We promote file-system operations to first-class memory actions alongside task actions, letting the model itself decide how to manage its memory. This memory skill improves along two axes: the structure that supports it (prompts, file schemas, action vocabulary), and the proficiency of the model exercising it. Both axes resist manual optimization: episodes in long-horizon tasks run for thousands of steps, and a single memory mistake can hide long before it surfaces, making human review of full trajectories impractical. We introduce AutoMem, a framework that automates both axes. In the first loop, a strong LLM reviews complete agent trajectories and iteratively revises the memory structure that shapes how the agent interacts with its memory files. In the second loop, the agent's own good memory decisions are identified from many episodes and used as training signal to sharpen the model's memory proficiency directly. Across three procedurally generated long-horizon games (Crafter, MiniHack, and NetHack), optimizing memory alone--without modifying the model's task-action behavior--improved the base agent's performance ~2x-4x, bringing a 32B open-weight model competitive with frontier systems such as Claude Opus 4.5 and Gemini 3.1 Pro Thinking. Our results show that memory management is an independently learnable skill, and a high-leverage objective yielding large gains on long-horizon tasks.

---


### 109. [Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training](https://arxiv.org/abs/2607.01232)

**<font color=#1a73e8>作者：</font>** Zijian Zhang, Rizhen Hu, Athanasios Glentis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that training a single transformer layer can recover most of the gains achieved by full-parameter RL training, and in some cases even surpass it. To quantify this phenomenon, we introduce the quantity layer contribution, which measures the fraction of full RL improvement recovered by training a layer in isolation. Across seven models spanning two model families (Qwen3, Qwen2.5), three RL algorithms (GRPO, GiGPO, Dr. GRPO), and multiple task domains including mathematical reasoning, code generation, and agentic decision-making, we observe a remarkably stable pattern: RL gains are highly concentrated in a small subset of, and in many cases even a single, transformer layers. More strikingly, the same structural pattern consistently emerges: high-contribution layers concentrate in the middle of the transformer stack, while layers near the input and output ends contribute substantially less. The resulting layer rankings remain strongly correlated across datasets, tasks, model families, and RL algorithms.

---


### 110. [Measuring the Gap Between Human and LLM Research Ideas](https://arxiv.org/abs/2607.01233)

**<font color=#1a73e8>作者：</font>** Ziyu Chen, Yilun Zhao, Arman Cohan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used to brainstorm research ideas, but existing evaluations mostly judge individual ideas by novelty, feasibility, or expert preference. We instead ask: how far are current LLM-generated ideas from human researchers? To characterize this gap, we build a large-scale evaluation framework for ideation from high-quality human research papers. For each paper, we reverse-engineer a small set of closely related prior works that likely inspired its core idea. LLMs are then prompted to generate a new idea from the set of paper titles and summaries. We introduce a two-axis research-taste taxonomy to profile each idea by its opportunity pattern and research paradigm, and use it to quantify the divergence between human and LLM ideas. Across idea sets generated by different LLMs, we observe a consistent distributional gap: LLM ideas are disproportionately concentrated around bridge-like opportunities and synthesis methods, whereas the human paper reference distribution spreads more broadly across ways of framing gaps and constructing contributions. This result suggests that strong LLMs can produce a range of reasonable ideas, but that range remains narrower than, and systematically shifted relative to, human research taste.

---


> [!TIP]
> 当前位于：**101-110**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-110**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
