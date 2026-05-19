# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-346](./part-07.md)

---

### 251. [PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows](https://arxiv.org/abs/2605.18032)

**<font color=#1a73e8>作者：</font>** Kazuki Kawamura, Satoshi Waki, Kei Tateno  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM workflows -- systems composed of multiple role-specific LLM calls -- often outperform single-prompt baselines, but they remain difficult to debug and refine. Failures can originate from subtle errors in intermediate outputs that propagate to downstream nodes, requiring developers to inspect long traces and infer which agent to modify. We present PROTEA, a unified interface for offline, test-driven improvement of multi-agent workflows. PROTEA executes a workflow, scores intermediate node outputs with configurable rubrics, and overlays per-node states and rationales on the workflow graph to localize likely bottlenecks. To support complex systems where final-answer references are the primary supervision, PROTEA performs backward node evaluation: it generates candidate node-level expectations from final-answer references and graph context, then compares them with observed node outputs. For selected nodes, PROTEA presents targeted prompt revisions as editable before/after comparisons, then automatically reruns and re-evaluates the workflow to show output changes and score trajectories within the same interface. In two production-adjacent workflows, PROTEA improved document-inspection accuracy from 64.3% to 83.9% and recommendation Hit@5 from 0.30 to 0.38. In a formative study with six experienced LLM developers, participants valued graph-level localization, per-node rationales, and editable before/after prompt revisions.

---


### 252. [OmniSelect: Dynamic Modality-Aware Token Compression for Efficient Omni-modal Large Language Models](https://arxiv.org/abs/2605.18041)

**<font color=#1a73e8>作者：</font>** Morunliu Yang, Ruotao Xu, Le Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal large language models (OmniLLMs) have recently gained increasing attention for unified audio-video understanding. However, processing long multimodal token sequences introduces substantial computational overhead, making efficient token compression crucial. Existing methods typically rely on fixed, modality-specific guidance, which fails to account for the varying importance of modalities across different queries. To address this limitation, we propose $\textbf{OmniSelect}$, a training-free, modality-adaptive token pruning framework that dynamically selects appropriate compression strategies for multimodal inputs. Specifically, we leverage a lightweight AudioCLIP model to estimate cross-modal relevance and categorize each input into three pruning regimes: Audio-Centric, Video-Centric, and Uniform pruning. Based on these relevance scores, OmniSelect further performs fine-grained token pruning within each temporal group, adaptively allocating pruning ratios to preserve informative tokens across modalities. By explicitly modeling modality preference and enabling dynamic strategy selection, OmniSelect effectively avoids the pitfalls of one-size-fits-all compression. Extensive experiments demonstrate that our method achieves efficient multimodal token reduction while maintaining strong performance, without requiring any additional training.

---


### 253. [FLAG: Foundation model representation with Latent diffusion Alignment via Graph for spatial gene expression prediction](https://arxiv.org/abs/2605.18055)

**<font color=#1a73e8>作者：</font>** Qi Si, Penglei Wang, Yushuai Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from routine H\&E enables large-scale molecular profiling, yet current models treat this as isolated pointwise tasks, thereby overlooking essential biological structures like gene coordination and spatial distribution. To preserve these relationships, we introduce \textbf{FLAG}, a diffusion-based framework that redefines this task as structured distribution modeling. At the same time, we identify the critical \textbf{Gene Dimension Curse}, where joint modeling gene expression and their spatial interactions fail in high-dimensional spaces, and FLAG solves this challenge by integrating a spatial graph encoder for topological consistency and utilizing Gene Foundation Model (GFM) alignment for gene-gene fidelity in the generation process. To rigorously assess model performance, we propose a set of novel structural evaluation metrics, including Gene Structural Correlation (\textbf{GSC}) and Spatial Structural Correlation (\textbf{SSC}). Our experiments demonstrate that FLAG is highly competitive in traditional accuracy (PCC/MSE) while achieving significantly enhanced structural fidelity in capturing both gene-gene and gene-spatial relationships. The code is available at this https URL.

---


### 254. [PPAI: Enabling Personalized LLM Agent Interoperability for Collaborative Edge Intelligence](https://arxiv.org/abs/2605.18067)

**<font color=#1a73e8>作者：</font>** Zile Wang, Qianli Liu, Kaibin Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying large language model (LLM) on edge device enables personalized LLM agents for various users. The growing availability of diverse personalized agents presents a unique opportunity for peer-to-peer (P2P) collaboration, wherein each user can delegate tasks beyond the local agent's expertise to remote agents more suited for the specific query. This paper introduces PPAI, the first personalized LLM agent interoperability system, which enables users to collaborate with each other based on agent specialization. However, the ever-changing pool of agents and their interchangeable capacity introduce new challenges when it comes to matching queries to agents and balancing loads, compared with existing P2P systems. Therefore, we propose a scalable query-agent pair scoring mechanism based on prototypes to identify suitable agents within a P2P network with churn. Moreover, we propose a multi-agent interoperability Bayesian game to balance local demand and global efficiency, when changes in remote agent load occur too quickly to be observed. Finally, we implement a prototype of PPAI and demonstrate that it substantially broadens the range of tasks that could be carried out while maintaining load balance. On average, it achieves an accuracy improvement of up to 7.96% across multiple tasks, while reducing latency by 16.34% compared to the baseline.

---


### 255. [KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference](https://arxiv.org/abs/2605.18071)

**<font color=#1a73e8>作者：</font>** Jian Lin, Jiazhi Mi, Zicong Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supporting long-context LLMs is challenging due to the substantial memory demands of the key-value (KV) cache. Existing offloading systems store the full cache in host memory and selectively fetch critical entries during decoding, but this strategy quickly hits a ceiling: sparsity cannot be pushed further without degrading accuracy. As a result, when context length and batch size grow, the volume of KV transfers rises sharply and becomes the dominant source of decoding latency. We present KVDrive, a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. Unlike prior work that pursues greater sparsity through algorithmic refinements, KVDrive tackles the problem from a systems perspective - jointly orchestrating cache placement, pipeline scheduling, and cross-tier coordination to sustain high-throughput inference under tight GPU budgets. KVDrive advances three fundamental capabilities: it adapts cache management to attention behavior to maximize reuse and minimize redundant data movement; it restructures the decoding pipeline to overlap I/O- and CPU/GPU compute-bound stages, eliminating stalls across heterogeneous resources; and it harmonizes data movement across memory tiers to unlock scalable long-context inference far beyond GPU and DRAM limits. We have implemented a fully functional prototype of KVDrive and evaluated it on long-context benchmarks with popular LLMs. The system achieves up to 1.74x higher throughput compared to state-of-the-art works while preserving accuracy.

---


### 256. [LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.18077)

