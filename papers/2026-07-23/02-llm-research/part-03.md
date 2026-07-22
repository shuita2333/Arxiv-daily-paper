# 🧠 大模型相关研究 | 2026年07月23日

> 本类共 **104** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-104**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-104**

---

### 101. [OmniReasoner: Thinking with Long Audio-Video via Native Tool Use](https://arxiv.org/abs/2607.19339)

**<font color=#1a73e8>作者：</font>** Yu Chen, Caorui Li, Ziyu Xiong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long audio-video reasoning is difficult for omnimodal LLMs because the decisive evidence is often sparse, cross-modal, and too expensive to preserve with uniformly high-fidelity inputs. We introduce OmniReasoner, a tool-use post-training framework for Thinking with Long Audio-Video: omni-modal LLMs learn, via supervised fine-tuning and reinforcement learning, to decide whether and where to call a zoom-in tool before answering. OmniReasoner first builds a low-cost global preview of the full stream and then, when needed, calls the zoom-in tool with a requested temporal interval for higher-fidelity visual and audio inspection before answering. Because the model observes different sampling granularities before and after this call -- a sparse global preview and a denser local clip -- we introduce TimeAnchor, which keeps the tool's temporal argument valid and round-trip-consistent across these granularities, rather than tied to frame indices from a particular sampling rate. To make this tool-use behavior trainable without expensive manual interval annotation, we build a Temporal Augmented Data Engine that synthesizes tool-use post-training trajectories by video editing and composition. Experiments across omnimodal and video benchmarks show that OmniReasoner improves both answer accuracy and temporal grounding while concentrating high-fidelity computation on informative regions. Code is available at this https URL.

---


### 102. [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343)

**<font color=#1a73e8>作者：</font>** Hadi Alzayer, Wenlong Huang, Haonan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrary entity in a video. Revealing robot motion makes the model act as a forward dynamics model that predicts the scene's response to low-level robot actions, while revealing desired object motion makes the same model recover robot behavior consistent with that outcome. Finetuned with only 15 hours of masked examples from real videos and simulation, a single checkpoint achieves strong visual fidelity and controllability across diverse scenes and multiple embodiments. In downstream manipulation settings, the model produces imagined rollouts whose outcomes correlate with real-world execution for policy evaluation, improves decision making by ranking candidate futures in model-based planning, and supports inverse modeling by synthesizing robot motion from desired object motion.

---


### 103. [Appearance Pointers -- Multimodal Region Control of Diffusion Transformers](https://arxiv.org/abs/2607.19344)

**<font color=#1a73e8>作者：</font>** Rahul Sajnani, Yulia Gryaditskaya, Radomír Měch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone. Diffusion Transformers (DiTs) can natively ingest heterogeneous tokens stemming from texts and images, but they lack mechanisms for determining where and how these tokens should influence the output. We introduce appearance pointers, compact tokens that guide DiTs toward the correct appearance cues at the correct spatial locations by aligning text or image inputs with user-specified masks. Appearance pointers are produced by a region correspondence network and refined through a spatial aggregation mechanism, enabling the model to handle multiple regional descriptions without significantly increasing token load. Our approach introduces the first modality-agnostic interface for localized multimodal control in a DiT without retraining the base model from scratch. Across a range of metrics, our single model reaches or surpasses the performance of modality-specific state of the art methods, offering a simple and extensible path toward precise, region-aware, multimodal guidance in generative image synthesis.

---


### 104. [Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning](https://arxiv.org/abs/2607.19345)

**<font color=#1a73e8>作者：</font>** Lizhe Fang, Weizhou Shen, Tianyi Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models that generate step-by-step reasoning traces have achieved strong performance on complex tasks, and extending them to long-context settings has emerged as an important frontier. However, we identify a critical failure mode in this regime: \emph{repetitive copying}, where models extensively copy text from the input into their reasoning traces rather than productively solving the problem. We show that this behavior is pervasive across frontier long-context LLMs and intensifies with context length. By separating each prompt into task-relevant key evidence and irrelevant distractor context, we further show that the root cause is insufficient grounding: models copy from the prompt indiscriminately, and those that fail to focus on key evidence are far more likely to answer incorrectly. Motivated by this diagnosis, we propose GEAR (Grounding Evidence-Aware Reward), a reward shaping method that augments the accuracy signal with a grounding reward for overlap with key evidence and a distractor penalty for overlap with irrelevant context. To enable GEAR on natural-language data, we develop an automated pipeline that constructs evidence-annotated training data from arbitrary documents. We validate GEAR across multiple model scales and benchmarks, showing consistent improvements of up to +4.6 average points over standard RL with accuracy-based rewards, with larger gains at longer contexts, while also reducing repetitive copying and thinking length. Our findings suggest that, even as long-context evaluation shifts from simple retrieval toward complex reasoning, accurate grounding in relevant evidence remains an indispensable capability with substantial room for improvement.

---


> [!TIP]
> 当前位于：**101-104**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-104**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
