# 🧠 大模型相关研究 | 2026年06月17日

> 本类共 **270** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 1. [MiroBench: Benchmarking Realism in Agentic Simulation of Real-world Discussions](https://arxiv.org/abs/2606.14715)

**<font color=#1a73e8>作者：</font>** Yaoning Yu, Ye Yu, Haojing Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used to simulate real world interactions, but it remains unclear whether simulated behaviors preserve the content patterns and interaction dynamics of real human behaviors. Existing evaluations remain fragmented, which makes it difficult to compare systems or measure progress. In this paper, we focus on Reddit discussions as a concrete first step toward evaluating real-world social simulation. Reddit threads provide public, topic-grounded, multi-party interactions where people share experiences, debate, seek advice, express emotion, and collectively respond to products, events, and social issues. These discussions offer an observable window into broader social behavior, making them a useful setting for testing whether LLM agents can reproduce not only fluent text, but also the distributional patterns and interaction dynamics of real online communities. We introduce MiroBench, a benchmark for Reddit discussion simulation built from 4,292 real Reddit threads. MiroBench uses statistical tests to compare generated and real discussions across four major aspects: repetition and semantic uniformity, narrative content, toxicity and aggression, and structural complexity. Experiments across five domains and five models show that current simulators remain distributionally mismatched with real Reddit threads, while a lightweight prompt-based improvement procedure provides only limited gains. MiroBench offers a concrete benchmark for measuring, diagnosing, and improving realism in LLM-based social simulation.

---


### 2. [FUSE: Quantifying Uncertainty in Vision-Language Models by Bayesian Fusing Epistemic and Aleatoric Uncertainty](https://arxiv.org/abs/2606.14728)

**<font color=#1a73e8>作者：</font>** Harry Zhang, Luca Carlone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are playing an increasingly important role across multiple domains. In many applications, such as robotics, it is crucial to quantify the uncertainty in the output of these models. } We develop FUSE, a probabilistic framework for capturing two complementary sources of uncertainty in vision-language modeling: (i) aleatoric embedding-level uncertainty derived from input data vision-language ambiguity, and (ii) epistemic model-level uncertainty estimated from the semantic response diversity of VLMs. Our approach formulates a Bayesian fusion mechanism that analytically combines these uncertainty sources to produce a scalar measure of uncertainty. This measure can be used to reliably predict the model's output correctness for downstream applications. We demonstrate that our method outperforms baselines and achieves SOTA uncertainty calibration.

---


### 3. [GridVQA-X: A Framework for Evaluating Multimodal Explainability Methods](https://arxiv.org/abs/2606.14740)

**<font color=#1a73e8>作者：</font>** Sujay Belsare, Sudarshan Nikhil, Sushant Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the increasing development of Vision-Language Models, it becomes imperative that their predictions are readily explainable to relevant stakeholders. However, the field of explainability has not kept pace with the multimodal surge. While recent Multimodal Explainable AI (MxAI) methods generate explanations to attribute the interaction between different modalities, current evaluation protocols lack the ground truth required to distinguish between true cross-modal reasoning (e.g., spatial composition) and shallow cross-modal shortcuts (e.g., Bag-of-Words attribute matching). It remains unknown whether MxAI methods faithfully capture synergistic interactions or merely hallucinate reasoning on models acting as simple feature detectors. In this paper, we introduce GridVQA-X, the first diagnostic framework specifically designed to evaluate cross-modal explainability. Unlike natural datasets, GridVQA-X leverages a closed-world synthesis logic to generate unique, mathematically guaranteed explanations. We utilize this controlled environment to train paired ground-truth models on identical architectures: $M_{\text{pure}}$, which learns robust spatial-relational reasoning and $M_{\text{spur}}$, which is structurally forced to rely on cross-modal shortcuts. This behavioral divergence creates a rigorous testbed: a faithful explainer must report distinct reasoning pathways for each model. Our findings reveal that widely used methods fail to distinguish between models relying on genuine spatial-relational reasoning and those exploiting cross-modal shortcuts, highlighting a critical gap in capturing true cross-modal synergy and misrepresenting how multimodal models actually make decisions.

---


### 4. [MMLongEmbed: Benchmarking Multimodal Embedding Models in Long-Context Scenarios](https://arxiv.org/abs/2606.14747)

**<font color=#1a73e8>作者：</font>** Haitian Wang, Ruoxi Sun, Quantong Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements have significantly expanded the theoretical context windows of Multimodal Embedding Models (MEMs). However, larger context windows do not necessarily translate into effective comprehension and representation of long-context multimodal inputs, which remains a critical bottleneck for real-world deployment. To address the lack of systematic evaluation in this setting, we introduce MMLongEmbed, the first comprehensive benchmark for evaluating MEMs in long-context scenarios. MMLongEmbed comprises four retrieval tasks spanning multiple context-length ranges, covering text, document, and video modalities. Through extensive evaluation of state-of-the-art models, we find that current architectures rely heavily on superficial feature matching and struggle to capture deep semantic and structural dependencies. We further observe that performance degradation varies systematically with context length and key information placement. Moreover, models exhibit substantially different robustness to redundant contextual information across modalities. For reproducibility, the benchmark and code are publicly available.

---


### 5. [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](https://arxiv.org/abs/2606.14752)

**<font color=#1a73e8>作者：</font>** Xirui Kang, Yanpei Shi, Lucy Liang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Vision-Language-Action (VLA) models must bridge pretrained vision-language reasoning and precise continuous robot control. Existing action tokenizers discretize actions primarily for reconstruction, producing codes that preserve motion geometry but provide only weak semantic supervision to the backbone. We therefore formulate action tokenization not as mere compression, but as semantic interface learning between multimodal reasoning and executable control. To this end, we introduce X-Tokenizer, a lightweight encoder-Semantic Residual Quantization (SRQ)-decoder architecture that provides a shared action interface across diverse robotic arm embodiments. Its key component, SRQ, imposes an asymmetric structure on residual vector quantization: the first level is trained with Masked Action Modeling (MAM) to form a discrete action language that captures coarse motion intent, while deeper levels remain reconstruction-oriented residuals that preserve fine-grained details. To further align action tokens with multimodal semantics, X-Tokenizer is pretrained with contrastive alignment to the representation space of a pretrained foundation model and with next-frame vision-language feature prediction. Pretrained on 2.4M trajectories (2.0B action frames), a single frozen X-Tokenizer plugs into a mixed discrete-continuous VLA as a representation-shaping supervision signal. X-Tokenizer achieves top real-world aggregate and strong RoboTwin 2.0 simulation results. Outperforming FAST in multimodal grounding (+13.5%) and long-horizon tasks (+8.25), it shows that action tokenizers serve as semantic interfaces for VLA pretraining beyond mere action compression.

---


### 6. [GeoRoPE: Ground-Aware Rotary Adaptation for Remote Sensing Foundation Models](https://arxiv.org/abs/2606.14760)

**<font color=#1a73e8>作者：</font>** Yu Luo, Kun Hu, Mengwei He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote-sensing foundation models (RSFMs) benefit from pretraining on imagery from multiple sensors and ground sampling distances (GSDs), but such exposure alone does not resolve scale mismatch during downstream adaptation. A fixed token-grid offset can correspond to different ground distances across sensors, making grid-based positional priors physically inconsistent. Meanwhile, heterogeneous spatial granularity means that compact urban regions and homogeneous landscapes may require different positional sensitivities even under the same GSD. Therefore, we propose {GeoRoPE}, a ground-aware, RoPE-compatible, and parameter-efficient spatial adaptation method for RSFMs. GeoRoPE recalibrates token-level positional interactions from two complementary aspects. First, \textit{Geo-Coordinate Calibration (GCC)} rescales raw token-grid offsets according to the ground distance represented by one token-grid step, producing geo-calibrated relative coordinates across GSDs. Second, \textit{Geo-Frequency Calibration (GFC)} adjusts the native RoPE frequency with a relation-specific factor, enabling position sensitive adaptation to scene-dependent spatial granularity. GeoRoPE is injected into pretrained RSFMs through a lightweight adapter, preserving the frozen spatial prior while adding geo-aware positional corrections. Experiments across multiple RSFMs, sensors, resolutions, and downstream tasks demonstrate that GeoRoPE improves cross-resolution robustness and scale-sensitive representation learning.

---


### 7. [Scribby: A Multi-Level LLM Framework for Semantic Video Analysis](https://arxiv.org/abs/2606.14762)

**<font color=#1a73e8>作者：</font>** Julian Abelarde, Hugo Garrido-Lestache Belinchon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video content continues to expand across educational platforms, recorded lectures, and live-streamed entertainment, the need for efficient and structured analysis of long-form footage has increased \cite{1}. Although many existing AI programs provide high-level video summaries based on AI-generated transcripts \cite{2,3,4,5}, these approaches are often limited to coarse overviews and lack detailed analysis of a video's structure, thematic progression, and semantic relationships, all of which are required for comprehensive video analysis.
This paper proposes an LLM-based video summarization framework that balances macro-level comprehension with micro-level semantic analysis \cite{6,12,13}. The first stage of the process indexes the video at a micro level by (1) analyzing the full transcript, (2) analyzing individual transcript sentences, and (3) grouping these sentences by semantic similarity using an LLM as a judge \cite{6,13}. Contextual continuity is retained during sentence-level processing by incorporating both the global transcript analysis and adjacent sentence information into each evaluation prompt.
This framework establishes a foundation for video analysis tools that visualize semantic chunking and semantic matching through relevance-based heatmaps. Limitations and future expansions of the framework are also discussed.

---


### 8. [XMedFusion: A Knowledge-Guided Multimodal Perception and Reasoning Framework for Autonomous Medical Systems](https://arxiv.org/abs/2606.14766)

**<font color=#1a73e8>作者：</font>** Hamza Riaz, Arham Haroon, Maha Baig 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous medical and robotic systems increasingly rely on intelligent perception and reasoning capabilities to interpret visual data and support clinical decision making. Radiology report generation represents a critical component of such automated diagnostic workflows, yet existing end-to-end multimodal models often suffer from weak visual grounding, resulting in unreliable interpretations and omission of subtle clinical findings. This paper presents XMedFusion, a modular AI framework designed as an intelligent perception and reasoning module for autonomous medical systems. The proposed framework decomposes visual information into coordinated functional components that emulate expert-driven analysis, including a visual perception agent that extracts image-grounded evidence, a knowledge graph construction agent that structures clinically relevant findings, and a retrieval-guided drafting process that ensures a consistent reporting structure. A synthesis agent iteratively integrates visual and structured evidence through reasoning-driven verification to produce reliable and interpretable diagnostic outputs. Experimental evaluation on a public chest radiograph dataset demonstrates significant improvements over baseline vision-language models, achieving gains from 0.0493 to 0.3359 in BLEU-1, 0.0863 to 0.2440 in ROUGE-L, and 0.0829 to 0.1708 in METEOR, along with substantial improvements in semantic evaluation metrics such as Consistency (2.38 to 7.80) and Accuracy (2.34 to 6.93). The results highlight the effectiveness of structured multi-agent perception and reasoning for enhancing robustness, transparency, and automation in intelligent medical imaging systems, enabling integration into autonomous healthcare and robotic diagnostic workflows.

---


### 9. [YTClickbait21K: Human-Annotated Multimodal Dataset for YouTube Clickbait Detection Across Diverse Channels and Content Categories](https://arxiv.org/abs/2606.14780)

**<font color=#1a73e8>作者：</font>** Md. Minhazul Islam, Md. Tanbeer Jubaer, Amith Khandakar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clickbait content on video-sharing platforms poses a significant challenge to information reliability, yet progress in automated detection has been constrained by the lack of large-scale, high-quality multimodal datasets. We present YTClickbait21K, a human-annotated YouTube clickbait dataset comprising 21,238 videos collected from 40 channels across 29 countries, covering diverse content categories such as news, entertainment, education, and gaming. Each sample includes structured metadata (title, description, engagement statistics) along with associated thumbnail images, enabling comprehensive multimodal analysis. To ensure annotation quality, every video was independently labeled by three annotators using a standardized decision framework that incorporates textual, visual, and cross-modal consistency cues, with final labels determined through majority voting. The dataset exhibits substantial inter-annotator agreement (k=0.65), confirming reliable labeling despite the inherent subjectivity of clickbait detection. By combining scale, annotation rigor, and multimodal richness, this dataset provides a robust benchmark for developing and evaluating machine learning models, facilitating research in cross-modal semantic understanding, and advancing automated content moderation systems.

---


### 10. [Last But Not Least: Boundary Attention CalibratiON for Multimodal KV Cache Compression](https://arxiv.org/abs/2606.14782)

**<font color=#1a73e8>作者：</font>** Tianhao Chen, Yuheng Wu, Kelu Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) achieve strong vision-language reasoning, but long visual contexts enlarge the KV cache and increase decoding latency. Existing compression methods rely on observation window attention for stable token-importance estimation, yet this aggregation can dilute sparse visual evidence and discard answer-critical tokens under aggressive compression. Therefore, we identify last-query attention as a complementary source for recovering such evidence, but its answer-irrelevant signals can mislead retention. We propose BACON, a plug-and-play method that calibrates observation window attention with last-query evidence and suppresses isolated noise via intra-layer coherence and inter-layer persistence. Across diverse benchmarks, models, budgets, and compression methods, BACON improves multimodal KV compression by 7.5% on average under the most aggressive budget, with gains up to 30.9%.

---


### 11. [The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models](https://arxiv.org/abs/2606.14783)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Shuning Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A vision encoder compresses image pixels into semantic embeddings, implicitly acting as a privacy boundary by preserving semantic content while attenuating pixel-local detail required for exact text recovery. Encoder-free vision-language models (VLMs) remove this boundary by routing image patches directly into the language-model token stream, thereby exposing an architectural privacy attack surface: intermediate visual tokens become a pre-output side channel. Under a token-access adversary, decoders invert visual-token streams from two encoder-free VLMs, Gemma4 and Fuyu, recovering recognizable image structure and readable held-out access codes, whereas matched encoder-based controls localize target regions but recover no exact strings. Within-model ablations show that the operative factor is spatial sampling fidelity of the visual-token grid, especially character-direction sampling density, rather than token or value count. The leakage is not limited to exported tokens: Gemma4 layer-0 key-value cache tensors are directly invertible, placing the side channel within KV caches commonly persisted by production serving stacks for decoding efficiency. The attack survives clutter, realistic document degradation, and zero-shot transfer to public document images, and it resists value-level defenses such as additive noise and quantization. Effective mitigation must therefore reduce spatial sampling, making removal of the vision encoder a first-class privacy decision in VLM deployment.

---


### 12. [A Definition of Good Explanations and the Challenges Explaining LLM Outputs](https://arxiv.org/abs/2606.14838)

**<font color=#1a73e8>作者：</font>** Louis Mahon, Elliot Ford, Callum Hackett  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How to define a good explanation is a long-standing philosophical debate which has found recent renewed interest in the context of AI outputs. Explainability is crucial for AI adoption in many contexts, but in order to produce good explanations of AI systems, we must first have an understanding of what good explanations are. In this paper we propose a definition inspired by the notion of counterfactual explanations, however we argue that one must also take into account the interlocutor's prior beliefs in each fact that could be offered in an explanation. We explore the ramifications of this definition for AI explainability and, in particular, why LLM outputs are difficult to produce good explanations for.

---


### 13. [Understanding Cross-Modal Contributions in Continual Vision-Language Models: A Theoretical Perspective](https://arxiv.org/abs/2606.14883)

**<font color=#1a73e8>作者：</font>** Salimeh Sekeh, Mary Wisell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual vision-language models are commonly addressed through sequential fine-tuning; however, although this paradigm enables adaptation to new environments (tasks), it inherently emphasizes the contribution of previously learned environments (tasks) at the expense of the stability required to preserve previously acquired knowledge. While existing approaches have adequately studied continual learning and catastrophic forgetting in vision-language models (VLMs), the theoretical understanding of modality-specific contributions across a sequence of environments remains largely unexplored. In this paper, we present a new theoretical perspective to understand the cross-modal (vision-language) contributions to consecutive environments. We empirically evaluate our theoretical findings on large VLMs and demonstrate their effectiveness in capturing environment-level cross-modal contributions. Our analysis provides deeper insights into continual VLMs, highlighting their contribution robustness to varying task orders and inter-task similarities, and their improved generalization performance.

---


### 14. [Separable Neural Architectures as Physical World Models: from Mathematical Theory to Applications](https://arxiv.org/abs/2606.14934)

**<font color=#1a73e8>作者：</font>** Reza T Batley, Andrew Kichline, Sourav Saha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work introduces the Separable Neural Architecture (SNA), a function representational class combining neural approximation with tensor decomposition. The SNA decouples localized coordinate functions (atoms) from global interactions governed by a sparse, low-rank interaction object. This architecture possesses a compact and smooth inductive bias well-suited for solving partial differential equations (PDEs). When viewed as a Galerkin trial space under the variational SNA (VSNA) framework, the formulation satisfies classical variational guarantees under Lax-Milgram: well-posedness, quasi-optimality, convergence, and stability. In high-dimensional spatiotemporal--parametric PDEs, the VSNA mitigates the curse of dimensionality by scaling algebraically rather than exponentially. Exploiting an entirely factorized, tensor-native alternating least squares (ALS) optimization framework reduces this cost to linear in dimension. The VSNA is validated across elliptic, hyperbolic, and parabolic systems, demonstrating close alignment with predicted algebraic and spectral scaling rates. We showcase the SNA as a "solve once, query anywhere" physical world model via two engineering case studies: a 7D parametric manufacturing simulation and an experimental thermal-to-property inversion pipeline for Inconel 718. The VSNA executes a 1,000,000-query Monte Carlo sweep in 102s on a standard laptop CPU, yielding a 150,000x speedup over a full-grid finite element baseline hosted on an NVIDIA A100 GPU. It further enables real-time generative inverse-mode reconstructions under 100ms. These results demonstrate that the SNA serves as a compact mathematical substrate for continuous parameter manifolds to enable real-time inversion, optimization loops, and rapid uncertainty propagation.

---


### 15. [PrologMCP: A Standardized Prolog Tool Interface for LLM Agents](https://arxiv.org/abs/2606.14935)

**<font color=#1a73e8>作者：</font>** Agnieszka Mensfelt, Adarsh Prabhakaran, Adrian Haret 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier reasoning-tuned language models still fail on deductive tasks at depth, and the cost of improved performance through extended internal reasoning scales poorly. Symbolic delegation offers a complementary route: a language model translates the problem, while a solver performs the inference. However, current autoformalization pipelines for logic programming are typically bespoke integrations tied to particular tasks or agents. We introduce PrologMCP, a task-agnostic, open-source server that exposes Prolog as a stateful tool through the Model Context Protocol (MCP). Its compact tool interface, structured error reporting, and per-session isolation make the translate-run-inspect-repair loop a reusable primitive for MCP-capable agents. We evaluate a formalizer agent enhanced with PrologMCP against standard and reasoning LLMs (Claude Sonnet 4.6, GPT-4.1, and o4-mini) on two subsets of PARARULE-Plus: a general-purpose sample and a more challenging one targeting a specific failure mode of natural-language reasoning. On the general sample, the formalizer matches or exceeds reasoning LLMs (accuracy 1.00 vs.\ 1.00 / 0.998), with the largest gains over standard models (0.762 for GPT-4.1). On the challenging subset, the formalizer remains near-perfect (1.00 / 0.99) while reasoning LLMs drop to 0.95 / 0.94. These results suggest that delegating inference to Prolog via MCP is a robust and inspectable alternative to extended natural-language reasoning.

---


### 16. [Learning Sparse Latent Predictive Foundation Model for Multimodal Neuroimaging](https://arxiv.org/abs/2606.14957)

**<font color=#1a73e8>作者：</font>** Haoxu Huang, Long Chen, Jingyun Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain MRIs are routinely acquired as multiple complementary sequences with unique contrast weighting, including T1-weighed imaging (T1w) anatomic and fluid-sensitive T2-weighted (T2w) contrasts. However, methods for learning unified representations across the multitude of MRI contrast mechanisms at health-system scale are lacking. In this study, we introduce Neuro-JEPA, a sparse multimodal neuroimaging foundation model that combines a latent predictive objective with a Mixture-of-Experts architecture to encode brain MRI across core T1w, T2w, and fluid-suppressed FLAIR imaging (FLAIR). We further provide a systematic methodological study of architectural, masking, objective, and sparsity design choices beneficial for robust neuroimaging multimodal representation learning. Neuro-JEPA was pretrained on 1,551,862 scans from 428,647 studies after modality-specific preprocessing with data curation across three core structural brain MRI sequences. We evaluated the learned representations across clinical and research settings, including 25 tasks from three health systems: NYU Langone, NYU Long Island, and Massachusetts General Hospital, and 22 tasks from 12 public datasets, covering unimodal, multimodal and cross-domain evaluation configurations. Across these benchmarks, existing neuroimaging foundation models showed inconsistent gains over a simple convolutional neural network (CNN) baseline, whereas Neuro-JEPA achieved stronger and more consistent performance across all evaluated settings. These results establish a scalable methodological framework for multimodal neuroimaging representation learning and highlight the need for foundation model evaluation protocols that include simple baselines, clinically heterogeneous cohorts and controlled multimodal comparisons.

---


### 17. [Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning](https://arxiv.org/abs/2606.14960)

**<font color=#1a73e8>作者：</font>** Lala Yamazaki, Ramchandra Rimal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study investigates the application of machine learning models to predict exam outcomes using physiological data collected during examination sessions. Physiological stress indicators, including electrodermal activity, heart rate, and skin temperature, were analyzed to uncover their association with academic performance. A variety of machine learning approaches were employed, ranging from standard models like logistic regression, random forest, and support vector machines to more advanced architectures, including transformers, long short-term memory (LSTM), and gated recurrent unit (GRU) models. This diversity aimed to capture the complex interactions within the data effectively. A key focus was assessing the adaptability of transformers in processing numerical data and evaluating their performance in this novel context. Standard performance metrics, such as accuracy, precision, recall, and F1-score, were used to compare model efficacy. The experimental results demonstrate that while deep learning models generally excel at capturing complex relationships in physiological data, simpler models like random forests can sometimes achieve superior performance while offering computational efficiency and interpretability. Furthermore, transformers demonstrated notable versatility, showcasing performances comparable to those of the LSTM and GRU models. This research underscores the importance of experimenting with a broad class of models that align with the objectives of the problem at hand, balancing precision, efficiency, and interpretability. By elucidating the relationships between physiological signals and academic performance, this study contributes to understanding stressors affecting students' mental health. It further promotes leveraging physiological data to enhance student well-being and academic outcomes.

---


### 18. [CoRA: Confidence-Rationale Alignment for Reliable Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.14961)

**<font color=#1a73e8>作者：</font>** Juming Xiong, Weixin Liu, Kevin Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning can improve LLM performance, but high answer confidence may be misleading when the accompanying CoT rationale is plausible yet incomplete or poorly supported. We study confidence--rationale alignment: whether a model's confidence in its committed answer is justified by its generated rationale. We introduce a GRPO-based reinforcement learning framework that jointly rewards answer correctness, committed-answer probability, and rubric-based rationale support, where the rubric assesses grounding, coherence, task match, and connection to the selected answer without revealing the gold answer to the judge. Across MedQA, MathQA, and OpenBookQA using three open-weight LLMs, our method reduces the confidence--rationale alignment error by up to 26.51% compared with untuned checkpoints, SFT, and correctness-only GRPO, while maintaining competitive accuracy and often improving calibration. These results show that reliable CoT reasoning requires not only confident answers, but rationales that substantively support them.

---


### 19. [Zero-order Parameter-free Optimization for LMO-based Methods: Novel Approach for Efficient Fine-tuning](https://arxiv.org/abs/2606.14970)

**<font color=#1a73e8>作者：</font>** Dmitriy Bystrov, Daniil Medyakov, Dmitry Bylinkin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) has become a central application of modern optimization, enabling pretrained models to adapt to diverse downstream tasks and domain-specific data. A major obstacle in large-scale fine-tuning is the memory overhead of backpropagation, which requires storing activations, gradients, and optimizer states. Zeroth-order (ZO) optimization offers a memory-efficient alternative, but its performance is highly sensitive to the stepsize and smoothing parameter, often requiring costly task-specific tuning. Parameter-free (PF) optimization addresses this issue by adapting algorithmic parameters without prior knowledge of problem-dependent constants. Moreover, large-scale fine-tuning can benefit from geometry-aware updates that account for the heterogeneous structure of parameter blocks, which can be modeled through methods that exploit linear minimization oracle (LMO). In this work, we study PF adaptation for LMO-based ZO optimization and introduce $\texttt{AdaNAGED}$, a method that unifies gradient-free training, adaptive tuning, and non-Euclidean update geometry. We establish convergence guarantees and validate the method on large-scale LLM fine-tuning task with $\texttt{OPT}-1.3\mathrm{B}$ model.

---


### 20. [Hierarchical Generative Agents for Simulating Sequential Human Behavior](https://arxiv.org/abs/2606.14989)

**<font color=#1a73e8>作者：</font>** Maria G. Mendoza, Lucas Waldburger, Jin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Complex cognitive, emotional, and social processes shape human evacuations during natural disasters. Accurate modeling and understanding of human behavior in disasters or emergencies can greatly impact the evacuation process by informing more effective planning and resource allocation. However, collecting human data in these situations is very difficult, and existing computational evacuation models assume rational, homogeneous behavior, leading to unrealistic, overly optimistic predictions. To address this gap, we present a simulation framework of sequential human decision-making during an evacuation scenario, introducing cognitively grounded, persona-driven agents. Our framework models evacuation behavior in a grid-based urban environment that evolves over time, capturing fire and other hazards. Human agents are modeled as personas that make sequential decisions in response to environmental stimuli with cognition structured in three levels: high-level evacuation goals, mid-level route reasoning, and low-level navigation. Decision-making is driven by large language models (LLMs) coupled with a cognitive module and calibrated with empirical human evacuation data. We propose a dynamic, stimulus-driven disaster simulation framework that models human evacuation decision-making using persona-conditioned LLM agents and a cognitive hierarchy.

---


### 21. [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2606.15007)

**<font color=#1a73e8>作者：</font>** NVIDIA, Aaron Blakeman, Aaron Thomas 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Nemotron 3 Ultra, a 550 billion total and 55 billion active parameter Mixture-of-Experts Hybrid Mamba-Attention language model. We pre-trained Nemotron 3 Ultra on 20 trillion text tokens, then extended the context length to 1M tokens, and post-trained using Supervised Fine Tuning (SFT), Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD). Nemotron 3 Ultra is our most capable model yet, employing multiple key technologies - LatentMoE, Multi Token Prediction (MTP), NVFP4 pre-training, multi-environment RLVR, MOPD, and reasoning budget control. Nemotron 3 Ultra achieves up to ~6x higher inference throughput as compared to state-of-the-art publicly available LLMs while attaining on-par accuracy. The state-of-the-art accuracy, high inference throughput, and 1M token context length make Nemotron 3 Ultra ideal for long-running autonomous agentic tasks. We open-source the base, post-trained, and quantized checkpoints, along with the training data and recipe on HuggingFace.

---


### 22. [Resilient Consensus in Agentic AI](https://arxiv.org/abs/2606.15024)

**<font color=#1a73e8>作者：</font>** Sribalaji C. Anand, George J. Pappas  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed in multi-agent systems where they must coordinate and agree on shared decisions. We ask whether classical resilient consensus theory, developed for deterministic agents, transfers to LLM agents that may behave adversarially. Framing LLM agreement as a Byzantine consensus game, we run controlled experiments on complete and general communication graphs. We find that prompted LLM agents fail to reach agreement that is achievable in principle: consensus can fail even in settings where classical theory guarantees that a convergent algorithm exists, and this failure persists across temperatures and horizons. At the same time, wrapping the agents with classical resilient consensus filters improves agreement. The benefit of filtering depends on how much robustness the underlying topology already provides. Our results suggest that classical resilient consensus theory is a useful lens for the safety of agentic AI.

---


### 23. [Deep Temporal Modeling and Ensemble Fusion for Multimodal Emotion Recognition from Physiological Signals](https://arxiv.org/abs/2606.15026)

**<font color=#1a73e8>作者：</font>** Desta Haileselassie Hagos, Saurav Keshari Aryal, Patrick Ymele-Leki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Physiological stress and emotion recognition are important for health monitoring and affective computing. In this work, we present a comprehensive evaluation of deep learning models such as Long Short-Term Memory (LSTM), Temporal Convolutional Networks (TCN), and Transformer on the WESAD dataset for multimodal affect recognition using wrist and chest sensor signals. We perform ablation studies to assess the individual contributions of each modality by training models on wrist-only and chest-only inputs. In addition, we implement a late-fusion ensemble strategy that combines predictions from all three architectures trained on multimodal input. We also employ early fusion at the sensor level by concatenating wrist and chest signals before feeding them into each model. Our results show that Transformer models consistently achieve the highest accuracy in multimodal settings, while TCN models perform best in the wrist-only configuration. The ensemble method yields the highest overall accuracy (98.91 +/- 0.13%) and macro-F1 score (98.56 +/- 0.17%). These findings demonstrate the effectiveness of sensor fusion and ensemble-based fusion in developing robust systems for physiological emotion recognition.

---


### 24. [Metric Match: A Subset Selection Approach to Evaluating LLM Judge Reliability](https://arxiv.org/abs/2606.15029)

**<font color=#1a73e8>作者：</font>** Alyssa Unell, Natalie Dullerud, Naomi Boneh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are used to reduce the need for costly human labor in evaluating open-ended text generation. However, the reliability of these judges depends critically on their alignment with human raters -- a property that itself depends on costly human annotations. In this work, we develop a method (Metric Match) for estimating correlation-based reliability metrics of LLM judges from limited annotations. Metric Match selects a subset of samples for human annotation such that the subset matches the population reliability metric with respect to acquired synthetic labels. We empirically show that Metric Match achieves a win-rate of 0.838 against random subset selection across four different correlation metrics and 15 datasets, with an 18.7% decrease in average estimation error and reduces annotation needs by 32.5%. We provide a cost model and highlight a medical case study where our method saves $1,041.67 compared to random selection for expert annotation. Further, we shift our task from reliability estimation to reliability classification of whether a given judge is above a deployment threshold, outperforming random selection with Metric Match. All project code is publicly available, and we additionally provide an installable package for ease of use.

---


### 25. [How Should World Models Be Evaluated? A Decision-Making-Centric Position](https://arxiv.org/abs/2606.15032)

**<font color=#1a73e8>作者：</font>** Yang Yu, Shiyuan Zhang, Yifei Sheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models have rapidly become one of the central abstractions in modern AI. Yet the term now refers to several different objects: action-conditioned environment models, latent imagination models, future-video predictors, interactive neural simulators, latent predictive representations, and synthetic-data engines. Evaluation has broadened with the term. Recent papers measure video realism, perceptual similarity, instruction following, physical plausibility, policy ranking, executability, planning success, and downstream policy improvement. The result is not only metric diversity but also a recurring problem of claim/evidence mismatch: papers frequently make a stronger claim about what their model is useful for than their evaluation can actually establish.
This paper surveys the recent literature and argues that the central question is use-dependent. When a model is presented as a world model for embodied decision-making, a more decisive issue is not whether it generates visually compelling videos, but whether it supports reliable counterfactual reasoning, policy evaluation, planning, and policy optimization under intervention, policy-induced distribution shift, and long-horizon rollout. We organize the literature using an L0--L7 ladder that ranges from visual plausibility to policy optimization utility. In our interpretation, L0--L3 are most naturally read as diagnostics of generated artifacts, L4 is often the first genuinely interventional test, and L5--L7 provide the most direct evidence of decision usefulness. Based on this diagnosis, we propose a decision-making-centric evaluation framework and a benchmark protocol that foreground counterfactual action fidelity, closed-loop rollout validity, reward/value prediction, policy-ranking agreement, optimization lift, model exploitability, and uncertainty calibration.

---


### 26. [Cloze: An Open Research Platform for Studying Human-AI Conversations in Mental Health Contexts](https://arxiv.org/abs/2606.15033)

**<font color=#1a73e8>作者：</font>** Matthew Flathers, Francesco Cipriani, John Torous  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cloze is an open-source web platform for conducting controlled, monitored studies of human-AI conversation in mental health research contexts. Consumer large language model (LLM) products such as ChatGPT, Claude, and Gemini are built for individual productivity, and offer researchers little experimental control, inconsistent data export, and no shared safety scaffolding that holds across providers. Cloze gives research teams a single environment in which they configure which models participants converse with, how the AI is instructed, how conversations are scheduled over time, and which safety constraints apply unconditionally, while every message is captured with full provenance (model version, prompt configuration, timing). The platform currently supports OpenAI, Anthropic, Google, and locally hosted open-weight models served through Ollama behind a unified interface, and runs in the cloud or fully on premises so that participant data need never leave an institution. Cloze is research infrastructure for building an evidence base on human-AI interaction in mental health contexts. It is not a therapeutic product.

---


### 27. [ReportQA: QA-Based Radiology Report Evaluation](https://arxiv.org/abs/2606.15037)

**<font color=#1a73e8>作者：</font>** Yiming Shi, Shaoshuai Yang, Xi Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Radiology report evaluation is essential for advancing automated report generation. Natural language generation metrics have limited clinical relevance. Clinical efficacy (CE) metrics evaluate important medical findings, but focus mainly on presence and cover only a limited set of entities. Due to heavy reliance on manual annotations, it is difficult for CE metrics to extend clinical entities or attributes. In clinical practice, radiology reports serve as a medium for information transfer. Clinicians use them to perform downstream diagnostic tasks without directly inspecting images. Based on this insight, we propose ReportQA, a clinical-related and flexible radiology report evaluation framework, supporting detailed quantitative analysis of radiology report generation systems. We first collect datasets covering multiple imaging modalities and anatomical regions. We then construct knowledge trees of clinical entities and attributes with radiologist guidance, and use large language models (LLMs) to extract structured information from raw reports. Next, we generate QA pairs from predefined templates and apply quality control through self-filtering and report-based filtering. During evaluation, the report is treated as context, and an LLM acts as a judge model to answer the QA pairs. Based on the resulting QA accuracy, we introduce QAScore metric. Compared with existing metrics, QAScore shows better alignment with radiologist judgments. Experiments on multiple state-of-the-art vision-language models reveal that current report-based inference paradigms struggle to learn fine-grained clinical representations and exhibit strong negative prior biases. In contrast, question-driven inference provides a more effective alternative. For reproducibility and extensibility, we release the knowledge trees, structured reports, and QA pairs, along with the pipeline code for QA construction and evaluation.

---


### 28. [Fusion is not one-size-fits-all: Cross-Modal Representation Alignment for Time-to-Event Modeling](https://arxiv.org/abs/2606.15038)

**<font color=#1a73e8>作者：</font>** Zhemin Zhang, Weijie Chen, David Le 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate time-to-event (TTE) prediction from multimodal clinical data remains challenging due to modality imbalance and distribution shift. We introduce a foundation model-driven framework for cross-modal representation alignment between CT imaging and longitudinal EHR data, designed to generalize across tasks and institutions. CT and EHR modalities are encoded independently using domain-specific foundation models and aligned in a shared latent space through four principled fusion strategies: late fusion, contrastive alignment, cross-attention, and co-attention. We evaluate two clinically distinct TTE tasks: pulmonary embolism (PE) mortality and cardiovascular disease (CVD) outcomes, on large-scale multi-institutional cohorts (PE: N=3,099 train; 1,098 internal; 435 external; CVD: N=2,951 train; 837 internal; 682 external). Fusion consistently improves concordance index by 1.5-5.4% over unimodal baselines when modalities contribute comparably. Overall, contrastive multimodal fusion, particularly with CLMBR representations, provided the most consistent and statistically robust improvements, especially for PE mortality prediction. For MACE, cross-attention (one-hot) achieved the highest internal performance and image-guided co-attention achieved the best external performance. We therefore introduce a generalizable foundation model-based cross-modal alignment framework and provide the first systematic analysis of fusion behavior under modality imbalance in TTE prediction. Our results establish task-aware multimodal alignment as a necessary design principle for robust generalization and scalable clinical deployment.

---


### 29. [Equity with Efficiency: An Empirical Study of Tokenizers for Multilingual Large Language Models](https://arxiv.org/abs/2606.15044)

**<font color=#1a73e8>作者：</font>** Kieron Seven Jun Wei Lee, Muhammad Reza Qorib, Andrew Ivan Soegeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models (LLMs) depend on subword tokenization to bridge discrete text and continuous neural representation. State-of-the-art multilingual LLMs often use Byte-level Byte-Pair Encoding (BPE) tokenizers that structurally favor high-resource languages and Latin scripts. For speakers of underrepresented languages, particularly those across Southeast Asia, this bias inflates inference costs and widens cross-lingual capability gaps. We present the first systematic comparison of equitable tokenizers on a unified benchmark spanning 11 Southeast Asian languages. Beyond tokenizer-level analysis of compression efficiency and cross-lingual equity, we assess downstream task performance through controlled 1.5B-parameter language model training using the same training data. Our results show that Parity-aware BPE lies on the Pareto frontier of the efficiency-equity trade-off, achieving strong compression parity at competitive cost. Morphology-Driven Byte Encoding delivers the best semantic reasoning performance through morphologically richer representations, albeit at a higher computational expense. Byte Latent Transformer underperforms on downstream tasks, possibly because its architectural assumptions misalign with the constraints of limited low-resource training data. Together, our findings demonstrate that cross-lingual fairness and tokenization efficiency are not fundamentally at odds, and offer practical guidance for designing equitable multilingual models.

---


### 30. [Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models](https://arxiv.org/abs/2606.15070)

**<font color=#1a73e8>作者：</font>** Jiakai Li, Ke Qin, Rongzheng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> By incorporating test-time compute scaling, large reasoning models (LRMs) can solve complex problems through explicit chain-of-thought (CoT) reasoning processes. However, they often suffer from overthinking, resulting in redundant token outputs and degraded accuracy. Current methods to mitigate this issue remain limited: training-based approaches require substantial computational resources, while training-free methods rely on well-crafted prompts or unreliable confidence signals. In this work, we investigate early stopping from the perspective of attention distributions and propose a simple method, ASAG, which infers the model's reasoning state and adaptively adjusts the generation strategy. The proposed framework is training-free and plug-and-play, enabling seamless integration into existing LRMs. Extensive experiments on nine benchmarks demonstrate consistent improvements across mainstream LRMs with varying parameter scales, including the DeepSeek-R1-Distill and Qwen3 series. Specifically, ASAG improves average accuracy by 3.2% while reducing the number of generated tokens by nearly 40% across all reasoning tasks on Qwen3-8B.

---


### 31. [TriAdReview: Triangular Adversarial Review Architecture for Multi-Model Technical Document Generation](https://arxiv.org/abs/2606.15074)

**<font color=#1a73e8>作者：</font>** Zhiqiang Zhou, Junliang Dai, Xu Ling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for technical document generation, yet single-model outputs often suffer from over-engineering, security blind spots, and incomplete coverage. We propose TriAdReview, a triangular adversarial review architecture that employs two independent reviewer models (engineering and boundary perspectives) and a triangular judging mechanism to iteratively improve a generator model's output. We evaluate TriAdReview across five benchmark tasks - architecture design, code generation, proposal review, security audit, and requirements analysis - using three configurations: single model (baseline), dual model (single review), and triple model (full system). Results across 75 experiments (n=5 per cell) show that the triple model configuration achieves a 10.1% overall improvement over the single model baseline (26.2 vs. 23.8 out of 50; p<0.05, paired t-test), with particularly strong gains on security audit (+27.6%), code generation (+20.8%), and architecture design (+15.6%). A second scorer (mimo-v2.5-pro) confirms the direction with a smaller effect (+2.7%), suggesting moderate inter-rater agreement. However, the system shows a -7.5% degradation on requirements analysis, revealing that adversarial review architectures have a structural bias toward simplification that is counterproductive for completeness-oriented tasks. We analyze this boundary condition through a task-type framework and demonstrate that reviewer prompt adaptation partially mitigates the issue. Our findings provide the first empirical characterization of when multi-model adversarial review helps versus harms, with implications for the design of collaborative AI systems.

---


### 32. [Risk-Aware LLM Agents for Geospatial Data Retrieval: Design and Preliminary Adversarial Evaluation](https://arxiv.org/abs/2606.15077)

**<font color=#1a73e8>作者：</font>** Kyle Gao, Joel Cumming, Jonathan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an LLM-driven framework for retrieving remote sensing data from cloud-based geospatial catalogues using natural language queries. The system converts user intent into structured API calls, enabling efficient access to satellite imagery and environmental datasets. The architecture integrates three agents: Guardrail for safety and policy enforcement, General-QA for intent interpretation, and Recommender-Analyst for schema-aware API call generation. This coordinated design ensures reliable, semantically aligned interaction with external data services. The modular framework is portable across platforms through API schema substitution and supports applications in environmental monitoring, disaster response, and climate analysis. It establishes a scalable interface between user intent and geospatial infrastructure, enabling streamlined and automated Earth observation workflows. Preliminary experiments under adversarial multi-turn settings show that prompt-level safety instructions improve robustness, although rare high-impact failures persist in API manipulation scenarios and highlight the need for adaptive, system-level defenses that balance safety, usability, and cost efficiency, which motivates the use of our intercept-level Guardrail agent.

---


### 33. [Cognitive Debt: AI as Intellectual Leverage and the Dynamics of Systemic Fragility](https://arxiv.org/abs/2606.15078)

**<font color=#1a73e8>作者：</font>** Shuchen Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop a formal theory of cognitive debt: the stock of unverified reasoning obligations that accumulates when individuals use AI as a substitute rather than a complement for first-principles cognition. The model features two state variables per agent, cognitive capital and cognitive debt, and a multiplicative production technology in which cognitive capital functions as collateral that determines the return to AI adoption. We establish six propositions. Rational agents incur positive cognitive debt because the costs are deferred, partially external, and masked by short-run productivity gains. Tranquil periods lower subjective risk assessments, raise AI substitution intensity, and compound leverage, generating a cognitive Minsky moment in which subjective risk falls while true systemic fragility rises. Expected crisis losses are convex in aggregate leverage. Post-crisis, output-target pressure can produce a false-correction loop in which agents patch AI failures with more AI. The decentralised equilibrium over-adopts substitutive AI relative to the social optimum because of systemic risk, cognitive public goods, and arms-race externalities. In a two-type heterogeneous-agent economy, high-cognitive-capital agents adopt AI more intensively and may eventually erode their unaided cognitive capital below that of initially lower-skilled agents.

---


### 34. [Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale](https://arxiv.org/abs/2606.15079)

**<font color=#1a73e8>作者：</font>** Ang Li, Ben Liu, Bin Han 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient and scalable agentic intelligence requires models that can deliver both low-latency responses and strong reasoning capabilities while remaining practical to train, serve, and deploy. In this report, we present Ling-2.6 and Ring-2.6, a family of models designed to address this challenge at scale. Ling-2.6 is optimized for instant response generation and high capability per output token, whereas Ring-2.6 is tailored for deeper reasoning and more advanced agentic workflows. Instead of training from scratch, we upgrade the Ling-2.0 base model through architectural migration pre-training and large-scale post-training. This upgrade is guided by a unified co-design of model architecture, optimization objectives, serving systems, and agent training environments, enabling improvements in both model capability and deployment efficiency. At the architectural level, we introduce a hybrid linear attention design that integrates Lightning Attention with MLA, improving the efficiency of long-context training and decoding. To further enhance token efficiency, we optimize capability per output token through Evolutionary Chain-of-Thought, Linguistic Unit Policy Optimization, bidirectional preference alignment, and shortest-correct-response distillation. For agentic capabilities, we propose KPop, a reinforcement learning framework designed to support stable training of Ring-2.6-1T on large-scale environment-grounded data. KPop improves training efficiency through asynchronous scheduling across coding, search, tool use, and workflow execution, enabling scalable learning from complex agent-environment interactions. Together, Ling-2.6 and Ring-2.6 provide a practical pathway toward efficient, scalable, and open agentic systems. We open-source all checkpoints in the 2.6 family to support further research and development in practical agentic intelligence.

---


### 35. [High-Dimensional Random Projection for Activation Steering in Language Models](https://arxiv.org/abs/2606.15092)

**<font color=#1a73e8>作者：</font>** Minh-Hieu Pham, Bach Do, Laziz Abdullaev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering has emerged as a key methodology for controlling the behavior of large language models (LLMs). Existing difference-in-means based methods, however, are fundamentally limited: they capture only mean differences between class activations and fail to recover discriminative signals that naturally exist in the nonlinear feature subspace under the superposition hypothesis. Motivated by that, we propose High-Dimensional Random-projection for Activation Steering (HiDRA), a training-free approach that integrates seamlessly with existing activation steering methods. By performing activation addition in the projected high-dimensional space, HiDRA can provably capture a better discriminative structure beyond the reach of linear methods. Experiments across diverse LLM families and benchmarks demonstrate that HiDRA consistently outperforms baseline counterparts, achieving stronger behavioral control without significant computational overhead.

---


### 36. [VGPT-RSI for RH-Adjacent Formal Progress: Boundary Certificates, Verified Finite Lagarias Inequalities, and Explicit Failure Localization](https://arxiv.org/abs/2606.15096)

**<font color=#1a73e8>作者：</font>** Zhixin Hu, Tao Xu, Xiaodian Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Riemann Hypothesis remains one of the central unsolved problems in mathematics. Rather than claiming proof, we investigate whether a verifiable AI-assisted reasoning system can produce reliable, formally checked partial progress while explicitly identifying the remaining mathematical obstructions. We apply the Verifiable Growing Physical Transformer with Recursive Self-Improvement (VGPT-RSI) to two RH-adjacent certification tasks. First, we construct and verify a finite RH-boundary certificate for inequality on a parameterized safe lower curve over a region. The numerical boundary curve is converted into a certificate-backed lower curve, audited using outward-rounded interval arithmetic and Arb/FLINT ball arithmetic, and then checked in Rocq/CoqInterval for the parameterized theorem. Second, we initiate a formal Lagarias-route certificate. Lagarias criterion states that RH is equivalent to the global inequality. We formalize the finite quantity and produce a Coq-checked finite certificate. The final system identifies the exact unresolved mathematical bottlenecks: formalizing the Lagarias equivalence, proving the global tail theorem beyond any finite cutoff, and potentially reducing counterexamples to colossally abundant or related extremal integers. These results demonstrate that VGPT-RSI can produce certified RH-adjacent formal progress, organize proof dependencies, and avoid overclaiming when the remaining obstruction is genuinely mathematical.

---


### 37. [Towards Verifiable Agentic Data Science: Solving Irregular TSQA Via Tool-Grounded Reasoning](https://arxiv.org/abs/2606.15107)

**<font color=#1a73e8>作者：</font>** Sanhorn Chen, Xiaoyang Chen, Boyu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series data in real-world deployments is overwhelmingly irregular. Observations are asynchronous, missing values are informative rather than random, and sampling frequencies vary across sensors and operational windows. However, existing Time Series Question Answering (TSQA) benchmarks mostly assume regularly sampled inputs, leaving a fundamental gap in understanding how large language models (LLMs) and AI agents perform under irregular conditions. To bridge this gap, we introduce IRTS-ToolBench, a benchmark of 1,700 questions spanning 10 task types across 13 domains. IRTS-ToolBench is designed to be used independently by any researcher working on LLM-based irregular time series analysis, providing standardized inputs and a reproducible evaluation protocol. Code can be found in this https URL.

---


### 38. [When Cognitive Graphs Meet LLMs: BDEI Cognitive Pathways for Panic Emotional Arousal Prediction](https://arxiv.org/abs/2606.15121)

**<font color=#1a73e8>作者：</font>** Mengzhu Liu, Long Qin, Chuan Ai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predicting individual panic emotional arousal timing before manifestation is essential for proactive emergency intervention. Existing methods incorporate cognitive elements but none explicitly model the emotional arousal process, making them ill-suited for emotional arousal timing prediction. We argue that grounding prediction in appraisal emotion theory is necessary because it explicitly models this process, but three problems must be solved. (1) Appraisal theory posits that emotion arises from simultaneous evaluation across multiple threat dimensions, yet no prior work fuses these inputs into risk perception. (2) Existing cognitive models lack an Emotion node, decoupling threat appraisal from emotional arousal and forcing emotions to be inferred indirectly from behaviors. (3) Given their generalizable cognitive reasoning, current approaches adopt LLMs as the primary decision-maker, yet overlook the fragility and hallucination-proneness of their outputs. To address these issues, we introduce PanicCognitivePath (PCP), a framework that addresses all three. A Psychological Safety Distance (PSD) model, grounded in psychological distance theory, maps four-domain signals into a unified risk metric as the entry condition for subsequent cognitive reasoning. An explicit Emotion node grounded in appraisal emotion theory is introduced into BDI, forming a Belief-Desire-Emotion-Intention (BDEI) pathway. Agents whose risk metric exceeds the PSD threshold enter this pathway, coupling threat appraisal directly to emotional arousal. The BDEI pathway governs all state transitions while the LLM is confined to parameter estimation for the Belief-to-Desire transition, confining hallucinations to a single step and preventing error propagation. Experiments on Hurricane Sandy show PCP improves arousal timing accuracy by 10.68% over baselines, reduces peak count error to 7.07%.

---


### 39. [Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for Visual Embeddings](https://arxiv.org/abs/2606.15134)

**<font color=#1a73e8>作者：</font>** Shubhang Bhatnagar, Dheeraj Baiju, Narendra Ahuja  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision encoders for retrieval are typically trained with class-label supervision: each training pair reduces to a scalar that uniformly pushes the embedding apart or pulls it together, as if every visual attribute either differed or matched. A multimodal large language model (MLLM), shown the same pair, can articulate those attributes and use them to predict whether the images share a class. We propose \textbf{SAGA}, a framework that turns this language-grounded, attribute-aware perception into a training signal for the encoder itself. Specifically, we use Group Relative Policy Optimization (GRPO) to reward the MLLM for correct predictions on the vision encoder's tokens. Since correct predictions require those tokens to expose the specific attributes that differ or match between the pair, the gradient pushes the encoder to encode them, replacing the uniform pair-level scalar with attribute-resolved supervision. An auxiliary attention-distillation loss anchors the encoder's embedding to tokens the MLLM attended to, and a standard metric-learning loss shapes the embedding geometry for nearest-neighbour retrieval. The MLLM is frozen throughout and discarded at inference, matching the deployment cost of a metric-learning baseline. SAGA improves Recall@1 by 3 to 6 points over state-of-the-art baselines on CUB-200-2011, Cars-196, FGVC-Aircraft, and iNaturalist Aves on zero-shot image retrieval.

---


### 40. [Can Agents Read the Room? Benchmarking Visual Social Intelligence in Multimodal Simulation](https://arxiv.org/abs/2606.15152)

**<font color=#1a73e8>作者：</font>** Shijun Wan, Xuehai Wu, Jiwen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social interaction depends on both language and visible social signals, such as facial expressions, posture, gaze, and emotional shifts. Yet existing social-agent benchmarks are largely text-based and rarely test whether multimodal agents can use visual cues to guide interaction. We introduce \textsc{\benchmarkname{}}, a benchmark evaluating visual social intelligence in multimodal social simulation. It contains 240 scenarios, 585 role instances, and 2,340 role-task instances, combining aligned textual-visual evidence, structured role profiles, and four role-level tasks: expression task, characteristic task, interaction regulation task, and interaction outcome task. Evaluating seven recent MLLMs under verbalized-vision and direct-vision reveals a clear gap between local role enactment and interaction management: role-specific expression and conflict handling are near saturation, whereas interaction regulation and visually grounded outcome achievement remain substantially more difficult. The code is released at this https URL, and the dataset is available at this https URL.

---


### 41. [PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression](https://arxiv.org/abs/2606.15157)

**<font color=#1a73e8>作者：</font>** Chao Fei, Panos Kalnis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache compression is essential for reducing the memory cost of long-context large language model inference. Existing approaches, however, typically apply a single compression policy and a uniform cache budget across all transformer layers. This uniform design ignores the fact that different layers can play different roles during prefill and decoding, and may therefore require different eviction strategies and cache capacities. We present PolyKV, a layer-wise KV cache optimization framework that considers design space with method selection and budget allocation. PolyKV routes each layer to a suitable KV compression policy based on layer-level signals, while assigning non-uniform budgets under a fixed total budget. This formulation enables heterogeneous compositions of existing KV cache methods. Experiments on LLaMA-3.1-8B and Qwen3-8B show that, under the same 512-token average KV budget, PolyKV recovers 54.5% and 25.7% of the LongBench performance gap between the strongest single-policy baseline and FullKV, respectively. Across 128-1024 budget sweep, PolyKV consistently improves over the strongest baseline by 1.7%-6.4%, corresponding to 40.0%-54.5% recovery of the FullKV gap.

---


### 42. [DLWM: Diverse Latent World Models for Efficient Multimodal Reasoning](https://arxiv.org/abs/2606.15160)

**<font color=#1a73e8>作者：</font>** David Huang, Lianlei Shan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning capabilities of multimodal large language models (MLLMs) have improved considerably in recent years. Existing approaches typically rely on explicit chain-of-thought or continuous latent-space trajectories to enhance multi-step reasoning. However, these methods generally assume that an input admits a single latent interpretation and unfold reasoning along a fixed path or under a uniform computation budget. In real-world multimodal settings, visual observations are often subject to occlusion, blur, viewpoint variation, or semantic ambiguity, giving rise to multiple plausible interpretations. A uniform reasoning strategy not only limits the model's ability to explore multiple hypotheses but also incurs high memory usage and rollout cost. We present DLWM (Diverse Latent World Models), a multimodal reasoning framework that combines latent-space reasoning with reinforcement learning. First, we construct a set of diverse latent world hypotheses in continuous latent space, each capturing a different plausible interpretation of the visual input, and unfold latent reasoning independently on each hypothesis. An orthogonality-based diversity regularizer explicitly prevents hypothesis collapse. Second, we formulate the latent reasoning process as a resource-constrained sequential decision problem and introduce a resource-aware reinforcement learning policy that adaptively allocates computation across hypotheses, dynamically deciding whether to expand, terminate, or merge reasoning paths, thereby substantially reducing memory footprint and improving rollout efficiency. Experiments on multiple multimodal reasoning benchmarks demonstrate that DLWM outperforms existing methods by 2-5 points in accuracy while reducing memory usage by 24%.

---


### 43. [Label Shift Aware Adaptation for Online Zero-shot Learning with Contrastive Language-Image Pre-Training (CLIP)](https://arxiv.org/abs/2606.15169)

**<font color=#1a73e8>作者：</font>** Pengxiao Han, Changkun Ye, Yanshuo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models like Contrastive Language-Image Pre-Training (CLIP) have been extensively studied in data-scarce scenarios. A particularly challenging and realistic task in this area is online zero-shot learning with CLIP, where unknown test samples are predicted sequentially in random order by CLIP while keeping the feature extraction and model parameters fixed during the sequential inference phase. Most existing approaches in this setting address the problem by adapting representations online using incoming test samples, while neglecting the distribution of the data on which CLIP was initially trained. This mismatch can lead to degraded performance when the label distribution in the test data differs from that of the training domain. To address this gap, we propose Label Shift Aware (LSA), which formulates the online zero-shot classification task as a domain adaptation problem. Specifically, LSA adapts the predictions computed by CLIP, which was trained on an unknown source distribution, to a target distribution using only unlabeled test data, and applies label shift correction to mitigate the mismatch between the source and target domains. The extensive experiments across multiple datasets demonstrate that the proposed LSA consistently outperforms state-of-the-art online zero-shot learning methods based on CLIP.

---


### 44. [CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation](https://arxiv.org/abs/2606.15179)

**<font color=#1a73e8>作者：</font>** Xuedong Hu, Zhiqing Tang, Zhi Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) has emerged as a pivotal technique for improving language models by incorporating external knowledge at inference time. As device-cloud collaborative inference makes it feasible to deploy small language models on edge devices, a new setting arises in which private documents remain on the device and public knowledge resides in the cloud. Privacy and policy constraints often forbid raw document exchange, creating a document-isolated dual-end RAG setting. However, existing methods rely on frequent remote synchronization and dense evidence transfer, limiting throughput under realistic latency and bandwidth conditions. To address this issue, we propose CONCORD, an asynchronous sparse aggregation framework for dual-end RAG under document isolation. CONCORD treats the cloud as an asynchronously arriving evidence source rather than a continuously synchronized co-generator. Specifically, we introduce waiting debt control to decide whether each decoding step should continue waiting for remote participation based on the observed return of waiting. We also design a certificate-guided minimal supplementation mechanism that requests only the remote evidence needed to determine the current greedy decision. Steps that consult the cloud preserve the same greedy token as dense dual-end aggregation, while the remaining steps commit locally without remote evidence. Experiments on Natural Questions and WikiText-2 show that CONCORD improves end-to-end throughput over baselines by $1.66\times$ and $2.15\times$, respectively, while reducing per-token communication by over two orders of magnitude and maintaining comparable answer quality and perplexity.

---


### 45. [CogGuard: Cognitive and Operational Profiling for Proactive Warning in Edge Intelligent Services](https://arxiv.org/abs/2606.15199)

**<font color=#1a73e8>作者：</font>** Zhi Yao, Weihao Chen, Zhiqing Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive warning is an important capability for edge intelligent services, where the system predicts whether a subject will successfully complete an incoming task under strict latency and privacy constraints. Such prediction depends on both long-term static attributes and short-term dynamic states derived from historical interaction logs. Recent Large Language Models (LLMs) offer strong long-context reasoning for constructing structured profiles from these logs, but existing solutions face two challenges for edge deployment: (1) profiling methods are typically domain-specific and lack a reusable abstraction across service scenarios, and (2) fine-tuning alignment models on heterogeneous edge clusters incurs high synchronization overhead due to the variance in input sequence lengths. To address these challenges, we propose CogGuard, a proactive-warning framework for edge intelligent services. CogGuard decouples offline LLM-based profile construction from online Small Language Model (SLM)-based score prediction through a shared static-dynamic profile-to-score pipeline, and instantiates it in two representative scenarios: educational performance warning and operational task outcome warning. For efficient profile construction, we design scenario-specific profiling methods with prefix-aligned KV-cache reuse to reduce repeated encoding overhead. For edge-side model alignment, we propose a length-aware distributed fine-tuning strategy with contrastive regularization to mitigate workload imbalance on heterogeneous clusters. Experiments on education and operation datasets show that CogGuard reduces profile construction time by up to 48% and distributed fine-tuning time by 19%, while achieving MAEs of 13.4 and 5.9, respectively, on 100-point-scale warning tasks. In the largest educational setting, CogGuard reduces prediction error by 15.4% compared with the strongest baseline.

---


### 46. [Comparing Human Gaze and Vision-Language Model Attention in Safety-Relevant Environments](https://arxiv.org/abs/2606.15202)

**<font color=#1a73e8>作者：</font>** Marta Vallejo, Siwen Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human visual attention plays an important role in how people perceive and respond to environments containing potential risks. This study investigates whether large vision-language models can identify the same regions of a scene that attract human attention in safety-relevant environments. Eye-tracking data were collected from ten participants viewing 33 scene images representing environments with varying levels of potential risk using Pupil Invisible wearable glasses. Gaze coordinates were mapped onto stimulus images to generate population-averaged human gaze heatmaps. In parallel, GPT-4o was prompted through the OpenAI Vision Application Programming Interface (API) to generate spatial predictions of visual attention, which were converted into saliency maps for comparison with human gaze patterns.
Spatial alignment between human gaze heatmaps and model-generated saliency maps was evaluated using four complementary metrics: Pearson correlation (r = 0.515 +- 0.117), Normalised Scanpath Saliency (NSS = 0.988 +- 0.323), Kullback-Leibler divergence (KL = 1.766 +- 0.844), and Area Under the Receiver Operating Characteristic Curve using the Judd formulation (AUC-Judd = 0.806 +- 0.076). A cross-model comparison with Gemini Pro, Gemini Flash, and Claude showed that all models exceeded the AUC-Judd chance baseline of 0.5 and achieved positive NSS scores. Gemini Pro demonstrated the strongest spatial localisation according to three of the four metrics, whereas GPT-4o produced the closest distributional match to human attention as measured by KL divergence.
These findings suggest that large vision-language models can identify regions that broadly correspond to where humans direct visual attention in safety-relevant scenes without requiring eye-tracking training data. The results highlight the potential of vision-language models as a scalable tool for approximating human attentional patterns.

---


### 47. [Visual-Seeker: Towards Visual-Native Multimodal Agentic Search via Active Visual Reasoning](https://arxiv.org/abs/2606.15231)

**<font color=#1a73e8>作者：</font>** Zhengbo Zhang, Changtao Miao, Jinbo Su 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated impressive capabilities in many visual tasks, but they often struggle with factual grounding when confronted with complex, open-world scenarios. While recent multimodal deep search agents attempt to address this issue by utilizing external tools, the visual-native search paradigm remains underexplored. Existing methods primarily rely on simple images with explicit semantics and text-only evidence trajectories, limiting the agent's ability to perform multi-hop, cross-modal reasoning and search. To address these limitations, we propose Visual-Seeker, a visual-native multimodal deep search agent via active visual reasoning. Rather than treating vision as a static input, our agent actively attends to fine-grained visual details, dynamically harvests visual evidence throughout the search process. To unlock its visual-native potential, we design an active visual reasoning data pipeline and synthesize 5K high-quality multimodal trajectories for model training. Extensive experiments demonstrate the state-of-the-art performance across five challenging multimodal search benchmarks, even surpassing several proprietary models, validating robust visual-native reasoning and search in real-world web environments. The code and data can be accessed at: this https URL.

---


### 48. [Landmark-free Assessment of Lower-limb Alignment with Implicit Neural Shape Functions from Knee Radiographs](https://arxiv.org/abs/2606.15250)

**<font color=#1a73e8>作者：</font>** Zhisen Hu, Antti Kemppainen, David Johnson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiographic assessment of lower-limb alignment (LLA) is important for predicting joint health and surgical outcomes in total knee arthroplasty. Traditional measurement methods are manual and time-consuming, while recent machine learning approaches typically rely on locating a fixed set of anatomical landmarks. This dependence limits flexibility and may require re-annotation when clinical definitions change. To address this, we propose an automated workflow using Implicit Neural Shape Functions (INSF). Rather than relying on explicit landmark coordinates, we encode the anatomy into a compact latent space and regress clinical alignment measurements directly from these latent codes. This architecture allows for rapid extendability to new tasks without altering the backbone representation. We trained our method on an internal dataset of 566 knee radiographs, each annotated with the outline of the femur and tibia. We evaluated it on both an internal test dataset of 50 patients and a separate external set of 402 preoperative cases from the MRKR dataset. Manual clinical measurements are available for these data, and the MRKR measurements will be made publicly accessible. Performance was comparable to state-of-the-art landmark-based methods and manual agreement, while offering a flexible shape representation that can be extended to additional measurement tasks.

---


### 49. [Mask-Proof: An LLM-based Automated Data Curation Pipeline on Mathematical Proofs](https://arxiv.org/abs/2606.15258)

**<font color=#1a73e8>作者：</font>** Jierui Zhang, Siyuan Tan, Xinhang Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly capable of mathematical problem solving and can even assist with research-level proofs, yet we still lack a scalable and reproducible way to measure step-level reasoning in long proofs across diverse sources. This evaluation gap limits trustworthy AI assistance in proof-certified scientific progress. Existing evaluations often emphasize final answers or rely on costly expert grading, while end-to-end proof generation remains open-ended and hard to verify automatically. We introduce Mask-Proof, a pipeline that turns real proofs into automatically checkable masked-step tasks. It masks key formula steps, provides the necessary surrounding context, and evaluates model reconstructions with an LLM-based equivalence judge using repeated votes for stability. The resulting Mask-ProofBench contains 292 curated problems across diverse research areas. Experiments with 17 models show that reasoning-enhanced models outperform standard models by 12% to 27%. Our evaluator achieves 96.8% agreement with expert annotators, enabling faithful, reproducible, and comparable measurement of step-level mathematical reasoning. Benchmark, annotations, and code are available at this https URL.

---


### 50. [Hybrid NARX-LLM for Greenland Iceberg Discharge: Prompt-Driven Residual Correction](https://arxiv.org/abs/2606.15288)

**<font color=#1a73e8>作者：</font>** Yiquan Gao, Duohui Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Greenland iceberg discharge exhibits complex nonlinear dynamics with limited observability, challenging traditional predictive models. We present a Hybrid NARX-LLM framework that combines a nonlinear autoregressive model with exogenous inputs (NARX) and a large language model (LLM) for residual correction. We further propose a Physics-Informed Prompt (PIP) method that transforms unstructured physical knowledge into structured prompts for zero-shot in-context reasoning. The primary objective is to explore the corrective potential of this framework for modeling Greenland iceberg discharge, rather than merely optimizing predictive accuracy. The NARX component captures intrinsic temporal dependencies, while the LLM, guided by PIP, encodes glacier dynamics and environmental drivers and perceives key trend patterns to correct systematic prediction errors. This integration allows the model to reason about unmodeled factors and produce interpretable residuals, enhancing overall predictive accuracy. Applied to Greenland iceberg discharge time series, our approach addresses extreme events that are difficult to predict due to rare variations and nonstationary trends, a limitation often overlooked by traditional methods. By fusing structured time-series modeling with knowledge-driven foundation AI, the framework offers a scalable and interpretable pathway to bridge data-limited climate forecasting with physics-informed LLM reasoning. The code is available.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