**<font color=#1a73e8>作者：</font>** Sangjun Bae, Yisak Park, Sanghyeon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Communication is a key component in multi-agent reinforcement learning (MARL) for mitigating partial observability, yet prior approaches often rely on inefficient information exchange or fail to transmit sufficient state information. To address this, we propose LLM-driven Multi-Agent Communication (LMAC), which leverages an LLM's reasoning capability to design a communication protocol that enables all agents to reconstruct the underlying state as accurately and uniformly as possible. LMAC iteratively refines the protocol using an explicit state-awareness criterion, improving state recovery while narrowing differences in agents' knowledge. Experiments on diverse MARL benchmarks show that LMAC improves state reconstruction across agents and yields substantial performance gains over prior communication baselines.

---


### 257. [A Data-Efficient Path to Multilingual LLMs: Language Expansion via Post-training PARAM$Δ$ Integration into Upcycled MoE](https://arxiv.org/abs/2605.18083)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Tianhao Li, Zhijun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expanding Large Language Models~(LLMs) to new languages is a costly endeavor, demanding extensive Continued Pre-Training~(CPT) and data-intensive alignment. While recent data-free merging techniques attempt to bypass alignment by fusing a multilingual CPT-enhanced model with its instruct counterpart, they are plagued by a critical trade-off: mitigating parameter conflicts to preserve original abilities inevitably dilutes new language acquisition, and vice-versa. To resolve this conflict, we introduce \method, which upcycles a dense model into a Mixture-of-Experts~(MoE) architecture, allocating different experts to different languages. Alignment ability is then transferred by grafting a MoE-expanded parameter delta~($\Delta_{\text{post}}$) to the CPT-enhanced base model, bypassing the complex alignment phase. Experiments demonstrate \method's superiority even against baselines with similar FLOPs or number of parameters; it improves performance on expanded languages while effectively preserving original capabilities. We further show our approach is highly applicable across different models and Post-training deltas.

---


### 258. [Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction](https://arxiv.org/abs/2605.18104)

**<font color=#1a73e8>作者：</font>** Jiahe Guo, Xiangran Guo, Jiaxuan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often fail to transfer safety capabilities learned in the text modality to semantically equivalent non-text inputs, revealing a persistent multimodal safety gap. We study this gap from a representation-geometric perspective by analyzing a text-aligned refusal direction and a modality-induced drift direction. We show that multimodal inputs compress the usable separation along the refusal direction, making it no longer reliable for identifying and refusing harmful inputs. We refer to this failure mode as Safety Geometry Collapse. We quantify it through conditional refusal separability and show that stronger modality-induced drift is consistently associated with weaker refusal separability and higher attack success rates. We then validate the causal role of modality-induced drift through a fixed-strength activation intervention: counteracting the estimated drift restores refusal separability and improves multimodal safety. After drift correction, we further observe self-rectification, where the model recovers its ability to recognize and refuse harmful multimodal inputs during forward dynamics. This effect also provides an internal signal of the model's perceived harmfulness of each input. Motivated by this signal, we propose ReGap, a training-free inference-time method that adaptively corrects modality drift using self-rectification. Experiments across multiple multimodal safety benchmarks and utility benchmarks demonstrate the effectiveness of ReGap, which significantly improves the safety of MLLMs without compromising general capabilities. Our findings highlight representation-level modality alignment as a crucial direction for real-time safety improvement and for building safer, more reliable MLLMs.

---


### 259. [How Loud Rumbles Hit Newsstands: A Data Analysis of Coverage and Spatial Bias in German News about Landslides Around the World](https://arxiv.org/abs/2605.18105)

**<font color=#1a73e8>作者：</font>** Brielen Madureira, Andreas Niekler, Marc Keuschnigg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Landslides often hit newsstands due to their destructive and potentially fatal effects. News are a valuable source of information for creating or enriching disaster databases and for expediting media-based studies of the dynamics of media attention. To accomplish that, news datasets must be filtered, geolocated and validated. This paper focuses on how landslides around the world are reported in German newspapers. We analyse almost 60k news articles about 5.5k news events in a 25-year period, compare it with external measures of countries' susceptibility to landslides and provide insights, e.g.~the overreporting of Southern and Western Europe, to foment further studies on inequalities in media attention to international disasters.

---


### 260. [How Good LLMs Are at Answering Bangla Medical Visual Questions? Dataset and Benchmarking](https://arxiv.org/abs/2605.18111)

**<font color=#1a73e8>作者：</font>** Rafid Ahmed, Intesar Tahmid, Mir Sazzat Hossain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Large Language Models (LLMs) and Large Vision Language Models (LVLMs) have enabled general-purpose systems to demonstrate promising capabilities in complex reasoning tasks, including those in the medical domain. Medical Visual Question Answering (MedVQA) has particularly benefited from these developments. However, despite Bangla being one of the most widely spoken languages globally, there exists no established MedVQA benchmark for it. To address this gap, we introduce BanglaMedVQA, a dataset comprising clinically validated image-question-answer pairs, along with a comprehensive evaluation of current foundation models on this resource. Consistent with prior findings that report low performance of current models on English MedVQA benchmarks, our analysis reveals that Bangla performance is substantially lower, reflecting the challenges inherent to low-resource languages. Even top-performing models such as Gemini and GPT-4.1 mini fail to accurately answer specialized diagnostic questions, indicating severe limitations in fine-grained medical reasoning. Although certain open-source models, such as Gemma-3, occasionally outperform these models in general categories, they too struggle with clinically complex questions, underscoring the urgent need for top-notch evaluation method.

---


### 261. [Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving](https://arxiv.org/abs/2605.18137)

**<font color=#1a73e8>作者：</font>** Lijun Zhou, Hongcheng Luo, Zhenxin Zhu 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.

---


### 262. [A Brief Overview: On-Policy Self-Distillation In Large Language Models](https://arxiv.org/abs/2605.18141)

**<font color=#1a73e8>作者：</font>** Fangming Cui, Sunan Li, Jiahong Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) introduces a unified learning framework in which a single large language model simultaneously serves as both teacher and student. Unlike conventional knowledge distillation that relies on a separate, often larger teacher model, OPSD operates under different contextual roles: the teacher policy is granted privileged access to verified reasoning traces, while the student policy observes only the problem statement. OPSD is trained to minimize per-token distributional divergence between the two roles over trajectories sampled from the student itself, thereby aligning its own reasoning behavior with solution-aware rationalizations. OPSD eliminates the need for an external teacher, directly leverages ground-truth solution information, and resolves the distribution mismatch inherent in off-policy distillation. OPSD typically reduces GPU memory consumption by approximately 40%-60% compared to standard On-Policy Distillation (OPD). In this paper, we present a brief analysis of the conceptual foundations, methodological innovations, and principled designs underlying recent advances in OPSD for large language models. This discussion, crafted from the perspective of beginners in this field, aims to provide a concise overview of the design principles and emerging patterns of OPSD in LLMs, intended for researchers who are similarly new to this area.

---


### 263. [Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine](https://arxiv.org/abs/2605.18144)

**<font color=#1a73e8>作者：</font>** Christiaan G.A. Viviers, Koen de Bruin, Mirre M. Trines 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.

---


### 264. [Foundation Models for Credit Risk Prediction: A Game Changer?](https://arxiv.org/abs/2605.18147)

