# 🧠 大模型相关研究 | 2026年05月17日

> 本类共 **165** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-165**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-165**

---

### 151. [Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG](https://arxiv.org/abs/2605.15109)

**<font color=#1a73e8>作者：</font>** Riccardo Terrenzi, Maximilian von Zastrow, Serkan Ayvaz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful. In these systems, an agent explores a knowledge graph before producing an answer and a small set of citations. We frame citation faithfulness as a trajectory-level problem: final citations should not only support the answer, but also account for the graph traversal, structure, and visited-but-uncited entities that may influence it. Through controlled ablation experiments, we compare the effects of isolating, removing, and masking cited and uncited graph entities. Our results show that cited evidence is often necessary, as removing it substantially changes answers and reduces accuracy. However, citations are not sufficient, because accurate answers can also depend on uncited traversal context and surrounding graph structure. These findings suggest that citation evaluation in Agentic GraphRAG should move beyond source support toward provenance over the broader retrieval trajectory.

---


### 152. [Understanding How International Students in the U.S. Are Using Conversational AI to Support Cross-Cultural Adaptation](https://arxiv.org/abs/2605.15127)

**<font color=#1a73e8>作者：</font>** Laleh Nourian, Anisa Callis, Stephanie Patterson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Moving to a new culture and adapting to a new life, as an international student, can be a stressful experience. In the US, international students face unique overlapping challenges, yet the current support ecosystem, including university support systems and informal social networks, remains largely fragmented. While conversational AI has emerged as a tool used by many (e.g., generative AI chatbots like ChatGPT and Google Gemini), we do not have a clear understanding of how international students adopt and perceive these technologies as support tools. We conducted a survey study (n=60) to map the relationship between international students' challenges and AI adoption patterns, followed by an interview study with 14 participants to identify the underlying motivations and boundaries of use. Our findings show that AI is perceived as a first-aid tool for immediate challenges, however, there is an interest in transforming AI from a tool for short-term help into a long-term support companion. By identifying where and how AI can provide long-term support, and where it is insufficient, we contribute recommendations for creating AI-powered support tailored to the unique needs of international students.

---


### 153. [MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/abs/2605.15128)

**<font color=#1a73e8>作者：</font>** Minghao Guo, Qingyue Jiao, Zeru Shi 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning. In prior work, many visually grounded questions can be answered using only captions or textual traces, allowing answers to be inferred without preserving the fine-grained visual evidence. Meanwhile, harder cases that require reasoning over changing visual states are largely absent. Therefore, we introduce MemEye, a framework that evaluates memory capabilities from two dimensions: one measures the granularity of decisive visual evidence (from scene-level to pixel-level evidence), and the other measures how retrieved evidence must be used (from single evidence to evolutionary synthesis). Under this framework, we construct a new benchmark across 8 life-scenario tasks, with ablation-driven validation gates for assessing answerability, shortcut resistance, visual necessity, and reasoning structure. By evaluating 13 memory methods across 4 VLM backbones, we show that current architectures still struggle to preserve fine-grained visual details and reason about state changes over time. Our findings show that long-term multimodal memory depends on evidence routing, temporal tracking, and detail extraction.

---


### 154. [Natural Synthesis: Outperforming Reactive Synthesis Tools with Large Reasoning Models](https://arxiv.org/abs/2605.15131)

**<font color=#1a73e8>作者：</font>** Frederik Schmitt, Matthias Cosler, Niklas Metzger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reactive synthesis, the problem of automatically constructing a hardware circuit from a logical specification, is a long-standing challenge in formal verification. It is elusive for two reasons: It is algorithmically hard, and writing formal specifications by hand is notoriously difficult. In this paper, we tackle both sides of the problem. For the algorithmic side, we present a neuro-symbolic approach to reactive synthesis that couples large reasoning models with model checkers to iteratively repair a synthesized Verilog implementation via sound symbolic feedback. Our approach solves more benchmarks than the best dedicated tools in the annual synthesis competition and extends to constructing parameterized systems, a problem known to be undecidable. On the specification side, we introduce an autoformalization step that shifts the specification task from temporal logic to natural language by introducing a hand-authored dataset of natural-language specifications for evaluation. We demonstrate performance comparable to that of starting from formal specifications, establishing natural synthesis as a viable end-to-end workflow.

---


### 155. [APWA: A Distributed Architecture for Parallelizable Agentic Workflows](https://arxiv.org/abs/2605.15132)

