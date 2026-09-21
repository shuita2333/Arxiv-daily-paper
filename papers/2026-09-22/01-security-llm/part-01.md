# 🔐 大模型安全相关研究 | 2026年09月22日

> 本类共 **3** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision-Language Models](https://arxiv.org/abs/2609.21363)

**<font color=#1a73e8>作者：</font>** Yining Wang, Xi Li, Mi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large reasoning models (MLRMs) have demonstrated remarkable capabilities in complex visual understanding. However, this very power introduces a critical yet underexplored privacy threat: adversaries can exploit MLRMs to precisely infer users' geographic locations from casually shared photographs, by performing structured reasoning over subtle visual cues such as architectural styles, vegetation, and lighting conditions. In this work, we present a systematic study of MLRM-driven geolocation privacy leakage. We first reveal that refusal-based safeguards are critically insufficient, as carefully crafted jailbreak prompts can raise model response rates to 100%. We further identify that existing defenses, which inject imperceptible perturbations into shared images, suffer from structural limitations intrinsic to their pixel-space optimization, resulting in degraded black-box transferability and pronounced visual artifacts. Motivated by these findings, we propose a diffusion-based framework that provides targeted, proactive defense against geolocation privacy leakage. By injecting perturbations into the latent space of a diffusion model during reverse sampling, our method operates directly on high-level semantic representations, thereby resolving the effectiveness-utility bottlenecks by construction. We further ground our optimization with GeoCLIP, a model explicitly aligned with GPS coordinates, as a surrogate to pinpoint and disrupt the geographic signals that MLRMs exploit for location inference. This targeted semantic disruption yields significantly stronger black-box transferability while preserving perceptual image quality, offering a seamless integration on social media platforms.

---


### 2. [HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference](https://arxiv.org/abs/2609.21484)

**<font color=#1a73e8>作者：</font>** Byeongseo Min, Yongwoo Lee, Young-Sik Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic encryption (HE) has emerged as a promising approach to privacy-preserving machine learning (PPML), enabling computation directly over encrypted data. In HE-based PPML, a client submits an encrypted input to the server, which evaluates models such as large language models (LLMs) without access to the underlying plaintext. However, we identify a critical security vulnerability in this setting: HE-LLM inference is vulnerable to malicious clients that submit adversarial prompts, such as jailbreak attacks. The same confidentiality that protects benign clients also prevents the server from inspecting incoming prompts or generated responses, making adversarial attempts difficult to detect or block and potentially allowing successful attacks to remain entirely invisible to the server. To address this vulnerability, we propose HE-Guardrail, a framework that evaluates guardrail mechanisms entirely over encrypted data and homomorphically controls whether the target-model response is returned to the client. We instantiate HE-Guardrail with three representative guardrails - Llama Guard, JBShield, and GradSafe. Our results show that HE-Guardrail closely reproduces the decisions of the corresponding plaintext guardrails in the encrypted domain, with distinct security-efficiency-utility trade-offs.

---


### 3. [CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/abs/2609.21686)

**<font color=#1a73e8>作者：</font>** Tao Huang, Guosen Wu, Guolong Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy leakage in LLM agents is commonly evaluated within individual components such as memory, retrieval, or tool-use pipelines, which makes it difficult to distinguish internal exposure from information that an external observer can actually recover. We present CIPL (Channel Inversion for Privacy Leakage), a channel-aware evaluation framework for black-box privacy leakage in LLM agents. CIPL represents a target through sensitive source, selection, assembly, execution, observation, and extraction stages and evaluates the transition from selected sensitive units to attacker-recoverable output under a shared protocol. Experiments across memory-based, retrieval-mediated, and tool-mediated targets, together with a BrowserUse live-agent case study, show that storage labels alone do not determine recoverability. Memory targets form a near-saturated reference case, retrieval-mediated leakage is frequently partial, and tool-mediated and live-agent leakage varies strongly with observation surface, prompt-to-channel alignment, retrieval depth, and provider behavior. A stratified semantic audit further identifies attacker-useful disclosures that canonical exact matching misses. CIPL therefore provides a common framework for comparing how internal sensitive dependence is realized as externally recoverable leakage across heterogeneous agent pipelines.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