**<font color=#1a73e8>作者：</font>** Bart Baesens, Andreas Goethals, Stefan Lessmann 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.

---


### 265. [Vision Inference Former: Sustaining Visual Consistency in Multimodal Large Language Models](https://arxiv.org/abs/2605.18160)

**<font color=#1a73e8>作者：</font>** Xinpeng Dong, Min Zhang, Kairong Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, multimodal large language models (MLLMs) have achieved remarkable progress, primarily attributed to effective paradigms for integrating visual and textual information. The dominant connector-based paradigm projects visual features into textual sequence, enabling unified multimodal alignment and reasoning within a generative architecture. However, our experiments reveal two key limitations: (1) Although visual information serves as the core evidential modality in MLLMs, it is treated on par with textual tokens, diminishing the unique contribution of the visual modality; (2) As generation length increases, particularly within a limited context window, the model's dependence on visual information progressively weakens, resulting in deteriorated vision-language alignment and reduced consistency between generated content and visual semantics. To address these challenges, we propose the Vision Inference Former (VIF), a lightweight architectural module that establishes a direct bridge between pure visual representations and the model's output space. Specifically, VIF continuously injects visual semantics throughout the decoding phase of the inference process, ensuring that the model remains firmly grounded in visual content during generation. We conduct experiments on 14 benchmark tasks covering general reasoning, OCR, table understanding, vision-centric evaluation, and hallucination. Experimental results show that VIF consistently improves model performance across diverse architectures while introducing minimal additional overhead. The code for this work is available at this https URL.

---


### 266. [Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency](https://arxiv.org/abs/2605.18162)

**<font color=#1a73e8>作者：</font>** Junming Liu, Yuqi Li, Yifei Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.

---


### 267. [Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs](https://arxiv.org/abs/2605.18165)

**<font color=#1a73e8>作者：</font>** Junyi Wu, Tianchen Zhao, Shaoqiu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlike autoregressive models, which generate one token at a time, dLLMs denoise a chunk of [MASK] tokens jointly and sample one or more tokens per step; despite enabling parallel decoding, this process incurs substantial computational cost due to the large chunk size of masked tokens. We observe that much of this cost is spent on repeatedly processing the preceding context and many [MASK] tokens with the same feature representations, indicating considerable computational redundancy. In this work, we revisit dLLM's redundancy from the perspective of [MASK] tokens. Through systematic analysis, we verify the redundancy of [MASK] tokens while revealing their critical role in providing structural information. Guided by these findings, we propose position-preserving [MASK] token compression and terminal-aware augmentation. By compressing redundant [MASK] computation, this approach accelerates decoding and further provides a natural extension toward context-folding-like long-context scaling under limited input-length constraints for full-sequence dLLMs such as LLaDA-8B-Instruct and LLaDA-1.5. Moreover, for block dLLMs such as LLaDA2.0-mini, it augments the context with a protected terminal [MASK] token to enhance generation quality with negligible overhead.

---


### 268. [Visualizing the Invisible: Generative Visual Grounding Empowers Universal EEG Understanding in MLLMs](https://arxiv.org/abs/2605.18172)

**<font color=#1a73e8>作者：</font>** Junyu Pan, Yansen Wang, Enze Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Leveraging the universal representations of pre-trained LLMs and MLLMs offers a promising path toward brain foundation models. However, visually-evoked EEG datasets remain scarce, leading existing methods to align neural signals mainly with abstract text, a lossy translation that may discard fine-grained perceptual information encoded in brain activity. We propose Generative Visual Grounding (GVG), a framework that visualizes the invisible by using an EEG-to-image generative model as a visual translator. Instead of forcing EEG into text alone, GVG hallucinates instance-specific proxy images for non-visual EEG, providing structured visual contexts that allow MLLMs to exploit their visual priors for clinical-state interpretation. We validate this idea on two MLLM backbones, GVG-X-Omni and GVG-Janus. Image-only alignment is already competitive: the lightweight GVG-X-Omni matches 1.7B-parameter text-aligned baselines while tuning only 170M parameters on a frozen 7B backbone. We further extend GVG-Janus with trimodal Image+Text alignment, where text supplies categorical semantic anchors and visual proxies enrich neural representations with perceptual details. Experiments show consistent gains in EEG understanding and visual generation, suggesting visual proxy grounding as an effective complement to textual alignment.

---


### 269. [MARS: Technical Report for the CASTLE Challenge at EgoVis 2026](https://arxiv.org/abs/2605.18176)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Qiaohui Chu, Yisen Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at this https URL.

---


### 270. [UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction](https://arxiv.org/abs/2605.18188)

**<font color=#1a73e8>作者：</font>** Robson W. S. Pessoa, Julien Amblard, Alessandra Russo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in batch processes is hindered by transient dynamics, scarce fault labels, and reliance on single-modality sensor data. This work introduces UTOPYA (Unified Temporal Observation for Physics-Informed Anomaly Detection and Time-Series Prediction), a 15.2M-parameter multimodal framework that jointly addresses anomaly detection, time-series prediction, and phase classification in batch distillation by fusing eight data modalities through Feature-wise Linear Modulation (FiLM) conditioned cross-modal attention and gated fusion. A physics-informed regularisation scheme introduced in this work enforces temporal smoothness and thermodynamic monotonicity, while curriculum learning introduces training samples in order of physical difficulty. On the 119-experiment multimodal batch distillation dataset of Arweiler et al. (2026), UTOPYA achieves a window-level test AUROC of 0.832 and 0.874 under multi-signal experiment-level scoring, substantially outperforming four external baselines (PCA, autoencoder, Isolation Forest, and LSTM autoencoder) evaluated under identical conditions (+0.147 window-level AUROC over the best baseline). A multimodal ablation over 15~architectural configurations shows that static context via FiLM conditioning is the key enabler, lifting experiment-level multi-signal AUROC by +0.145 over the unimodal baseline (0.729 to 0.874). Separately, a training ablation across 14 design choices reveals that several widely-adopted techniques, including instance normalisation, Mixup, ensembling, test-time augmentation, and stochastic weight averaging, fail to improve or actively degrade generalisation in this data-scarce setting. These negative results expose a fundamental tension between smoothing-based regularisation and anomaly detection, providing practical guidance for multimodal process monitoring deployment.

---


### 271. [View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification](https://arxiv.org/abs/2605.18192)

**<font color=#1a73e8>作者：</font>** Quan Zhang, Zeqiang Cai, Peiming Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial-Ground Person Re-Identification (AGPReID) remains highly challenging due to drastic viewpoint variations between drones and fixed cameras. Existing methods typically follow a view-invariant paradigm, aligning shared features across views to achieve robustness. However, view-invariant inherently enforces part-level alignment, which ignores view-specific cues and discriminative identity information. To this end, this work proposes ViSA (View-aware Semantic Alignment), a view-aware framework that achieves cross-view semantic consistency containing an Expert-driven Token Generation Module (ETGM) and a Dual-branch Local Fusion Module (DLFM). Technically, the former constructs a set of view-aware experts to generate adaptive semantic queries that perceive viewpoint-specific patterns, while the latter leverages graph reasoning to extract and align local regions responsive to different experts. Extensive experiments on three AGPReID benchmarks including AG-ReID.v2, CARGO and LAGPeR demonstrate that ViSA consistently achieves superior performance, with a notable 10.06\% mAP improvement on the challenging CARGO cross-view protocol. The code is available at \href{this https URL}{this https URL}.