**<font color=#1a73e8>作者：</font>** Evan Rose, Tushin Mallick, Matthew D. Laws 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. However, these systems hit critical reasoning, coordination, and computational scaling bottlenecks as the size and complexity of their tasks grow. These limitations hinder multi-agent systems from achieving high-throughput processing for highly parallelizable tasks, despite the availability of parallel computing and reasoning primitives in the underlying LLMs. We introduce the Agent-Parallel Workload Architecture (APWA), a distributed multi-agent system architecture designed for the efficient processing of heavily parallelizable agentic workloads. APWA facilitates parallel execution by decomposing workflows into non-interfering subproblems that can be processed using independent resources without cross-communication. It supports heterogeneous data and parallel processing patterns, and it accommodates tasks from a wide breadth of domains. In our evaluation, we demonstrate that APWA can dynamically decompose complex queries into parallelizable workflows and scales on larger tasks in settings where prior systems fail completely.

---


### 156. [Causal Foundation Models with Continuous Treatments](https://arxiv.org/abs/2605.15133)

**<font color=#1a73e8>作者：</font>** Christopher Stith, Medha Barath, Vahid Balazadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal inference, estimating causal effects from observational data, is a fundamental tool in many disciplines. Of particular importance across a variety of domains is the continuous treatment setting, where the variable of intervention has a continuous range. This setting is far less explored and represents a substantial shift from the binary treatment setting, with models needing to represent effects across a continuum of treatment values. In this paper, we present the first causal foundation model for the continuous treatment setting. Our model meta-learns the ability to predict causal effects across a wide variety of unseen tasks without additional training or fine-tuning. First, we design a novel prior over data-generating processes with continuous treatment variables in order to generate a rich causal training corpus. We then train a transformer to reconstruct individual treatment-response curves given only observational data, leveraging in-context learning to amortize expensive Bayesian posterior inference. Our model achieves state-of-the-art performance on individual treatment-response curve reconstruction tasks compared to causal models which are trained specifically for those tasks.

---


### 157. [Widening the Gap: Exploiting LLM Quantization via Outlier Injection](https://arxiv.org/abs/2605.15152)

**<font color=#1a73e8>作者：</font>** Xiaohua Zhan, Kazuki Egashira, Robin Staab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM quantization has become essential for memory-efficient deployment. Recent work has shown that quantization schemes can pose critical security risks: an adversary may release a model that appears benign in full precision but exhibits malicious behavior once quantized by users. However, existing quantization-conditioned attacks have been limited to relatively simple quantization methods, where the attacker can estimate weight regions that remain invariant under the target quantization. Notably, prior attacks have consistently failed to compromise more popular and sophisticated schemes, limiting their practical impact. In this work, we introduce the first quantization-conditioned attack that consistently induces malicious behavior that can be triggered by a broad range of advanced quantization techniques, including AWQ, GPTQ, and GGUF I-quants. Our attack exploits a simple property shared by many modern quantization methods: large outliers can cause other weights to be rounded to zero. Consequently, by injecting outliers into specific weight blocks, an adversary can therefore induce a targeted, predictable weight collapse in the model. This effect can be used to craft seemingly benign full-precision models that exhibit a wide range of malicious behaviors after quantization. Through extensive evaluation across three attack scenarios and LLMs, we show that our attack achieves high success rates against a broad range of quantization methods on which prior attacks fail. Our results demonstrate, for the first time, that the security risks of quantization are not restricted to simpler schemes but are broadly relevant across complex, widely-used quantization methods.

---


### 158. [Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2605.15155)

**<font color=#1a73e8>作者：</font>** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction. On-Policy Self-Distillation (OPSD) complements RL by introducing dense token-level guidance from a teacher branch augmented with privileged context. However, transferring OPSD to multi-turn agents proves problematic: compounding multi-turn instability destabilizes supervision, while skill-conditioned privileged guidance requires asymmetric treatment for negative teacher rejections may arise from imperfect skills retrieval or utilization. We introduce SDAR (Self-Distilled Agentic Reinforcement Learning), which treats OPSD as a gated auxiliary objective while keeping RL as the primary optimization backbone. SDAR maps detached token-level signals into a sigmoid gate, strengthening distillation on teacher-endorsed positive-gap tokens and softly attenuating negative teacher rejections. Across the Qwen2.5 and Qwen3 families on ALFWorld, WebShop, and Search-QA, SDAR substantially improves over GRPO (+9.4% on ALFWorld, +7.0% on Search-QA, +10.2% on WebShop-Acc), avoids the instability of naive GRPO+OPSD, and consistently outperforms hybrid RL--OPSD baselines across model scales.

---


### 159. [Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment](https://arxiv.org/abs/2605.15168)