---


### 272. [Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks](https://arxiv.org/abs/2605.18194)

**<font color=#1a73e8>作者：</font>** Yajing Zhou, Xiangyu Kong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.

---


### 273. [SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning](https://arxiv.org/abs/2605.18209)

**<font color=#1a73e8>作者：</font>** Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.

---


### 274. [Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction](https://arxiv.org/abs/2605.18211)

**<font color=#1a73e8>作者：</font>** Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.

---


### 275. [Context Memorization for Efficient Long Context Generation](https://arxiv.org/abs/2605.18226)

**<font color=#1a73e8>作者：</font>** Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.

---


### 276. [Multilingual jailbreaking of LLMs using low-resource languages](https://arxiv.org/abs/2605.18239)

**<font color=#1a73e8>作者：</font>** Dylan Marx, Marcel Dunaiski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) remain vulnerable to jailbreak attempts that circumvent safety guardrails. We investigate whether multi-turn conversations using low-resource African languages (Afrikaans, Kiswahili, isiXhosa, and isiZulu) can bypass safety mechanisms across commercial LLMs. We translated prompts from existing datasets and evaluated ChatGPT, Claude, DeepSeek, Gemini, and Grok through automated testing and human red-teaming with native speakers. Single-turn translation attacks proved ineffective, while multi-turn conversations achieved English harmful response rates from 52.7% (Claude 3.5 Haiku) to 83.6% (GPT-4o-mini), Afrikaans from 60.0% (Claude 3.5 Haiku) to 78.2% (GPT-4o-mini), and Kiswahili from 41.8% (Claude 3.5 Haiku) to 70.9% (DeepSeek). Human red-teaming increased jailbreak rates compared to automated methods. Over all evaluated languages, the average jailbreak rate increased from 59.8% to 75.8%, with improvements of +20.0% (Afrikaans), +12.7% (isiZulu), +12.3% (isiXhosa), and +1% (Kiswahili), demonstrating that poor translation quality limits jailbreak success. These findings suggest that vulnerabilities in LLMs persist in multilingual contexts and that translation quality is the critical factor determining jailbreak success in low-resource languages.

---


### 277. [Machine Unlearning for Masked Diffusion Language Models](https://arxiv.org/abs/2605.18253)

**<font color=#1a73e8>作者：</font>** Georu Lee, Seungwon Jeong, Hoki Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent masked diffusion language models (MDLMs), such as LLaDA and Dream, have achieved performance comparable to autoregressive large language models. Unlike autoregressive models, which generate text sequentially, MDLMs generate text by iteratively denoising masked positions in parallel. During fine-tuning, MDLMs learn to recover responses from masked response states conditioned on a prompt, thereby shifting their predictions from a prompt-masked unconditional distribution toward a prompt-conditional distribution. Despite this distinct generative and fine-tuning mechanism, machine unlearning for MDLMs remains largely unexplored. In this paper, we propose Masked Diffusion Unlearning (MDU), the first unlearning framework for MDLMs, by revisiting the process of learning specific knowledge in terms of diffusion. Specifically, MDU minimizes a forward KL divergence from the prompt-conditional prediction to a prompt-masked unconditional anchor at every masked response position, with a temperature scaling parameter to control the privacy-utility trade-off. Our empirical results on standard benchmarks and MDLM backbones show that MDU achieves high unlearning performance compared to existing LLM unlearning methods. Code is available at this https URL.

---


### 278. [CodeBind: Decoupled Representation Learning for Multimodal Alignment with Unified Compositional Codebook](https://arxiv.org/abs/2605.18257)

**<font color=#1a73e8>作者：</font>** Zeyu Chen, Jie Li, Kai Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal representation alignment is pivotal for large language models and robotics. Traditional methods are often hindered by cross-modal information discrepancies and data scarcity, leading to suboptimal alignment spaces that overlook modality-unique features. We propose CodeBind, a framework that optimizes multimodal representation spaces through a modality-shared-specific codebook design. By incrementally aligning target and bridging modalities, CodeBind bypasses the need for fully paired data. Unlike traditional hard alignment, CodeBind decomposes features into shared components for semantic consistency and specific components for modality-unique details. This design utilizes a compositional vector quantization scheme, where a shared codebook bridges modality gaps and modality-specific codebooks mitigate representation bias by preventing dominant modalities from overshadowing others. Validated across nine modalities (text, image, video, audio, depth, thermal, tactile, 3D point cloud, EEG), CodeBind achieves state-of-the-art performance in multimodal classification and retrieval tasks.

---


### 279. [Knowledge-to-Verification: Exploring RLVR for LLMs in Knowledge-Intensive Domains](https://arxiv.org/abs/2605.18261)

**<font color=#1a73e8>作者：</font>** Zhonghang Yuan, Zhefan Wang, Fang Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has demonstrated promising potential to enhance the reasoning capabilities of large language models (LLMs) in domains such as mathematics and coding. However, its applications on knowledge-intensive domains have not been effectively explored due to the scarcity of high-quality verifiable data. Furthermore, current RLVR focuses solely on the correctness of final answers, leading to the limitations of flawed reasoning and sparse reward signals. In this work, we propose Knowledge-to-Verification (K2V), a framework that extends RLVR to knowledge-intensive domains through automated verifiable data synthesis, while enabling verification of the LLM's reasoning process. Extensive experiments demonstrate that K2V enhances the reasoning of LLM in knowledge-intensive domains without significantly compromising the model's general capabilities. This study also suggests that integrating automated data synthesis with reasoning verification is a promising direction to enhance model capabilities in these broader domains. Code is available at this https URL.

---


### 280. [From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG](https://arxiv.org/abs/2605.18271)

**<font color=#1a73e8>作者：</font>** Changmin Lee, Jaemin Kim, Taesik Gong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid emergence of personal AI agents based on Large Language Models (LLMs), implementing them on-device has become essential for privacy and responsiveness. To handle the inherently personal and context-dependent nature of real-world requests, such agents must ground their generation in device-resident personal context. However, under tight memory budgets, the core bottleneck is what to store so that retrieval remains aligned with the user. We propose EPIC (Efficient Preference-aligned Index Construction), which focuses on user preferences as a compact and stable form of personal context and integrates them throughout the RAG pipeline. EPIC selectively retains preference-relevant information from raw data and aligns retrieval toward preference-aligned contexts. Across four benchmarks covering conversations, debates, explanations, and recommendations, EPIC reduces indexing memory by 2,404 times, improves preference-following accuracy by 20.17 percentage points, and achieves 33.33 times lower retrieval latency over the best-performing baseline. In our on-device experiment, EPIC maintains a memory footprint under 1 MB with 29.35 ms/query latency in streaming updates.

---


### 281. [DARE-EEG: A Foundation Model for Mining Dual-Aligned Representation of EEG](https://arxiv.org/abs/2605.18298)

**<font color=#1a73e8>作者：</font>** Yang Shao, Peiliang Gong, Qun Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models pre-trained through masked reconstruction on large-scale EEG data have emerged as a promising paradigm for learning generalizable neural representations across diverse brain-computer interface applications. However, a critical yet overlooked challenge is that EEG encoders must learn representations invariant to incomplete observations-when different masked views of the same signal have minimal overlap, existing methods fail to constrain them to a consistent latent subspace, leading to degraded transferability. To address this, we propose DARE-EEG, a self-supervised foundation model that explicitly enforces the mask-invariance property through dual-aligned representation learning during pre-training. Specifically, we introduce mask alignment that constrains representations from multiple masked views of the same EEG sample via contrastive learning, complementing anchor alignment that aligns masked representations to momentum-updated complete features for semantic stability. Additionally, we propose conv-linear-probing, a parameter-efficient strategy that adapts pre-trained representations to heterogeneous electrode configurations and sampling rates through decoupled spectro-spatial projections. Extensive experiments across diverse EEG benchmarks demonstrate that DARE-EEG consistently achieves state-of-the-art in accuracy performance while maintaining relatively low parameter complexity and superior cross-dataset portability compared to existing methods. Furthermore, DARE-EEG contributes to effectively discovering and utilizing the rich potential representations in EEG.

---


### 282. [What Would GPT Click: Practical Effects of Human-AI Behavioral Misalignment and the Cost of Synthetic Participants in User Experience](https://arxiv.org/abs/2605.18302)

**<font color=#1a73e8>作者：</font>** Eduard Kuric, Peter Demcak, Matus Krajcovic  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Synthetic participants represent a methodologically concerning concept that threatens the integrity of UX research. Findings from previous experiments specify how AI outputs are misaligned with the behaviors and thoughts of real humans in various ways. However, industry voices keep underestimating their severity, advocating for practical compromises where good-enough data does not need to be perfect, and all issues will be solved by future tuning. Our study tackles the lack of systematic understanding of the practical issues that arise with synthetic behavior and its use for steering decisions within real contexts. Within twelve diverse first click tests (n = 3431) obtained from real UX practice, we examine the ability of GPT to predict where humans click and how they reason about their behavior. Results (e.g., significantly different distribution from real data in 53% of tasks) demonstrate critical failures to reflect the patterns in which users click on visual elements and the underlying cognitive processes. Participant personas, chain-of-thought reasoning in GPT, and different sampling parameters fail to create sensible fidelity improvements apart from inflating believability. We expose a multitude of nuanced distortions in synthetic responses that reduce their overall analytical usefulness as a decision-making resource, compared with real data. Observed distortions can be theoretically linked to the properties categorically inherent to LLMs: their statistical nature and encoding of semantic heuristics dependent on their training on linguistic data.

---


### 283. [PH-Dreamer: A Physics-Driven World Model via Port-Hamiltonian Generative Dynamics](https://arxiv.org/abs/2605.18303)

**<font color=#1a73e8>作者：</font>** Xueyu Luan, Chenwei Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models built on recurrent state space architectures enable efficient latent imagination, yet remain physically unstructured, producing dynamics that violate conservation and dissipative principles. We introduce a unified Port-Hamiltonian framework that remedies this through three synergistic mechanisms. First, we embed implicit physical priors into recurrent transitions by modeling projected latent evolution as action controlled energy routing governed by flow and dissipation, biasing the projected PH phase space toward a more compact and physically structured representation. Second, we develop a kinematics aware energy world model that estimates the Hamiltonian and power balance from proprioceptive observations, providing an explicit physical signal for thermodynamic reasoning. Third, leveraging these energy gradients, we establish an energy guided Actor-Critic that uses Lagrangian multipliers to regularize policy optimization toward lower energy and smoother control. Across visual control benchmarks, this paradigm not only attains superior asymptotic returns but also elevates internal simulator fidelity by establishing a tighter, lower variance alignment between imagined and real rewards, all while reducing latent phase space volume by 4.18-8.41%, energy consumption by up to 7.80%, and mean squared jerk by up to 9.38%.

---


### 284. [Alignment Dynamics in LLM Fine-Tuning](https://arxiv.org/abs/2605.18309)

**<font color=#1a73e8>作者：</font>** Yuhan Huang, Huanran Chen, Yinpeng Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) achieve strong alignment through supervised fine-tuning and reinforcement learning from human feedback, the alignment is often fragile under subsequent fine-tuning. Existing explanations either attribute alignment fragility to gradient geometry or characterize it as a distributional shift in model outputs, yet few provide a unified account that bridges parameter-space learning dynamics with function-space alignment behavior during fine-tuning. In this work, we introduce a tractable alignment score and derive its closed-form update during fine-tuning, yielding a unified framework for alignment dynamics. Our analysis decomposes alignment updates into two competing components: a \textbf{\color{red!60!black} Rebound Force}, governed jointly by the current alignment state and the narrowness of model distribution, and a \textbf{\color{green!60!black} Driving Force}, determined by how the training distribution aligns with outcome-conditioned posteriors over aligned and non-aligned completions. This decomposition explains why prior alignment can be reversed by later fine-tuning and why narrower posterior structure strengthens such reversal. Moreover, our framework predicts a \textbf{Rehearsal Priming Effect}: prior alignment leaves a latent posterior imprint that amplifies the effective Driving Force upon re-exposure, leading to faster re-alignment. We validate these predictions across safety alignment, emergent misalignment, and sentiment settings, demonstrating consistent alignment reversal and accelerated re-alignment under re-exposure. In addition, controlled experiments in safety alignment confirm the predicted dependence of rebound strength on posterior narrowness. Together, these results provide a unified dynamical perspective on how alignment is disrupted and reactivated during LLM fine-tuning.

---


### 285. [Distorted Perspectives of LLM-Simulated Preferences: Can AI Mislead Design?](https://arxiv.org/abs/2605.18311)

**<font color=#1a73e8>作者：</font>** Eduard Kuric, Peter Demcak, Matus Krajcovic  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designers of digital solutions increasingly consult Large Language Models (LLMs) for their work. However, it remains unclear how this may affect the user experiences they produce and there are no established practices. We investigate how design preferences expressed by LLM-driven simulation methods align with those of real users. We present a study that aggregates real-world data and design stimuli from twenty-nine preference tests conducted in practice by users of the UXtweak online research platform (n = 2073). We perform holistic multimodal simulations where we manipulate LLM variables (model reasoning, sampling, persona type, and specificity) and assess their effects on algorithmic fidelity. Our results unveil significant and systematic discrepancies between peoples' real design preferences and LLM simulations that are consistent across manipulations. Synthetic justifications lack genuine depth, nuance and reasoning, which they substitute by patterns like focus on generic properties, specific elements, elaboration and overpraising. The unique attention directed by this research toward preferences within visual design stimuli highlights misrepresentation of perception and meaning by LLMs in a context that is intuitive yet critical for design teams. The external and ecological validity of our findings is high, given their replication across a multitude of real-world studies.