**<font color=#1a73e8>作者：</font>** Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reconstructing precise clinical timelines is essential for modeling patient trajectories and forecasting risk in complex, heterogeneous conditions like sepsis. While unstructured clinical narratives offer semantically rich and contextually complete descriptions of a patient's course, they often lack temporal precision and contain ambiguous event timing. Conversely, structured electronic health record (EHR) data provides precise temporal anchors but misses a substantial portion of clinically meaningful events. We introduce a retrieval-augmented multimodal alignment framework that bridges this gap to improve the temporal precision of absolute clinical timelines extracted from text. Our approach formulates timeline reconstruction as a graph-based multistep process: it first extracts central anchor events from narratives to build an initial temporal scaffold, places non-central events relative to this backbone, and then calibrates the timeline using retrieved structured EHR rows as external temporal evidence. Evaluated using instruction-tuned large language models on the i2m4 benchmark spanning MIMIC-III and MIMIC-IV, our multimodal pipeline consistently improves absolute timestamp accuracy (AULTC) and improves temporal concordance across nearly all evaluated models over unimodal text-only reconstruction, without compromising event match rates. Furthermore, our empirical gap analysis reveals that 34.8% of text-derived events are entirely absent from tabular records, demonstrating that aligning these modalities can produce a more temporally faithful and clinically informative reconstruction of patient trajectories than either source alone.

---


### 160. [SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer](https://arxiv.org/abs/2605.15178)

**<font color=#1a73e8>作者：</font>** Haoyi Zhu, Haozhe Liu, Yuyang Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control. SANA-WM achieves visual quality comparable to large-scale industrial baselines such as LingBot-World and HY-WorldPlay, while significantly improving efficiency. Four core designs drive our architecture: (1) Hybrid Linear Attention combines frame-wise Gated DeltaNet (GDN) with softmax attention for memory-efficient long-context modeling. (2) Dual-Branch Camera Control ensures precise 6-DoF trajectory adherence. (3) Two-Stage Generation Pipeline applies a long-video refiner to stage-1 outputs, improving quality and consistency across sequences. (4) Robust Annotation Pipeline extracts accurate metric-scale 6-DoF camera poses from public videos to yield high-quality, spatiotemporally consistent action labels. Driven by these designs, SANA-WMdemonstrates remarkable efficiency across data, training compute, and inference hardware: it uses only $\sim$213K public video clips with metric-scale pose supervision, completes training in 15 days on 64 H100s, and generates each 60s clip on a single GPU; its distilled variant can be deployed on a single RTX 5090 with NVFP4 quantization to denoise a 60s 720p clip in 34s. On our one-minute world-model benchmark, SANA-WM demonstrates stronger action-following accuracy than prior open-source baselines and achieves comparable visual quality at $36\times$ higher throughput for scalable world modeling.

---


### 161. [Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing](https://arxiv.org/abs/2605.15179)

**<font color=#1a73e8>作者：</font>** Ellwil Sharma, Arastu Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling Scientific Machine Learning (SciML) toward universal foundation models is bottlenecked by negative transfer: the simultaneous co-training of disparate partial differential equation (PDE) regimes can induce gradient conflict, unstable optimization, and plasticity loss in dense neural operators. In particular, broadband open-channel fluid dynamics and boundary-dominated porous media flows impose incompatible spectral and geometric demands on a single dense parameter path. We introduce Shodh-MoE, a sparse-activated latent transformer architecture for multi-physics transport. Shodh-MoE operates on compressed 16^3 physical latents produced by a physics-informed autoencoder with an intra-tokenizer Helmholtz-style velocity parameterization, restricting decoded states to divergence-free velocity manifolds. The model guarantees exact mass conservation, achieving a physically verifiable velocity divergence of ~2.8 x 10^-10 (evaluated post-hoc in FP64) on 128^3 grids. A Top-1 soft-semantic router dynamically assigns localized latent patches to expert subnetworks, enabling specialized parameter paths for distinct physical mechanisms while preserving shared experts for universal symmetries. In a 20,000-step distributed pretraining run over mixed three-dimensional physical tensors, routing telemetry shows autonomous domain bifurcation: held-out validation tokens from the open-channel domain route exclusively to Expert 0, while porous-media tokens route exclusively to Expert 1. The model converges simultaneously across both regimes, achieving latent validation MSEs of 2.46 x 10^-5 and 9.76 x 10^-6, and decoded physical MSEs of 2.48 x 10^-6 and 1.76 x 10^-6. These results support sparse expert routing as a practical architectural mechanism for mitigating multi-physics interference in universal neural operators.

---


### 162. [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](https://arxiv.org/abs/2605.15184)