---


### 286. [Wasserstein Equilibrium Decoding for Reliable Medical Visual Question Answering](https://arxiv.org/abs/2605.18313)

**<font color=#1a73e8>作者：</font>** Luca Hagen, Johanna P. Müller, Weitong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small vision-language models (2-8B) are well-suited for clin- ical deployment due to privacy constraints, limited connectivity, and low-latency requirements favouring on-device or on-premise inference. However, their limited capacity exacerbates the generation of plausible but incorrect outputs. We extend game-theoretic decoding, previously restricted to text-only, closed-ended NLP tasks, to vision-language mod- els for open-ended Medical VQA. We introduce a semantically aware Wasserstein stopping criterion that replaces lexical order matching, en- abling convergence based on semantic consensus among near-synonymous candidate answers and avoiding unnecessary iterations caused by clini- cally equivalent ranking swaps. On VQA-RAD and PathVQA, we ob- tain consistent, statistically significant improvements over greedy and discriminative baselines. On VQA-RAD, we improve Qwen3-VL-2B by +3.5 percentage points (p < 0.01), surpassing the greedy 4B model, with similar trends at larger scales. On PathVQA, Gemma-3-4B with BDG matches MedGemma-4B under greedy decoding despite no domain- specific fine-tuning. At accuracy parity with classic BDG, the Wasser- stein criterion reduces average convergence iterations by approximately 20%, improving inference efficiency while preserving the game-theoretic equilibrium behaviour. Code is available at this https URL Wasserstein-BDG-medical-VQA.

---


### 287. [Prune, Update and Trim: Robust Structured Pruning for Large Language Models](https://arxiv.org/abs/2605.18331)

**<font color=#1a73e8>作者：</font>** Diego Coello de Portugal Mecke, Tom Hanika, Lars Schmidth-Thieme  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have experienced significant growth and development in recent years. However, performing inference on LLMs remains costly, especially for long-context inference or in resource-constrained devices. This motivates the development of new post-training pruning (PTP) methods. These methods reduce LLMs' requirements by removing a substantial part of the model's parameters. The discarded weights are selected depending on their impact on the models performance. Current PTP methods prune the models by removing the less informative hidden nodes from the FFN layers, and the least important attention layers. We propose Putri, a PTP method that introduces three changes to the State- of-the-art. First, we update the un-pruned weights of the FFN to compensate for the introduced pruning error. Second, the FFN layers are pruned sequentially, taking into account the updates done to the previous layers. Third, instead of removing full attention layers, we remove individual attention-heads. We extend this method such that it can also address Grouped-Query Attention. In summary, Putri is a structure pruning method which remains simple while showing SOTA performance. Pruning experiments on multiple models with a wide variety of sparsity ranges and on different datasets, validate the generality of Putri. Notably, we demonstrate that, unlike previous methods, Putri can prune LLMs on extreme sparsity ratios. The code is available at: this https URL.

---


### 288. [Presupposition and Reasoning in Conditionals: A Theory-Based Study of Humans and LLMs](https://arxiv.org/abs/2605.18352)

**<font color=#1a73e8>作者：</font>** Tara Azin, Yongan Yu, Raj Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Presupposition projection in conditionals is central to theories of meaning and pragmatics, yet it remains largely unevaluated in large language models. We address this gap through a parallel behavioral study comparing human judgments and LLM predictions on a normed dataset of conditional sentences that controls the relation between the antecedent and the projected presupposition. We collect likelihood ratings from 120 participants and four LLMs under matched contextual conditions. Results show that humans integrate probabilistic and pragmatic cues in their judgment, whereas LLMs show variable alignment with human patterns. Using a linguistically motivated checklist within an LLM-as-a-Judge framework, we further evaluate model reasoning. We observe models that best match human ratings often lack coherent pragmatic reasoning, while models with stronger reasoning produce less human-like judgments. These findings suggest that LLMs' performance on such tasks may result from surface pattern matching rather than pragmatic competence. Our findings highlight the importance of benchmarks grounded in linguistic theory for comparing humans and models.

---


### 289. [RAVE: Re-Allocating Visual Attention in Large Multimodal Models](https://arxiv.org/abs/2605.18359)

**<font color=#1a73e8>作者：</font>** Xi Leng, Xinhong Ma, Ziqiang Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large multimodal models (LMMs) inherit the self-attention mechanism of pretrained language backbones, yet standard attention can exhibit suboptimal allocation, including cross-modal misallocation between textual and visual evidence and intra-visual imbalance among visual tokens. We propose RAVE (Re-Allocating Visual Attention), a lightweight pair-gating mechanism that adds a learned query--key bias to pre-softmax attention scores over visual keys, derived from pre-RoPE query and key features. RAVE requires no architectural modification to the backbone and can be trained end-to-end with the rest of the model. Across a suite of multimodal benchmarks, RAVE improves over standard attention by an average of 3 points, with the largest gains on perception-intensive tasks -- including multilingual OCR, chart understanding, document VQA, and scene text VQA -- where accurate visual grounding is critical.

---


### 290. [The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human-AI Collaboration](https://arxiv.org/abs/2605.18372)

**<font color=#1a73e8>作者：</font>** Cansu Koyuturk, Sabrina Guidotti, Dimitri Ognibene  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in educational settings as interactive tools for collaboration. However, their tendency toward sycophancy, aligning with user beliefs even when incorrect, raises concerns for learning and decision-making, especially for less knowledgeable users. This study investigates how sycophantic alignment emerges in authentic multi-turn human-AI interactions and whether interventions targeting increasing AI literacy and prompting competencies can mitigate its effects. In a controlled mixed-design experiment, 60 participants completed analytical survival ranking tasks by first generating individual rankings and then making final decisions after collaborating with an AI assistant, both before and after receiving either general or sycophancy-focused prompting training. Preliminary results show that LLMs are highly sensitive to user input: lower-quality initial responses lead to poorer AI advice, suggesting that the model mirrors or incorporates user reasoning rather than correcting it or offering better alternatives that are missing or less frequent in the conversation. Critically, the propagation of user errors into AI responses significantly reduced both the quality of AI feedback and final user task performance, revealing a form of contextual sycophantic dependence. While the intervention did not eliminate the propagation of contextual errors, it significantly improved AI advice by reducing the direct mirroring of incorrect user rankings. These findings suggest that prompting and AI literacy alone may be insufficient to ensure epistemically independent AI support, highlighting the need for system-level approaches that better promote critical engagement in human-AI collaboration.

---


### 291. [Beyond Inference-Time Search: Reinforcement Learning Synthesizes Reusable Solvers](https://arxiv.org/abs/2605.18374)

**<font color=#1a73e8>作者：</font>** Soheyl Massoudi, Gabriel Apaza, Milad Habibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) typically approach combinatorial optimization as an inference-time procedure, solving each instance separately through sampling, search, or repeated prompting. We ask whether reinforcement learning can instead shift part of this reasoning cost into the weights of a code LLM, so that the model synthesizes a reusable solver for an entire problem family. We study this question on Synergistic Dependency Selection (SDS), a controlled variant of constrained Quadratic Knapsack designed to expose a specific failure mode: local signals and strict feasibility constraints make greedy heuristics attractive but unreliable. Under identical scaffolding, Best-of-64 base-model sampling saturates at an approximately 28.7% gap to the global Virtual Best Solver (VBS); code audits show that the base model often retrieves Simulated Annealing templates but misimplements the Metropolis acceptance rule. We fine-tune Qwen2.5-Coder-14B-Instruct with Group Relative Policy Optimization (GRPO) using a feasibility-gated reward and light structural scaffolding. The resulting policy converges to a constraint-aware Simulated Annealing template in 99.8% of feasible SDS outputs, achieves a 5.0% gap to that VBS, and is 91 times cheaper in post-generation execution/search cost than cumulative Best-of-64 evaluation. A compile-once check shows that one best frozen solver per seed remains highly competitive when reused unchanged across the SDS test set, while an additional-domain evaluation on Job Shop Scheduling provides narrower but positive evidence that the scaffold transfers beyond SDS. Negative ablations reveal the limits of this recipe: standard stabilizers degrade performance, a soft feasibility gate fails, and results remain sensitive to reward normalization and domain-specific design choices.

---


### 292. [QSTRBench: a New Benchmark to Evaluate the Ability of Language Models to Reason with Qualitative Spatial and Temporal Calculi](https://arxiv.org/abs/2605.18380)

**<font color=#1a73e8>作者：</font>** Anthony G. Cohn, Robert E. Blackwell  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce an extensive qualitative spatial and temporal reasoning (QSTR) benchmark for evaluating large language models (LLMs). We pose questions concerning compositional reasoning (using composition tables, CT), converse relations, and conceptual neighbourhoods (CN) for QSTR calculi, Point Algebra (PA), Allen's Interval Algebra, Interval and Duration (INDU), Region Connection Calculus (RCC-5, RCC-8, and RCC-22), the nine intersection model, cardinal direction calculus, and STAR. The RCC-22 CN is published here for the first time. An extended benchmark systematically varies question presentation including prefix/infix, words/symbols/nonce terms and schematic descriptions for selected calculi. We report results for contemporary frontier models. All models tested perform better than guessing but none can consistently answer all questions correctly. Performance varies sharply by calculus, with PA being the most straightforward, and RCC-22 the most difficult. We release the benchmark, and our results under an open licence to facilitate further assessment of qualitative spatio/temporal reasoning in LLMs.

---


### 293. [TabH2O: A Unified Foundation Model for Tabular Prediction](https://arxiv.org/abs/2605.18383)

**<font color=#1a73e8>作者：</font>** Pascal Pfeiffer, Dmitry Gordeev, Mathias Müller 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present TabH2O, a foundation model for tabular data that performs classification and regression in a single forward pass via in-context learning. TabH2O builds on the TabICL architecture with several key modifications: (1) unified training, a single model handles both classification and regression via a dual-head architecture, eliminating the need for separate models and reducing total pretraining cost; (2) single-stage pretraining, training stability improvements (bounded scalable softmax, inter-stage normalization, learnable residual scaling, logit soft-capping) eliminate the need for multi-stage curriculum learning, enabling training with full-length sequences from the start; and (3) noise-aware pretraining, synthetic datasets include explicit noise dimensions to teach the model robustness to irrelevant features. We evaluate TabH2O v1 (29.2M parameters) on the TALENT benchmark (300 datasets), where it achieves an average rank of 2.55 out of 6 evaluated methods, outperforming tuned CatBoost (4.07), H2O AutoML (4.18), and LightGBM (5.08), competitive with TabPFN v2.6 (2.74), and behind TabICL v2 (2.12), while placing in the top-3 on 81% of the testing datasets across classification and regression tasks.

---


### 294. [Vision Foundation Models as Generalist Tokenizers for Image Generation](https://arxiv.org/abs/2605.18390)

**<font color=#1a73e8>作者：</font>** Anlin Zheng, Qi Han, Xin Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we explore the largely unexplored direction of building a generalist image tokenizer directly on top of a frozen vision foundation model (VFM). To build this tokenizer, we utilize a frozen VFM as the encoder and introduce two key innovations: (1) a region-adaptive quantization framework to eliminate spatial redundancy in standard 2D grid features, and (2) a semantic reconstruction objective that aligns the decoded outputs with the VFM's representations to preserve semantic fidelity. Grounded in these designs, we propose VFMTok, a generalist visual tokenizer capable of operating seamlessly in both discrete and continuous latent spaces. VFMTok achieves substantial improvements in synthesis quality while drastically enhancing token efficiency. For discrete autoregressive (AR) generation, it accelerates model convergence by \textbf{3 times} and achieves a state-of-the-art gFID of \textbf{1.36} on ImageNet class-conditional synthesis. Similarly, for continuous-space generation, integrating VFMTok with a denoising model yields an exceptional gFID of \textbf{1.25}. Furthermore, because the latent space inherently captures rich spatial semantics, VFMTok enables high-fidelity class-conditional synthesis without classifier-free guidance (\textbf{w/o CFG}) across both generative paradigms, significantly accelerating inference speed. Beyond these remarkable empirical results, we systematically investigate the underlying mechanisms of our approach. We discover that the specific self-supervised learning objectives utilized during VFM pre-training dictate its effectiveness as a tokenizer. Specifically, a VFM jointly optimized with global contrastive learning and latent masked image modeling provides the optimal representations for image tokenization. These insights establish a strong foundation and offer valuable guidance for the design of future image tokenizers.

---


### 295. [NEWTON: Agentic Planning for Physically Grounded Video Generation](https://arxiv.org/abs/2605.18396)

**<font color=#1a73e8>作者：</font>** Yuxiang Feng, Juncheng Wang, Chao Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models produce visually compelling results but systematically violate physical commonsense -- on VideoPhy-2, the best model achieves only 32.6% joint accuracy. We identify a specification bottleneck: text prompts are lossy compression of the physical world, omitting the parameters that fully determine dynamics, and no amount of model scaling can recover what was never specified. From this diagnosis we derive three properties that physics conditioning must satisfy -- sufficiency, dynamism, and verifiability -- and show that no existing approach satisfies all three. We present NEWTON, in which video generation is demoted from the system output to one action inside an agent's toolbox: a learned planner orchestrates physics-aware tools (keyframe generation, scientific computation, prompt refinement) to construct rich conditioning, and a verifier closes the loop for iterative re-planning. The planner is the sole trainable component, optimized on-policy via Flow-GRPO inside the live multi-turn loop. On VideoPhy-2, NEWTON improves joint accuracy from 21.4% to 29.7% on LTX-Video and from 30.7% to 37.4% on Veo-3.1, without modifying either generator. Our project page: \href{this https URL}{this https URL}

---


### 296. [SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution](https://arxiv.org/abs/2605.18401)