**<font color=#1a73e8>作者：</font>** Sahil Sen, Akhil Kasturi, Elias Lumer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. Despite the growing adoption of retrieval-augmented generation (RAG) in agentic search systems, existing literature lacks a systematic comparison of how retrieval strategy choice interacts with agent architecture and tool-calling paradigm. Important practical dimensions, including how tool outputs are presented to the model and how performance changes when searches must cope with more irrelevant surrounding text, remain under-explored in agent loops. This paper reports an empirical study organized into two experiments. Experiment 1 compares grep and vector retrieval on a 116-question sample from LongMemEval, using a custom agent harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, and Gemini CLI), for both inline tool results and file-based tool results that the model reads separately. Experiment 2 compares grep-only and vector-only retrieval while progressively mixing in additional unrelated conversation history, so that each query is embedded in more distracting material alongside the passages that matter. Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same.

---


### 163. [Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185)

**<font color=#1a73e8>作者：</font>** Jiaxin Wu, Yihao Pi, Yinling Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. Most existing video evaluation pipelines rely heavily on human judgment or learned graders, which can be subjective and weakly diagnostic for geometric failures. We introduce PDI-Bench (Perspective Distortion Index), a quantitative framework for auditing geometric coherence in generated videos. Given a generated clip, we obtain object-centric observations via segmentation and point tracking (e.g., SAM 2, MegaSaM, and CoTracker3), lift them to 3D world-space coordinates via monocular reconstruction, and compute a set of projective-geometry residuals capturing three failure dimensions: scale-depth alignment, 3D motion consistency, and 3D structural rigidity. To support systematic evaluation, we build PDI-Dataset, covering diverse scenarios designed to stress these geometric constraints. Across state-of-the-art video generators, PDI reveals consistent geometry-specific failure modes that are not captured by common perceptual metrics, and provides a diagnostic signal for progress toward physically grounded video generation and physical world model. Our code and dataset can be found at this https URL.

---


### 164. [Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187)

**<font color=#1a73e8>作者：</font>** Matt Zhou, Ruining Li, Xiaoyang Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A bottleneck in learning to understand articulated 3D objects is the lack of large and diverse datasets. In this paper, we propose to leverage large language models (LLMs) to close this gap and generate articulated assets at scale. We reduce the problem of generating an articulated 3D asset to that of writing a program that builds it. We then introduce a new agentic system, Articraft, that writes such programs automatically. We design a programmatic interface and harness to help the LLM do so effectively. The LLM writes code against a domain-specific SDK for defining parts, composing geometry, specifying joints, and writing tests to validate the resulting assets. The harness exposes a restricted workspace and interface to the LLM, validates the resulting assets, and returns structured feedback. In this way, the LLM is not distracted by details such as authoring a URDF file or managing a complex software environment. We show that this produces higher-quality assets than both state-of-the-art articulated-asset generators and general-purpose coding agents. Using Articraft, we build Articraft-10K, a curated dataset of over 10K articulated assets spanning 245 categories, and show its utility both for training models of articulated assets and in downstream applications such as robotics simulation and virtual reality.

---


### 165. [ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both](https://arxiv.org/abs/2605.15198)

**<font color=#1a73e8>作者：</font>** Ziyu Guo, Rain Liu, Xinyan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning, often interleaved with intermediate visual states, has emerged as a promising direction in the field. A straightforward approach is to directly generate images via unified models during reasoning, but this is computationally expensive and architecturally non-trivial. Recent alternatives include agentic reasoning through code or tool calls, and latent reasoning with learnable hidden embeddings. However, agentic methods incur context-switching latency from external execution, while latent methods lack task generalization and are difficult to train with autoregressive parallelization. To combine their strengths while mitigating their limitations, we propose ATLAS, a framework in which a single discrete 'word', termed as a functional token, serves both as an agentic operation and a latent visual reasoning unit. Each functional token is associated with an internalized visual operation, yet requires no visual supervision and remains a standard token in the tokenizer vocabulary, which can be generated via next-token prediction. This design avoids verbose intermediate visual content generation, while preserving compatibility with the vanilla scalable SFT and RL training, without architectural or methodological modifications. To further address the sparsity of functional tokens during RL, we introduce Latent-Anchored GRPO (LA-GRPO), which stabilizes the training by anchoring functional tokens with a statically weighted auxiliary objective, providing stronger gradient updates. Extensive experiments and analyses demonstrate that ATLAS achieves superior performance on challenging benchmarks while maintaining clear interpretability. We hope ATLAS offers a new paradigm inspiring future visual reasoning research.

---


> [!TIP]
> 当前位于：**151-165**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-165**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