**<font color=#1a73e8>作者：</font>** Hongyi Liu, Haoyan Yang, Tao Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents leave traces that could become reusable experience, but raw trajectories are noisy and hard to govern. We treat Agent Skills as an experience schema that couples executable scripts, with non-executable guidance on procedures. Yet open skill ecosystems contain redundant, uneven, environment-sensitive artifacts, and indiscriminate updates can pollute future context. We present SkillsVote, a lifecycle-governance framework for Agent Skills from collection and recommendation to evolution. SkillsVote profiles a million-scale open-source corpus for environment requirements, quality, and verifiability, then synthesizes tasks for verifiable skills. Before execution, SkillsVote performs agentic library search over structured skill library to expose instructional skill context. After execution, it decomposes trajectories into skill-linked subtasks, attributes outcomes to skill use, agent exploration, environment, and result signals, and admits only successful reusable discoveries to evidence-gated updates. In our evaluation, offline evolution improves GPT-5.2 on Terminal-Bench 2.0 by up to 7.9 pp, while online evolution improves SWE-Bench Pro by up to 2.6 pp. Overall, governed external skill libraries can improve frozen agents without model updates when systems control exposure, credit, and preservation.

---


### 297. [Cracks in the Foundation: A Civil Infrastructure Dataset to Challenge Vision Foundation Models](https://arxiv.org/abs/2605.18413)

**<font color=#1a73e8>作者：</font>** Nicola Farronato, Niccolo Avogaro, Thomas Frick 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated structural health monitoring is essential to prevent catastrophic infrastructure failures. Precise, pixel-level defect segmentation is needed to accurately assess structural integrity, but progress in defect segmentation for civil infrastructures has been held back by an extreme scarcity of data, which requires costly expert annotation. The need for data is accentuated by algorithmic hurdles intrinsic to the problem, including center-bias and the need to rely more on shape when inspecting nearly textureless building materials. To remove the bottleneck, we introduce Cracks in the Foundation (CiF), the largest and most detailed civil infrastructure (instance) segmentation dataset to date, comprising $\approx$150,000 high-resolution images meticulously curated over five years in collaboration with civil engineering experts. With the help of this unprecedented data source, we expose a blind spot of current visual AI: despite the advent of promptable Foundation Models (FMs) and Vision Language Models (VLMs), and despite the impressive abilities of today's specialised segmentation models, it turns out that dense image understanding in the built environment is nowhere near solved. Our evaluations indicate that even the most recent zero-shot FMs face significant challenges when deployed on real-world infrastructure and even the performance of specialised models with domain-specific supervision plateaus at $\approx$25% mAP. CiF establishes inspection of civil infrastructure, an elementary and seemingly easy perceptual task, as an open challenge that reveals fundamental weaknesses of present-day models trained predominantly on internet images, literally and figuratively highlighting cracks in the current foundation model paradigm.

---


### 298. [Geometry-Aware Uncertainty Coresets for Robust Visual In-Context Learning in Histopathology](https://arxiv.org/abs/2605.18419)

**<font color=#1a73e8>作者：</font>** Franciskus Xaverius Erick, Johanna Paula Müller, Bernhard Kainz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can couple visual perception with open-ended clinical reasoning, making them attractive for computational histopathology. However, fine-tuning billions of parameters on scarce, expert-annotated pathology data is prohibitive, while in-context learning (ICL), which conditions the VLM on demonstrative image-text pairs without parameter updates, suffers from high sensitivity to which examples are selected and how the query is phrased, producing unreliable diagnostics. Existing selection strategies rely on query-dependent nearest-neighbour retrieval that ignores global data structure, require costly parameter updates, or disregard the joint vision-text embedding geometry of VLMs. We propose GAUC, a training-free coreset selection method operating directly in the pre-trained multimodal embedding space. GAUC jointly optimises three objectives: (1) a Maximum Mean Discrepancy term enforcing distributional fidelity between coreset and full dataset, (2) an Effective Mutual Information Difference regulariser bounding performance degradation under prompt paraphrases by exploiting the VLM's joint vision-text alignment, and (3) a predictive-variance penalty suppressing overconfident, unstable outputs. On CRC-100K and MHIST across multiple open-source VLM architectures, GAUC consistently improves accuracy, calibration, and prompt robustness over recent ICL selection methods and dataset-distillation baselines, all without a single gradient update.

---


### 299. [Text2CAD-Bench: A Benchmark for LLM-based Text-to-Parametric CAD Generation](https://arxiv.org/abs/2605.18430)

**<font color=#1a73e8>作者：</font>** Liang Wang, Heng Meng, Zekai Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-CAD generation aims to create parametric CAD models from natural language, enabling rapid prototyping and intuitive design workflows. However, existing benchmarks focus on basic primitives and simple sketch-extrude sequences, lacking advanced features essential for real-world applications and covering only traditional mechanical parts. We introduce Text2CAD-Bench, the first benchmark systematically evaluating text-to-CAD across geometric complexity and application diversity. Our benchmark comprises 600 human-curated examples spanning four levels: L1-L2 cover fundamental geometry with standard features, L3 introduces complex topology and freeform surfaces, and L4 extends to real-world domains beyond mechanical parts. Each example pairs dual-style prompts -- geometric descriptions mimicking non-expert users, and procedural sequences aligned with expert-level conventions. Evaluating mainstream general LLMs and domain-specific models, we find that current models perform reasonably on basic geometry but degrade substantially on complex topology and advanced features. We release our benchmark to drive progress in text-to-CAD research.

---


### 300. [Seeing Together:Multi-Robot Cooperative Egocentric Spatial Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2605.18431)

**<font color=#1a73e8>作者：</font>** Kunyu Peng, Zhikun Zhou, Kailun Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have made substantial progress in egocentric video understanding, but their ability to reason cooperatively from multiple embodied viewpoints remains largely unexplored. We study this problem through multi-robot cooperative dynamic spatial reasoning, where a model must answer spatial, temporal, visibility, and coordination questions by integrating synchronized egocentric videos from a team of moving robots. To support this setting, we introduce CoopSR, the first benchmark for this task, together with EgoTeam, a multi-robot egocentric QA dataset. EgoTeam contains 114,227 QA pairs spanning 19 question types, four difficulty tiers, and three team sizes in Habitat and iGibson, along with a real-world test set of around 2,326 QAs collected using two quadruped robots. We further propose SP-CoR (Spectral and Physics-Informed Cooperative Reasoner), an MLLM framework for fine-grained cooperative spatial reasoning. SP-CoR combines dynamics-aware multi-robot frame sampling, spectral- and physics-guided view fusion, and physics-aligned prompt distillation, enabling the model to benefit from privileged robot-pose supervision during training while requiring only egocentric videos at test time. Across 22 MLLM baselines, SP-CoR consistently improves cooperative reasoning, outperforming the strongest fine-tuned baseline by +3.87% on Habitat and +7.12% on iGibson. It also shows stronger generalization to unseen team sizes and real-world robot tests. Code can be found at this https URL.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-346](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
